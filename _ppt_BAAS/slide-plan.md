# Complete slide plan

The audience-facing text below is exact proposed copy. Visual instructions and speaker notes are production guidance and do not belong on the audience slide. The 12 durations total 14 minutes; they include interaction and pointing time. Source IDs E01–E09 and claim IDs C01–C16 resolve in [evidence](evidence.md). Visual IDs V01–V06 resolve in [visual briefs](visual-briefs.md).

## S01 — Finding answers in equipment manuals

**Duration:** 55 seconds. **Purpose:** make the task recognizable before naming technology. **Takeaway:** we are exploring help with finding manual information.

### Audience-facing text

**Finding answers in equipment manuals**

An introduction to our EDAV bot pilot

“Where does the manual explain how to clean this instrument?”

### Visual composition

Use V01: one colleague, a screen, and a few manuals, with the question large on the left. Keep equipment in the background and show no procedure being performed. The scene is a conceptual illustration. Avoid multiple panels and decorative robot imagery.

### Speaker notes

Deliver the 30-second introduction from the package README. Then say: “Keep that one question in mind. We are asking whether software can help us locate and understand the relevant information, while keeping the manual available for checking. You will not need to know any programming to follow this. We will start with the experience, give names to the pieces, and come back to how a person checks the result.” Point at the manual, not at the computer. “This picture is an example of the situation we want to help with. We have not measured how long everyone currently spends searching.”

### Transition

**From previous:** opening slide. **To next:** “Imagine typing that question. What should the first response be?”

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

### Speaker notes

“Before I reveal the reply, what information is missing?” Allow up to 15 seconds. If nobody speaks, offer: “Could different instruments have different instructions?” Reveal the reply. “A useful assistant should ask which instrument and model we mean. Giving a confident answer too early would be a problem. After we clarify, the intended experience is to find relevant manual information and show us what supports the answer. We then check it. This is an illustration of the behavior we want to test. It is not a recording of a working bot, and we are not showing any cleaning instructions today.” Reveal the final frame and leave all frames visible.

### Transition

**From previous:** the colleague has a question. **To next:** “The place where you type and read is part of an app. Here is what that word means.”

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

### Speaker notes

“Software is the instructions that tell a computer what to do. An application, usually shortened to app, puts software to work on a task. For example, a calculator app helps you calculate. Here, the task is asking a question and reading a reply. You can reach some apps through a browser—the program you use to open websites. You do not always need to install something new. The visible page helps you use the tool, but some of the work may happen on other computers. We will return to that in a moment. For now, follow these three actions: type, send, and read.”

### Transition

**From previous:** we name the place the conversation appears. **To next:** “Inside that app, what is producing the conversational response?”

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

### Speaker notes

“A bot is software that performs tasks automatically. A chatbot is a kind of bot we interact with through messages. That does not mean every bot uses artificial intelligence, or AI. In the experience planned here, an AI model helps produce language from the information it receives. Think of the model as a component within a larger system. We also need documents, instructions, access arrangements, and checks. The chatbot and the app are related: an app may contain a chatbot alongside other features. Neither a fluent sentence nor the word AI tells us whether the answer is supported. That is why we keep the manual in the story.”

### Transition

**From previous:** the app gives us a way to interact. **To next:** “Our team is using shared bot technology supplied through EDAV. That is where ‘as a service’ comes in.”

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

Use V03: one cohesive library illustration with five adjacent editable labels. Do not draw the chatbot as a human scientist. A desk sign can represent the helper. Reveal “Bot as a Service (BaaS)” in the speaker's explanation after the audience understands the shared capability. Keep the exact title on the slide.

### Speaker notes

“Imagine a reference library. You bring a question. There is a collection to consult and a way to ask for help. Our project uses shared technology from another team instead of constructing every supporting capability ourselves. That is the service idea. EDAV is the name of the platform we are using. In this project, BaaS means Bot as a Service. We still choose the approved sources, define the behavior we need, and evaluate what happens. The analogy has a limit: this helper is software, not a trained librarian or a laboratory expert. It can make mistakes. Using the service still requires setup, testing, maintenance, and evaluation.”

### Transition

**From previous:** we know what a chatbot does. **To next:** “Let us put the library analogy aside and name the actual pieces in our pilot.”

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

### Speaker notes

“Our temporary app provides a page that can display EDAV's chat interface. EDAV calls that interface Microbot. The official guide describes how an app embeds it and passes the information needed for the connection. Our pilot is intended to use EM Knowledge Bot with an approved collection of manuals. The project documents describe that intended arrangement, but they do not establish that the manuals have been processed or that the bot is answering correctly. The app itself does not search the manuals or implement the bot. Also, the arrow from the manuals shows a planned source relationship. It does not tell us where EDAV stores or processes documents.”

