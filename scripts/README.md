# Validation scripts

Run these commands from the repository root. The scripts do not deploy the
host or modify manuals.

| Script | What it verifies | Required local input | Safe without manuals? | Command | Result |
|---|---|---|---|---|---|
| `verify_bot.py` | The tracked bot instructions, behavior record, tests, and root README agree on the release ID and required test set. | Tracked repository files only. | Yes. | `python scripts/verify_bot.py` | A passing result reports `behavior_artifacts_consistent=True`; it does not prove live EDAV behavior. |
| `verify_source_register.py` | The local manual register matches the local PDF corpus by filename, size, SHA-256, and page count. | Ignored `Docs/manual-register.md`, all approved `Docs/*.pdf` files, and `pypdf`. | No. Do not run it on an incomplete corpus. | `python scripts/verify_source_register.py` | A passing result reports `all_registered_rows_match_disk=True`; a failure identifies missing or mismatched local material. |
| `archive_chat.py` | Creates or appends private, lossless local conversation archives. | A UTF-8 conversation input or legitimate Codex session record. | Yes; it does not read manuals. | See the [archive workflow](../Docs/chat-archive-workflow.md). | It creates local ignored archives and refuses unsafe overwrite or non-append operations. |

## Related tests

Run the Python suites with:

```text
python -m unittest discover -s tests
python -m pytest tests/test_app.py tests/test_entra_auth.py tests/test_microbot_contract.py tests/test_deployment_boundary.py
```

If Node.js is available, run the iframe contract tests with:

```text
node --test tests/test_microbot_js.mjs tests/test_auth_check_js.mjs
```

Passing repository checks verify the local implementation and packaging rules.
They do not validate EDAV portal configuration, manual ingestion, citations, or
live bot behavior.
