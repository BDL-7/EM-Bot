# Complete slide plan

The audience-facing text below is exact proposed copy. Visual instructions describe the composition; the HTML contains only audience content and source information. The 12 durations total 14 minutes; they include interaction and pointing time. Source IDs E01–E09 and claim IDs C01–C16 resolve in [evidence](evidence.md). Visual IDs V01–V06 resolve in [visual briefs](visual-briefs.md).

## S01 — Finding answers in equipment manuals

**Duration:** 55 seconds. **Purpose:** make the task recognizable before naming technology. **Takeaway:** we are exploring help with finding manual information.

### Audience-facing text

**Finding answers in equipment manuals**

An introduction to our EDAV bot pilot

“Where does the manual explain how to clean this instrument?”

### Visual composition

Use V01: one colleague, a screen, and a few manuals, with the question large on the left. Keep equipment in the background and show no procedure being performed. The scene is a conceptual illustration. Avoid multiple panels and decorative robot imagery.



### Evidence and uncertainty

E01, E03; C01, C15. The purpose is documented; usefulness is a pilot question. The pictured scene and running question are illustrative. No search-time claim or equipment instruction is made.

## S02 — A question becomes a conversation

**Duration:** 65 seconds. **Purpose:** preview the intended experience and introduce clarification. **Takeaway:** a useful response may first ask what equipment the person means.

### Audience-facing text

**A question becomes a conversation**

| Ask | Proposed first reply | Then check |
|---|---|---|
| “Where does the manual explain how to clean this instrument?” | “Which instrument and model are you using?” | After clarification, check the supporting manual before acting. |

Illustration of intended behavior

### Visual composition

Use V02 as a three-frame sequence rather than a screenshot. Initially conceal the middle and final frames. Reveal the proposed first reply after the audience prediction, then reveal the source-check step. The final frame contains a generic document, with no invented page number or manual passage. The exact copy above defines the frame labels; the eventual slide need not use a grid.



### Evidence and uncertainty

E03, E04; C06, C08. Clarification and source checking are required behaviors. They are not live observations. Source locators depend on what EDAV actually provides. Interaction A1 appears in [short introduction](short-introduction.md).

## S03 — An app is a tool for a task

**Duration:** 55 seconds. **Purpose:** define app without assuming familiarity with software or browsers. **Takeaway:** an app can help someone do a task through a web page.

### Audience-facing text

**An app is a tool for a task**

Software is a set of instructions a computer follows.

An app uses software to help you do something.

In this example: type a question, send it, read the reply.

An app can run on a web page.

### Visual composition

Use a simple editable interface diagram: a page outline with three numbered labels, “1 Type,” “2 Send,” and “3 Read.” Label it “Illustration.” This is an explanatory diagram of actions, not a replica of the EDAV interface. Leave visual detail out so the three actions remain obvious.



### Evidence and uncertainty

E02, E07; C02. Definitions are simplified teaching language. The official integration guide supports embedding EDAV chat within an app; E07 supports the browser context. This diagram does not promise particular controls or a deployed route.

## S04 — A chatbot responds through messages

**Duration:** 65 seconds. **Purpose:** distinguish app, bot, and AI model. **Takeaway:** a chatbot can be one feature of an app; an AI model is one component of the intended system.

### Audience-facing text

**A chatbot responds through messages**

| Term | Everyday meaning | Here |
|---|---|---|
| App | Software for a task | The place we ask and read |
| Chatbot | Software that exchanges messages | EM Knowledge Bot |
| AI model | A component that produces language from input | Helps form a response |

A chatbot can be one feature inside an app.

### Visual composition

Use the three-row native table. Give the caption breathing room below it. Do not add a brain, personified robot, or a fourth technical diagram. A small bracket under the app and chatbot rows may emphasize the relationship if it remains readable.



### Evidence and uncertainty

E02, E03, E08; C03, C04. E08 supports conversational bots within apps; the AI-model explanation is an intentionally broad description of the documented intended model role. No model vendor, version, reasoning ability, or live selection is claimed.

