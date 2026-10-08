# Five-slide introduction and audience activities

This compact version introduces the concepts before a technical status presentation. It is **5 slides / 360 seconds / 6 minutes**, including one short comprehension check. It reuses the full deck's evidence and visual briefs while reducing repetition. It is a proposed insertion, not an edit to the existing deck.

## Insertion into the existing local deck

The inspected deck is `ppt/emkb-phase2-phase3-status/`, titled **EM Knowledge Bot: Status and Safe Execution**. Its source is `.workshop/deck-state.json`. The first three stable slide IDs are `s01-title`, `s02-evidence`, and `s03-scope`. This local deck is not present in the inspected published `dev` baseline; the references here identify where to integrate if that local deck remains the chosen target.

Insert B01–B05 **after `s01-title` and before `s02-evidence`**. Preserve all existing stable IDs. Use the bridge below to enter the status material. The existing `s03-scope` can serve as a brief ownership recap after the evidence table; avoid repeating the whole analogy there. Reconfirm current slide IDs and content before a later edit.

The existing deck contains checkout history, token-provider details, and activation checklists. For a wholly nontechnical audience, propose moving those to an optional technical appendix during a separately authorized revision; otherwise the beginner introduction will be followed by material that assumes more software knowledge. No existing content is moved or removed by this package.

## B01 — One question, one manual

**Time:** 60 seconds. **Source slides:** S01–S02. **Purpose:** establish the practical task.

**Exact audience copy:**

> Where does the manual explain how to clean this instrument?
>
> Proposed first reply: “Which instrument and model are you using?”
>
> Illustration of intended behavior

**Visual:** V01 with the question large; reveal the proposed reply as a plain annotation. Do not combine the full three-frame storyboard with the photograph/illustration.

**Speaker notes:** “We are testing whether software can help colleagues find and understand approved manual information. We will follow this question. Before giving instructions, a useful assistant needs to know which equipment and model we mean. The reply shown here is a requirement we intend to test, not a live result. After clarification, the person should be able to check supporting manual information.”

**Transition:** “First, here are the names of the pieces involved.” **Evidence:** E01, E03, E04; C01, C06.

## B02 — App, chatbot, shared service

**Time:** 75 seconds. **Source slides:** S03–S05. **Purpose:** provide enough vocabulary to understand the status report.

**Exact audience copy:**

| Term | Everyday meaning | In this pilot |
|---|---|---|
| App | Software that helps with a task | The page where we ask and read |
| Chatbot | Software that exchanges messages | EM Knowledge Bot |
| Bot as a Service | Shared bot capabilities another team operates | EDAV's service arrangement |

> Our team still selects sources and checks results.

**Visual:** one editable table. Use a brief spoken reference-library analogy only; do not add another dense diagram.

**Speaker notes:** “Software is instructions a computer follows. An app puts those instructions to work on a task; some apps run in a browser, the program used to open web pages. A chatbot is conversational software and can be part of an app. For this project, Bot as a Service means we use shared technology supplied through EDAV. Like using a reference library, we gain access to an established service, but still need a suitable collection and careful checking. The chatbot is software that can make mistakes.”

**Transition:** “Here is how those pieces connect for our manual question.” **Evidence:** E01, E02, E03, E07, E08; C02, C03, C05, C10. Service support details remain to confirm.

## B03 — The intended answer journey

**Time:** 80 seconds. **Source slides:** S06–S08. **Purpose:** explain preparation, asking, and checking.

**Exact audience copy:**

> Before use: prepare the approved manuals in EDAV.
>
> Ask → clarify → find relevant passages → prepare a response → show sources → check
>
> Missing evidence should lead to an explanation of the gap.
>
> Intended process; live behavior still needs testing

**Visual:** V06b, simplified to one preparation line and one question line. Place the person at the final check. Keep citation caveats in the spoken explanation.

