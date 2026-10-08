# EM Knowledge Bot

For an introduction to apps, chatbots, and this project's use of EDAV Bot as a Service, open the [HTML presentation](ppt/ppt_BAAS/index.html). The [presentation guide](ppt/ppt_BAAS/README.md) explains its offline use, source references, and editable build files.

Planning and pilot-support materials for the Equipment Manual Knowledge Retrieval Pilot. The pilot tests whether an EDAV-hosted BaaS microbot can answer natural-language questions from 35 approved, non-PII equipment manuals while remaining grounded in those sources and showing useful citations when the platform supports them.

## Current status

- Phase 0: pilot purpose, boundaries, and technology direction are documented in a local-only record.
- Phase 1: the 35-manual corpus is inventoried and locally verified against a local-only source register.
- Phase 2: the local-only EDAV BaaS configuration package is prepared, but EDAV portal configuration and ingestion have not yet been performed or evidenced.
- Phase 3: release `EMKB-P3-v1.0` defines the bot behavior and ten configuration-level tests, but it has not yet been applied or verified in EDAV.
- A disposable Aquarius Flask parent application is deployed as the DEV Posit Connect host. It now supports the EDAV-approved Entra client-credentials token flow, but remains inactive until its secret is added in Connect and `EDAV_AUTH_MODE=client_credentials` is set.

This repository does not represent a production application or a production-ready bot. The temporary host is not CAT and is unrelated to the competency-assessment application.

## Pilot path

1. Use the frozen 35-manual source register.
2. Create and configure **EM Knowledge Bot** in EDAV BaaS.
3. Register the manuals through the BaaS-supported source path.
4. Deploy the disposable Aquarius Flask host to restricted DEV content on Posit Connect.
5. Obtain the provisioned `clientId` and supported JWT contract from EDAV.
6. Validate the EDAV-hosted iframe through the temporary parent application.
7. Evaluate grounding, citations, safety behavior, refusals, and user value.
8. Decide separately whether the future CAT application should embed the proven bot.

## Key files

| File | Purpose |
|---|---|
| `host_app/app.py` | Temporary Flask parent application, safe readiness endpoints, and authenticated token route |
| `host_app/entra_auth.py` | Server-only Entra client-credentials token provider with short-lived token caching |
| `host_app/templates/index.html` | Authenticated pilot status and future Microbot container |
| `host_app/static/microbot.js` | Exact-origin, nonce-validated EDAV iframe protocol scaffold |
| `PHASE_3_BEHAVIOR_CONFIGURATION.md` | Versioned grounding, citation, safety, refusal, and uncertainty configuration record |
| `PHASE_3_BEHAVIOR_TESTS.md` | Ten configuration-level acceptance tests for the live EDAV bot |
| `PILOT_BOT_INSTRUCTIONS.md` | Copy-ready grounding and safety instructions for EM Knowledge Bot |
| `scripts/verify_source_register.py` | Read-only comparison of the register with the local PDF corpus |
| `scripts/verify_phase3.py` | Read-only consistency check for the Phase 3 release artifacts |
| `Docs/chat-archive-workflow.md` | Local conversation-archive workflow |

## Manual handling

The 35 source PDFs remain local under `Docs/` and are intentionally excluded by `.gitignore`. The source register also remains local and is not published by Git.

## Local-only project artifacts

The following artifacts are required locally but intentionally excluded from Git:

| Local path or pattern | Purpose |
|---|---|
| `*.docx` | Word planning and reference documents |
| `Docs/*.pdf` | Approved equipment-manual corpus |
| `PILOT_SOURCE_REGISTER.md` | Manual filenames, sizes, page counts, hashes, and verification status |
| `PHASE_0_PILOT_BOUNDARY.md` | Pilot scope and decision record |
| `PHASE_2_BAAS_CONFIGURATION.md` | EDAV configuration, discovery, and evidence runbook |

Removing these files from Git tracking does not delete the local copies. A new clone will not contain them; obtain them through the approved project file-sharing process.

## Temporary Flask host

