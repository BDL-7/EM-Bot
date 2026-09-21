import json

import pytest

from host_app.app import create_app


@pytest.fixture()
def client(monkeypatch):
    monkeypatch.setenv("APP_ENV", "development")
    monkeypatch.setenv(
        "EDAV_MICROBOT_BASE_URL",
        "https://edav-dev-microbot-ui.edav-dev-app.appserviceenvironment.net/",
    )
    monkeypatch.setenv(
        "EDAV_MICROBOT_ORIGIN",
        "https://edav-dev-microbot-ui.edav-dev-app.appserviceenvironment.net",
    )
    monkeypatch.delenv("EDAV_MICROBOT_CLIENT_ID", raising=False)
    monkeypatch.setenv("EDAV_AUTH_MODE", "unconfigured")
    app = create_app()
    app.config.update(TESTING=True)
    return app.test_client()


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


def test_health_is_safe_and_reports_pending_edav(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {
        "application": "Aquarius Assistant",
        "auth_mode_configured": False,
        "bot": "EM Knowledge Bot",
        "client_id_configured": False,
        "edav_ready": False,
        "environment": "development",
        "status": "healthy",
    }


def test_token_endpoint_fails_closed_without_edav_contract(client):
    response = client.post("/api/edav-token")
    payload = response.get_json()
    assert response.status_code == 503
    assert payload["error"] == "EDAV_CONFIGURATION_PENDING"
    assert payload["missing_dependencies"] == [
        "EDAV Microbot clientId",
        "EDAV-approved JWT acquisition method",
    ]
    assert "token" not in payload


def test_security_headers_allow_only_documented_edav_origin(client):
    response = client.get("/")
    policy = response.headers["Content-Security-Policy"]
    assert (
        "frame-src https://edav-dev-microbot-ui.edav-dev-app.appserviceenvironment.net"
        in policy
    )
    assert "frame-src *" not in policy
    assert response.headers["Cache-Control"] == "no-store"
