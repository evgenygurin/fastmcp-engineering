from __future__ import annotations

from pathlib import Path

from tests.scenario_data import REPRESENTATIVE_SCENARIOS

ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / "skills"


def test_representative_scenarios_are_deterministic_and_complete() -> None:
    assert REPRESENTATIVE_SCENARIOS
    names = [scenario.skill for scenario in REPRESENTATIVE_SCENARIOS]
    assert len(names) == len(set(names))

    for scenario in REPRESENTATIVE_SCENARIOS:
        assert scenario.skill.startswith("fastmcp/")
        assert scenario.positive_input.strip()
        assert scenario.positive_expected.strip()
        assert scenario.negative_input.strip()
        assert scenario.negative_expected.strip()
        assert scenario.positive_input != scenario.negative_input
        assert scenario.positive_expected != scenario.negative_expected


def test_representative_scenarios_reference_existing_skill_packages() -> None:
    failures: list[str] = []
    for scenario in REPRESENTATIVE_SCENARIOS:
        skill_path = SKILLS_ROOT / Path(scenario.skill) / "SKILL.md"
        if not skill_path.is_file():
            failures.append(scenario.skill)

    assert not failures, (
        "Scenario fixtures must reference real skill packages:\n"
        + "\n".join(failures)
    )
