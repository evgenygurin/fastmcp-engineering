# Lifespan Skill Acceptance Criteria

## Research
- [ ] Exact FastMCP/Python versions identified.
- [ ] Official lifespan documentation read.
- [ ] Relevant official examples inspected.
- [ ] FastMCP source/tests inspected for lifecycle semantics.
- [ ] Relevant Starlette/FastAPI lifecycle docs inspected when applicable.
- [ ] First-party dependency docs inspected for managed resources.
- [ ] Evidence ledger completed.

## Architecture
- [ ] Every resource has an explicit owner and scope.
- [ ] Startup dependency order is explicit.
- [ ] Shutdown order is explicit.
- [ ] Partial startup failure is handled.
- [ ] Cleanup is guaranteed and observable.
- [ ] Cancellation behavior is explicit.
- [ ] Shared resource concurrency semantics are explicit.
- [ ] Context/DI does not become a service locator.
- [ ] Background tasks have explicit ownership and shutdown behavior.

## Integration
- [ ] Composed lifespans are verified.
- [ ] FastMCP HTTP lifespan is preserved when mounted into an ASGI application.
- [ ] Multiple server/provider/extension lifecycle semantics are understood where applicable.

## Verification
- [ ] Startup success tests pass.
- [ ] Partial startup failure tests pass.
- [ ] Shutdown/cleanup tests pass.
- [ ] Cancellation tests pass where applicable.
- [ ] Composition/order tests pass where applicable.
- [ ] MCP Client/in-process integration tests pass where applicable.
- [ ] Concurrency/resource-sharing tests pass where applicable.
- [ ] Static quality checks pass.
- [ ] Architecture re-check passes.
- [ ] Verification evidence is reproducible.