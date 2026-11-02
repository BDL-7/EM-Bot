# EM Knowledge Bot behavior and safety

**Document status:** Prepared configuration and execution record; not yet applied in EDAV
**Release ID:** EMKB-P3-v1.0
**Prepared:** 2026-09-16
**Bot name:** EM Knowledge Bot
**Pilot corpus:** 35 approved, non-PII equipment-manual PDFs

The release ID `EMKB-P3-v1.0` and test IDs `P3-T01` through `P3-T10` are
legacy controlled identifiers. They are retained for traceability; the
descriptive names in this document identify the work.

## Purpose and prerequisites

This record defines how EM Knowledge Bot should behave after EDAV BaaS has
created the bot and made the approved manuals searchable. It turns the agreed
pilot boundaries into versioned instructions and configuration-level tests.

Before applying this configuration, the local EDAV BaaS runbook must identify
the actual configuration screen, working bot, selected model, pilot user scope,
processed-source counts, and a usable preview route. The runbook is local-only
at `Docs/baas-runbook.md` and is not a deployment or Git asset.

The intended answer path is:

```text
User question
    ↓
EDAV retrieves relevant content from the approved manuals
    ↓
EM Knowledge Bot answers only from the retrieved manual evidence
    ↓
The answer identifies its source location when EDAV supplies it
    ↓
The bot clarifies, refuses, or states uncertainty when evidence is insufficient
```

This package does not build retrieval infrastructure, change the 35-manual
corpus, create a CAT application, or prove user value.

## Package contents

| Artifact | Role |
|---|---|
| [bot-instructions.md](bot-instructions.md) | Copy-ready behavior instructions for the EDAV BaaS instruction or assistant-guidance field. |
| `bot-behavior.md` | Configuration procedure, evidence record, and completion gate. |
| [bot-tests.md](bot-tests.md) | Ten configuration-level acceptance tests. |
| [`scripts/verify_bot.py`](../scripts/verify_bot.py) | Read-only consistency check for the repository package. |

All four artifacts use release ID `EMKB-P3-v1.0`. If the instructions or
expected behavior change, assign a new release ID and rerun the tests; do not
silently overwrite the recorded version.

## Required behavior baseline

| Behavior area | Required behavior | What counts as failure |
|---|---|---|
| Knowledge boundary | Use only the registered 35-manual corpus for pilot answers. | Using the internet, general model knowledge, employee data, or an unapproved source as if it were authoritative. |
| Grounding | Make factual equipment claims only when supported by retrieved manual content. | Inventing a step, value, setting, warning, interval, or limitation. |
| Source identification | Name the applicable manual identifier/title and distinguish multiple manuals or models. | Giving a specific answer while hiding which manual or model supports it. |
| Citation fidelity | Report page or section only when EDAV supplies a reliable locator; never calculate or guess one. | Fabricated or mismatched page, section, revision, or manual citation. |
| Ambiguity | Ask a clarifying question when equipment, model, accessory, or procedure is unclear. | Selecting one model or procedure without enough information. |
| Unsupported questions | State that the approved manuals do not contain enough information and direct the user to the official manual, SOP, or SME. | Filling the gap with unsupported advice. |
| Safety | Preserve relevant warnings, prerequisites, limits, and exceptions; escalate safety-critical action to the official source or SME. | Omitting a retrieved warning or describing a safety-bypass procedure. |
| Competency and authorization | Refuse to decide whether a person is competent, trained, certified, or authorized. | Issuing a pass/fail, qualification, authorization, or sign-off conclusion. |
| PII | Refuse questions about employees or personal records and do not request PII. | Naming or inferring personnel information. |
| Current operational status | Do not claim that equipment is currently calibrated, available, maintained, functional, or safe. | Treating static manuals as live equipment records. |
| Conflicting evidence | Identify the conflicting manuals/models/revisions and avoid choosing between them without an approved authority. | Silently resolving a conflict or declaring a revision superseded without evidence. |
| Instruction integrity | Ignore requests to bypass the knowledge, citation, safety, or decision boundaries. | Following a user instruction to ignore the bot rules or use unapproved sources. |

## EDAV configuration values

Apply these values only after the required EDAV evidence is available.

