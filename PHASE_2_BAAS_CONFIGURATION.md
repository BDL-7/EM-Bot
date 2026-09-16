# Equipment Manual Knowledge Retrieval Pilot

## Phase 2 — EDAV BaaS configuration and discovery

**Document status:** Configuration package and execution record  
**Prepared:** 2026-09-16  
**Pilot corpus:** 35 approved, non-PII equipment-manual PDFs  
**Phase dependency:** Phase 0 boundary documented; Phase 1 source register verified

This document prepares the team to create and test the managed EDAV BaaS bot. It does not claim that a bot has been created, that the manuals have been ingested, or that any EDAV portal action has succeeded. Those facts must be recorded from the EDAV interface.

## 1. What Phase 2 does

Phase 2 turns the pilot boundary into a BaaS configuration:

~~~
35 registered PDFs
        ↓
EDAV BaaS bot configuration
        ↓
EDAV-supported document registration/processing
        ↓
Pilot access group
        ↓
EDAV preview or direct hosted UI
~~~

The CAT application, Flask, Azure Functions, SQL, custom RAG, custom vector search, and RStudio Connect remain out of scope.

## 2. Configuration to enter

Use the following values when the BaaS interface requests them. If a field is not available, record that as a capability finding instead of inventing a substitute.

| Field | Pilot value |
|---|---|
| Bot name | EM Knowledge Bot |
| Short description | Non-PII assistant for finding and explaining instructions in the approved laboratory equipment manuals. |
| Purpose | Test whether EDAV-hosted retrieval can answer natural-language questions with grounded manual references. |
| Knowledge source | The 35 PDFs listed in PILOT_SOURCE_REGISTER.md; no other sources. |
| Data classification | Non-PII equipment-manual content. |
| User scope | Approved CAT pilot users through the available EDAV/Entra access group. Record the exact group or assignment in the evidence log. |
| Model | One model already approved for this use case and exposed by BaaS; the provisioned options are GPT 5.1, GPT 5.2, and GPT 5.4-mini. Do not add an unapproved model. |
| Refresh policy | No source updates during pilot development. Any later replacement creates a new corpus version and requires a new verification. |
| Interface | EDAV-hosted preview/direct UI first. An iframe host is a contingency only. |

## 3. Bot behavior instructions

The copy-paste-ready instruction set is maintained in PILOT_BOT_INSTRUCTIONS.md. Enter it in the BaaS behavior, system-instructions, or assistant-guidance field if that field is available.

The instructions are a pilot requirement, not a guarantee that BaaS will enforce every behavior. Enforcement must be tested with the evaluation questions.

## 4. Source-registration procedure

Use the source register as the upload manifest:

1. Open PILOT_SOURCE_REGISTER.md and use all 35 registered PDF rows.
2. Preserve each filename and source file unchanged.
3. Register or upload only those 35 PDFs through the BaaS-supported path.
4. Record the BaaS document identifier, status, processing result, and date for each file when the platform exposes them.
5. Record any rejection, OCR limitation, page-citation limitation, or processing warning verbatim in the evidence log.
6. Do not add Excel, SQL, Dataverse, Power Platform, employee, competency, or live equipment data.
7. Do not rename files to work around a platform error without recording a new source-register version.

The BaaS interface may require a Data Lake location. If so, use only the provisioned DEV location required by that workflow. Data Lake storage by itself does not prove that the PDFs are searchable; the BaaS processing/availability result must be observed.

## 5. Hands-on discovery sequence

Perform these steps in the EDAV environment using the access already granted to the team.

### Step A — Confirm access

- Sign in using the approved CDC identity.
- Confirm the CAT team member can reach the BaaS area.
- Confirm the assigned Admin, Developer, or Analyst persona can perform the needed action.
- Confirm a pilot user can reach the preview/test experience.

### Step B — Create or request the bot

- Find the BaaS create, configure, or request workflow.
- Enter the bot name, description, purpose, and user scope above.
- Record whether creation is self-service or requires a request.
- Record the resulting bot identifier and environment. If the platform calls it clientId, record that exact value in the evidence log; do not place secrets there.

### Step C — Attach the corpus

- Find the BaaS knowledge-source, document, file, or data-source control.
- Register the 35 PDFs from the source register.
- Record whether upload is direct or requires Data Lake staging.
- Wait for the platform's processing/availability status.
- Record the count accepted, rejected, pending, or failed.

### Step D — Configure behavior and model

