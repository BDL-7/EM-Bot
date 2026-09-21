# EM Knowledge Bot

Planning and pilot-support materials for the Equipment Manual Knowledge Retrieval Pilot. The pilot tests whether an EDAV-hosted BaaS microbot can answer natural-language questions from 35 approved, non-PII equipment manuals while remaining grounded in those sources and showing useful citations when the platform supports them.

## Current status

- Phase 0: pilot purpose, boundaries, and technology direction are documented in a local-only record.
- Phase 1: the 35-manual corpus is inventoried and locally verified against a local-only source register.
- Phase 2: the local-only EDAV BaaS configuration package is prepared, but EDAV portal configuration and ingestion have not yet been performed or evidenced.
- Phase 3: release `EMKB-P3-v1.0` defines the bot behavior and ten configuration-level tests, but it has not yet been applied or verified in EDAV.
- A disposable Aquarius Flask parent application is being used to establish the DEV Posit Connect host URL and demonstrate readiness for the EDAV iframe protocol while the Microbot `clientId` and JWT contract remain pending.

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
| `host_app/app.py` | Temporary Flask parent application and safe readiness endpoints |
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

The host intentionally fails closed until EDAV provides the EM Knowledge Bot `clientId` and authoritative JWT acquisition method. Posit Connect identity metadata identifies the signed-in pilot user but is never treated as the EDAV JWT.

Required runtime configuration:

```text
APP_ENV=development
EDAV_MICROBOT_BASE_URL=https://edav-dev-microbot-ui.edav-dev-app.appserviceenvironment.net/
EDAV_MICROBOT_ORIGIN=https://edav-dev-microbot-ui.edav-dev-app.appserviceenvironment.net
EDAV_MICROBOT_CLIENT_ID=
EDAV_AUTH_MODE=unconfigured
```

For local development, create an isolated environment satisfying the host's `>=3.10,<3.14` Python constraint, install `requirements-dev.txt`, and run from the repository root:

```text
flask --app host_app.app run
```

Do not commit `.env` files, tokens, client secrets, subscription keys, or Connect API keys.

### Posit Connect deployment

Generate and inspect the deployment manifest from the isolated host directory. This directory boundary prevents manuals and project-only records from entering the bundle:

```text
rsconnect write-manifest api --entrypoint app:app host_app
```

Deploy that inspected manifest rather than rebuilding the bundle implicitly:

```text
rsconnect deploy manifest -n <saved-server-name> --title "Aquarius Assistant - EM Knowledge Bot Pilot Host" host_app/manifest.json
```

On Connect, require login, restrict access to the designated pilot users or group, configure runtime variables outside Git, and disable public access. The initial deployment should show a controlled configuration-pending state; it must not load an iframe until the `clientId` and approved JWT implementation exist.

The temporary host remains on its draft issue branch. If it is superseded, close the draft PR and delete the branch without merging it into `dev`.

## Local validation

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
