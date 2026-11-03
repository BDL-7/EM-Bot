# Flask parent host

`host_app/` is a disposable Flask parent application for the EDAV-hosted EM
Knowledge Bot iframe in restricted DEV Posit Connect. It is not the bot, does
not ingest manuals, does not retrieve passages, and does not implement RAG,
CAT, or a production application.

## File map

| Path | Role |
|---|---|
| `app.py` | Flask entry point, safe readiness endpoints, and the authenticated token route. |
| `entra_auth.py` | Server-only Entra client-credentials provider, used only when `EDAV_AUTH_MODE=client_credentials`. |
| `auth_diagnostics.py` | Allowlisted, credential-safe diagnostics for token failures (`EDAV_AUTH_DIAGNOSTIC` runtime log entries). |
| `static/microbot.js` | Exact-origin, nonce-validated iframe protocol. |
| `static/auth-check.js` | **Test token connection** button on the host page. |
| `templates/index.html` | Parent page and configuration-pending status UI. |
| `manifest.json` | Posit Connect application manifest; the entry point remains `app:app`. |
| `requirements.txt` and `.python-version` | Runtime dependencies and Python version. |

## Configuration and secrets

The required runtime setting names and controlled activation order are in the
[root runtime-configuration guide](../README.md#runtime-configuration). Put
secrets only in approved Posit Connect runtime configuration or secret storage;
never in this folder, Git, application assets, or documentation.

The host remains inactive until EDAV configuration is available. In the
unconfigured state it does not load the iframe and the token route fails closed.
Deployment and connection details are available under the collapsed
**Technical details** section. Closing the chat removes its iframe; reopening
starts a fresh view and may discard the previous chat session. The embedded
chat's appearance and contents are managed separately by EDAV.

## Deployment boundary

Posit Connect must target this directory. `manifest.json` lists the host runtime
files and deliberately excludes this guide, the repository documentation,
manuals, source registers, chat archives, and all other local-only records.

Do not add PDFs, Word records, registers, tokens, templates for documentation,
or new static documentation assets here. Use `python -m pytest
tests/test_deployment_boundary.py` after any deployment-boundary change.
