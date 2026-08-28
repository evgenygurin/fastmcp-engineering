# Skill Contract

A skill is a reusable engineering procedure, not a topic summary.

## Required sections

Every production skill MUST define:

1. Scope and non-goals.
2. Trigger conditions.
3. Required upstream context.
4. Mandatory research sources.
5. Decision procedure.
6. Implementation procedure, when applicable.
7. Verification procedure.
8. Failure / escalation conditions.
9. Outputs and artifacts.
10. Version compatibility notes.

## Agent behavior

The skill MUST prefer evidence over memory, explicit decisions over implicit assumptions, and the smallest sufficient design over speculative generality.

A skill MUST NOT silently override project-level architecture rules. Conflicts are escalated to the Architecture Governor.

## Artifact quality

Outputs must be concrete and reviewable: decision records, contracts, source references, test evidence, diffs, or implementation artifacts. Generic advice is not sufficient completion evidence.