# Presentation Template

This project is managed by the `build-html-slide-workshop` skill.

## Authoritative and generated files

- `.workshop/deck-state.json` is the editable source for deck metadata, validated visual-style identifiers, slide content, exact layout data, presenter notes, transitions, approvals, and QA receipts.
- `deck-content.js` and `speaker-notes.js` are generated from workshop state.
- `theme.css` and `deck.js` define the 1280 x 720 visual and interaction system.
- `index.html` is the modular audience view; `presenter.html` adds presenter notes.
- `*-audience.html` and `*-presenter.html` are generated portable outputs.

Put new images under `assets/` and reference them with relative paths from each slide's `content.renderData`.

## Controls

- Left/Right arrows or Space: navigate.
- `F`: fullscreen.
- `D`: debug overflow.
- `P`: print or save as PDF.
- `N`: toggle presenter notes.
- `?slide=4`: open slide 4.
- `?debug=1`: enable overflow diagnostics.

## Editing boundary

Edit workshop state for ordinary content changes. Change `theme.css` or `deck.js` only for a deliberate design-system capability. Do not edit portable HTML.

Use `set-visual-style.mjs` to list, preview, and confirm named font-family, font-scale, and color-scheme choices. Do not place arbitrary CSS values in workshop state.

The audience page does not load presenter notes. Notes included in presenter HTML remain inspectable and must not be treated as confidential.
