"""Disposable Posit Connect host for the EDAV EM Knowledge Bot iframe."""

from __future__ import annotations

import json
import os
from dataclasses import dataclass
from typing import Callable
from urllib.parse import urlparse

from flask import Flask, jsonify, render_template, request, url_for

if __package__:
    from .entra_auth import EntraTokenProvider, TokenProviderError
else:
    from entra_auth import EntraTokenProvider, TokenProviderError


DEFAULT_BASE_URL = (
    "https://edav-dev-microbot-ui.edav-dev-app.appserviceenvironment.net/"
)


@dataclass(frozen=True)
class Settings:
    """Runtime settings for the temporary host; values are never logged."""

    app_env: str
    base_url: str
    origin: str
    client_id: str
    auth_mode: str
    entra_tenant_id: str
    entra_client_id: str
    entra_client_secret: str
    microbot_scope: str

    @property
    def missing_dependencies(self) -> list[str]:
        missing: list[str] = []
        if not self.client_id:
            missing.append("EDAV Microbot clientId")
        if self.auth_mode != "client_credentials":
            missing.append("EDAV client-credentials authentication")
        else:
            if not self.entra_tenant_id:
                missing.append("EDAV Entra tenant ID")
            if not self.entra_client_id:
                missing.append("EDAV Entra client ID")
            if not self.entra_client_secret:
                missing.append("EDAV Entra client secret")
            if not self.microbot_scope:
                missing.append("EDAV Microbot scope")
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
    """Load configuration without logging or returning the client secret."""

    base_url = os.getenv("EDAV_MICROBOT_BASE_URL", DEFAULT_BASE_URL).strip()
    derived_origin = _origin_from_url(base_url)
    configured_origin = os.getenv("EDAV_MICROBOT_ORIGIN", derived_origin).strip()
    if configured_origin != _origin_from_url(configured_origin):
        raise ValueError("EDAV_MICROBOT_ORIGIN must contain only scheme and host")
    if configured_origin != derived_origin:
        raise ValueError("EDAV_MICROBOT_ORIGIN must match EDAV_MICROBOT_BASE_URL")
    microbot_scope = os.getenv("EDAV_MICROBOT_SCOPE", "").strip()
    if microbot_scope and not microbot_scope.endswith("/.default"):
        raise ValueError("EDAV_MICROBOT_SCOPE must use the /.default scope")
    return Settings(
        app_env=os.getenv("APP_ENV", "development").strip() or "development",
        base_url=base_url,
        origin=configured_origin,
        client_id=os.getenv("EDAV_MICROBOT_CLIENT_ID", "").strip(),
        auth_mode=os.getenv("EDAV_AUTH_MODE", "unconfigured").strip()
        or "unconfigured",
        entra_tenant_id=os.getenv("EDAV_ENTRA_TENANT_ID", "").strip(),
        entra_client_id=os.getenv("EDAV_ENTRA_CLIENT_ID", "").strip(),
        entra_client_secret=os.getenv("EDAV_ENTRA_CLIENT_SECRET", "").strip(),
        microbot_scope=microbot_scope,
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


def create_app(
    token_provider_factory: Callable[..., EntraTokenProvider] = EntraTokenProvider,
) -> Flask:
    app = Flask(__name__)
    token_provider: EntraTokenProvider | None = None
    token_provider_signature: tuple[str, str, str, str] | None = None

    def get_token_provider(settings: Settings) -> EntraTokenProvider:
        """Reuse the in-process provider only while its configuration is unchanged."""

        nonlocal token_provider, token_provider_signature
        signature = (
            settings.entra_tenant_id,
            settings.entra_client_id,
            settings.entra_client_secret,
            settings.microbot_scope,
        )
        if token_provider is None or signature != token_provider_signature:
            token_provider = token_provider_factory(
                tenant_id=settings.entra_tenant_id,
                client_id=settings.entra_client_id,
                client_secret=settings.entra_client_secret,
                scope=settings.microbot_scope,
            )
            token_provider_signature = signature
        return token_provider

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
                "entra_tenant_configured": bool(settings.entra_tenant_id),
                "entra_client_id_configured": bool(settings.entra_client_id),
                "microbot_scope_configured": bool(settings.microbot_scope),
                "auth_mode_configured": settings.auth_mode == "client_credentials",
            }
        )

    @app.post("/api/edav-token")
    def edav_token():
        settings = load_settings()
        user = _connect_user()
        if not user["authenticated"]:
            return (
                jsonify(
                    {
                        "error": "CONNECT_AUTH_REQUIRED",
                        "message": "A valid Posit Connect user is required.",
                    }
                ),
                401,
            )
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
        try:
            token = get_token_provider(settings).get_token()
        except TokenProviderError:
            return (
                jsonify(
                    {
                        "error": "EDAV_TOKEN_UNAVAILABLE",
                        "message": "Unable to obtain an EDAV access token.",
                    }
                ),
                502,
            )
        except Exception:
            return (
                jsonify(
                    {
                        "error": "EDAV_TOKEN_UNAVAILABLE",
                        "message": "Unable to obtain an EDAV access token.",
                    }
                ),
                502,
            )
        return jsonify({"token": token.value, "expiresAt": token.expires_at})

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=False)