## S05 — Bot as a Service

**Duration:** 70 seconds. **Purpose:** make the service relationship concrete. **Takeaway:** using a shared service leaves important project responsibilities with our team.

### Audience-facing text

**Bot as a Service**

Using bot capabilities supplied and operated by another team

Imagine a reference library:

- Manuals: the collection
- Chatbot: a reference helper
- App: the way to reach that help
- EDAV: shared technology
- Our team: sources, instructions, and evaluation

The helper is software and can make mistakes.

### Visual composition

Use V03's five-role text-diagram fallback. It maps the reference-library analogy to manuals, chatbot, app, EDAV, and project-team responsibilities. Keep “Bot as a Service” as the visible title and explain the analogy's limits on the slide.



### Evidence and uncertainty

E01, E02, E03; C05, C10. The analogy and definition are explanatory framing. The exact EDAV operating/support agreement is not established by the integration README. Do not promise cost, availability, security certification, or a service-level guarantee.

## S06 — The pieces in our pilot

**Duration:** 70 seconds. **Purpose:** map the concepts to this project without a technical architecture lecture. **Takeaway:** the host app displays EDAV chat; retrieval and bot behavior are part of the intended EDAV arrangement.

### Audience-facing text

**The pieces in our pilot**

Person asking a question

Our app → EDAV chat inside the page ↔ EDAV service

EM Knowledge Bot + approved manual collection

The person checks the source.

Intended pilot arrangement

### Visual composition

Use V06a, an editable diagram. Put “EDAV chat” inside the “Our app” outline, with the person to its left. Put “EM Knowledge Bot” inside the “EDAV service” outline to its right. Place “Approved manual collection” below the service with a connector labeled “Manuals to consult.” Return an arrow labeled “Reply and source information” toward the person. Treat manual placement as a logical source relationship, not a storage-location claim.



### Evidence and uncertainty

E01, E02, E03, E05; C05, C06, C11. Embedding is documented; the retrieval arrangement is intended. The EDAV guide does not document the retrieval backend. Live connection and document processing were not inspected.

## S07 — Preparing manuals and answering questions

**Duration:** 85 seconds. **Purpose:** separate document preparation from use. **Takeaway:** a question seeks relevant evidence from a prepared collection and ends with human review.

### Audience-facing text

**Preparing manuals and answering questions**

Before use: select approved manuals → prepare them in EDAV → verify setup

For a question: ask → clarify if needed → find passages → draft from evidence → show sources → check

If evidence is missing: explain the gap.

Intended process; live behavior still needs testing

### Visual composition

Use V06b: two horizontal lanes with clear titles. Keep the preparation lane visible while revealing the question lane. Split the “find passages” step into a supported-evidence path and a short “explain the gap” branch. The final “check” step carries a person label. This is a conceptual sequence, not a claim about EDAV's internal algorithm or exact execution order.



### Evidence and uncertainty

E03, E04; C06, C07. The approved collection is documented as 35 manuals; no fresh corpus inventory or ingestion check was performed for this package. The diagram specifies desired behavior, not a verified implementation of retrieval, model training, or storage.

## S08 — A source you can check

**Duration:** 75 seconds. **Purpose:** make evidence-checking visible. **Takeaway:** a source must support the actual answer and apply to the right equipment.

### Audience-facing text

**A source you can check**

1. Is this the right instrument and model?
2. Does the passage support the answer?
3. Are the relevant warnings and conditions included?

Page or section: only when reliably available.

Illustration; no live answer shown

### Visual composition

Use V04: a simplified answer outline on the left, source information in the middle, and a generic document excerpt area on the right. The excerpt area reads “Supporting passage shown here.” Highlight the relationship, not fictional manual text. No page number, fabricated citation, or approved checkmark. Leave space for a real, permission-cleared passage in a later build if available.



### Evidence and uncertainty

E03, E04; C08. Citation fidelity and preservation of conditions are requirements. Page-level citation availability and accuracy remain unverified. Nothing in this slide authorizes performing a procedure.

