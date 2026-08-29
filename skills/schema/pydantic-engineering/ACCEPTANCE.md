# Pydantic / Schema Engineering Acceptance Criteria

## Research
- [ ] Exact Python/Pydantic/FastMCP/MCP versions identified.
- [ ] Official Pydantic v2 docs read for relevant APIs.
- [ ] Official FastMCP schema/structured-output docs and examples read.
- [ ] MCP schema/result requirements checked.
- [ ] Source/tests inspected for ambiguity.
- [ ] Evidence ledger completed.

## Model architecture
- [ ] MCP transport models are explicitly identified.
- [ ] Application models are explicitly identified.
- [ ] Domain models/value objects are explicitly identified.
- [ ] Persistence models are explicitly identified.
- [ ] Reuse across layers is justified rather than assumed.

## Validation/serialization
- [ ] Structural validation has clear ownership.
- [ ] Business rules are not hidden in Pydantic validators.
- [ ] Strict/lax behavior is intentional.
- [ ] Security-sensitive coercion is controlled.
- [ ] Serialization/aliases are explicit.
- [ ] Secrets/internal fields cannot leak.

## Schema contract
- [ ] Generated JSON Schema is reviewed.
- [ ] FastMCP-visible input schemas are verified.
- [ ] FastMCP-visible output schemas are verified where applicable.
- [ ] Structured output semantics are tested.
- [ ] Union/discriminator behavior is tested.
- [ ] Required/null/default semantics are tested.
- [ ] Schema evolution compatibility is assessed.

## Verification
- [ ] Formatter/lint/type checks pass.
- [ ] Schema regression fixtures pass.
- [ ] Boundary validation tests pass.
- [ ] Serialization tests pass.
- [ ] MCP integration tests pass where required.
- [ ] Security/boundary input tests pass.
- [ ] Architecture re-check passes.