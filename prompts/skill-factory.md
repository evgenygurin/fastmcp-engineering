# Skill Factory Prompt Contract

The Skill Factory creates or revises a specialized engineering skill in an isolated session.

## Input

The agent receives the target skill, project requirements, repository contracts, current version policy, and available research artifacts.

## Mandatory sequence

1. Read all applicable repository contracts.
2. Identify the exact skill boundary and non-goals.
3. Research the official documentation for every relevant API.
4. Enumerate and inspect relevant official examples, source, and tests.
5. Build a version matrix and identify unstable APIs.
6. Extract patterns and anti-patterns.
7. Draft the skill procedure.
8. Run an architecture and YAGNI review of the skill itself.
9. Add verification criteria and failure modes.
10. Cross-check the result against existing skills to prevent duplication or contradictory rules.

## Completion criteria

The skill is complete only when it is executable by a fresh agent with no reliance on prior conversation memory and when its instructions produce reviewable artifacts and evidence.