## S09 — Choosing the right next step

**Duration:** 80 seconds. **Purpose:** explore boundaries through recognizable questions. **Takeaway:** useful assistance includes clarification and directing the person to the right information owner.

### Audience-facing text

**Choosing the right next step**

| Question | Expected handling | Reason |
|---|---|---|
| Where are the cleaning instructions? | Clarify model; find source | Equipment matters |
| Is it calibrated today? | Use current records | Manuals are static |
| Am I authorized to use it? | Ask the responsible person | Authorization needs human authority |
| Who last used it? | Decline personnel lookup | Outside this collection |

Required behavior; still to verify

### Visual composition

Use a native editable table. Reveal the question column first; after the activity, reveal expected handling and reason. Give every row a text label. Do not use green/red alone to distinguish acceptable and unacceptable questions. Avoid characterizing the person asking as wrong.



### Evidence and uncertainty

E03, E04; C09. The examples adapt the documented behavior categories. They are not live test results. Interaction A2 appears in [short introduction](short-introduction.md).

## S10 — Shared work, clear responsibilities

**Duration:** 65 seconds. **Purpose:** prevent the idea that using a service eliminates project work. **Takeaway:** EDAV, our team, and users have different contributions.

### Audience-facing text

**Shared work, clear responsibilities**

| EDAV contribution | Project-team contribution | User contribution |
|---|---|---|
| Chat service and connection guidance | Connect the app | Use the approved route |
| Service features to confirm | Select sources; set behavior | Give useful context |
| Support arrangements to confirm | Test and maintain the pilot | Check sources; report problems |

Responsibilities to confirm with platform owners

### Visual composition

Use a native three-column table with equal visual weight. Add no logos unless approved assets exist. Keep “to confirm” visible. The table describes contributions, not a binding support agreement.



### Evidence and uncertainty

E01, E02, E03; C10. Platform responsibility beyond the published integration contract needs confirmation. Our documented configuration and evaluation tasks are established project requirements; their completion is not claimed.

## S11 — What is ready and what needs evidence

**Duration:** 80 seconds. **Purpose:** give an honest status and explain what would count as useful progress. **Takeaway:** repository preparation is evidenced; live outcomes and user value still require evaluation.

### Audience-facing text

**What is ready and what needs evidence**

| Available now | Prepared | Still to verify |
|---|---|---|
| App connection software | Bot instructions | Live EDAV setup |
| Checks of that software | Ten behavior tests | Manual processing and replies |
| Pilot documentation | Evaluation direction | Accuracy and user value |

Is it supported? Checkable? Useful? Within scope?

Documented status · October 8, 2026

### Visual composition

Use a native table with neutral labels. Keep “Available now” visually linked to “repository” in the spoken explanation. Do not put completion ticks over a pipeline or use a percentage-progress chart. Place the four evaluation questions as one readable line below the table.



### Evidence and uncertainty

E01, E03, E04, E05; C11, C12, C13, C14. Documentation was inspected on October 8; live EDAV and Connect were not. No tests were run against the bot, and this package reports no new host-test result. Evaluation measures in [production handoff](production-handoff.md) are proposals.

## S12 — The person checks the source

**Duration:** 75 seconds. **Purpose:** close the story and check understanding. **Takeaway:** shared technology may help locate information; the person checks the source.

### Audience-facing text

**The person checks the source**

An illustrative search today: open manuals → look for the passage → check

Proposed experience: ask → clarify → review answer and source → check

App: where we interact. Bot: the conversation. EDAV: shared technology.

The pilot will test whether this helps.

### Visual composition

Use V05: two equal-length horizontal paths ending at the same person checking a manual. Label the first “Illustrative search” and the second “Proposed experience.” Do not make the proposed path shorter or add stopwatches. A single manual remains visible at the end of both paths.



### Evidence and uncertainty

E01, E03; C14, C15. Both workflows are teaching illustrations. Neither is a measured baseline or a demonstrated live improvement. Interaction A3 is the final comprehension check.
