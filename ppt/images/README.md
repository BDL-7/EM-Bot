# EMLab BaaS architecture image

[Open the architecture image](emlab-baas-architecture.png).

Generated October 9, 2026 with the built-in image-generation tool and visually inspected after one correction pass. EMLab is the audience-facing name requested by the user; repository code names remain Aquarius / EM Knowledge Bot. This is a conceptual integration diagram, not proof of successful live service operation.

## Evidence and interpretation

Reviewed against `origin/dev` at `b155c03`:

- [Root README](../../README.md): Posit Connect hosting, restricted signed-in access, pilot manual collection and no host retrieval/model calls.
- [Flask application](../../host_app/app.py): parent page and authenticated token endpoint.
- [Entra provider](../../host_app/entra_auth.py): server-side app-only authentication using MSAL.
- [Microbot client](../../host_app/static/microbot.js): separately hosted iframe, `clientId`, exact-origin message checks, token handoff and acknowledgment.

Nested browser boxes mean display containment. Flask runs on Posit Connect. The EDAV UI is separately hosted even though displayed inside the parent page. The conceptual service-to-UI path does not specify actual backend routing. Instructions, retrieval and drafting are intended functions; no backend database, model vendor, storage, logging or retention implementation is asserted. User identity and application authentication are distinct; the Connect sign-in provider is not asserted. Generic manual covers and conversation are illustrative, not real source material or test outputs. The per-question path describes intended behavior, not implemented host retrieval. The manuals' preparation arrow describes a supported setup objective, not verified ingestion.

## Validation

PNG file signature and dimensions checked; identical bytes copied to the user workspace and publication worktree. Visual inspection checked labels, hosting/display boundaries, evidence flow, illustrative conversation, and unverified-function qualifications. No existing presentation slides or application code were edited. This is a raster asset: labels are embedded in the PNG. [Generation prompts](generation-prompt.md) are retained for revision.
