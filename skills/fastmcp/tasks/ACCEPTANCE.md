# FastMCP Tasks Skill Acceptance Criteria

## Research
- [ ] Exact FastMCP/Python versions identified.
- [ ] Official task documentation and llms material read.
- [ ] Relevant official examples inspected.
- [ ] Source/tests inspected for ambiguous task semantics.
- [ ] MCP task specification/SEP material checked.
- [ ] First-party dependency behavior verified.
- [ ] Evidence ledger completed.

## Semantics
- [ ] Protocol task, framework task, coroutine and durable job are explicitly distinguished.
- [ ] Actual target-version state machine is documented.
- [ ] Polling and result retrieval semantics are verified.
- [ ] Cancellation semantics are verified.
- [ ] Timeout/deadline and expiry semantics are verified.

## Architecture
- [ ] Execution owner is explicit.
- [ ] Storage and durability guarantees are explicit.
- [ ] Worker/process boundary is explicit.
- [ ] Restart/crash recovery is explicit.
- [ ] Lifespan shutdown behavior is explicit.
- [ ] Business logic remains outside task orchestration.
- [ ] No untracked background tasks exist.

## Reliability / Security
- [ ] Retry policy is justified.
- [ ] Idempotency is addressed before retries.
- [ ] Task creation authorization is tested.
- [ ] Task status/result authorization is tested.
- [ ] Tenant isolation is preserved where applicable.
- [ ] Sensitive arguments/results/errors are not leaked.

## Verification
- [ ] Creation/polling/completion tests pass.
- [ ] Failure/cancellation/timeout/expiry tests pass where applicable.
- [ ] Concurrent polling/access tests pass where applicable.
- [ ] Persistence/recovery tests pass where applicable.
- [ ] Shutdown behavior is tested where applicable.
- [ ] MCP Client/in-process protocol tests pass.
- [ ] Static quality checks pass.
- [ ] Architecture re-check passes.
- [ ] Verification evidence is reproducible.