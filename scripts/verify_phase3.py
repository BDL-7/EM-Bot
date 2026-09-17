"""Read-only consistency check for the Phase 3 behavior artifacts.

This validates the repository package, not the behavior of a live EDAV bot.
Live behavior must be recorded through the Phase 3 execution and test records.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


RELEASE_ID = "EMKB-P3-v1.0"
EXPECTED_TEST_IDS = {f"P3-T{number:02d}" for number in range(1, 11)}


def verify(root: Path) -> int:
    paths = {
        "configuration": root / "PHASE_3_BEHAVIOR_CONFIGURATION.md",
        "instructions": root / "PILOT_BOT_INSTRUCTIONS.md",
        "tests": root / "PHASE_3_BEHAVIOR_TESTS.md",
        "readme": root / "README.md",
    }
    errors: list[str] = []
    content: dict[str, str] = {}

    for label, path in paths.items():
        if not path.is_file():
            errors.append(f"missing {label} artifact: {path.name}")
            continue
        content[label] = path.read_text(encoding="utf-8")

    for label in ("configuration", "instructions", "tests", "readme"):
        text = content.get(label, "")
        if RELEASE_ID not in text:
            errors.append(f"{label} does not identify release {RELEASE_ID}")

    instruction_requirements = {
        "bot identity": "You are EM Knowledge Bot",
        "35-manual boundary": "approved 35-manual corpus",
        "citation restraint": "never calculate, infer, or invent one",
        "ambiguity handling": "ask a clarifying question",
        "competency refusal": "competent, trained, certified, or authorized",
        "PII boundary": "personnel records, or PII",
        "current-status boundary": "calibrated, available, functional, or safe right now",
        "safety-control boundary": "bypassing an interlock",
    }
    instructions = content.get("instructions", "")
    for label, required_text in instruction_requirements.items():
        if required_text not in instructions:
            errors.append(f"instructions missing {label}: {required_text!r}")

    tests = content.get("tests", "")
    observed_test_ids = set(re.findall(r"\| (P3-T\d{2}) \|", tests))
    if observed_test_ids != EXPECTED_TEST_IDS:
        missing = sorted(EXPECTED_TEST_IDS - observed_test_ids)
        unexpected = sorted(observed_test_ids - EXPECTED_TEST_IDS)
        errors.append(f"test ID mismatch: missing={missing}, unexpected={unexpected}")

    configuration = content.get("configuration", "")
    for test_id in sorted(EXPECTED_TEST_IDS):
        if test_id not in tests:
            errors.append(f"test artifact missing {test_id}")
    if "prepared, not applied or verified" not in configuration:
        errors.append("configuration does not preserve prepared-versus-applied status")

    readme = content.get("readme", "")
    for filename in (
        "PHASE_3_BEHAVIOR_CONFIGURATION.md",
        "PHASE_3_BEHAVIOR_TESTS.md",
        "PILOT_BOT_INSTRUCTIONS.md",
        "scripts/verify_phase3.py",
    ):
        if filename not in readme:
            errors.append(f"README does not reference {filename}")

    print(f"release_id={RELEASE_ID}")
    print(f"phase3_artifacts={len(content)}/{len(paths)}")
    print(f"behavior_test_ids={len(observed_test_ids)}")
    if errors:
        print("errors:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("phase3_artifacts_consistent=True")
    print("live_edav_behavior_verified=False")
    return 0


if __name__ == "__main__":
    sys.exit(verify(Path(__file__).resolve().parents[1]))
