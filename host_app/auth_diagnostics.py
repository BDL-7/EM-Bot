"""Bounded, allowlisted diagnostics; never serialize raw provider responses."""

import re
import socket
from datetime import datetime, timezone
from uuid import UUID, uuid4

from requests import exceptions as request_errors


OAUTH_ERRORS = {
    "invalid_client", "invalid_scope", "invalid_resource", "invalid_request",
    "unauthorized_client", "access_denied", "invalid_grant", "interaction_required",
    "temporarily_unavailable", "server_error",
}
DESCRIPTIONS = {
    7000215: "Entra rejected the client secret; verify the secret value and app registration.",
    7000222: "The client secret has expired; replace it in approved runtime storage.",
    7000218: "Entra requires a client credential.",
    700016: "Application not found in the selected tenant; verify tenant and client ID.",
    90002: "Tenant not found; verify the tenant ID.",
    70011: "Entra rejected the scope; verify the complete approved resource scope.",
    500011: "Resource principal not found in the tenant; verify the scope resource and tenant.",
    65001: "Consent is required for the requested resource.",
    53003: "Access was blocked by Conditional Access policy.",
}


def _uuid(value):
    try:
        return str(UUID(value)) if isinstance(value, str) else None
    except ValueError:
        return None


def failure_details(stage, *, result=None, exception=None):
    """Keep codes and UUIDs, replacing unrestricted descriptions with safe summaries."""
    data = {
        "stage": stage,
        "category": "provider_error" if result is not None else "unexpected_error",
        "exception_type": None,
        "error": None,
        "error_codes": [],
        "correlation_id": None,
        "trace_id": None,
        "description": "Token acquisition failed; use the stage and codes to investigate.",
    }
    if isinstance(result, dict):
        error = result.get("error")
        data["error"] = error if isinstance(error, str) and error in OAUTH_ERRORS else "unrecognized_error"
        codes = result.get("error_codes", [])
        if isinstance(codes, list):
            data["error_codes"] = list(dict.fromkeys(
                code for code in codes[:16]
                if type(code) is int and 0 < code < 1_000_000_000
            ))
        data["correlation_id"] = _uuid(result.get("correlation_id"))
        data["trace_id"] = _uuid(result.get("trace_id"))
    # MSAL can embed Entra errors in initialization exceptions. Extract only
    # known structural fields, never URLs, exception text, or response bodies.
    description = result.get("error_description", "") if isinstance(result, dict) else ""
    if exception is not None:
        description = str(exception)
        data["exception_type"] = type(exception).__name__ if type(exception) in {
            ValueError, TypeError, RuntimeError, KeyError, OSError,
            request_errors.ConnectTimeout, request_errors.ReadTimeout,
            request_errors.Timeout, request_errors.ProxyError, request_errors.SSLError,
            request_errors.ConnectionError, request_errors.HTTPError,
        } else "Exception"
        chain, current = [], exception
        while current is not None and len(chain) < 8 and all(current is not item for item in chain):
            chain.append(current)
            current = current.__cause__ or current.__context__
        kinds = (
            (request_errors.ProxyError, "proxy_error", "Connection through the configured proxy failed."),
            (request_errors.SSLError, "tls_error", "TLS verification or negotiation failed; check the server trust chain."),
            (request_errors.Timeout, "network_timeout", "The outbound Entra request timed out."),
            (socket.gaierror, "dns_error", "The server could not resolve an outbound host name."),
            (request_errors.ConnectionError, "connection_error", "The server could not establish the outbound Entra connection."),
            (request_errors.HTTPError, "http_error", "Entra discovery or token HTTP request failed."),
            (ValueError, "configuration_error", "MSAL rejected configuration or authority discovery."),
        )
        for kind, category, summary in kinds:
            if any(isinstance(item, kind) for item in chain):
                data.update(category=category, description=summary)
                break
        if isinstance(exception, request_errors.HTTPError):
            response = exception.response
            status = getattr(response, "status_code", None)
            if type(status) is int and 100 <= status <= 599:
                data["upstream_http_status"] = status
    if isinstance(description, str):
        # Bound inspection and output; raw descriptions never leave this function.
        description = description[:8192]
        extracted = [int(code) for code in re.findall(r"\bAADSTS([0-9]{4,9})\b", description)[:16]]
        data["error_codes"] = list(dict.fromkeys(data["error_codes"] + extracted))[:16]
        for field, label in (("correlation_id", "Correlation ID"), ("trace_id", "Trace ID")):
            match = re.search(label + r":\s*([0-9a-fA-F-]{36})\b", description)
            if data[field] is None and match:
                data[field] = _uuid(match.group(1))
    for code in data["error_codes"]:
        if code in DESCRIPTIONS:
            data["description"] = DESCRIPTIONS[code]
            break
    return data


def diagnostic_event(details):
    return {
        "event": "edav_token_failure",
        "diagnostic_id": str(uuid4()),
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        **details,
    }
