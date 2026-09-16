#!/usr/bin/env python3
"""Create and append local, lossless Markdown conversation archives."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Iterable


APPEND_MARKER = "<!-- RAW_TRANSCRIPT_APPEND_POINT: archive_chat_v1 -->"
INDEX_HEADER = """# Local Conversation Archive

This index is derived navigation metadata. The archive files are canonical.

| Date | Topic | Archive | Status | Themes |
|---|---|---|---|---|
"""


@dataclass(frozen=True)
class Message:
    role: str
    text: str
    timestamp: str | None = None
    label: str | None = None


def repository_root() -> Path:
    return Path(__file__).resolve().parents[1]


def archive_root() -> Path:
    return repository_root() / ".local" / "chat-archives"


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.casefold()).strip("-")
    return slug[:80] or "conversation"


def read_utf8_bytes(path: Path | None) -> bytes:
    data = path.read_bytes() if path else sys.stdin.buffer.read()
    if not data:
        raise ValueError("Transcript input is empty; no archive was created.")
    data.decode("utf-8", errors="strict")
    return data


def git_value(*args: str) -> str | None:
    try:
        result = subprocess.run(
            ["git", *args],
            cwd=repository_root(),
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
        )
    except (FileNotFoundError, subprocess.CalledProcessError):
        return None
    return result.stdout.strip() or None


def parse_codex_session(path: Path) -> tuple[list[Message], str | None]:
    messages: list[Message] = []
    session_id: str | None = None
    with path.open("r", encoding="utf-8", newline="") as stream:
        for line_number, line in enumerate(stream, start=1):
            try:
                event = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(
                    f"Invalid JSON on line {line_number} of {path}: {exc}"
                ) from exc

            payload = event.get("payload", {})
            if event.get("type") == "session_meta" and not session_id:
                session_id = payload.get("session_id") or payload.get("id")

            if event.get("type") != "response_item":
                continue
            if payload.get("type") != "message":
                continue
            role = payload.get("role")
            if role not in {"user", "assistant"}:
                continue

            text_parts: list[str] = []
            for part in payload.get("content", []):
                if part.get("type") in {"input_text", "output_text"}:
                    text_parts.append(part.get("text", ""))
            messages.append(
                Message(
                    role=role,
                    text="".join(text_parts),
                    timestamp=event.get("timestamp"),
                )
            )

    if not messages:
        raise ValueError(f"No user or assistant messages found in {path}.")
    return messages, session_id


def render_messages(
    messages: Iterable[Message], *, user_start: int = 0, assistant_start: int = 0
) -> bytes:
    user_count = user_start
    assistant_count = assistant_start
    sections: list[str] = []
    for message in messages:
        if message.role == "user":
            user_count += 1
            identifier = f"U{user_count:03d}"
            anchor = f"archive-msg-u-{user_count:03d}"
            label = message.label or "User"
        else:
            assistant_count += 1
            identifier = f"A{assistant_count:03d}"
            anchor = f"archive-msg-a-{assistant_count:03d}"
            label = message.label or "Assistant"
        timestamp = f" — {message.timestamp}" if message.timestamp else ""
        sections.append(
            f'<a id="{anchor}"></a>\n'
            f"### {identifier} — {label}{timestamp}\n\n"
            f"{message.text}"
        )
    return "\n\n".join(sections).encode("utf-8")


def next_archive_path(root: Path, date: str, topic: str) -> Path:
    root.mkdir(parents=True, exist_ok=True)
    base = root / f"{date}-{slugify(topic)}.md"
    if not base.exists():
        return base
    stamp = datetime.now().strftime("%H%M%S")
    candidate = root / f"{date}-{stamp}-{slugify(topic)}.md"
    counter = 2
    while candidate.exists():
        candidate = root / f"{date}-{stamp}-{slugify(topic)}-{counter}.md"
        counter += 1
    return candidate


def build_header(
    *,
    topic: str,
    date: str,
    source: str,
    session_id: str | None,
    tags: str,
    checksum: str,
) -> bytes:
    repo = repository_root().name
    branch = git_value("branch", "--show-current") or "unavailable (not a Git worktree)"
    session_line = f"- Session identifier: {session_id}\n" if session_id else ""
    tags_line = f"- Tags: {tags}\n" if tags else ""
    text = f"""# Conversation Archive: {topic}

- Archived: {date}
- Repository: {repo}
- Branch: {branch}
- Source: {source}
- Privacy: local only / intended to be gitignored
- Preservation mode: append-only raw transcript
- Source completeness: complete for messages present in the supplied source at capture time
{session_line}{tags_line}- Raw input SHA-256: `{checksum}`

## Preservation Contract

This archive contains canonical source conversation material.

Rules:

1. Raw transcript content is append-only.
2. Original messages are never rewritten.
3. Original messages are never deleted because they appear redundant.
4. Derived summaries may consolidate ideas.
5. Derived material never replaces the raw source transcript.
6. Missing source text is never fabricated.

## Derived Index

> The content in this section is derived from the raw transcript. It may be
> updated or regenerated, but it must never replace or modify the transcript.

### Major topics

- Not indexed yet.

### Decisions and action items

- Not indexed yet.

---

## Raw Transcript

