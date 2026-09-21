"""Disposable Posit Connect host for the EDAV EM Knowledge Bot iframe."""

from __future__ import annotations

import json
import os
from dataclasses import dataclass
from urllib.parse import urlparse

from flask import Flask, jsonify, render_template, request, url_for


DEFAULT_BASE_URL = (
    "https://edav-dev-microbot-ui.edav-dev-app.appserviceenvironment.net/"
)


@dataclass(frozen=True)
class Settings:
    """Non-secret runtime settings for the temporary host."""

    app_env: str
    base_url: str
    origin: str
    client_id: str
    auth_mode: str

    @property
    def missing_dependencies(self) -> list[str]:
        missing: list[str] = []
        if not self.client_id:
            missing.append("EDAV Microbot clientId")
        if self.auth_mode == "unconfigured":
            missing.append("EDAV-approved JWT acquisition method")
        return missing

    @property
    def ready(self) -> bool:
        return not self.missing_dependencies


def _origin_from_url(value: str) -> str:
    parsed = urlparse(value)
    if parsed.scheme not in {"https", "http"} or not parsed.netloc:
        raise ValueError("EDAV_MICROBOT_BASE_URL must be an absolute HTTP(S) URL")
    return f"{parsed.scheme}://{parsed.netloc}"


def load_settings() -> Settings:
    """Load public configuration without reading or logging secrets."""

    base_url = os.getenv("EDAV_MICROBOT_BASE_URL", DEFAULT_BASE_URL).strip()
    derived_origin = _origin_from_url(base_url)
    configured_origin = os.getenv("EDAV_MICROBOT_ORIGIN", derived_origin).strip()
    if configured_origin != _origin_from_url(configured_origin):
        raise ValueError("EDAV_MICROBOT_ORIGIN must contain only scheme and host")
    if configured_origin != derived_origin:
        raise ValueError("EDAV_MICROBOT_ORIGIN must match EDAV_MICROBOT_BASE_URL")
    return Settings(
        app_env=os.getenv("APP_ENV", "development").strip() or "development",
        base_url=base_url,
        origin=configured_origin,
        client_id=os.getenv("EDAV_MICROBOT_CLIENT_ID", "").strip(),
        auth_mode=os.getenv("EDAV_AUTH_MODE", "unconfigured").strip()
        or "unconfigured",
    )


def _connect_user() -> dict[str, object]:
    """Return safe Posit Connect identity fields; never return the raw header."""

    raw_credentials = request.headers.get("RStudio-Connect-Credentials")
    if not raw_credentials:
        return {"authenticated": False, "display_name": "Not provided by Posit Connect"}
    try:
        credentials = json.loads(raw_credentials)
    except (TypeError, json.JSONDecodeError):
        return {"authenticated": False, "display_name": "Invalid Connect identity header"}
    username = credentials.get("user")
    if not isinstance(username, str) or not username.strip():
        return {"authenticated": False, "display_name": "Connect user not identified"}
    return {"authenticated": True, "display_name": username.strip()}


def create_app() -> Flask:
    app = Flask(__name__)

    @app.after_request
    def add_security_headers(response):
        settings = load_settings()
        response.headers["Content-Security-Policy"] = "; ".join(
            [
                "default-src 'self'",
                "script-src 'self'",
                "style-src 'self'",
                f"frame-src {settings.origin}",
                "connect-src 'self'",
                "img-src 'self' data:",
                "object-src 'none'",
                "base-uri 'self'",
                "form-action 'self'",
                "frame-ancestors 'self'",
            ]
        )
        response.headers["Referrer-Policy"] = "no-referrer"
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["Cache-Control"] = "no-store"
        return response

    @app.get("/")
    def index():
        settings = load_settings()
        user = _connect_user()
        browser_config = {
            "baseUrl": settings.base_url,
            "origin": settings.origin,
            "clientId": settings.client_id,
            "ready": settings.ready,
            "tokenEndpoint": url_for("edav_token"),
            "missingDependencies": settings.missing_dependencies,
        }
        return render_template(
            "index.html",
            settings=settings,
            user=user,
            browser_config=browser_config,
        )

    @app.get("/health")
    def health():
        settings = load_settings()
        return jsonify(
            {
                "application": "Aquarius Assistant",
                "bot": "EM Knowledge Bot",
                "environment": settings.app_env,
                "status": "healthy",
                "edav_ready": settings.ready,
                "client_id_configured": bool(settings.client_id),
                "auth_mode_configured": settings.auth_mode != "unconfigured",
            }
        )

    @app.post("/api/edav-token")
    def edav_token():
        settings = load_settings()
        if not settings.ready:
            return (
                jsonify(
                    {
                        "error": "EDAV_CONFIGURATION_PENDING",
                        "message": (
                            "EDAV Microbot authentication is not configured. "
                            "The host will not invent or substitute a JWT flow."
                        ),
                        "missing_dependencies": settings.missing_dependencies,
                    }
                ),
                503,
            )
        return (
            jsonify(
                {
                    "error": "EDAV_AUTH_MODE_UNSUPPORTED",
                    "message": "The EDAV-approved token provider has not been implemented.",
                }
            ),
            501,
        )

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=False)
