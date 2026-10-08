# Presentation maintenance

The user authorized the HTML build, requested `ppt/ppt_BAAS`, and removed the need for speaker notes. This folder now contains the audience-only HTML, editable build sources, conceptual illustration, and supporting evidence/design documents.

## Editing and rebuilding

1. Update audience copy and semantic diagrams in `src/slides.html`.
2. Update behavior in `src/deck.js` and styling in `src/theme.css` only as needed.
3. Preserve source IDs, intended-behavior labels, and the distinction between documented status and live outcomes.
4. Run `python ppt/ppt_BAAS/build.py` from the repository root.
5. Check `index.html` in a modern browser, including reveals, source dialogs, keyboard navigation, print output, and reduced motion.

Do not add a presenter view or talk tracks unless requested. The Sources control holds evidence and limitations for the audience. The HTML requires no network requests for fonts, scripts, or images.

## Review before presenting

- Confirm audience and available time. The full deck has 12 slides and a planned 14-minute duration.
- Check readability at the actual display size. The 1280 × 720 design scales to the viewport.
- Recheck project status against current evidence. The displayed evidence date is October 8, 2026.
- Keep demonstrations conceptual unless a live response and its source have been verified and cleared for use.
- Recheck the separate status deck before any future short-section insertion; do not silently alter it.

## Limits that must remain visible

The EDAV integration guide supports embedding chat, not conclusions about this pilot's retrieval quality, live setup, model choice, or service guarantees. The manual count comes from project records. The ten tests are prepared and do not establish overall usefulness. Static manuals cannot determine today's instrument status or personal authorization.

Source diagrams and workflow comparisons are conceptual. They contain no actual equipment instructions or manual excerpts and report no measured accuracy, time saving, or cost saving.

## Optional future additions

If requested, a technical appendix could explain the embedded chat view, approved access arrangements, and the distinction between software checks, live behavior tests, and broader evaluation. Add these only after the basic concepts are understood. Use current evidence and avoid publishing private manuals, registers, runbooks, personnel records, or credential values.
