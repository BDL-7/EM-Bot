# Production handoff

This package implements the requested planning prompt. The user's follow-up selected **the complete planning package**, so production of slides and images remains a separate task. The plan is ready for content review; it has no fabricated phase approvals or visual-QA receipts.

## What is ready for review

The package provides the spoken opening, three title options, a recommended narrative, a timed 12-slide storyboard, exact draft audience text, notes and transitions, six visual concepts, four kinds of comparison table, three activities, a five-slide insertion, and evidence-linked claim boundaries.

The visible planned tables are deliberately compact: terms on S04, handling questions on S09, responsibilities on S10, and status on S11. S02's table specifies the text for a three-frame illustration; it does not require another table in the finished deck. The five-slide variant supplies its own exact copy rather than relying on a future author to improvise a summary.

## Decisions and assets needed before production

| Item | Proposed default or available fallback | What a decision changes |
|---|---|---|
| Delivery format | A 16:9 deck; HTML or PowerPoint remains unselected | Build tools, navigation, export, and accessibility checks |
| Title | Finding answers in equipment manuals | Cover and file naming |
| Presenter, organization, occasion | Omit until supplied; no invented name or event | Cover metadata and spoken introduction |
| Duration and audience | 14 minutes, adult laboratory colleagues with no software background | Full deck versus five-slide introduction |
| Brand/style | Proposed warm paper, dark text, teal and amber, familiar sans-serif | Theme approval; use approved organizational assets if provided |
| Human-task and library illustrations | V01/V03 briefs; conceptual diagrams are fallbacks | Image generation/sourcing and attribution |
| Live example | Use the clearly labeled conceptual sequence | A real example needs owner approval, verified response/source pairing, and a permitted screenshot or excerpt |
| Status refresh | Keep the October 8 documented-status label | Newly reviewed evidence may change S11/B05; it must have a source |
| Existing deck integration | Five-slide insertion after `s01-title` | Reconfirm target state and scope before editing it |

Most missing details have explicit fallbacks. A live screenshot, manual excerpt, or logo is not required to explain the concept and should not be invented to fill a visual gap.

## Proposed usefulness evaluation, for explanation rather than execution

Explain these measures conversationally on S11. This table is an evaluation proposal, not a new approved study protocol or a set of results.

| Question | Possible observation | Interpretation boundary |
|---|---|---|
| Is the answer supported? | A qualified reviewer checks each equipment claim against the applicable approved manual | Record the tested question set and which claims were scored; a plausible response is insufficient |
| Is the source checkable? | The displayed source leads to content that supports the answer for the correct model; missing locators are recorded | Citation presence and citation correctness are different observations |
| Does it handle uncertainty? | On unclear or unsupported questions, record clarification, an explicit gap, or an inappropriate answer | Keep Pass, Fail, and Blocked distinct; do not silently omit blocked cases |
| Does it help colleagues? | Observe representative users doing agreed information-finding tasks and collect feedback on finding and checking the evidence | State who and what was sampled; do not generalize beyond that evidence |

If a future evaluation measures time, use comparable tasks, include source-check time in both routes, describe the sampling and scoring rules, and report the observed results. Do not add a “minutes saved” figure to the planned deck before such evidence exists. The ten prepared behavior tests establish a different, narrower question than broad user usefulness.

## Optional technical appendix

These are topics only and are not part of the 12-slide count or 14-minute plan. Add them in a later build only if the audience needs them.

- **Embedding:** explain iframe as an embedded web view after showing app/chat containment. E02 supports the integration pattern.
- **Access:** explain that the connection requires approved configuration and access arrangements. Refer technical reviewers to E01/E02/E05; do not show credential values or assume the portal's token acknowledgment proves answer quality.
- **Retrieval vocabulary:** introduce retrieval-augmented generation only after “find passages, then draft from evidence” makes sense. Keep the explanation conceptual; the guide does not establish EDAV's internal retrieval implementation.
- **Verification:** distinguish repository checks, the ten live behavior tests, and a broader usefulness evaluation. E03/E04 define their different roles.

## Content-review questions

1. Can a colleague explain app, chatbot, and shared service after S05 without knowing an acronym?
2. Does the running question stay about finding information, with no invented equipment advice?
3. Does every intended/live distinction remain visible where it affects interpretation?
4. Does the source-check slide show what to inspect without fabricating evidence?
5. Is the main deck useful for this audience, or should the five-slide version introduce a separate status update?

These are review prompts, not records of user approval. A later author should record actual feedback and change only the agreed scope.

## Reusable production prompt

```text
Build a presentation from the reviewed planning package in _ppt_BAAS/.

Read README.md, storyboard.md, slide-plan.md, visual-briefs.md,
short-introduction.md, evidence.md, and review-record.md before editing.
Follow the repository's current contribution workflow and preserve unrelated
work. Use the presentation skill appropriate to the selected output format.

First identify which version I have authorized: the 12-slide, 14-minute deck
or the five-slide introduction for an existing deck. Confirm the output format
if I have not specified it. Use the exact audience text as the starting point,
with detailed explanations, sources, limitations, and transitions in notes.

Refresh drift-prone project facts from current evidence. Preserve intended,
illustrative, and documented-status labels. The EDAV integration guide supports
embedding; it does not prove this pilot's retrieval quality, live setup, model
choice, or service guarantees. Do not copy private manuals, registers, runbooks,
credential values, or personnel data into the deck or repository.

Use editable tables and diagrams. Create or source the proposed illustrations
only within the authorized production scope; record provenance and alt text.
Treat V01 and V03 as conceptual artwork. Keep V02 and V04 clearly illustrative
unless a permitted live response and matching source have been verified.
Do not invent cleaning instructions, settings, page numbers, screenshots,
success rates, time savings, or completed tests.

Separate audience material from presenter notes. Validate content coverage,
timing, links, source fidelity, and note separation; inspect every rendered
slide and reveal at presentation size. Report structural checks and visual
inspection separately. Record unresolved limits honestly.

If I authorize the short-section insertion, recheck the existing deck's state
and stable IDs. The proposed insertion is after s01-title and before
s02-evidence. Preserve the other slides unless I explicitly include them.
```

## Final comprehension check

Ask: **“Using our equipment-manual example, what is the app, what is the bot, and what does EDAV provide?”**

Accept a response such as: **“The app is where I interact. The bot exchanges messages with me. EDAV supplies shared technology for that experience. The manual supports the answer, and I check it.”**
