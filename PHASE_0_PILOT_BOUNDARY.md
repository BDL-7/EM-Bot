# Equipment Manual Knowledge Retrieval Pilot

## Phase 0 — Pilot boundary and scope

**Document status:** Agreed planning boundary  
**Recorded:** 2026-09-16  
**Purpose:** Establish what this proof of concept will test, what it will not test, and which platform path will be used before further implementation.

This document records the Phase 0 decisions for the Equipment Manual Knowledge Retrieval Pilot. It is a scope and decision record, not a production design and not a claim that the EDAV bot has already been configured.

## 1. Pilot purpose

The pilot will test whether an EDAV-hosted microbot can:

1. Accept natural-language questions about laboratory equipment.
2. Retrieve relevant information from the approved equipment-manual collection.
3. Produce answers grounded in those manuals.
4. Provide useful manual, section, and page references when available.
5. Tell the user when the answer is not found or is outside the approved source collection.
6. Provide enough value to justify a later CAT application integration.

This is a technical and user-value proof of concept. It is not a production application, a replacement for official manuals, or an authority for laboratory decisions.

## 2. Agreed pilot boundaries

| Boundary | Agreed position |
|---|---|
| Knowledge source | The approved equipment-manual collection is the knowledge base. |
| Corpus size | The pilot targets all 35 approved manuals; the corpus will not be reduced to a smaller sample. |
| Data type | Non-PII manual content only. |
| Question type | Information retrieval, explanation, procedure lookup, troubleshooting, settings, maintenance, and safety information contained in the manuals. |
| Decision authority | The bot will not make competency determinations, authorize equipment use, or replace SME review. |
| Manual changes | Manuals are treated as static during pilot development; updates are outside this pilot iteration. |
| Other data | No Excel workbooks, SQL tables, Dataverse, Power Platform, employee records, or production CAT data. |
| Hosting direction | Use EDAV BaaS and its hosted bot experience as the primary path. |
| CAT application | The future CAT application is not required to create or test the pilot bot. |
| First user interface | Try the EDAV-hosted preview/direct interface first. |
| Host application | Build a thin iframe host only if the EDAV-hosted interface is unavailable or unusable and the authentication contract can be implemented safely. |
| RStudio Connect | An optional hosting surface only; it is not the bot, retrieval engine, model service, or authentication service. |
| MaaS | Do not use direct MaaS model APIs while BaaS can support the pilot. |
| Custom AI infrastructure | Do not build custom parsing, chunking, embeddings, vector search, retrieval APIs, model hosting, or custom RAG for this pilot. |
| Production readiness | Not an objective of this phase or pilot. |

## 3. What the bot must and must not do

### Required behavior

The pilot bot configuration should instruct the bot to:

- Answer from the approved manual collection.
- Identify the applicable equipment and manual when possible.
- Preserve warnings, prerequisites, conditions, limits, and exceptions.
- Cite the manual title or identifier and page or section whenever the platform provides that information.
- Distinguish a manual-backed answer from a general explanation.
- State clearly when the manuals do not contain an answer.
- Ask for clarification when the equipment or procedure is ambiguous.
- Direct users to the official manual, applicable SOP, or an SME for safety-critical action.
- Refuse competency, authorization, certification, or sign-off decisions.
- Avoid claims about current calibration, equipment availability, maintenance status, or operational status.

### Explicitly prohibited behavior

The pilot bot must not:

- Invent procedures, values, warnings, maintenance intervals, or operating limits.
- Treat a generated answer as a substitute for the official manual or SOP.
- Decide whether a person is competent or authorized to operate equipment.
- Use PII or answer questions about employees.
- Use CAT assessment records or other production data to personalize answers.
- Claim that an answer is supported by a manual when the source cannot be identified.
- Expand its knowledge boundary to the general internet or unapproved documents without a separate decision.

## 4. Selected implementation direction

The smallest credible path is:

