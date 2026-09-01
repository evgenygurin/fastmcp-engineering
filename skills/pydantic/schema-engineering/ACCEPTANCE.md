# Pydantic / Schema Acceptance Criteria

## Research
- [ ] Exact Python/Pydantic/FastMCP versions identified.
- [ ] Official Pydantic docs read.
- [ ] Official FastMCP schema docs read.
- [ ] Relevant official examples inspected.
- [ ] Source/tests inspected for ambiguous semantics.
- [ ] JSON Schema/MCP requirements checked.
- [ ] Evidence ledger completed.

## Architecture
- [ ] MCP DTOs are not accidentally ORM entities.
- [ ] Application/domain boundaries are explicit.
- [ ] Validation ownership is explicit.
- [ ] Serialization ownership is explicit.
- [ ] Authorization is not delegated to validation.

## Contract
- [ ] Required/optional/null semantics are intentional.
- [ ] Strictness/coercion is intentional.
- [ ] Generated JSON Schema is verified.
- [ ] Public field/enum semantics have evolution policy.
- [ ] Breaking changes have migration/version treatment.
- [ ] Payload limits/security constraints are explicit.

## Verification
- [ ] Validation success/failure tests pass.
- [ ] Serialization round-trip tests pass.
- [ ] Schema fixtures pass.
- [ ] FastMCP invocation tests pass.
- [ ] Boundary/malicious input tests pass.
- [ ] Static quality checks pass.
- [ ] Architecture re-check passes.
- [ ] Stops when schema behavior cannot be established from evidence; rejects invented behavior and escalates to the user instead of guessing.
