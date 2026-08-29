from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / "skills"

POSITIVE_MARKERS = (
    "positive scenario",
    "happy path",
    "success scenario",
)
NEGATIVE_MARKERS = (
    "negative scenario",
    "failure scenario",
    "failure mode",
    "invalid scenario",
)
EVIDENCE_MARKERS = (
    "evidence",
    "verification",
    "expected result",
    "expected outcome",
)


def skill_files() -> list[Path]:
    return sorted(SKILLS_ROOT.rglob("SKILL.md"))


def normalized(text: str) -> str:
    return re.sub(r"\s+", " ", text.lower())


def contains_any(text: str, markers: tuple[str, ...]) -> bool:
    return any(marker in text for marker in markers)


def test_every_skill_has_explicit_positive_and_negative_scenarios() -> None:
    failures: list[str] = []
    for skill in skill_files():
        acceptance = skill.parent / "ACCEPTANCE.md"
        text = normalized(skill.read_text(encoding="utf-8"))
        if acceptance.exists():
            text += " " + normalized(acceptance.read_text(encoding="utf-8"))

        missing: list[str] = []
        if not contains_any(text, POSITIVE_MARKERS):
            missing.append("positive scenario")
        if not contains_any(text, NEGATIVE_MARKERS):
            missing.append("negative scenario")
        if not contains_any(text, EVIDENCE_MARKERS):
            missing.append("verification/evidence")

        if missing:
            failures.append(f"{skill.parent.relative_to(ROOT)}: missing {', '.join(missing)}")

    assert not failures, (
        "Every skill must expose executable QA intent in its package.\n"
        "Missing scenario/evidence markers:\n" + "\n".join(failures)
    )


def test_scenario_contract_requires_a_stop_condition() -> None:
    failures: list[str] = []
    for skill in skill_files():
        acceptance = skill.parent / "ACCEPTANCE.md"
        if not acceptance.exists():
            continue
        text = normalized(acceptance.read_text(encoding="utf-8"))
        has_failure = contains_any(
            text,
            ("stop", "reject", "escalate", "deny", "must not", "invalid"),
        )
        if not has_failure:
            failures.append(str(acceptance.relative_to(ROOT)))

    assert not failures, (
        "Acceptance contracts must define a deterministic failure/stop condition:\n"
        + "\n".join(failures)
    )
