import json
from uuid import UUID

import pytest
from requests.exceptions import ConnectTimeout, HTTPError, ProxyError, SSLError
from requests import Response

from host_app.auth_diagnostics import failure_details
from host_app.entra_auth import EntraTokenProvider
from test_app import build_client, configured_settings, connect_identity


CORRELATION = "12345678-1234-4234-8234-123456789abc"
RAW_SECRET = "test-only-secret"
RAW_TOKEN = "sensitive.token.value"


def provider_factory(stage, failure):
    def make_provider(**kwargs):
        class Application:
            def acquire_token_for_client(self, **ignored):
                if isinstance(failure, Exception):
                    raise failure
                return failure

        def application_factory(**ignored):
            if stage == "client_initialization":
                raise failure
            return Application()

        return EntraTokenProvider(**kwargs, application_factory=application_factory)
    return make_provider


def log_event(caplog):
    records = [r for r in caplog.records if r.getMessage().startswith("EDAV_AUTH_DIAGNOSTIC ")]
    assert len(records) == 1
    assert records[0].exc_info is None
    return json.loads(records[0].getMessage().split(" ", 1)[1])


@pytest.mark.parametrize("stage", ["client_initialization", "token_request"])
@pytest.mark.parametrize("exception,category", [
    (ConnectTimeout, "network_timeout"),
    (SSLError, "tls_error"),
    (ProxyError, "proxy_error"),
    (RuntimeError, "unexpected_error"),
])
def test_exception_stages_have_safe_correlated_logs(monkeypatch, caplog, stage, exception, category):
    client = build_client(
        monkeypatch, provider_factory(stage, exception(RAW_SECRET + RAW_TOKEN)),
        **configured_settings(),
    )
    response = client.post("/api/edav-token", headers=connect_identity())
    assert response.status_code == 502
    event = log_event(caplog)
    assert event["diagnostic_id"] == response.json["diagnostic_id"]
    UUID(event["diagnostic_id"])
    assert event["stage"] == stage
    assert event["category"] == category
    assert event["exception_type"] == exception.__name__
    assert event["timestamp_utc"].endswith("+00:00")
    assert set(response.json) == {"error", "message", "diagnostic_id"}
    for sensitive in (RAW_SECRET, RAW_TOKEN):
        assert sensitive not in caplog.text + response.get_data(as_text=True)


def test_entra_rejection_preserves_exact_codes_but_not_description(monkeypatch, caplog):
    failure = {
        "error": "invalid_client",
        "error_codes": [7000215],
        "correlation_id": CORRELATION,
        "error_description": f"AADSTS7000215: {RAW_SECRET} {RAW_TOKEN} user@example.invalid",
        "refresh_token": RAW_TOKEN,
        "client_secret": RAW_SECRET,
    }
    client = build_client(monkeypatch, provider_factory("token_request", failure), **configured_settings())
    response = client.post("/api/edav-token", headers=connect_identity())
    event = log_event(caplog)
    assert event["stage"] == "token_response"
    assert event["error"] == "invalid_client"
    assert event["error_codes"] == [7000215]
    assert event["correlation_id"] == CORRELATION
    assert "secret value" in event["description"]
    assert response.status_code == 502
    for sensitive in (RAW_SECRET, RAW_TOKEN, "user@example.invalid"):
        assert sensitive not in caplog.text + response.get_data(as_text=True)


def test_initialization_extracts_only_structured_aadsts_fields():
    error = ValueError(f"AADSTS90002: {RAW_SECRET}. Correlation ID: {CORRELATION}")
    data = failure_details("client_initialization", exception=error)
    assert data["error_codes"] == [90002]
    assert data["correlation_id"] == CORRELATION
    assert RAW_SECRET not in json.dumps(data)


def test_untrusted_fields_are_bounded_and_never_logged():
    data = failure_details("token_response", result={
        "error": ["invalid_client"],
        "error_codes": [True, -1, 7000215, RAW_SECRET, 9999999999999],
        "correlation_id": RAW_TOKEN,
        "trace_id": RAW_SECRET,
        "error_description": {"secret": RAW_SECRET},
    })
    assert data["error"] == "unrecognized_error"
    assert data["error_codes"] == [7000215]
    assert data["correlation_id"] is None
    assert data["trace_id"] is None
    assert RAW_SECRET not in json.dumps(data)


def test_http_exception_records_status_without_response_body():
    response = Response()
    response.status_code = 403
    response._content = RAW_SECRET.encode()
    data = failure_details("client_initialization", exception=HTTPError(RAW_TOKEN, response=response))
    assert data["upstream_http_status"] == 403
    assert RAW_SECRET not in json.dumps(data)
    assert RAW_TOKEN not in json.dumps(data)


def test_success_is_not_logged_and_uses_existing_response_contract(monkeypatch, caplog):
    client = build_client(monkeypatch, provider_factory("token_request", {
        "access_token": RAW_TOKEN, "expires_in": 3600,
    }), **configured_settings())
    response = client.post("/api/edav-token", headers=connect_identity())
    assert response.status_code == 200
    assert response.json["token"] == RAW_TOKEN
    assert "diagnostic_id" not in response.json
    assert not caplog.records


def test_failed_attempts_have_distinct_references(monkeypatch, caplog):
    client = build_client(monkeypatch, provider_factory("token_request", {
        "error": "invalid_client", "error_codes": [7000215],
    }), **configured_settings())
    first = client.post("/api/edav-token", headers=connect_identity())
    second = client.post("/api/edav-token", headers=connect_identity())
    assert first.json["diagnostic_id"] != second.json["diagnostic_id"]


def test_unauthenticated_request_never_calls_provider(monkeypatch, caplog):
    def forbidden(**kwargs):
        pytest.fail("Unauthenticated request reached MSAL")
    client = build_client(monkeypatch, forbidden, **configured_settings())
    assert client.post("/api/edav-token").status_code == 401
    assert not caplog.records
