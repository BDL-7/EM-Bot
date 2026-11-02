# Documentation and local manuals

`Docs/` contains the repository's project documentation and may also contain
the approved equipment-manual PDFs on a project member's local machine.

## Read the tracked documentation

- [Bot instructions](bot-instructions.md): the copy-ready EDAV behavior and safety requirements.
- [Bot behavior and safety](bot-behavior.md): the configuration record, evidence expectations, and completion gate.
- [Bot acceptance tests](bot-tests.md): the ten live-EDAV tests and pass rules.
- [Chat archive workflow](chat-archive-workflow.md): how to retain private local conversation history without publishing it.

## Do not publish or deploy local material

The PDF manuals are intentionally ignored by Git as `Docs/*.pdf`. Obtain them
only through approved project file sharing; do not add them to a clone by
committing, copying, or deploying them.

The following local-only files, when provided through the approved process, are
also ignored:

- `Docs/manual-register.md`
- `Docs/pilot-boundary.md`
- `Docs/baas-runbook.md`
- Word planning or reference records (`*.docx`)
- private chat archives under `.local/chat-archives/`

Manuals, source registers, Word records, and private chat archives are not
deployment assets. Never copy them into Git, `host_app/`, static assets,
templates, or deployment bundles. Keep credentials, tokens, bearer headers,
PII, and secrets out of every documentation file.