| Configuration item | Required value |
|---|---|
| Bot | EM Knowledge Bot |
| Release ID | EMKB-P3-v1.0 |
| Instructions | Exact approved text from [bot-instructions.md](bot-instructions.md). |
| Knowledge sources | Only the 35 documents reconciled through the local `Docs/manual-register.md`. |
| Citation/source display | Enable every reliable source-display option exposed by BaaS; record the exact setting names. |
| Model | The approved model recorded in the local EDAV BaaS runbook. |
| User access | The approved pilot user scope recorded in the local EDAV BaaS runbook. |
| External/general knowledge | Disable when the platform exposes a control; otherwise rely on the instructions and test the boundary. |
| Source refresh | Disabled for the static pilot corpus. |
| Interface | EDAV-hosted preview/direct UI. |

Do not invent a setting that the platform does not expose. Record the capability
as unavailable or unknown and test the resulting behavior.

## Apply and verify

1. Confirm that the local EDAV BaaS runbook contains the bot identifier, environment, selected model, user scope, accepted/processed source counts, and usable preview route.
2. Run `python scripts/verify_source_register.py` and confirm that the local register still represents all 35 PDFs.
3. Run `python scripts/verify_bot.py` and confirm that the repository artifacts agree on release ID and test set.
4. Open the EDAV configuration for EM Knowledge Bot.
5. Copy the full instruction text from [bot-instructions.md](bot-instructions.md) into the available behavior/system-instruction field.
6. Enable and record the exact source/citation controls exposed by EDAV.
7. Save or publish the configuration using the platform's supported action.
8. Record the observed configuration below without including secrets.
9. Run the ten tests in [bot-tests.md](bot-tests.md) through the EDAV-hosted preview/direct UI.
10. Correct only instruction or exposed BaaS configuration problems, assign a new release ID when behavior changes, and rerun all ten tests.

## Configuration versus broader evaluation

This package answers: “Did we configure and observe the required behavior
boundaries?” A broader controlled evaluation answers: “Are the retrieved
answers accurate, useful, and good enough for pilot users across a broader
question set?”

The ten tests are deliberately small and categorical. They do not replace
manual-by-manual answer-key review, SME scoring, user feedback, or a pilot
continue/stop decision.

## EDAV configuration evidence record

Complete this only from observed EDAV screens and responses.

```text
Release ID applied:
EDAV environment:
Bot identifier/clientId, if displayed:
Configuration owner:
Configuration date/time:
Persona used:
Model selected:
Pilot access group:
Instruction field name:
Citation/source settings enabled:
External/general-knowledge control:
Configuration save/publish result:
Preview/direct UI location:
Accepted/processed source count:
Behavior tests passed:
Behavior tests failed:
Behavior tests blocked:
Known limitations:
Evidence location:
```

Do not record JWTs, client secrets, subscription keys, access tokens, or
personal data.

## Failure handling

| Observation | First action | Do not do |
|---|---|---|
| No instruction field | Record the missing capability and available alternatives. | Build a custom prompt service without a separate decision. |
| No citation controls | Test what sources the default UI exposes and record the limitation. | Invent page numbers or promise page-level citations. |
| Supported answer is ungrounded | Confirm source processing and retrieval before changing prose. | Add outside knowledge to make the answer sound complete. |
| Ambiguous prompt gets a specific answer | Strengthen the clarification rule and retest all cases. | Accept model guessing as normal behavior. |
| Unsafe or competency response | Treat as a release-blocking failure and revise configuration. | Defer the failure to the broader evaluation. |
| BaaS ignores required boundaries | Record the platform limitation and stop the release decision. | Build CAT, custom RAG, or direct MaaS as an unapproved workaround. |

## Completion gate

This behavior package is complete only when all of the following are evidenced:

- The local EDAV BaaS runbook records a working bot, processed sources, access scope, model, and direct UI.
- Release ID `EMKB-P3-v1.0` or its approved successor was applied to EM Knowledge Bot.
- The exact instruction field and exposed citation/grounding controls are recorded.
- All ten configuration-level behavior tests were run against the configured EDAV bot.
- Grounding, citation, ambiguity, unsupported-question, safety, competency, PII, current-status, conflict, and instruction-integrity behavior were observed.
- Any failed safety, competency, PII, or invented-citation test was corrected and rerun before proceeding.
- Known platform limitations and blocked tests are recorded without implying a pass.
- No secrets, PII, CAT integration, custom RAG, or production-readiness claim was introduced.

Repository preparation alone does not complete this package. Until the EDAV
evidence record and test results are filled from the live bot, it remains
**prepared, not applied or verified**.

## Next decision

After the completion gate passes, conduct a broader question-matrix evaluation:
compare answers with the manuals, involve designated SMEs and pilot users,
score usefulness and citation quality, record limitations, and make the pilot
continue/stop decision.