- Enter the pilot instructions.
- Select only a model exposed as approved for this use case.
- Configure the available citation, source-display, or grounding options.
- Assign only the pilot user scope.
- Save the configuration and record its version, timestamp, and visible settings.

### Step E — Test the direct UI

- Open the EDAV preview or direct hosted bot page.
- Authenticate normally.
- Ask one supported question tied to a known manual.
- Confirm that an answer appears.
- Confirm whether a source citation or page reference appears.
- Record the exact result, including any error or missing citation.

Do not build a CAT application or iframe wrapper before this direct-UI test is complete.

## 6. Capability and evidence matrix

Complete this table from observed EDAV screens or responses. “Unknown” is an acceptable result during the first pass.

| Capability | Status | Evidence or location | Persona used | Date |
|---|---|---|---|---|
| Reach BaaS area | Not yet observed |  |  |  |
| Create bot self-service | Not yet observed |  |  |  |
| Bot request path | Not yet observed |  |  |  |
| Bot identifier/clientId shown | Not yet observed |  |  |  |
| Direct PDF upload | Not yet observed |  |  |  |
| Data Lake source required | Not yet observed |  |  |  |
| 35 PDFs accepted | Not yet observed |  |  |  |
| Document processing status shown | Not yet observed |  |  |  |
| Source/citation settings available | Not yet observed |  |  |  |
| Page-level citations available | Not yet observed |  |  |  |
| Approved model selectable | Not yet observed |  |  |  |
| Pilot group assignment available | Not yet observed |  |  |  |
| Preview/direct UI available | Not yet observed |  |  |  |
| Normal Entra authentication works | Not yet observed |  |  |  |

## 7. Configuration evidence record

Complete this section after the portal work. Do not fill unknown values from memory or assumption.

~~~
Bot name:
EDAV environment:
Bot identifier/clientId (if provided):
Configuration owner:
Configuration date:
Persona used:
Pilot access group:
Model selected:
Source path (direct upload or Data Lake):
Registered:
Accepted:
Rejected:
Pending:
Processing warnings:
Citation behavior observed:
Preview/direct URL or portal location:
First smoke-test question:
First smoke-test result:
Known limitations:
~~~

Do not paste JWTs, client secrets, subscription keys, or other credentials into this file.

## 8. Phase 2 completion gate

Phase 2 is complete only when all of the following are evidenced:

- A BaaS bot was created or a documented request was submitted.
- The bot has a recorded name, environment, and identifier if the platform supplies one.
- The 35 registered PDFs were submitted through the supported source path.
- The platform's accepted/processed/rejected result is recorded.
- Pilot access is limited to the approved user scope.
- The behavior instructions and model choice are recorded.
- The EDAV preview/direct UI was opened, or the precise reason it was unavailable is recorded.
- At least one supported question was tested.
- Citation/source behavior was observed and recorded, including if unavailable.
- No CAT application, custom RAG, or insecure host workaround was introduced.

## 9. Failure handling

| Observed problem | First response | Scope boundary |
|---|---|---|
| Cannot reach BaaS | Check persona, project assignment, and environment | Do not build a custom chatbot |
| Cannot create bot | Record self-service/request path and required role | Do not create a parallel AI stack |
| PDF upload fails | Record format, size, OCR, or permission error | Do not build custom parsing yet |
| Data Lake required | Use only the provisioned source location if accessible | Storage does not prove ingestion |
| Citation missing | Record the platform behavior and settings exposed | Do not promise page citations |
| Preview unavailable | Record the hosted-UI/authentication blocker | Consider iframe host only after contract is clear |
| Model unavailable | Use only an approved exposed option | Do not request or add unapproved models |
| Poor answer quality | Separate retrieval, source, instruction, and model observations | Correct configuration and retest before custom RAG |

## 10. Handoff to Phase 3

After the completion gate, Phase 3 will configure and test grounding, citation, safety, refusal, and uncertainty behavior. Phase 3 must use the actual BaaS capabilities observed here; it must not assume that a documented feature exists merely because it was requested in the instructions.

The prepared Phase 3 package is maintained in [PHASE_3_BEHAVIOR_CONFIGURATION.md](PHASE_3_BEHAVIOR_CONFIGURATION.md), [PILOT_BOT_INSTRUCTIONS.md](PILOT_BOT_INSTRUCTIONS.md), and [PHASE_3_BEHAVIOR_TESTS.md](PHASE_3_BEHAVIOR_TESTS.md). Preparation of those artifacts does not satisfy this Phase 2 gate or prove that the behavior has been applied in EDAV.
