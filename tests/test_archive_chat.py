from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

from scripts import archive_chat


class ArchiveChatTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name) / "chat-archives"
        self.root.mkdir()

    def tearDown(self) -> None:
        self.temp.cleanup()

    def test_collision_does_not_overwrite(self) -> None:
        first = archive_chat.next_archive_path(self.root, "2026-09-08", "Test")
        first.write_text("original", encoding="utf-8")
        second = archive_chat.next_archive_path(self.root, "2026-09-08", "Test")
        self.assertNotEqual(first, second)
        self.assertEqual(first.read_text(encoding="utf-8"), "original")

    def test_capture_creates_archive_for_hello(self) -> None:
        source = Path(self.temp.name) / "conversation.md"
        source.write_bytes(b"hello")
        args = SimpleNamespace(
            date="2026-09-08",
            session_id=None,
            user_attachment=None,
            codex_session=None,
            input=source,
            topic="Hello test",
            source="test",
            tags="smoke",
        )
        with patch.object(archive_chat, "archive_root", return_value=self.root):
            with patch.object(archive_chat, "repository_root", return_value=Path(self.temp.name)):
                archive_chat.capture(args)
        archives = list(self.root.glob("2026-09-08-hello-test*.md"))
        self.assertEqual(len(archives), 1)
        self.assertIn(b"hello", archives[0].read_bytes())
        self.assertTrue((self.root / "INDEX.md").is_file())

    def test_utf8_rendering_survives(self) -> None:
        raw = "résumé\n日本語\n🙂"
        rendered = archive_chat.render_messages(
            [archive_chat.Message(role="user", text=raw)]
        )
        self.assertIn(raw.encode("utf-8"), rendered)

    def test_message_label_does_not_change_source_text(self) -> None:
        raw = "exact attached request"
        rendered = archive_chat.render_messages(
            [
                archive_chat.Message(
                    role="user", text=raw, label="User request attachment"
                )
            ]
        )
        self.assertIn(b"U001 \xe2\x80\x94 User request attachment", rendered)
        self.assertIn(raw.encode("utf-8"), rendered)

    def test_empty_input_fails(self) -> None:
        empty = Path(self.temp.name) / "empty.md"
        empty.write_bytes(b"")
        with self.assertRaisesRegex(ValueError, "empty"):
            archive_chat.read_utf8_bytes(empty)

    def test_exclusive_write_refuses_overwrite(self) -> None:
        target = self.root / "archive.md"
        archive_chat.exclusive_write(target, [b"hello"])
        with self.assertRaises(FileExistsError):
            archive_chat.exclusive_write(target, [b"replacement"])
        self.assertEqual(target.read_bytes(), b"hello")

    def test_append_preserves_existing_bytes(self) -> None:
        target = self.root / "archive.md"
        original = b"header\n" + archive_chat.APPEND_MARKER.encode() + b"\n"
        target.write_bytes(original)
        addition = Path(self.temp.name) / "turns.md"
        addition.write_bytes("résumé 日本語 🙂".encode("utf-8"))
        args = type(
            "Args", (), {"archive": target, "input": addition, "codex_session": None}
        )()
        with patch.object(archive_chat, "archive_root", return_value=self.root):
            with patch.object(archive_chat, "repository_root", return_value=Path(self.temp.name)):
                archive_chat.append(args)
        result = target.read_bytes()
        self.assertTrue(result.startswith(original))
        self.assertIn(addition.read_bytes(), result)

    def test_legacy_marker_in_source_is_not_an_append_sentinel(self) -> None:
        target = self.root / "archive.md"
        target.write_bytes(b"quoted <!-- RAW_TRANSCRIPT_APPEND_POINT --> only")
        addition = Path(self.temp.name) / "turns.md"
        addition.write_bytes(b"new")
        args = SimpleNamespace(archive=target, input=addition, codex_session=None)
        with patch.object(archive_chat, "archive_root", return_value=self.root):
            with self.assertRaisesRegex(ValueError, "Append marker not found"):
                archive_chat.append(args)


if __name__ == "__main__":
    unittest.main()
