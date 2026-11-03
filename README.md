# EM Knowledge Bot

This repository supports a restricted DEV pilot of an EDAV-hosted knowledge bot
for 35 approved, non-PII equipment manuals. It records the bot requirements,
the disposable Flask parent host used to load the EDAV iframe, and the checks
that keep the pilot grounded and safely bounded.

A detailed [EMLab BaaS architecture image](ppt/images/emlab-baas-architecture.png) shows browser, Flask/Posit Connect, EDAV, authentication, and intended manual-retrieval boundaries. See its [evidence and generation notes](ppt/images/README.md).

For an introduction to apps, chatbots, and this project's use of EDAV Bot as a Service, open the [HTML presentation](ppt/ppt_BAAS/index.html). The [presentation guide](ppt/ppt_BAAS/README.md) explains its offline use, source references, and editable build files.

## In one minute

| Question | Answer |
|---|---|
| What is being tested? | Whether an EDAV BaaS microbot can give grounded, cited answers from the approved equipment manuals. |
| What is implemented? | A restricted Flask/Posit Connect parent host, an exact-origin iframe contract, a no-token mode (EDAV-confirmed) with an Entra client-credentials fallback, and repository-level validation. |
| What is prepared? | The bot instructions, behavior-and-safety record, and ten acceptance tests for release `EMKB-P3-v1.0`. |
| What is not yet validated? | EDAV portal setup, manual ingestion, live bot behavior, and pilot user value. |
| What is outside scope? | Production deployment, custom RAG, CAT integration, live equipment status, PII, and competency or authorization decisions. |

The legacy release ID `EMKB-P3-v1.0` and test IDs `P3-T01` through `P3-T10`
remain controlled identifiers. They are not names for the current work.

## Start here

- [Understand the pilot and its current status](Docs/bot-behavior.md).
- [Review the EDAV bot instructions and safety rules](Docs/bot-instructions.md).
- [Run or review the acceptance tests](Docs/bot-tests.md).
- [Work on the disposable Flask host](host_app/README.md).
- [Run a repository check](scripts/README.md).
- [Handle manuals and other protected local material](Docs/README.md).

## Repository map

| Location | Purpose and boundary |
|---|---|
| `Docs/` | Pilot documentation and the local manuals directory. Its guide identifies what must remain outside Git and deployment. |
| `host_app/` | The isolated Flask/Posit Connect parent host. It embeds an EDAV iframe but does not ingest manuals, retrieve passages, or implement the bot. |
| `scripts/` | Read-only behavior and corpus checks plus the local chat-archive tool. |
| `tests/` | Automated checks for the Flask host, iframe contract, deployment boundary, and archive behavior. |
| `.gitignore` | Enforces exclusion of manuals, local registers, Word records, transcripts, runtime configuration, and generated deployment material. |

## Protected local material

Approved PDF manuals live locally under `Docs/` and are intentionally ignored
by Git. Obtain them only through approved project file sharing. The local
manual register, pilot-boundary record, EDAV BaaS runbook, Word records, and
private chat archives are also excluded from Git.

Do not copy any of those materials into `host_app/`, static assets, templates,
or a deployment bundle. Do not commit secrets, bearer tokens, `.env` files,
client credentials, PII, or source registers.

## Temporary Flask host

`host_app/` is the Posit Connect deployment target for a disposable DEV parent
application. It is not the EM Knowledge Bot, a RAG system, CAT, or a production
application. It remains configuration-pending until EDAV supplies the required
settings and the approved runtime configuration is present. See the
[host guide](host_app/README.md) for its file map and deployment boundary.

## Runtime configuration

The host reads non-secret settings and secrets only from approved runtime
configuration or secret storage. The expected setting names are:

