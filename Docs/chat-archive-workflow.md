# Local conversation archive workflow

Important ChatGPT and Codex conversations can contain project history that is
not yet represented in design documents, issues, or code. This repository uses
a local archive convention to preserve that source material without publishing
it.

## Storage and privacy

Private transcripts live beneath `.local/chat-archives/`. The directory is
listed in `.gitignore` and must remain outside commits, packages, application
assets, and deployment bundles. Review transcript content for credentials,
personal information, and other sensitive material even though it is local.

The raw transcript is canonical and append-only. Summaries, indexes, decisions,
and action items are derived material: they may consolidate ideas, but they must
never replace, rewrite, or delete source messages.

## Capture a conversation

Capture a UTF-8 Markdown export from a file:

```powershell
python scripts/archive_chat.py capture `
  --topic "authentication redesign" `
  --source chatgpt `
  --input conversation.md
```

Or pipe UTF-8 transcript text through standard input:

```powershell
Get-Content -Raw conversation.md |
  python scripts/archive_chat.py capture --topic "authentication redesign"
```

For a legitimate local Codex JSONL session record, use:

```powershell
python scripts/archive_chat.py capture `
  --topic "authentication redesign" `
  --source codex `
  --codex-session C:\path\to\rollout-session.jsonl
```

The Codex-session mode selects only recorded `user` and `assistant` message
items. It does not reconstruct absent messages.

If the logged user message refers to a separate, user-authored pasted-text
attachment, preserve that source explicitly:

```powershell
python scripts/archive_chat.py capture `
  --topic "chat preservation infrastructure" `
  --codex-session C:\path\to\rollout-session.jsonl `
  --user-attachment C:\path\to\pasted-text.txt
```

The attachment receives its own labeled transcript entry immediately after the
last logged user message. Its text is not merged with or substituted for the
logged message.

Each capture uses exclusive file creation. If the date/topic filename already
exists, the script creates a timestamped successor instead of overwriting it.
The local `INDEX.md` is navigation metadata and can be regenerated; it is not a
substitute for an archive.

## Append additional turns

```powershell
python scripts/archive_chat.py append `
  --archive .local/chat-archives/2026-09-08-authentication-redesign.md `
  --input new-turns.md
```

Append accepts UTF-8 from `--input` or standard input, requires the archive's
append marker, writes only at the end of the file, and never rewrites earlier
bytes.

To append only later messages from the same Codex session, supply the timestamp
of the last captured message as an exclusive boundary:

```powershell
python scripts/archive_chat.py append `
  --archive .local/chat-archives/2026-09-08-authentication-redesign.md `
  --codex-session C:\path\to\rollout-session.jsonl `
  --after 2026-09-08T16:46:01.401Z
```

The explicit boundary is required to reduce the risk of duplicating already
captured turns.

## Verify Git exclusion

From a Git worktree, run:

```powershell
git check-ignore -v .local/chat-archives/<archive-name>.md
git status --short
```

The first command should identify the `.gitignore` rule and the archive must not
appear as an untracked file in the second command. If an archive was previously
tracked, stop and investigate; `.gitignore` does not untrack existing files.

## Recovery and promotion

Start with `.local/chat-archives/INDEX.md`, then open the linked Markdown
archive. Promote useful material by copying or deriving it into an appropriate
project artifact such as an ADR, issue, test, or design document. Never delete
the original transcript as part of promotion or deduplication.
