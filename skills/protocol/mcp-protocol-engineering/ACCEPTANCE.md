# MCP Protocol Engineering Acceptance Criteria

## Research
- [ ] Exact MCP specification version identified.
- [ ] Exact FastMCP version identified.
- [ ] Official MCP lifecycle, transport, capability, primitive and error documentation read.
- [ ] Relevant FastMCP documentation/examples read.
- [ ] Official source/tests inspected for ambiguous behavior.
- [ ] Stable vs experimental/draft features separated.
- [ ] Evidence ledger and compatibility matrix completed.

## Protocol
- [ ] Initialization/version negotiation is explicit.
- [ ] Capability advertisement matches actual implementation.
- [ ] Lifecycle states are enforced.
- [ ] Notification semantics are correct.
- [ ] Transport/session ownership is explicit.
- [ ] Cancellation/disconnect behavior is defined.
- [ ] Tools/resources/prompts have distinct contracts.
- [ ] Protocol errors are distinct from application errors.
- [ ] Authorization is independent from model/tool descriptions.

## Security / reliability
- [ ] External protocol inputs are validated.
- [ ] Sensitive internal details are not leaked in errors.
- [ ] Session mutable state is concurrency-safe.
- [ ] No global mutable protocol state.
- [ ] Native FastMCP capabilities are preferred over custom protocol plumbing.

## Verification
- [ ] Initialization tests pass.
- [ ] Version/capability negotiation tests pass.
- [ ] Discovery/invocation tests pass.
- [ ] Invalid-message/error mapping tests pass.
- [ ] Notification tests pass.
- [ ] Cancellation/disconnect tests pass.
- [ ] Authorization tests pass.
- [ ] Transport tests pass for the target deployment.
- [ ] Interoperability tests cover supported client combinations where practical.
- [ ] Static quality gates pass.
- [ ] Architecture re-check passes.