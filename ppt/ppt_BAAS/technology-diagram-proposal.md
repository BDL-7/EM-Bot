# Technology diagram proposal — review before implementation

No slide is added or changed by this proposal. The existing twelve-slide order remains intact.

## The story to show

A person opens our page in a browser and asks a question through EDAV chat. Our temporary Flask application runs on Posit Connect and supplies the parent page. The EDAV Microbot interface is displayed inside that page in an iframe, but is separately hosted by EDAV. Display containment does not mean that EDAV software runs inside Flask.

Draw two adjacent hosting areas rather than a single vertical technology stack. On the left, put the person's browser above a Posit Connect area containing Flask. Inside the browser page, show a smaller EDAV chat window. On the right, show the separately hosted EDAV interface communicating with a configured bot service. Use a dashed boundary around intended bot functions: instructions define scope, retrieval finds relevant passages, and an AI language model drafts a response using the question and evidence. These are functional steps, not verified backend products or deployment units.

Place approved equipment manuals beside those functional steps as the intended evidence collection. Do not place them inside the browser, Flask, or a named EDAV storage product. The response and available source information return through chat; the person checks the supporting manual. Source display and retrieval quality still require live verification.

## Visual grammar

| Relationship | Proposed treatment | Meaning |
|---|---|---|
| Inside | Nested outline | Chat is displayed inside the parent page; Flask belongs inside its hosting area |
| Runs on | Short labeled connector | Flask runs on Posit Connect; the browser displays the page |
| Communicates with | Solid two-way connector | Parent page and EDAV iframe exchange documented messages; this is not a storage relationship |
| Document preparation | Dashed amber path | Approve versions, register through the supported source path, and verify search/source behavior before use and after updates |
| Each question | Numbered teal path | Ask, clarify equipment/model, find passages, draft, return sources, check |

Do not draw the answer as passing through Flask: the host supports access and authentication; it does not retrieve manual passages or create the answer. Keep the exact backend routing unclaimed.

## Detail placement

| Detail | Placement | Treatment and qualification |
|---|---|---|
| Person, browser, host page, embedded EDAV chat | Main diagram | Familiar task labels first; technical names second |
| Flask on Posit Connect; separately hosted EDAV | Main diagram | Explicit hosting boundaries; repository-documented deployment, not a new live check |
| Instructions, retrieval, AI language model | Main diagram | Intended functions; no model vendor, index, database, or orchestration technology inferred |
| Manuals and answer/source return | Main diagram | Evidence collection and intended response flow, not storage locations |
| Preparation versus each question | Main diagram | Two visually distinct paths |
| Equipment model and manual version | Expandable detail | Match before answering; ambiguous questions prompt clarification |
| Missing evidence | Expandable detail | Explain the gap and avoid inventing instructions |
| Updates and stale information | Expandable detail | Version tracking, reprocessing where required, and rechecking representative questions; mechanism unverified |
| Source reliability | Expandable detail | Verify that displayed document links and available locators support the answer; no invented page numbers |
| User identity versus app authentication | Expandable detail | Signed-in Connect user controls host access; the application's app-only EDAV authentication is separate |
| Token handoff | Expandable detail | Host obtains access authorization and browser hands it to the intended EDAV frame; omit values, secret names, and mechanics from main visual |
| Exact-origin message checking | Technical appendix | Outgoing destination and incoming origin are checked; acknowledgment is correlated. Do not imply this alone proves complete security |
| Bot/client identifier | Technical appendix | `clientId` selects configured bot context; it is not a credential or proof of user identity |
| EDAV/authentication unavailable | Expandable detail | Show unavailable/pending state and a manual-access fallback as proposed user behavior; do not represent a waiting acknowledgment as a successful answer |
| Detailed failure handling | Technical appendix | Current client reports configuration/token failures and waits for acknowledgment; outage timeout and recovery behavior require verification |
| Document storage, logging, retention, backend retrieval implementation | Evidence register only | Unknown until EDAV provides authoritative confirmation; do not name technologies |

## Evidence and limits

Reviewed against repository base `81d2f92` on October 8, 2026:

- [Repository README](../../README.md): pilot scope, temporary host, Connect deployment, identity separation, exclusion of manuals from host deployment, and no host retrieval/model calls.
- [Host application](../../host_app/app.py) and [authentication provider](../../host_app/entra_auth.py): server responsibilities and app authentication implementation. Code presence does not establish successful live authentication.
- [Microbot integration](../../host_app/static/microbot.js): iframe, `clientId`, token handoff, exact-origin checks, acknowledgment, and failure/pending states.
- [Official EDAV integration guide](https://github.com/cdcent/edav-BaaS): authoritative integration reference. The current revision's web fetch was unavailable; the local implementation was inspected, and prior guide review is recorded in [evidence.md](evidence.md). Backend design must not be inferred from this guide.

Review the boundaries and desired detail level before drawing or adding a future technology slide. No assumption of live retrieval, approved model selection, verified citation behavior, or production readiness is made.