The host uses Entra client credentials to obtain an app-only EDAV access token. Posit Connect identity metadata identifies the signed-in pilot user and is required before the token route responds, but it is never treated as the EDAV JWT.

Required runtime configuration:

```text
APP_ENV=development
EDAV_MICROBOT_BASE_URL=https://edav-dev-microbot-ui.edav-dev-app.appserviceenvironment.net/
EDAV_MICROBOT_ORIGIN=https://edav-dev-microbot-ui.edav-dev-app.appserviceenvironment.net
EDAV_MICROBOT_CLIENT_ID=
EDAV_ENTRA_TENANT_ID=
EDAV_ENTRA_CLIENT_ID=
EDAV_ENTRA_CLIENT_SECRET=
EDAV_MICROBOT_SCOPE=
EDAV_AUTH_MODE=unconfigured
```

`EDAV_ENTRA_CLIENT_SECRET` is never committed. Add it only through Posit Connect's **Vars** tab or an approved secret store. `EDAV_MICROBOT_SCOPE` must be the complete EDAV-provided scope ending in `/.default`. Use the same Entra application/client ID for `EDAV_ENTRA_CLIENT_ID` and `EDAV_MICROBOT_CLIENT_ID` when EDAV has provisioned one client for both purposes.

For local development, create an isolated Python 3.11.2 environment, install `requirements-dev.txt`, and run from the repository root:

```text
flask --app host_app.app run
```

Do not commit `.env` files, tokens, client secrets, subscription keys, or Connect API keys.

### Git-backed Posit Connect deployment

Git-backed Connect deployment does not require a personal Connect API key. The committed `host_app/manifest.json` identifies the Flask application, and the isolated `host_app/` target directory prevents manuals and project-only records from entering the Git archive used by Connect.

Connect treats `host_app/` as the deployment root and imports `app:app` from that directory. The host supports this top-level import while retaining package-relative imports for local tests.

The deployed host page includes a safe **Connection testing** guide. It directs
pilot users through the safe `/health` readiness check, the browser Network
request to `/api/edav-token`, token-request outcomes, and the EDAV iframe
handoff without exposing access tokens, client secrets, or Connect credentials.

To refresh the manifest after changing application code or dependencies, run `rsconnect write-manifest api --overwrite --entrypoint app:app host_app`, inspect it, and commit it with the corresponding application changes.

For the first deployment:

1. Open the EDAV Posit Connect Content page.
2. Select **Publish → Import from Git**.
3. Enter `https://github.com/BDL-7/EM-Bot.git` as the repository URL.
4. Select branch `dev` after the feature pull request has been merged.
5. Select `host_app` as the target directory containing `manifest.json`.
6. Enter **Aquarius Assistant - EM Knowledge Bot Pilot Host** as the content title.
7. Deploy the content.

After deployment, require login, restrict access to the designated pilot users or group, configure runtime variables outside Git, and disable public access. Configure the non-secret tenant ID, client IDs, and scope first. After the provider code is deployed, add `EDAV_ENTRA_CLIENT_SECRET` in Connect and set `EDAV_AUTH_MODE=client_credentials` last. Until then, the host remains in a controlled configuration-pending state and does not load the iframe.

Connect must already be able to read the private GitHub repository through its server-managed GitHub credential or OAuth integration. If the repository cannot be selected or cloned, that is a Connect-side private-repository access issue; do not put GitHub credentials in the repository URL.

The Git-backed content should track `dev` for this DEV pilot. After a successful DEV validation, promote the tested `dev` change to `main` through a separate pull request.

## Local validation

### Diagnose a live token failure in Connect

After the diagnostic change is promoted from dev to main, use **Update Now**
on the existing main-backed Connect content (directory `host_app`). Confirm
the new revision, Python 3.11.2, and application startup in the deployment log.
Open the signed-in application's root page and click **Test token connection**.
This calls `POST /api/edav-token` on Connect using its saved variables, even
when the Microbot iframe cannot load. It never displays the token.

