# Finding answers in equipment manuals

> Think of the last time you knew an answer was somewhere in a manual, but finding the right passage took several steps. Our pilot asks whether you could start with an ordinary question, get help finding relevant information, and check the source yourself. Today we will follow that journey, explain the software behind it, and show what we still need to test.

This is the proposed **30-second spoken introduction**. The planning package is complete for review; its proposed slide content and visual direction have not received separate content approval. No slides, images, live demonstrations, or EDAV configuration were created.

**Audience:** laboratory colleagues with no assumed software background. **Format:** 12 slides, 14 minutes including three short interactions. **Evidence date:** October 8, 2026, America/New_York. **Tracking:** [issue #22](https://github.com/BDL-7/EM-Bot/issues/22).

## Read in this order

| Document | What you can review |
|---|---|
| [Storyboard](storyboard.md) | Audience questions, learning sequence, visuals, and a timed run of show |
| [Complete slide plan](slide-plan.md) | Exact draft slide copy, table contents, talk tracks, evidence cues, and transitions for all 12 slides |
| [Visual briefs](visual-briefs.md) | Six visual concepts, composition, alt text, sourcing needs, and production specifications |
| [Short introduction and activities](short-introduction.md) | Five slides for the existing status deck, insertion points, spoken transitions, and three audience exercises |
| [Evidence and claims](evidence.md) | Published source links, local-to-published document mapping, claim limits, and missing evidence |
| [Production handoff](production-handoff.md) | Review questions, needed assets/facts, optional technical appendix, and a reusable next-step prompt |
| [Review record](review-record.md) | Checks performed on this package and the limits of those checks |

## Recommended approach

Follow one colleague asking: **“Where does the manual explain how to clean this instrument?”** The example concerns locating information. It supplies no cleaning instructions and makes no claim about a particular instrument.

Show a proposed conversation before teaching terminology. Reveal a clarifying question, then explain the app that displays the conversation, the bot that responds, and the shared service supporting it. Finish by returning to the person who checks the source. This sequence gives every new word a concrete referent.

The single analogy is a reference library. The approved manuals are the collection; the chatbot acts like a conversational reference helper; the app is the tool used to reach it; EDAV supplies shared technology; our team selects sources, specifies behavior, and checks results. Introduce the analogy on slide 5, explain its limits immediately, then return to the real project on slide 6. The helper is software and has no human expert's judgment.

The presentation's interest comes from revealing how a familiar problem could be handled, predicting a response, and checking its evidence. Avoid technical spectacle, simulated success, and performance claims without measurements. The illustrated starting workflow is a recognizable scenario, not a measured account of every colleague's experience.

## Title options

| Title | Use |
|---|---|
| **Finding answers in equipment manuals** | Recommended: begins with the task and works for an audience unfamiliar with software |
| Asking our equipment manuals a question | More conversational; explain that the software searches documents and the manuals themselves do not speak |
| EM Knowledge Bot: the idea, the pieces, the pilot | Useful when the audience already knows the project name |

Recommended subtitle: **An introduction to our EDAV bot pilot**. Spell out **Bot as a Service** when it first appears on slide 5. Use the term in this project's sense; other industries also use BaaS to mean Backend as a Service.

## What the audience should leave able to explain

1. The pilot explores help with locating and understanding approved manual information.
2. An app helps someone perform a task; a chatbot can be one feature within it.
3. A shared service supplies capabilities another team operates, while our team still has responsibilities.
4. Preparing documents is separate from asking a question.
5. An answer needs supporting evidence, and the person still checks the source.
6. Repository code and prepared instructions do not establish live bot quality or usefulness.

## Evidence and scope

The package uses the published `dev` baseline `dc2d11fae2ecd3d6448d38b32452485fe0469107` and the inspected local documentation reorganization. Project status is reported as **documented in those sources**, not independently verified in a live environment. The EDAV GitHub guide was accessible; the EDAV portal was not. [Evidence and claims](evidence.md) records exactly what each source supports.

This change adds planning documents and a repository README link. It does not alter the existing status deck, application, manuals, controlled bot instructions, or acceptance tests. It contains no private manual register, EDAV runbook, personnel information, or credential values.

The next production step is a separate instruction to build the deck using this review package. Presenter name, branding, design approval, and demonstration evidence remain open; they do not prevent reviewing the proposed story now.