**Speaker notes:** “The preparation happens first. A question should then lead to relevant manual passages and an answer supported by those passages. If the evidence is missing or the model is unclear, the bot should say so or clarify. The person checks whether the source supports the answer for the right equipment. Source details depend on what EDAV reliably supplies; page numbers must never be invented. Our app displays the chat, while the intended evidence-seeking behavior belongs to the configured EDAV bot arrangement.”

**Transition:** “A manual can answer some questions, but other questions need different evidence.” **Evidence:** E02, E03, E04, E05; C06, C07, C08, C11.

## B04 — Manuals and their limits

**Time:** 65 seconds. **Source slide:** S09. **Purpose:** set practical expectations.

**Exact audience copy:**

| Question | Expected next step |
|---|---|
| Where are the cleaning instructions? | Clarify the model and find supporting content |
| Is this instrument calibrated today? | Check current equipment records |
| Am I authorized to operate it? | Consult the responsible person |

> Required behavior; still to verify

**Visual:** compact three-row table, no illustrative machine operation.

**Speaker notes:** “A manual describes information about equipment, but it does not establish what happened to our instrument today. It also does not authorize a person to use it. These are legitimate questions that require different sources or decision makers. This pilot is for help with the approved manuals. Testing includes whether the bot respects that boundary and avoids guessing.”

**Transition:** “Now we can understand what the project has prepared and what remains to be shown.” **Evidence:** E03, E04; C09.

## B05 — What the pilot must demonstrate

**Time:** 80 seconds. **Source slides:** S11–S12. **Purpose:** close the introduction and bridge to status evidence.

**Exact audience copy:**

> We have app connection software, prepared instructions, and tests.
>
> Live setup, manual processing, answer quality, and user value still need evidence.
>
> Explain it back: what is the app, what is the bot, and what does EDAV supply?
>
> Documented status · October 8, 2026

**Visual:** three labeled concepts—app, bot, shared service—with a manual and person-checking step. Use plain text rather than status percentages.

**Speaker notes:** “We have software and documents prepared, including tests of the bot's required responses. We still need evidence from the live bot and from people evaluating its answers. The ten behavior tests check specific requirements; they do not establish overall usefulness. In one sentence, how would you explain the difference between the app, the bot, and EDAV's service?” Allow 20 seconds. Accept “the app is where I interact; the bot responds; EDAV provides shared technology.” Add: “The manual supplies the evidence, and the person checks it.”

**Bridge into `s02-evidence`:** “You now know what the pieces mean. The next table separates what we can show in project files, what we have prepared, and what still needs evidence from the live service.” **Evidence:** E01, E03, E04; C11–C15.

## Three activities for the full deck

| ID / location | Presenter instruction | Expected learning | Fallback and time |
|---|---|---|---|
| A1 / S02 | Hide the reply. Ask, “What should the first response be?” | Recognize the need to identify equipment/model before advice | Offer “Could different instruments have different instructions?” Reveal after 15 seconds |
| A2 / S09 | Ask whether “Is it calibrated today?” calls for a manual answer, clarification, or current records | Separate static reference information from current operational evidence | Invite a show of hands; explain that even a known model does not establish today's status. 15 seconds |
| A3 / S12 | Ask someone to explain app, bot, and shared service using our example | Demonstrate understanding of the relationship, not acronym recall | Point to the three labels; add manuals and human review. 25 seconds |

The short version uses A3 in B05. All activities work through speech or raised hands; no phones, accounts, live bot, or polling tool are required. Do not record names or score participants. If no one volunteers, offer the sample explanation and move on.

## Comprehension check for the presenter

An adequate answer says the app is the tool/place used to interact, the chatbot exchanges messages, and EDAV supplies shared technology for that experience. A stronger answer adds that the manual is the intended evidence source and a person still checks it. Correct the idea that the app itself contains every manual or that the bot is a human expert. Re-explain through the running question, rather than adding more technical vocabulary.