For a 502, copy the diagnostic reference and locate the matching
`EDAV_AUTH_DIAGNOSTIC` JSON entry in the protected **runtime** log, not just
the build log. Record the UTC timestamp, stage, category, exception type,
Entra error codes, and correlation/trace IDs. Browser responses remain generic.
The description is an allowlisted explanation, not raw Entra text: unrestricted
error descriptions and exceptions may contain credentials or identifying data.
Unknown codes remain available for investigation rather than being guessed.

| Evidence | Next action |
|---|---|
| `client_initialization` | Failure occurred while creating MSAL's client, including authority discovery. Inspect category and codes. |
| `token_request` | An exception occurred while requesting the token; inspect network/TLS/proxy category. |
| `token_response` | Inspect the returned Entra error and AADSTS codes. |
| `token_response_validation` | The returned token/expiration metadata was unusable; inspect provider behavior. |
| `network_timeout`, `connection_error`, `dns_error`, `proxy_error` | Check Connect-server DNS, outbound access to Entra, and approved proxy configuration. A desktop test does not prove server connectivity. |
| `tls_error` | Check the Connect server's trusted CA chain; do not disable certificate verification. |
| `7000215` / `7000222` | Verify the actual secret value for this app, or replace an expired secret in Connect Vars. |
| `700016` / `90002` | Verify the application/tenant combination. |
| `70011` / `500011` | Verify the approved full API scope and its tenant resource registration. The iframe URL is not necessarily the scope. |
| `65001` / `53003` | Investigate consent or Conditional Access with the Entra owner. |

MSAL outbound calls use a 15-second timeout per HTTP operation (not a total
request deadline). Initialization and token-request exceptions are both captured.
For 401, verify Connect identity; for 503, complete configuration. A 502 without
our JSON diagnostic reference may be a proxy failure. A healthy `/health`
only proves configuration presence/shape, not credentials or EDAV acceptance.

Share only the diagnostic entry's safe fields through the approved support
channel. Never export full Network HAR files, successful token responses, raw
headers, or full MSAL result dictionaries. Re-test after the evidence-based
correction; HTTP 200 confirms token acquisition (including cache hits), then
test iframe acknowledgment separately.

MSAL references: [client-credentials acquisition](https://learn.microsoft.com/en-us/entra/msal/python/getting-started/acquiring-tokens)
and [client timeout option](https://learn.microsoft.com/en-us/python/api/msal/msal.application.confidentialclientapplication).

The Phase 3 package can be checked with:

```text
python scripts/verify_phase3.py
python -m unittest discover -s tests
python -m pytest tests/test_app.py tests/test_microbot_contract.py tests/test_deployment_boundary.py
```

If Node.js is available, the executable JavaScript contract tests can also be run with `node --test tests/test_microbot_js.mjs`.

When the local source register and all 35 PDFs are present, the local corpus can also be checked with Python and `pypdf`:

```text
python scripts/verify_source_register.py
```

The corpus command verifies that every registered manual matches the corresponding local PDF. The Phase 3 command checks that its documents agree on the release identifier and ten required behavior tests. The unit-test command checks the conversation-archive workflow.

## Scope boundary

The disposable Flask application is only a parent window for the EDAV-hosted iframe. CAT development, Azure Functions, custom RAG, direct MaaS integration, production databases, PII, and competency or authorization decisions remain outside the pilot scope. The host does not ingest manuals, retrieve passages, call a model, or implement competency-assessment behavior.

## Repository workflow

- `main` is the stable branch and receives reviewed promotion pull requests from `dev`.
- `dev` is the integration branch for active development.
- Each change starts with a GitHub issue and an issue-numbered feature branch created from an up-to-date `dev`, such as `12-add-evaluation-matrix`.
- Feature pull requests target `dev`; feature branches do not merge directly into `main`.
- `dev` is promoted to `main` through a separate pull request after the integrated changes are ready.
- Both `main` and `dev` are protected: changes require pull requests, unresolved review conversations block merging, and force-pushes and branch deletion are disabled.
