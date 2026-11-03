import json
import subprocess
import sys
from pathlib import Path

import pytest

from host_app.app import create_app, load_settings
from host_app.entra_auth import AccessToken, TokenProviderError


HOST_ROOT = Path(__file__).parents[1] / "host_app"


def test_connect_style_top_level_app_import_succeeds():
    result = subprocess.run(
        [sys.executable, "-c", "import app"],
        cwd=HOST_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr


def build_client(monkeypatch, token_provider_factory=None, **settings):
    """Build an isolated application with explicit, non-secret test configuration."""

    defaults = {
        "APP_ENV": "development",
        "EDAV_MICROBOT_BASE_URL": (
            "https://edav-dev-microbot-ui.edav-dev-app.appserviceenvironment.net/"
        ),
        "EDAV_MICROBOT_ORIGIN": (
            "https://edav-dev-microbot-ui.edav-dev-app.appserviceenvironment.net"
        ),
        "EDAV_MICROBOT_CLIENT_ID": "",
        "EDAV_MICROBOT_INTEGRATION_ID": "",
        "EDAV_AUTH_MODE": "unconfigured",
        "EDAV_ENTRA_TENANT_ID": "",
        "EDAV_ENTRA_CLIENT_ID": "",
        "EDAV_ENTRA_CLIENT_SECRET": "",
        "EDAV_MICROBOT_SCOPE": "",
    }
    defaults.update(settings)
    for name, value in defaults.items():
        monkeypatch.setenv(name, value)
    app = create_app() if token_provider_factory is None else create_app(token_provider_factory)
    app.config.update(TESTING=True)
    return app.test_client()


def connect_identity(username="pilot.user"):
    return {"RStudio-Connect-Credentials": json.dumps({"user": username})}


def configured_settings():
    return {
        "EDAV_MICROBOT_CLIENT_ID": "microbot-client-id",
        "EDAV_AUTH_MODE": "client_credentials",
        "EDAV_ENTRA_TENANT_ID": "tenant-id",
        "EDAV_ENTRA_CLIENT_ID": "microbot-client-id",
        "EDAV_ENTRA_CLIENT_SECRET": "test-only-secret",
        "EDAV_MICROBOT_SCOPE": "api://edav-microbot/.default",
    }


@pytest.fixture()
def client(monkeypatch):
    return build_client(monkeypatch)


def test_index_shows_pending_state_without_creating_iframe(client):
    response = client.get("/")
    body = response.get_data(as_text=True)
    assert response.status_code == 200
    assert "Aquarius Assistant" in body
    assert "EM Knowledge Bot" in body
    assert "Waiting for EDAV" in body
    assert '"ready": false' in body
    assert "<iframe" not in body


def test_index_extracts_only_safe_connect_user_field(client):
    raw_header = json.dumps(
        {"user": "pilot.user", "groups": ["secret-group"], "token": "not-a-jwt"}
    )
    response = client.get("/", headers={"RStudio-Connect-Credentials": raw_header})
    body = response.get_data(as_text=True)
    assert "Authenticated as pilot.user" in body
    assert "secret-group" not in body
    assert "not-a-jwt" not in body


def test_index_includes_safe_connection_testing_guide(client):
    response = client.get("/")
    body = response.get_data(as_text=True)
    assert response.status_code == 200
    assert "Connection testing" in body
    assert 'href="/health"' in body
    assert "POST /api/edav-token" in body
    assert "Chat status" in body
    assert "Do not send tokens, client" in body
    assert "secrets, or full request headers." in body


def test_chat_precedes_collapsed_diagnostics_and_status_is_visible(client):
    body = client.get("/").get_data(as_text=True)
    chat = body.index('id="microbot-heading"')
    status = body.index('id="iframe-status"')
    details = body.index('<details class="technical-details">')
    assert chat < status < details
    assert body.index("Deployment status", details) > details
    assert body.index("Integration readiness", details) > details
    assert body.index("Required from EDAV", details) > details
    assert body.index("Connection testing", details) > details
    assert 'id="open-microbot"' in body
    assert 'aria-live="polite"' in body


def test_health_is_safe_and_reports_pending_edav(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {
        "application": "Aquarius Assistant",
        "auth_mode": "unconfigured",
        "auth_mode_configured": False,
        "bot": "EM Knowledge Bot",
        "client_id_configured": False,
        "integration_id_configured": False,
        "edav_ready": False,
        "entra_client_id_configured": False,
        "entra_tenant_configured": False,
        "environment": "development",
        "microbot_scope_configured": False,
        "status": "healthy",
    }


def test_token_endpoint_requires_connect_identity(monkeypatch):
    client = build_client(monkeypatch, **configured_settings())
    response = client.post("/api/edav-token")
    assert response.status_code == 401
    assert response.get_json()["error"] == "CONNECT_AUTH_REQUIRED"


def test_token_endpoint_fails_closed_without_complete_configuration(client):
    response = client.post("/api/edav-token", headers=connect_identity())
    payload = response.get_json()
    assert response.status_code == 503
    assert payload["error"] == "EDAV_CONFIGURATION_PENDING"
    assert payload["missing_dependencies"] == [
        "EDAV Microbot clientId",
        "EDAV authentication mode",
    ]
    assert "token" not in payload


def test_token_endpoint_returns_token_without_echoing_the_secret(monkeypatch):
    observed = []

    class FakeProvider:
        def __init__(self, **kwargs):
            observed.append(kwargs)

        def get_token(self):
            return AccessToken(value="one.two.three", expires_at=1_700_000_000)

    client = build_client(monkeypatch, FakeProvider, **configured_settings())
    response = client.post("/api/edav-token", headers=connect_identity())
    assert response.status_code == 200
    assert response.get_json() == {
        "token": "one.two.three",
        "expiresAt": 1_700_000_000_000,
    }
    assert observed == [
        {
            "tenant_id": "tenant-id",
            "client_id": "microbot-client-id",
            "client_secret": "test-only-secret",
            "scope": "api://edav-microbot/.default",
        }
    ]
    assert "test-only-secret" not in response.get_data(as_text=True)


def test_token_endpoint_reuses_the_provider_for_matching_configuration(monkeypatch):
    factory_calls = []

    class FakeProvider:
        def __init__(self, **kwargs):
            factory_calls.append(kwargs)

        def get_token(self):
            return AccessToken(value="one.two.three", expires_at=1_700_000_000)

    client = build_client(monkeypatch, FakeProvider, **configured_settings())
    assert client.post("/api/edav-token", headers=connect_identity()).status_code == 200
    assert client.post("/api/edav-token", headers=connect_identity()).status_code == 200
    assert len(factory_calls) == 1


def test_token_endpoint_sanitizes_provider_errors(monkeypatch):
    class FailingProvider:
        def __init__(self, **kwargs):
            pass

        def get_token(self):
            raise TokenProviderError("test-only-secret must never be returned")

    client = build_client(monkeypatch, FailingProvider, **configured_settings())
    response = client.post("/api/edav-token", headers=connect_identity())
    assert response.status_code == 502
    assert response.get_json()["error"] == "EDAV_TOKEN_UNAVAILABLE"
    assert "test-only-secret" not in response.get_data(as_text=True)


def test_no_token_mode_is_ready_with_only_integration_id(monkeypatch):
    client = build_client(
        monkeypatch,
        EDAV_MICROBOT_INTEGRATION_ID="integration-id",
        EDAV_AUTH_MODE="none",
        EDAV_MICROBOT_SCOPE="unused-invalid-scope",
    )
    body = client.get("/", headers=connect_identity()).get_data(as_text=True)
    assert '"ready": true' in body
    assert '"requiresToken": false' in body
    assert '"integrationId": "integration-id"' in body
    assert "Token-free integration configured" in body
    assert "Test token connection" not in body
    assert 'href="/health"' in body
    assert "verify chat response" in body.lower() or "confirm that chat works" in body
    assert "Configured for DEV" not in body
    health = client.get("/health").get_json()
    assert health["edav_ready"] is True
    assert health["auth_mode"] == "none"
    assert health["integration_id_configured"] is True


def test_no_token_mode_requires_integration_id_not_legacy_client_id(monkeypatch):
    client = build_client(
        monkeypatch, EDAV_AUTH_MODE="none", EDAV_MICROBOT_CLIENT_ID="legacy-id"
    )
    assert client.get("/health").get_json()["edav_ready"] is False
    assert "EDAV Microbot IntegrationId" in client.get("/").get_data(as_text=True)


def test_no_token_mode_never_issues_a_token(monkeypatch):
    def unexpected_provider(**kwargs):
        raise AssertionError("no token provider should be created")

    client = build_client(
        monkeypatch,
        unexpected_provider,
        EDAV_MICROBOT_INTEGRATION_ID="integration-id",
        EDAV_AUTH_MODE="none",
    )
    response = client.post("/api/edav-token", headers=connect_identity())
    assert response.status_code == 404
    assert response.get_json()["error"] == "EDAV_TOKEN_NOT_USED"
    assert "token" not in response.get_json()


def test_settings_reject_scope_without_default_suffix(monkeypatch):
    build_client(monkeypatch, EDAV_AUTH_MODE="client_credentials", EDAV_MICROBOT_SCOPE="api://edav-microbot/read")
    with pytest.raises(ValueError, match="/.default"):
        load_settings()


def test_security_headers_allow_only_documented_edav_origin(client):
    response = client.get("/")
    policy = response.headers["Content-Security-Policy"]
    assert (
        "frame-src https://edav-dev-microbot-ui.edav-dev-app.appserviceenvironment.net"
        in policy
    )
    assert "frame-src *" not in policy
    assert response.headers["Cache-Control"] == "no-store"
