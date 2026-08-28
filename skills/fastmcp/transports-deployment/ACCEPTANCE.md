# Transport / Deployment Acceptance Criteria

## Research
- [ ] Exact FastMCP/Python/ASGI versions identified.
- [ ] Official transport/deployment docs read.
- [ ] Relevant official examples inspected.
- [ ] Source/tests inspected for ambiguous semantics.
- [ ] MCP specification checked where required.
- [ ] First-party ASGI/server documentation checked.
- [ ] Evidence ledger completed.

## Protocol
- [ ] Selected transport and rationale are explicit.
- [ ] Endpoint/path semantics are verified.
- [ ] Initialization/session semantics are verified.
- [ ] Streaming semantics are verified.
- [ ] Cancellation/timeouts are verified.
- [ ] Error behavior is verified.

## Deployment
- [ ] Stateful/stateless model is explicit.
- [ ] Worker/replica scaling assumptions are explicit.
- [ ] Shared state requirements are explicit.
- [ ] ASGI mounting/path prefix behavior is tested.
- [ ] Proxy/load-balancer requirements are documented.
- [ ] Timeout/buffering/connection policy is explicit.
- [ ] Health/readiness is defined.
- [ ] Graceful shutdown is defined and tested.

## Security
- [ ] TLS/network boundary is explicit.
- [ ] Authentication/authorization boundary is explicit.
- [ ] Trusted proxy boundary is explicit.
- [ ] Forwarded headers are not implicitly trusted.
- [ ] Tenant/session isolation is verified where applicable.

## Verification
- [ ] In-process/MCP Client checks pass.
- [ ] Real transport integration checks pass where applicable.
- [ ] Failure injection passes.
- [ ] Streaming/cancellation checks pass where applicable.
- [ ] Static quality checks pass.
- [ ] Architecture re-check passes.
- [ ] Verification evidence is reproducible.