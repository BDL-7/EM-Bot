# Evidence, claims, and access limits

Evidence reviewed **October 8, 2026 (America/New_York)**. This is a presentation evidence index, not the private manual inventory. No manual content, private source register, or local EDAV runbook is included.

## Source hierarchy and baseline

Use current repository records for project scope and status; official EDAV material for the integration contract; clearly labeled educational explanations for terminology and analogies. Never convert required behavior into an observed outcome. An external capability document does not establish that the pilot has configured or verified that capability.

The publication baseline is `dev` commit `dc2d11fae2ecd3d6448d38b32452485fe0469107`. The original working checkout contains a documentation reorganization that has not been published in that baseline. Both were inspected. The claims used here agree on the intended 35-manual pilot and the absence of live behavior evidence. Links below use the published baseline so they work in a fresh clone and remain stable if local files are renamed.

## Source index

| ID | Source and locator | What it supports | Access and limits |
|---|---|---|---|
| E01 | [Project README at reviewed commit](https://github.com/BDL-7/EM-Bot/blob/dc2d11fae2ecd3d6448d38b32452485fe0469107/README.md), Current status, Pilot path, Scope boundary | Pilot purpose, documented 35 approved non-PII manuals, implementation versus preparation, future evaluation | Read from Git and compared with local README. Deployment statements are repository reports; no live inspection was performed |
| E02 | [EDAV Microbot UI Integration Guide](https://github.com/cdcent/edav-BaaS/blob/master/README.md), Quick Overview, Authentication Flow, URL Format | Embedding EDAV chat in a parent app, supported message exchange, bot configuration identifier | Read through GitHub connector. Observed README blob SHA `bc9b9afcad8d64f98eeca42410882331497b0a0b`; the linked branch can change. This guide does not establish backend retrieval, source ingestion, model choice, or service guarantees |
| E03 | [Behavior configuration](https://github.com/BDL-7/EM-Bot/blob/dc2d11fae2ecd3d6448d38b32452485fe0469107/PHASE_3_BEHAVIOR_CONFIGURATION.md), sections 1, 3, 4, 6, 9, 10; [Bot instructions](https://github.com/BDL-7/EM-Bot/blob/dc2d11fae2ecd3d6448d38b32452485fe0469107/PILOT_BOT_INSTRUCTIONS.md), Knowledge boundary, How to answer, Citation and uncertainty rules | Intended evidence path, source boundaries, clarification, reliable locators, uncertainty, human review, configuration prerequisites, broader evaluation | Prepared requirements. The evidence record is unfilled. Neither artifact proves compliance by a live bot |
| E04 | [Behavior tests](https://github.com/BDL-7/EM-Bot/blob/dc2d11fae2ecd3d6448d38b32452485fe0469107/PHASE_3_BEHAVIOR_TESTS.md), How to run, Acceptance tests, Test result record | Ten prepared tests; source checking; current-status, authorization, ambiguity, personnel, and safety boundaries | All ten result rows say Not run in the inspected baseline. No tests were executed against EDAV for this package |
| E05 | [Host app](https://github.com/BDL-7/EM-Bot/blob/dc2d11fae2ecd3d6448d38b32452485fe0469107/host_app/app.py), [token provider](https://github.com/BDL-7/EM-Bot/blob/dc2d11fae2ecd3d6448d38b32452485fe0469107/host_app/entra_auth.py), [chat integration](https://github.com/BDL-7/EM-Bot/blob/dc2d11fae2ecd3d6448d38b32452485fe0469107/host_app/static/microbot.js), with E01's Temporary Flask host and Scope boundary | Repository presence of app integration and authentication components; the documented host role excludes retrieval and bot implementation | Presence checked in the reviewed tree and described by the inspected README/local host guide. This was not a new security audit or live connection test |
| E06 | [EDAV BaaS portal](https://edav.cdc.gov/ai/baas) | User-supplied platform destination | Inaccessible through the research tool. It supplies no independently verified feature, model, ingestion, UI, privacy, or operating-status claim in this package |
| E07 | [MDN: Browsing the web](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Environment_setup/Browsing_the_web), browser and web-app explanations | General explanation of using a browser to access web content and applications | Read online. General education only; not evidence about EDAV implementation |
| E08 | [Microsoft: Designing your bot](https://learn.microsoft.com/en-us/microsoftteams/platform/bots/design/bots), introductory bot description and Use tabs with bots | Conversational software can respond to questions and be a feature within an app | Relevant explanatory text was accessible. Used only for this general concept, not to infer that EDAV uses Teams, Bot Framework, or any named backend |
| E09 | Existing local deck: `ppt/emkb-phase2-phase3-status/.workshop/deck-state.json` and its README | Existing title, stable slide IDs, order, and editing boundary for the proposed five-slide insertion | Read locally. Not present in the reviewed published dev tree; no copy of it is published here. Its October 6 status content is not treated as refreshed live evidence |

## Local-to-published document mapping

| Inspected original-checkout path | Published baseline equivalent | Use here |
|---|---|---|
| `Docs/bot-behavior.md` | `PHASE_3_BEHAVIOR_CONFIGURATION.md` | E03; plain behavior names are used on slides instead of phase jargon |
| `Docs/bot-instructions.md` | `PILOT_BOT_INSTRUCTIONS.md` | E03; approved-source and citation requirements |
| `Docs/bot-tests.md` | `PHASE_3_BEHAVIOR_TESTS.md` | E04; prepared test set and unfilled results |
| `host_app/README.md` | Root README host/scope sections plus `host_app/` source files | E01/E05; host role and limits |
| `README.md` | Root README at the reviewed commit | E01; use the status common to both, and qualify it as documented |

The local documents are corroborating context, not unpublished dependencies of the package. The word “equivalent” describes the role and claims used here; it does not claim the files are byte-identical. Do not bundle unrelated documentation edits into this presentation change.

## Claim ledger

| ID | Claim and status | Sources | Slides | Limitation or required wording |
|---|---|---|---|---|
| C01 | Documented purpose: explore help with approved equipment-manual information | E01, E03 | S01, B01 | Call it a pilot; usefulness is not established |
| C02 | Background: an app helps with a task and can be used through a browser | E02, E07 | S03, B02 | Simplified explanation; not every app is a web app |
| C03 | Background: conversational bots exchange messages and may be part of an app | E08, E02 | S04, B02 | Not every automated bot uses AI; app and bot are not mutually exclusive categories |
| C04 | Intended model role: a model is one component involved in producing language | E03 | S04 | Generic educational description; no selected model or internal architecture verified |
| C05 | Documented integration: a parent app can embed EDAV Microbot chat | E02 | S05–S06, B02–B03 | An integration guide is not proof of this pilot's live readiness |
| C06 | Required behavior: clarify, find relevant evidence, answer from it, identify sources or gaps | E03, E04 | S02, S06–S07, B01, B03 | Say intended/required; retrieval quality and controls remain unverified |
| C07 | Documented scope: 35 approved, non-PII manuals must be prepared before use | E01, E03 | S07, B03 | Count comes from project records; no fresh inventory, approval audit, or ingestion check performed |
| C08 | Required behavior: source support, correct model, reliable locations, preserved conditions | E03, E04 | S02, S08, B03 | A citation alone does not prove correctness; page/section only when reliably supplied |
| C09 | Required boundaries: manuals cannot establish today's equipment status, personal authorization, or personnel facts | E03, E04 | S09, B04 | These are information-scope distinctions, not an observed refusal success rate |
| C10 | Documented/proposed responsibility split: shared platform, project configuration and evaluation, user checking | E01, E02, E03 | S05, S10, B02 | Platform operating/support duties beyond the integration guide must be confirmed |
| C11 | Repository implementation: host and integration components are present; host does not implement retrieval | E01, E05 | S06, S11, B03, B05 | Code presence is not a live health, security, or readiness result |
| C12 | Prepared configuration: instructions and ten behavior tests exist | E03, E04 | S11, B05 | Prepared does not mean applied or passed |
| C13 | Documented evidence gap: live setup, processing, and bot behavior remain unverified in reviewed records | E01, E03, E04 | S11, B05 | This is an absence of recorded proof, not an assertion that no external work has occurred |
| C14 | Recommendation: evaluate source support, citation quality, handling of gaps, and user usefulness | E03, E04 | S11–S12, B05 | Future evaluation; no accuracy, cost, adoption, or speed metric is reported |
| C15 | Teaching scenario: manual-search and proposed conversation routes end with human source checking | E01, E03 | S01, S12, B05 | Illustrative workflows; not measurements or findings about user performance |
| C16 | Editorial proposal: beginner sequence and short-section insertion | E09; audience brief | All; B01–B05 | Pedagogical recommendation, not a research result or approval of existing deck edits |

## Facts deliberately left unresolved

- The exact portal workflow, source-processing counts, selected model, and citation controls exposed to this pilot.
- The current approved pilot access arrangement and observed connection state.
- Whether a live answer displays a reliable manual page or section, or only a broader source reference.
- Which platform team owns ongoing support, source changes, and incidents under an agreed operating arrangement.
- Measured answer accuracy, usefulness, time savings, or costs.
- The presenter, audience size, meeting date, approved branding, and whether a final deck will be HTML or PowerPoint.

These gaps do not prevent explaining the concept. They do prevent presenting a live demonstration, a completed pilot, or a measured benefit as fact.

## Refresh before presenting

Recheck E01/E03/E04 against current `dev`, confirm any newly recorded live evidence with its owner, and update the evidence date only for facts actually reviewed. Re-read the E02 guide if making integration claims. Replace an illustrative answer with a real one only after verifying the exact source, locators, and allowed disclosure. Keep the original status wording if no new evidence is available; do not turn passage of time into progress.
