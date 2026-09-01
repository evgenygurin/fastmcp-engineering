# FastMCP Components Acceptance Criteria

## Research
- [ ] Exact FastMCP/Python versions identified.
- [ ] Official docs for every component involved read.
- [ ] Relevant official examples inspected.
- [ ] Source/tests inspected for ambiguous behavior.
- [ ] MCP specification checked where required.
- [ ] Evidence ledger completed.

## Architecture
- [ ] Tool/Resource/Template/Prompt choice is semantically justified.
- [ ] Component is a thin MCP adapter.
- [ ] Application/domain layers do not depend on FastMCP runtime details.
- [ ] Public schema is deliberate and stable.
- [ ] Identity/registration semantics are verified.
- [ ] Provider/Transform/Middleware/Context/Lifespan alternatives considered.

## Security / Reliability
- [ ] Discovery and execution/read authorization are explicit.
- [ ] Tenant/user scope is explicit where applicable.
- [ ] Side effects and idempotency are explicit for Tools.
- [ ] Errors do not leak internals.
- [ ] Cancellation/timeouts are safe where applicable.

## Verification
- [ ] Component discovery tests pass.
- [ ] Schema validation tests pass.
- [ ] Happy/error paths pass.
- [ ] Client/in-process integration tests pass where applicable.
- [ ] Composition/collision behavior is tested where applicable.
- [ ] Static quality checks pass.
- [ ] Architecture re-check passes.
- [ ] Evidence is reproducible.
- [ ] Stops when MCP component behavior cannot be established from evidence; rejects invented behavior and escalates to the user instead of guessing.
