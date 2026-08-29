# Resilience / Reliability Acceptance Criteria

## Research
- [ ] Exact stack versions identified.
- [ ] Official FastMCP/MCP lifecycle and transport semantics verified.
- [ ] Official PydanticAI retry/limits/cancellation semantics verified.
- [ ] DB/driver/SQLAlchemy transaction and pooling semantics verified.
- [ ] Every external boundary has documented failure behavior.
- [ ] Evidence ledger completed.

## Reliability design
- [ ] Failure domains are explicit.
- [ ] End-to-end deadline/timeout budget exists.
- [ ] Cancellation reaches underlying work.
- [ ] Each logical operation has one retry owner/budget.
- [ ] Retryable and non-retryable failures are classified.
- [ ] Backoff/jitter and retry exhaustion are bounded.
- [ ] Side effects have idempotency/replay semantics.
- [ ] Concurrency/resource limits are explicit.
- [ ] No unbounded task creation or queues.
- [ ] Overload/backpressure behavior is explicit.
- [ ] Degradation does not produce misleading success.
- [ ] Recovery and graceful shutdown are defined.

## Database / side effects
- [ ] Transactions do not span unrelated remote calls without justification.
- [ ] Deadlock/serialization retry behavior follows DB/driver semantics.
- [ ] Duplicate delivery is safe or explicitly rejected.

## Verification
- [ ] Timeout tests pass.
- [ ] Cancellation tests pass.
- [ ] Transient/permanent failure tests pass.
- [ ] Retry exhaustion tests pass.
- [ ] Idempotency/duplicate-delivery tests pass.
- [ ] Concurrency/resource exhaustion tests pass.
- [ ] Overload/backpressure tests pass.
- [ ] Partial dependency failure tests pass.
- [ ] Recovery/shutdown tests pass.
- [ ] Real DB/transport semantics are integration-tested where necessary.
- [ ] Static quality gates pass.
- [ ] Architecture re-check passes.