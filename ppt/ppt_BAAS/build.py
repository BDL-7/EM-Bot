"""Build the offline, audience-only HTML presentation with Python's standard library."""
from pathlib import Path
import base64
import re

ROOT = Path(__file__).resolve().parent

def build():
    source = ROOT / 'src'
    html = (source / 'template.html').read_text(encoding='utf-8')
    slides = (source / 'slides.html').read_text(encoding='utf-8')
    css = (source / 'theme.css').read_text(encoding='utf-8')
    script = (source / 'deck.js').read_text(encoding='utf-8')
    assert slides.count('<section class="slide') == 12
    for marker in ('<!--__SLIDES__-->', '/*__THEME__*/', '/*__SCRIPT__*/'):
        assert html.count(marker) == 1, marker
    for asset_name in set(re.findall(r'asset:([A-Za-z0-9._-]+)', slides)):
        path = ROOT / 'assets' / asset_name
        assert path.suffix == '.png' and path.is_file(), path
        uri = 'data:image/png;base64,' + base64.b64encode(path.read_bytes()).decode('ascii')
        slides = slides.replace('asset:' + asset_name, uri)
    html = html.replace('<!--__SLIDES__-->', slides).replace('/*__THEME__*/', css).replace('/*__SCRIPT__*/', script)
    assert not re.search(r'<(?:script|link)[^>]+(?:src|href)=', html), 'External runtime dependency'
    assert 'asset:' not in html
    assert 'speaker' not in html.lower() and 'talktrack' not in html.lower()
    output = ROOT / 'index.html'
    output.write_text(html, encoding='utf-8', newline='\n')
    print(f'Built {output.name}: 12 slides, embedded illustration, no external runtime dependencies ({output.stat().st_size:,} bytes).')

if __name__ == '__main__':
    build()
