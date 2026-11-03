# Microbot and BaaS: beginner introduction

Open [src/slides.html](src/slides.html) directly in a modern browser for the
editable presentation. It uses local CSS, JavaScript and an illustration, so
keep the `src` and `assets` folders together. Alternatively, share the generated
[index.html](index.html), which embeds those assets and works offline alone.
External source links require access to their websites.

The 12 slides explain Microbots, EDAV BaaS, the equipment-manual example,
responsibilities, limitations and the evidence still needed. The 35-manual
pilot baseline and a screenshot reporting 25 documents are different kinds of
evidence; neither proves the current processed corpus or answer accuracy.
See [evidence.md](evidence.md) for sources and qualifications.

## Controls

Use the arrow keys or toolbar to navigate, and the selector to jump to a
slide. Right arrow or Space also reveals content. Select **Sources** (or press
S) for slide-specific evidence; `?` opens keyboard help, F toggles fullscreen,
and P opens print. Printing includes the reveal content.

## Maintain and rebuild

`src/slides.html` is the authoritative document; `src/theme.css`,
`src/deck.js`, and `assets/` provide its local dependencies. Edit those files,
then run from the repository root:

```text
python ppt/ppt_BAAS/build.py
```

Commit the regenerated `index.html` with the source. Do not edit the generated
output separately. [Illustration provenance](assets/README.md) and
[historical design notes](../../archive/presentations/introduction-design-notes/)
are retained separately. The [historical project status deck](../../archive/presentations/2026-10-project-status/)
is a different presentation, not a current status report.