"""
    return text.encode("utf-8")


def exclusive_write(path: Path, chunks: Iterable[bytes]) -> None:
    with path.open("xb") as stream:
        for chunk in chunks:
            stream.write(chunk)
        stream.flush()
        os.fsync(stream.fileno())


def atomic_update_index(
    root: Path, *, date: str, topic: str, path: Path, tags: str
) -> None:
    index_path = root / "INDEX.md"
    existing = index_path.read_text(encoding="utf-8") if index_path.exists() else INDEX_HEADER
    relative = f"./{path.name}"
    if relative in existing:
        return
    row = f"| {date} | {topic.replace('|', '\\|')} | [{path.name}]({relative}) | Active | {tags.replace('|', '\\|')} |\n"
    content = existing + ("" if existing.endswith("\n") else "\n") + row
    fd, temp_name = tempfile.mkstemp(prefix="INDEX-", suffix=".tmp", dir=root)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as stream:
            stream.write(content)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temp_name, index_path)
    finally:
        if os.path.exists(temp_name):
            os.unlink(temp_name)


def capture(args: argparse.Namespace) -> int:
    date = args.date or datetime.now().date().isoformat()
    session_id = args.session_id
    if args.user_attachment and not args.codex_session:
        raise ValueError("--user-attachment requires --codex-session.")
    if args.codex_session:
        messages, detected_session_id = parse_codex_session(args.codex_session)
        if args.user_attachment:
            insert_at = max(
                index for index, message in enumerate(messages) if message.role == "user"
            ) + 1
            attachments = [
                Message(
                    role="user",
                    text=read_utf8_bytes(path).decode("utf-8"),
                    label=f"User request attachment — {path.name}",
                )
                for path in args.user_attachment
            ]
            messages[insert_at:insert_at] = attachments
        raw = render_messages(messages)
        session_id = session_id or detected_session_id
    else:
        raw = read_utf8_bytes(args.input)

    checksum = hashlib.sha256(raw).hexdigest()
    root = archive_root()
    path = next_archive_path(root, date, args.topic)
    header = build_header(
        topic=args.topic,
        date=date,
        source=args.source,
        session_id=session_id,
        tags=args.tags,
        checksum=checksum,
    )
    exclusive_write(
        path,
        [header, raw, b"\n\n", APPEND_MARKER.encode("utf-8"), b"\n"],
    )
    atomic_update_index(root, date=date, topic=args.topic, path=path, tags=args.tags)
    print(f"Archive created:\n{path.relative_to(repository_root())}")
    return 0


def append(args: argparse.Namespace) -> int:
    root = archive_root().resolve()
    target = args.archive.resolve()
    try:
        target.relative_to(root)
    except ValueError as exc:
        raise ValueError(f"Append target must be beneath {root}.") from exc
    if not target.is_file():
        raise ValueError(f"Archive does not exist: {target}")
    if APPEND_MARKER.encode("utf-8") not in target.read_bytes():
        raise ValueError(f"Append marker not found in {target}; refusing to modify it.")

    codex_session = getattr(args, "codex_session", None)
    after = getattr(args, "after", None)
    if codex_session:
        if not after:
            raise ValueError("--after is required with --codex-session to prevent duplicates.")
        messages, _ = parse_codex_session(codex_session)
        messages = [
            message
            for message in messages
            if message.timestamp and message.timestamp > after
        ]
        if not messages:
            raise ValueError(f"No session messages found after {after}.")
        existing = target.read_text(encoding="utf-8")
        user_ids = [
            int(value)
            for value in re.findall(
                r'^<a id="(?:archive-)?msg-u-([0-9]+)"></a>$', existing, re.M
            )
        ]
        assistant_ids = [
            int(value)
            for value in re.findall(
                r'^<a id="(?:archive-)?msg-a-([0-9]+)"></a>$', existing, re.M
            )
        ]
        user_start = max(user_ids, default=0)
        assistant_start = max(assistant_ids, default=0)
        raw = render_messages(
            messages, user_start=user_start, assistant_start=assistant_start
        )
    else:
        raw = read_utf8_bytes(args.input)
    stamp = datetime.now().astimezone().isoformat(timespec="seconds")
    checksum = hashlib.sha256(raw).hexdigest()
    separator = (
        f"\n---\n\n### Transcript append — {stamp}\n\n"
        f"- Appended input SHA-256: {checksum}\n\n"
    ).encode("utf-8")
    with target.open("ab") as stream:
        stream.write(separator)
        stream.write(raw)
        if not raw.endswith((b"\n", b"\r")):
            stream.write(b"\n")
        stream.flush()
        os.fsync(stream.fileno())
    print(f"Transcript material appended to:\n{target.relative_to(repository_root())}")
    return 0


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description=__doc__)
    subparsers = result.add_subparsers(dest="command", required=True)

    capture_parser = subparsers.add_parser("capture", help="Create a new archive")
    capture_parser.add_argument("--topic", required=True)
    capture_parser.add_argument("--source", default="chatgpt/codex")
    capture_parser.add_argument("--date")
    capture_parser.add_argument("--session-id")
    capture_parser.add_argument("--tags", default="")
    source_group = capture_parser.add_mutually_exclusive_group()
    source_group.add_argument("--input", type=Path)
    source_group.add_argument("--codex-session", type=Path)
    capture_parser.add_argument(
        "--user-attachment",
        action="append",
        type=Path,
        help="Exact user-authored text to place after the final logged user message",
    )
    capture_parser.set_defaults(handler=capture)

    append_parser = subparsers.add_parser("append", help="Append supplied text")
    append_parser.add_argument("--archive", required=True, type=Path)
    append_source = append_parser.add_mutually_exclusive_group()
    append_source.add_argument("--input", type=Path)
    append_source.add_argument("--codex-session", type=Path)
    append_parser.add_argument(
        "--after", help="Exclusive ISO timestamp boundary for Codex session appends"
    )
    append_parser.set_defaults(handler=append)
    return result


def main() -> int:
    try:
        args = parser().parse_args()
        return args.handler(args)
    except (OSError, UnicodeError, ValueError) as exc:
        print(f"archive_chat: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