\`\`\`
Approved equipment manuals
        ↓
EDAV BaaS bot configuration
        ↓
EDAV-managed document processing and retrieval
        ↓
EDAV-approved model
        ↓
EDAV-hosted preview/direct Microbot UI
        ↓
Controlled questions and SME review
        ↓
Decision about future CAT integration
\`\`\`

The CAT application is a later consumer of a working bot:

\`\`\`
Future CAT application
        ↓
Secure user/session handoff
        ↓
EDAV Microbot iframe
        ↓
Existing equipment-manual BaaS bot
\`\`\`

This order prevents Flask, Azure Functions, SQL, Key Vault, RStudio Connect, and CAT workflows from delaying the basic question: can the EDAV bot retrieve useful, grounded information from these manuals?

## 5. Technology boundaries in plain language

| Technology or term | Role in this pilot |
|---|---|
| EDAV BaaS | The managed bot service expected to provide the bot runtime, retrieval-related services, model connection, and hosted experience. |
| EDAV Microbot UI | The ready-made chat window where a user asks questions and sees answers. |
| EDAV MaaS | Direct model API access; unnecessary if BaaS supplies the complete bot path. |
| Entra ID/groups | Identity and access controls for the people allowed to use EDAV resources and the pilot. |
| Data Lake | Possible document staging location only if the BaaS workflow requires it; storage alone does not make files searchable. |
| Key Vault | Secret storage for a future custom host or application; not needed for direct use of an EDAV-hosted UI. |
| Flask | Python web framework for the future CAT application; not a prerequisite for the pilot bot. |
| Azure Functions | Possible future cloud runtime for CAT backend functions; not a prerequisite for the pilot bot. |
| Azure SQL | Possible future storage for structured CAT records; not part of manual retrieval. |
| RStudio Connect | Optional place to host a temporary wrapper if direct EDAV UI cannot be used; it supplies no bot or retrieval capability itself. |
| iframe/postMessage | Later integration mechanism for placing the EDAV Microbot inside CAT; it does not create or configure the bot. |

## 6. Evidence, assumptions, and unknowns

### Confirmed from supplied materials or agreed by the team

- The pilot document describes an Equipment Manual Knowledge Retrieval Pilot and states that the initial collection contains 35 PDF files.
- The intended use is natural-language retrieval over equipment manuals with document/page references when possible.
- The pilot is limited to non-PII content.
- Competency determinations are outside the pilot.
- The EDAV-provided materials include BaaS/MaaS descriptions and Microbot iframe communication documentation.
- The supplied EDAV access information identifies Entra personas/groups and approved model access for the CAT use case.
- The CAT application will be developed later; its Python/Flask and Azure hosting choices do not need to block this pilot.

### Working assumptions for planning

- BaaS is the intended place for document processing, retrieval, and answer generation rather than a pipeline owned by the CAT team.
- EDAV will expose either a self-service bot configuration path or a bot-request path that can be used within the approved pilot scope.
- The EDAV-hosted preview/direct UI can be tested before an iframe host is considered.
- The manuals will remain unchanged during the pilot-development window.

These are operating assumptions to test through the platform workflow; they are not evidence that a particular EDAV screen or processing feature is available.

### Not yet verified and therefore not promised

- The exact EDAV screen or request process for creating a BaaS bot.
- The exact upload/registration mechanism for the manuals.
- Whether PDFs are parsed, chunked, OCR-processed, embedded, indexed, and cited automatically by the available BaaS configuration.
- Whether page-level citations are available for every manual and response.
- The exact BaaS access-control configuration for the pilot group.
- Whether a standalone authenticated preview is available for this bot.
- The exact JWT issuance path if a parent iframe host is required.
- Final evaluation thresholds and the number of pilot participants.

An unknown is a discovery item for the next phase, not permission to build a custom replacement immediately.

## 7. Explicitly out of scope

The following work is deferred until the pilot demonstrates value and a separate decision authorizes it:

- CAT Flask application development.
- Azure Functions deployment and production hosting.
- Custom front-end design.
- Custom RAG or AI platform development.
- Custom embeddings, vector database, document parser, or retrieval API.
- Direct MaaS integration.
- SQL/Dataverse/Power Platform integration.
- Competency scoring, training status, authorization, or certification decisions.
- PII ingestion or PII-aware personalization.
- Live equipment, calibration, inventory, or maintenance-system integration.
- Automated document refresh and revision workflows.
- Production monitoring, analytics, service-level objectives, and broad rollout.
- Production authorization or a claim of operational readiness.

## 8. Phase 0 exit gate

Phase 0 is considered documented when the following statements are accepted:

- The pilot objective is manual-grounded information retrieval and user-value testing.
- The full approved 35-manual corpus remains in scope.
- Only non-PII manuals are used.
- Competency and authorization decisions are excluded.
- EDAV BaaS is the first implementation path.
- Direct EDAV-hosted UI is tested before building a host application.
- CAT, Flask, Azure Functions, SQL, and RStudio Connect are not prerequisites.
- Unknown EDAV capabilities will be verified through hands-on discovery rather than replaced with speculative custom architecture.

Phase 0 does not mean that the BaaS bot is ready. It means the team has a stable boundary for the work that follows.

## 9. Next phases after this boundary

| Phase | Purpose | Exit evidence |
|---|---|---|
| Phase 1 | Inventory and verify the approved 35-manual corpus; freeze the corpus. | Source register and integrity check. |
| Phase 2 | Discover the usable EDAV BaaS path and create/configure the managed bot. | Bot identifier, source-registration evidence, access scope, and usable test route. |
| Phase 3 | Configure grounding, citation, safety, refusal, and uncertainty behavior. | Versioned bot instruction/configuration record. |
| Phase 4 | Run smoke tests and a small controlled evaluation with SME review. | Question matrix, responses, scores, limitations, and pilot decision. |
| Phase 5 | If the pilot succeeds, decide whether and how CAT should embed the existing bot. | Separate CAT integration decision and iframe/JWT design. |

Phase 1 is documented separately in [PILOT_SOURCE_REGISTER.md](PILOT_SOURCE_REGISTER.md). The current checkout contains the complete 35-PDF pilot corpus, and the register records that set for ingestion. Phase 2 execution is documented in [PHASE_2_BAAS_CONFIGURATION.md](PHASE_2_BAAS_CONFIGURATION.md), with the copy-paste bot behavior in [PILOT_BOT_INSTRUCTIONS.md](PILOT_BOT_INSTRUCTIONS.md).

## 10. Decision record

| ID | Decision | Status |
|---|---|---|
| P0-01 | The pilot is a proof of concept, not a production application. | Agreed |
| P0-02 | The target corpus is all 35 approved equipment manuals. | Agreed |
| P0-03 | The pilot uses non-PII manual content only. | Agreed |
| P0-04 | The bot provides information retrieval and explanation only. | Agreed |
| P0-05 | The bot will not make competency or authorization decisions. | Agreed |
| P0-06 | Manuals are treated as static during pilot development. | Agreed |
| P0-07 | EDAV BaaS is the primary bot-building path. | Agreed |
| P0-08 | The direct EDAV-hosted UI is attempted before an iframe host. | Agreed |
| P0-09 | A CAT app is not required to create or test the pilot bot. | Agreed |
| P0-10 | Flask, Azure Functions, SQL, Key Vault, MaaS, custom RAG, and RStudio Connect are deferred unless a specific pilot blocker justifies reconsideration. | Agreed |
| P0-11 | The exact EDAV ingestion and citation behavior must be discovered and recorded during implementation. | Open discovery item |
| P0-12 | The 35-PDF source register is the authoritative pilot corpus and must be used to control ingestion. | Phase 1 gate |
