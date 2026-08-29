# Skill QA

## Purpose

The repository contains reusable engineering skills rather than an executable application. Skill correctness is therefore tested as an executable contract over the skill package structure and as a scenario-based review of behavior.

## Current inventory

The `main` snapshot contains **59** `SKILL.md` packages. Every skill package must have a corresponding `ACCEPTANCE.md` contract. The QA test discovers skills recursively, so nested skill packages are included.

## Automated checks

Run:

```bash
python -m pytest tests/test_skill_contract.py
```

The suite checks:

- non-empty skill inventory;
- required semantic contract coverage: mission, research/evidence, verification/testing, failure/escalation, outputs/artifacts, and version/compatibility;
- valid YAML-like frontmatter when frontmatter is used;
- no runtime web-tool citation tokens in skill instructions;
- no unresolved TODO/TBD/FIXME placeholders;
- one non-empty `ACCEPTANCE.md` per skill package;
- agent-level lifecycle concepts remain present.

## Scenario checks

For each skill, review at least one positive and one negative scenario:

```text
positive scenario
  -> skill should be selected
  -> required upstream evidence exists
  -> decision/implementation procedure is followed
  -> verification evidence is produced

negative scenario
  -> skill should not be selected, OR
  -> skill must stop/escalate when prerequisites/evidence are missing
```

FastMCP-specific skills additionally require version-aware official documentation research and protocol semantics checks.

## Current environment limitation

GitHub Actions are not an available verification mechanism for this repository in the current environment. The repository also contains no application runtime/test manifest such as `pyproject.toml` or `package.json`. The QA suite is therefore intentionally standard-library based apart from the optional pytest runner, and its source is syntax-smoke-tested locally. A full 59-skill execution requires a local checkout of the repository.

Do not report the 59-skill suite as passing until `python -m pytest tests/test_skill_contract.py` has actually executed against the current checkout.
