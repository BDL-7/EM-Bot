"""Build a portable presentation from the directly openable source page."""
import base64
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "src"


def render():
    html = (SOURCE / "slides.html").read_text(encoding="utf-8")
    css = (SOURCE / "theme.css").read_text(encoding="utf-8")
    script = (SOURCE / "deck.js").read_text(encoding="utf-8")
    replacements = {
        '<link rel="stylesheet" href="theme.css">': f"<style>{css}</style>",
        '<script src="deck.js"></script>': f"<script>{script}</script>",
    }
    for marker, replacement in replacements.items():
        if html.count(marker) != 1:
            raise ValueError(f"Expected exactly one {marker}")
        html = html.replace(marker, replacement)
    for asset in set(re.findall(r'src="\.\./assets/([A-Za-z0-9._-]+)"', html)):
        path = ROOT / "assets" / asset
        if path.suffix.lower() != ".png" or not path.is_file():
            raise ValueError(f"Unsupported or missing asset: {path}")
        uri = "data:image/png;base64," + base64.b64encode(path.read_bytes()).decode("ascii")
        html = html.replace(f'src="../assets/{asset}"', f'src="{uri}"')
    if re.search(r'<(?:script|link)[^>]+(?:src|href)=|src="\.\./assets/', html):
        raise ValueError("Portable presentation has an external runtime dependency")
    if html.count('<section class="slide') != 12:
        raise ValueError("Expected 12 slides")
    return html


def build():
    html = render()
    output = ROOT / "index.html"
    output.write_text(html, encoding="utf-8", newline="\n")
    print(f"Built {output.name}: 12 slides, embedded assets ({output.stat().st_size:,} bytes).")


if __name__ == "__main__":
    build()
