from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / "skills"

SEMANTIC_REQUIREMENTS = {
    "mission": ("mission", "purpose", "goal"),
    "research": ("research", "evidence", "official"),
    "verification": ("verification", "testing", "test"),
    "failure": ("failure", "rejection", "escalation", "error"),
    "deliverables": ("deliverables", "outputs", "artifacts"),
    "version": ("version", "compatibility", "release"),
}

RUNTIME_CITATION = re.compile(r"\bturn\d+(?:search|news|image|product|business|youtube)\d+\b")
PLACEHOLDER = re.compile(r"\b(?:TODO|TBD|FIXME)\b|\[\s*insert\s+.+?\s*\]", re.I)


def skill_files() -> list[Path]:
    return sorted(SKILLS_ROOT.rglob("SKILL.md"))


def section_text(text: str) -> str:
    # Ignore fenced examples when checking semantic presence only loosely; the
    # contract is intentionally keyword-based so skills can use different prose.
    return re.sub(r"```.*?```", "", text, flags=re.S).lower()


def test_skill_inventory_is_nonempty() -> None:
    assert skill_files(), "No SKILL.md files found under skills/"


def test_every_skill_has_required_semantic_contract() -> None:
    failures: list[str] = []
    for path in skill_files():
        text = section_text(path.read_text(encoding="utf-8"))
        missing = [
            requirement
            for requirement, alternatives in SEMANTIC_REQUIREMENTS.items()
            if not any(token in text for token in alternatives)
        ]
        if missing:
            failures.append(f"{path.relative_to(ROOT)}: missing {', '.join(missing)}")
    assert not failures, "\n".join(failures)


def test_skill_frontmatter_is_valid_when_present() -> None:
    failures: list[str] = []
    for path in skill_files():
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            continue
        match = re.match(r"\A---\n(.*?)\n---\n", text, flags=re.S)
        if not match:
            failures.append(f"{path.relative_to(ROOT)}: malformed frontmatter")
            continue
        frontmatter = match.group(1)
        if not re.search(r"^name:\s*\S+", frontmatter, re.M):
            failures.append(f"{path.relative_to(ROOT)}: missing frontmatter name")
        if not re.search(r"^description:\s*\S+", frontmatter, re.M):
            failures.append(f"{path.relative_to(ROOT)}: missing frontmatter description")
    assert not failures, "\n".join(failures)


def test_no_runtime_citations_or_placeholders_in_skills() -> None:
    failures: list[str] = []
    for path in skill_files():
        text = path.read_text(encoding="utf-8")
        if RUNTIME_CITATION.search(text):
            failures.append(f"{path.relative_to(ROOT)}: runtime citation token")
        if PLACEHOLDER.search(text):
            failures.append(f"{path.relative_to(ROOT)}: unresolved placeholder")
    assert not failures, "\n".join(failures)


def test_acceptance_artifact_exists_for_each_skill() -> None:
    failures = [
        str(path.parent.relative_to(ROOT))
        for path in skill_files()
        if not (path.parent / "ACCEPTANCE.md").exists()
    ]
    assert not failures, "Missing ACCEPTANCE.md:\n" + "\n".join(failures)


def test_acceptance_files_are_nonempty() -> None:
    failures = []
    for path in skill_files():
        acceptance = path.parent / "ACCEPTANCE.md"
        if acceptance.exists() and not acceptance.read_text(encoding="utf-8").strip():
            failures.append(str(acceptance.relative_to(ROOT)))
    assert not failures, "Empty ACCEPTANCE.md:\n" + "\n".join(failures)


def test_agent_contract_requires_skill_qa() -> None:
    agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8").lower()
    required = ("documentation", "verification", "pr", "branch")
    missing = [word for word in required if word not in agents]
    assert not missing, f"AGENTS.md missing lifecycle/QA concepts: {missing}"