### Transition

**From previous:** the shared-service idea now has project names. **To next:** “There are two different moments to understand: preparing the collection and asking a question.”

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

### Speaker notes

“Before anyone asks, the approved collection has to be prepared through the supported EDAV process and checked. That is separate work. When a person asks a question, the intended system looks for relevant passages, uses that evidence to prepare an answer, and identifies the available source information. If the equipment is unclear, it should ask for clarification. If evidence is missing, it should explain that gap. It should not fill the gap with a confident guess. The person then checks the answer against the source. This diagram does not mean we upload every manual again for each question, search the entire internet, or train a new model each time. It is a simplified picture of the experience we intend to evaluate.”

### Transition

**From previous:** the arrangement has become a sequence. **To next:** “What exactly should you check when the source appears?”

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

### Speaker notes

“A source reference is an invitation to check. First, does it name the equipment and model we actually mean? Second, does the passage support the statement in the answer? Third, have the important conditions and warnings carried through? A document can be about the right instrument yet still fail to support a particular claim. A page or section can make checking easier, but our instructions say to show those details only when the platform supplies them reliably. If the exact location cannot be confirmed, the bot should say so. The official manual, applicable procedure, and expert review still govern the work. We are showing the checking process here, not a successful live answer.”

### Transition

**From previous:** the answer journey reaches evidence. **To next:** “Some questions cannot be settled by an equipment manual at all.”

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

### Speaker notes

“Take the second question: ‘Is it calibrated today?’ Should the bot answer from the manual, ask which model, or direct us to current records?” Allow up to 15 seconds, then reveal the table. “A manual may explain calibration, but it cannot establish what happened to our particular instrument today. Reading a manual also does not authorize someone to use the instrument. Personnel questions are outside this pilot's collection. These are reasonable things for a colleague to ask. A useful response should explain where the question belongs. If a manual question is unsupported or the model is unclear, the bot should explain the gap or ask for clarification. These are requirements we still need to verify in the live bot.”

### Transition

**From previous:** checking evidence reveals its limits. **To next:** “Making those boundaries work takes contributions from several people and teams.”

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

Use a native three-column table with equal visual weight. Add no logos unless approved assets exist. Keep “to confirm” visible rather than hiding it in notes. The table describes contributions, not a binding support agreement.

### Speaker notes

“The official EDAV guide gives us a hosted chat interface and an integration pattern. Our team still has to select approved sources, connect the app, specify the behavior, and evaluate the results. Users contribute clear questions and source checking. We also need to agree with platform owners which capabilities and support arrangements are actually available. This table is a proposed division of work, not a complete operating agreement. For example, we should not invent a guaranteed response time or assume that every citation control we want exists. Using a shared service changes the work our team does. It does not remove that work.”

### Transition

**From previous:** the boundaries require ownership. **To next:** “With those roles in mind, here is what the project records support today.”

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

### Speaker notes

“Available here means available in the project files: software for connecting the app, checks, and documentation. The behavior instructions and ten tests of the bot's required responses are prepared. The records we reviewed still lack the evidence needed to claim live bot readiness, successful manual processing, or useful answers. This presentation does not independently verify the running service. What would progress look like? Reviewers would compare answers with the manuals, check whether source references support the answers, observe how unclear or unsupported questions are handled, and ask pilot users whether the help is useful. The ten behavior tests cover specific boundaries. They do not establish an overall accuracy rate. A broader evaluation must decide whether to continue, revise, or stop the pilot.”

### Transition

**From previous:** each contribution needs evidence. **To next:** “Let us return to the person who needed help finding that manual passage.”

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

### Speaker notes

“We began with someone looking for a passage. The proposed experience changes how that person gets help, while keeping source checking at the end. We have not measured a time saving or shown that the proposed route is better. That is what the pilot needs to investigate.” Invite the final 25-second teach-back: “In this example, what is the app, what is the bot, and what does EDAV provide?” If needed, point to the three labels. Accept everyday language. Close with: “We are testing whether a shared bot service can help colleagues find and understand approved manual information, while keeping the answer checkable and the decisions with the right people.”

### Transition

**From previous:** evaluation gives the pilot a purpose. **To next:** invite questions, or use the bridge to the existing status deck in [short introduction](short-introduction.md).

### Evidence and uncertainty

E01, E03; C14, C15. Both workflows are teaching illustrations. Neither is a measured baseline or a demonstrated live improvement. Interaction A3 is the final comprehension check.
