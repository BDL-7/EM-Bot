"""Verify the directly openable and portable presentation stay in sync."""
import importlib.util
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
DECK = ROOT / "ppt" / "ppt_BAAS"
spec = importlib.util.spec_from_file_location("presentation_build", DECK / "build.py")
assert spec and spec.loader
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)


class PresentationTests(unittest.TestCase):
    def test_source_has_local_dependencies_and_controls(self):
        source = (DECK / "src" / "slides.html").read_text(encoding="utf-8")
        self.assertIn("<!doctype html>", source.lower())
        self.assertEqual(source.count('<section class="slide'), 12)
        for path in ("theme.css", "deck.js", "../assets/manual-retrieval.png"):
            self.assertTrue((DECK / "src" / path).is_file(), path)
            self.assertIn(path, source)
        for control in ("previous", "next", "slide-picker", "sources-dialog", "help-dialog"):
            self.assertIn(f'id="{control}"', source)

    def test_portable_output_matches_source_and_embeds_dependencies(self):
        output = (DECK / "index.html").read_text(encoding="utf-8")
        self.assertEqual(output, builder.render())
        self.assertIn("data:image/png;base64,", output)
        self.assertIsNone(re.search(r'<(?:script|link)[^>]+(?:src|href)=', output))


if __name__ == "__main__":
    unittest.main()
