# Scoped revision verification

Compared raw slide sections captured before editing with the final editable source. Slides 3 and 5–12 are byte-for-byte identical. All 12 slides retain their order. Shared theme CSS, navigation JavaScript, and page template are byte-for-byte unchanged.

| Protected section | Identical before/after SHA-256 |
|---|---|
| s03 | aa8df8c5bdc43cd886b398e6ffdadd07f9d66f105be87af2be4fa9ff98754c99 |
| s05 | 12c566770d1f9e8d2d78ca29d794f58aab7781a049baf22ced4460d5b7a7e4ec |
| s06 | 7eb32634becccb51bba94e9da082fc47a006edbee55c4093e990119aec4c66e7 |
| s07 | d3f3f56da69395c713f03a83fe425f5c5393f908ebc9ae3524a320d4ac3c9f67 |
| s08 | 5feabb3ed74df4091cac84ea221520b0e1557fcb1baeb2a279feb0c478517ecb |
| s09 | ef8e11f8bbb4b1ab2c6a9379ad11c74745c094fea72da3ce1c9bf116406ac58c |
| s10 | 61a157bf71530fad69faa6f6a4e86c41c0b2b4655371fda31283da01e081282d |
| s11 | fcb14f6b4edf7182e53d869ba406939b41d0032db4d30d74d4fff305d55941ad |
| s12 | 966a72a39d370d10eb0ac2b8df248259bec9333742b24214f369f4a5a23c5d86 |

Replacement image inspected: generic equipment and abstract manual evidence; no readable procedures or identifiers. Browser-based visual QA is unavailable: the browser inventory returned no browsers. Layout, fullscreen, and printed-page rendering remain pending.

Validation passed: self-contained build; balanced HTML; 12 ordered slides; unique IDs; source coverage; image alt text; local document links; no speaker-note content; two remaining reveals and three quiz options. Synthetic DOM checks passed for navigation, reveals, deep links, source dialogs, quiz feedback, print accessibility state, and resize logic. These checks do not constitute browser rendering tests.
