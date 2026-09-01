# Middleware Skill Acceptance Criteria

## Research

- [ ] Exact FastMCP version identified.
- [ ] Official middleware documentation read.
- [ ] Relevant official examples inspected.
- [ ] Source/tests inspected for ambiguous behavior.
- [ ] MCP specification checked where required.
- [ ] Evidence ledger completed.

## Architecture

- [ ] Concern is genuinely cross-cutting.
- [ ] Middleware is preferred over Provider, Transform, Component, Context/DI, Lifespan, or application-layer alternatives for a documented reason.
- [ ] Chain position and ordering are explicit.
- [ ] Short-circuit semantics are explicit.
- [ ] Error and cancellation propagation are explicit.
- [ ] Business logic is outside middleware.

## Security / Reliability

- [ ] Authentication vs authorization responsibilities are explicit.
- [ ] Trust boundary is explicit.
- [ ] Retry semantics are justified and safe if used.
- [ ] Timeout/cancellation behavior is safe.
- [ ] Stateful concurrency is analyzed.
- [ ] Streaming/tasks behavior is analyzed where applicable.

## Implementation / Verification

- [ ] Exact target-version APIs are used.
- [ ] Focused tests pass.
- [ ] Integration/MCP Client tests pass where applicable.
- [ ] Failure and short-circuit paths are tested.
- [ ] Ordering is tested where relevant.
- [ ] Static quality checks pass.
- [ ] Architecture re-check passes.
- [ ] All verification evidence is reproducible.
- [ ] Stops when middleware behavior cannot be established from evidence; rejects invented behavior and escalates to the user instead of guessing.
