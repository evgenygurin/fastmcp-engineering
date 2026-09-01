# Testing / Verification Engineering Acceptance Criteria

## Research
- [ ] Exact versions identified.
- [ ] Official FastMCP docs/examples read.
- [ ] MCP specification checked.
- [ ] Official pytest/testing docs read.
- [ ] Relevant PydanticAI/Pydantic/SQLAlchemy/database docs read.
- [ ] Source/tests inspected for ambiguity.
- [ ] Evidence ledger completed.

## Architecture
- [ ] Invariant-to-test matrix exists.
- [ ] Each invariant uses the cheapest sufficient test level.
- [ ] Test doubles are justified.
- [ ] Protocol behavior is tested through protocol mechanisms.
- [ ] Database semantics are tested against real DB where required.
- [ ] Live LLM is not required for deterministic CI.

## Verification
- [ ] Unit tests pass.
- [ ] Component tests pass where applicable.
- [ ] Integration tests pass.
- [ ] Contract tests pass.
- [ ] MCP protocol tests pass.
- [ ] Database/migration tests pass where applicable.
- [ ] Agent tests pass.
- [ ] Security regression tests pass.
- [ ] Property/mutation testing is executed where justified.
- [ ] Critical E2E tests pass.
- [ ] Async cancellation/timeout/isolation tests pass where applicable.
- [ ] Static quality gates pass.
- [ ] No unexplained flaky tests remain.
- [ ] Architecture re-check passes.
- [ ] Stops when verification behavior cannot be established from evidence; rejects invented behavior and escalates to the user instead of guessing.
