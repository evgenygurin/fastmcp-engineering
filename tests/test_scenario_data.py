from __future__ import annotations

from tests.scenario_data import REPRESENTATIVE_SCENARIOS


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
