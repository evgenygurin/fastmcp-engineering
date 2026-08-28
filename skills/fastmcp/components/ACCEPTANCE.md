# Components Skill Acceptance Criteria

A components-skill implementation is accepted only when all applicable criteria are satisfied.

## Research

- [ ] Target FastMCP version is explicit.
- [ ] Official documentation was read for the relevant APIs.
- [ ] Relevant official GitHub examples were inspected.
- [ ] Source/tests were inspected for ambiguous or version-sensitive behavior.
- [ ] MCP specification was checked where protocol semantics matter.
- [ ] Evidence is recorded.

## Design

- [ ] Tool/Resource/Prompt selection is justified.
- [ ] Provider/Transform/Middleware alternatives were considered where relevant.
- [ ] Public MCP contract is explicit.
- [ ] Application boundary is explicit.
- [ ] Domain and persistence responsibilities are not embedded in the MCP adapter.
- [ ] Any custom abstraction has passed Pattern Selection.

## Implementation

- [ ] Uses the exact APIs supported by the target version.
- [ ] Adapter remains thin.
- [ ] Validation and error semantics are explicit.
- [ ] Authorization semantics are explicit.
- [ ] No accidental exposure of internal models.

## Verification

- [ ] Relevant unit tests pass.
- [ ] Relevant integration/MCP Client tests pass.
- [ ] Failure paths are covered.
- [ ] Static quality checks pass.
- [ ] Architecture re-check passes.
- [ ] Verification evidence is reproducible.
