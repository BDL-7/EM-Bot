# EM Knowledge Bot

Planning and pilot-support materials for the Equipment Manual Knowledge Retrieval Pilot. The pilot tests whether an EDAV-hosted BaaS microbot can answer natural-language questions from 35 approved, non-PII equipment manuals while remaining grounded in those sources and showing useful citations when the platform supports them.

## Current status

- Phase 0: pilot purpose, boundaries, and technology direction are documented in a local-only record.
- Phase 1: the 35-manual corpus is inventoried and locally verified against a local-only source register.
- Phase 2: the local-only EDAV BaaS configuration package is prepared, but EDAV portal configuration and ingestion have not yet been performed or evidenced.
- Phase 3: release `EMKB-P3-v1.0` defines the bot behavior and ten configuration-level tests, but it has not yet been applied or verified in EDAV.

This repository does not represent a production application or a production-ready bot.

## Pilot path

1. Use the frozen 35-manual source register.
2. Create and configure **EM Knowledge Bot** in EDAV BaaS.
3. Register the manuals through the BaaS-supported source path.
4. Test the EDAV-hosted preview or direct UI before building any host application.
5. Evaluate grounding, citations, safety behavior, refusals, and user value.
6. Decide separately whether the future CAT application should embed the proven bot.

## Key files

| File | Purpose |
|---|---|
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

## Local validation

The Phase 3 package can be checked with:

```text
python scripts/verify_phase3.py
python -m unittest discover -s tests
```

When the local source register and all 35 PDFs are present, the local corpus can also be checked with Python and `pypdf`:

```text
python scripts/verify_source_register.py
```

The corpus command verifies that every registered manual matches the corresponding local PDF. The Phase 3 command checks that its documents agree on the release identifier and ten required behavior tests. The unit-test command checks the conversation-archive workflow.

## Scope boundary

The pilot uses EDAV BaaS and the EDAV-hosted UI first. CAT Flask development, Azure Functions, custom RAG, direct MaaS integration, production databases, PII, and competency or authorization decisions are outside the current pilot scope.

## Repository workflow

- `main` is the stable branch and receives reviewed promotion pull requests from `dev`.
- `dev` is the integration branch for active development.
- Each change starts with a GitHub issue and an issue-numbered feature branch created from an up-to-date `dev`, such as `12-add-evaluation-matrix`.
- Feature pull requests target `dev`; feature branches do not merge directly into `main`.
- `dev` is promoted to `main` through a separate pull request after the integrated changes are ready.
- Both `main` and `dev` are protected: changes require pull requests, unresolved review conversations block merging, and force-pushes and branch deletion are disabled.
