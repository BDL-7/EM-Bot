"""Read-only verification of the Phase 1 equipment-manual source register.

The check compares every register row with the PDF currently on disk.  It does
not modify the source manuals or the register.
"""

from __future__ import annotations

import hashlib
import sys
from pathlib import Path

from pypdf import PdfReader


def verify(root: Path) -> int:
    register_path = root / "PILOT_SOURCE_REGISTER.md"
    docs_dir = root / "Docs"
    rows = [
        line
        for line in register_path.read_text(encoding="utf-8").splitlines()
        if line.startswith("| EM-")
    ]
    mismatches: list[str] = []
    registered_names: set[str] = set()
    total_bytes = 0
    total_pages = 0

    for line in rows:
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) != 7:
            mismatches.append(f"malformed row ({len(cells)} cells): {line}")
            continue

        manual_id, _revision, filename, size, expected_sha, pages, _status = cells
        registered_names.add(filename)
        path = docs_dir / filename
        if not path.exists():
            mismatches.append(f"{manual_id}: missing file: {filename}")
            continue

        actual_size = path.stat().st_size
        actual_sha = hashlib.sha256(path.read_bytes()).hexdigest()
        actual_pages = len(PdfReader(str(path), strict=False).pages)
        total_bytes += actual_size
        total_pages += actual_pages
        if size != str(actual_size):
            mismatches.append(f"{manual_id}: size register={size}, disk={actual_size}")
        if expected_sha.lower() != actual_sha:
            mismatches.append(f"{manual_id}: sha register={expected_sha}, disk={actual_sha}")
        if pages != str(actual_pages):
            mismatches.append(f"{manual_id}: pages register={pages}, disk={actual_pages}")

    disk_names = {path.name for path in docs_dir.glob("*.pdf")}
    for filename in sorted(disk_names - registered_names):
        mismatches.append(f"unregistered PDF on disk: {filename}")

    print(f"register_rows={len(rows)}")
    print(f"pdfs_on_disk={len(disk_names)}")
    print(f"total_pdf_bytes={total_bytes}")
    print(f"total_pdf_pages={total_pages}")
    if mismatches:
        print("mismatches:")
        for mismatch in mismatches:
            print(f"- {mismatch}")
        return 1

    print("all_registered_rows_match_disk=True")
    return 0


if __name__ == "__main__":
    sys.exit(verify(Path(__file__).resolve().parents[1]))
