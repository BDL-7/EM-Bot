# EM Knowledge Bot

Planning and pilot-support materials for the Equipment Manual Knowledge Retrieval Pilot. The pilot tests whether an EDAV-hosted BaaS microbot can answer natural-language questions from 35 approved, non-PII equipment manuals while remaining grounded in those sources and showing useful citations when the platform supports them.

## Current status

- Phase 0: pilot purpose, boundaries, and technology direction are documented.
- Phase 1: the 35-manual corpus is inventoried and locally verified against the source register.
- Phase 2: the EDAV BaaS configuration package is prepared, but EDAV portal configuration and ingestion have not yet been performed or evidenced.

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
| `PHASE_0_PILOT_BOUNDARY.md` | Agreed pilot scope, decisions, assumptions, and exclusions |
| `PILOT_SOURCE_REGISTER.md` | Authoritative manifest and integrity record for the 35 manuals |
| `PHASE_2_BAAS_CONFIGURATION.md` | EDAV BaaS configuration, discovery, and evidence runbook |
| `PILOT_BOT_INSTRUCTIONS.md` | Copy-ready grounding and safety instructions for EM Knowledge Bot |
| `scripts/verify_source_register.py` | Read-only comparison of the register with the local PDF corpus |
| `Docs/chat-archive-workflow.md` | Local conversation-archive workflow |

## Manual handling

The 35 source PDFs remain local under `Docs/` and are intentionally excluded by `.gitignore`. Git tracks the source register, including filenames, sizes, page counts, and SHA-256 hashes, but it does not publish the manuals themselves.

## Local validation

With Python and `pypdf` available:

```text
python scripts/verify_source_register.py
python -m unittest discover -s tests
```

The first command verifies that every registered manual matches the corresponding local PDF. The second runs the conversation-archive unit tests.

## Scope boundary

The pilot uses EDAV BaaS and the EDAV-hosted UI first. CAT Flask development, Azure Functions, custom RAG, direct MaaS integration, production databases, PII, and competency or authorization decisions are outside the current pilot scope.
