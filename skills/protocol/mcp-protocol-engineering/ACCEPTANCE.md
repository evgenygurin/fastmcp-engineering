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
- [ ] Target lifecycle is explicit: modern stateless or handshake-era.
- [ ] Version/discovery behavior is explicit.
- [ ] Capability advertisement matches actual implementation.
- [ ] Lifecycle rules for the target version are enforced.
- [ ] Notification semantics are correct.
- [ ] Transport ownership/routing semantics are explicit.
- [ ] Cancellation/disconnect behavior is defined.
- [ ] Tools/resources/prompts have distinct contracts.
- [ ] Tool schemas are validated according to the target JSON Schema contract.
- [ ] Protocol errors are distinct from application errors.
- [ ] Authorization is independent from model/tool descriptions.

## Security / reliability
- [ ] External protocol inputs are validated and bounded.
- [ ] Sensitive internal details are not leaked in errors.
- [ ] Application mutable state is concurrency-safe.
- [ ] No accidental global mutable protocol state.
- [ ] Native FastMCP capabilities are preferred over custom protocol plumbing.
- [ ] Draft extensions and deprecated features are explicitly isolated/justified.

## Verification
- [ ] Lifecycle/discovery tests pass.
- [ ] Version/capability negotiation or compatibility tests pass.
- [ ] Discovery/invocation tests pass.
- [ ] Invalid-message/error mapping tests pass.
- [ ] Notification tests pass.
- [ ] Cancellation/disconnect tests pass.
- [ ] Authorization tests pass.
- [ ] Transport/routing-header tests pass for the target deployment.
- [ ] Interoperability tests cover supported client combinations where practical.
- [ ] Static quality gates pass.
- [ ] Architecture re-check passes.