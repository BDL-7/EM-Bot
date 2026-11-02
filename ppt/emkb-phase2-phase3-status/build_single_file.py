#!/usr/bin/env python3
from __future__ import annotations

import base64
import mimetypes
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "presentation-template-single-file.html"


def data_uri(path: Path) -> str:
    mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    payload = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{mime};base64,{payload}"


def main() -> None:
    html = (ROOT / "index.html").read_text(encoding="utf-8")
    css = (ROOT / "theme.css").read_text(encoding="utf-8")
    content = (ROOT / "deck-content.js").read_text(encoding="utf-8")
    js = (ROOT / "deck.js").read_text(encoding="utf-8")

    for asset in sorted((ROOT / "assets").glob("*")):
        if not asset.is_file():
            continue
        relative = f"assets/{asset.name}"
        content = content.replace(relative, data_uri(asset))

    html = re.sub(
        r'<link\s+rel="stylesheet"\s+href="theme\.css">',
        lambda _: f"<style>\n{css}\n</style>",
        html,
        count=1,
    )
    html = re.sub(
        r'<script\s+src="deck-content\.js"></script>',
        lambda _: f"<script>\n{content}\n</script>",
        html,
        count=1,
    )
    html = re.sub(
        r'<script\s+src="deck\.js"></script>',
        lambda _: f"<script>\n{js}\n</script>",
        html,
        count=1,
    )

    OUT.write_text(html, encoding="utf-8")
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