```text
APP_ENV
EDAV_MICROBOT_BASE_URL
EDAV_MICROBOT_ORIGIN
EDAV_MICROBOT_CLIENT_ID
EDAV_MICROBOT_INTEGRATION_ID
EDAV_ENTRA_TENANT_ID
EDAV_ENTRA_CLIENT_ID
EDAV_ENTRA_CLIENT_SECRET
EDAV_MICROBOT_SCOPE
EDAV_AUTH_MODE
```

Keep `EDAV_AUTH_MODE=unconfigured` until the settings for the intended
integration are in place. The host fails closed and does not load the iframe
while configuration is incomplete. Client-credentials mode also requires
`EDAV_ENTRA_CLIENT_SECRET` in Posit Connect **Vars** or an approved secret store.

### Git-backed Posit Connect deployment

Connect treats `host_app/` as the deployment root and imports `app:app` from that directory. The host supports this top-level import while retaining package-relative imports for local tests.

The host page provides mode-specific connection testing. The `/health` endpoint
reports configuration presence rather than confirming a working chat. Token
testing is available only in client-credentials mode.

To refresh the manifest after changing application code or dependencies, run `rsconnect write-manifest api --overwrite --entrypoint app:app host_app`, inspect it, and commit it with the corresponding application changes.

For the first deployment:

1. Open the EDAV Posit Connect Content page.
2. Select **Publish → Import from Git**.
3. Enter `https://github.com/BDL-7/EM-Bot.git` as the repository URL.
4. Select branch `dev` after the feature pull request has been merged.
5. Select `host_app` as the target directory containing `manifest.json`.
6. Enter **Aquarius Assistant - EM Knowledge Bot Pilot Host** as the content title.
7. Deploy the content.

After deployment, require login, restrict access to the designated pilot users
or group, configure runtime variables outside Git, and disable public access.
Select the integration mode only after its required settings are present.

Connect must already be able to read the private GitHub repository through its server-managed GitHub credential or OAuth integration. If the repository cannot be selected or cloned, that is a Connect-side private-repository access issue; do not put GitHub credentials in the repository URL.

The Git-backed content should track `dev` for this DEV pilot. After a successful DEV validation, promote the tested `dev` change to `main` through a separate pull request.

### No-token mode (`EDAV_AUTH_MODE=none`)

For the EDAV-supplied token-free integration, set `EDAV_AUTH_MODE=none`,
`EDAV_MICROBOT_BASE_URL` to the approved environment URL, and
`EDAV_MICROBOT_INTEGRATION_ID` to the identifier supplied by EDAV in Connect.
If `EDAV_MICROBOT_ORIGIN` is set, it must match the base URL's origin.
The iframe URL uses the case-sensitive `IntegrationId` query parameter and
`ShowHeader=false` to hide the EDAV header; it does not use the legacy
`clientId`. The host neither requests nor sends a token
or user profile in this mode. `/api/edav-token` refuses requests. Posit Connect
still controls who can open the host. Loading an iframe does not prove that the
bot can answer: verify a live question after deployment.

The separate `client_credentials` mode retains `EDAV_MICROBOT_CLIENT_ID` and
requires the Entra tenant, application, secret, and scope settings.

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

## Validation

From the repository root:

```text
python scripts/verify_bot.py
python -m unittest discover -s tests
python -m pytest tests/test_app.py tests/test_entra_auth.py tests/test_microbot_contract.py tests/test_deployment_boundary.py
node --test tests/test_microbot_js.mjs tests/test_auth_check_js.mjs
```

The behavior-package check does not need the manual corpus. The source-register
check does, so run it only when the approved local PDFs and local register are
available:

```text
python scripts/verify_source_register.py
```

See [scripts/README.md](scripts/README.md) for inputs and interpretation.

## Contribution and deployment path

`main` is the stable branch. `dev` is the integration branch. Normal changes
begin with an issue-numbered branch based on an up-to-date `dev` and reach
`dev` through a pull request; promotion from `dev` to `main` is a separate pull
request. Posit Connect must target `host_app/`, whose committed
`host_app/manifest.json` lists only the application runtime files.
