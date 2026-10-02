"""Server-side Entra client-credentials token acquisition for the EDAV host."""

from __future__ import annotations

import threading
import time
from dataclasses import dataclass
from typing import Callable

import msal


class TokenProviderError(RuntimeError):
    """A safe, non-provider-specific token acquisition failure."""


@dataclass(frozen=True)
class AccessToken:
    """The short-lived token data that the host may return to its browser client."""

    value: str
    expires_at: int


class EntraTokenProvider:
    """Acquire and cache one app-only EDAV access token at a time."""

    def __init__(
        self,
        *,
        tenant_id: str,
        client_id: str,
        client_secret: str,
        scope: str,
        application_factory: Callable[..., object] = msal.ConfidentialClientApplication,
        clock: Callable[[], float] = time.time,
        refresh_skew_seconds: int = 60,
    ) -> None:
        self._scope = scope
        self._clock = clock
        self._refresh_skew_seconds = refresh_skew_seconds
        self._application = application_factory(
            client_id=client_id,
            authority=f"https://login.microsoftonline.com/{tenant_id}",
            client_credential=client_secret,
        )
        self._cached_token: AccessToken | None = None
        self._lock = threading.Lock()

    def get_token(self) -> AccessToken:
        """Return a cached token unless it is close to expiry, otherwise refresh it."""

        with self._lock:
            now = self._clock()
            if (
                self._cached_token
                and self._cached_token.expires_at - self._refresh_skew_seconds > now
            ):
                return self._cached_token

            result = self._application.acquire_token_for_client(scopes=[self._scope])
            token = result.get("access_token") if isinstance(result, dict) else None
            expires_in = result.get("expires_in") if isinstance(result, dict) else None
            if not isinstance(token, str) or not token:
                raise TokenProviderError("EDAV token acquisition failed")
            try:
                expires_in_seconds = int(expires_in)
            except (TypeError, ValueError) as error:
                raise TokenProviderError("EDAV token acquisition failed") from error
            if expires_in_seconds <= 0:
                raise TokenProviderError("EDAV token acquisition failed")

            self._cached_token = AccessToken(
                value=token,
                expires_at=int(now + expires_in_seconds),
            )
            return self._cached_token
