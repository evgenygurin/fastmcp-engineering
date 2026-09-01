# PydanticAI / Agent Engineering Acceptance Criteria

## Research
- [ ] Exact Python/PydanticAI/Pydantic/FastMCP/MCP/provider versions identified.
- [ ] Official PydanticAI Agent/run/dependency documentation read.
- [ ] Official tools/toolsets documentation and examples read.
- [ ] MCPToolset/MCP integration documentation read.
- [ ] Structured output/validation/retry documentation read.
- [ ] Streaming/async/history/limits/approval documentation checked where applicable.
- [ ] Official source/tests inspected for ambiguous behavior.
- [ ] Provider-specific capabilities verified from first-party docs.
- [ ] Evidence ledger completed.

## Architecture
- [ ] Agent is not the domain/application authorization layer.
- [ ] Dependencies are explicit and appropriately scoped.
- [ ] Model/provider boundary is explicit.
- [ ] Tool/toolset inventory and least-privilege policy exist.
- [ ] MCP integration is isolated from domain logic.
- [ ] Prompt/instruction responsibilities are explicit.
- [ ] Structured output schemas are explicit.
- [ ] Retry/timeout/usage/cancellation policy exists.
- [ ] Side effects have idempotency/approval controls.
- [ ] History/context lifecycle is defined.

## Security
- [ ] Model output never authorizes access.
- [ ] MCP descriptions/results are treated as untrusted.
- [ ] Secrets are excluded from prompts/history/telemetry.
- [ ] Tool exposure follows least privilege.
- [ ] Side-effecting tools cannot be duplicated silently by retries.

## Verification
- [ ] Deterministic agent tests pass.
- [ ] Dependency injection/scoping tests pass.
- [ ] Tool schema/toolset availability tests pass.
- [ ] Structured-output and validation tests pass.
- [ ] Retry/limit/cancellation tests pass where applicable.
- [ ] Approval/deferred-tool tests pass where applicable.
- [ ] MCP integration tests pass where applicable.
- [ ] Security regression tests pass.
- [ ] Static quality gates pass.
- [ ] Real-provider tests are separated and only claimed when executed.
- [ ] Architecture re-check passes.
- [ ] Stops when agent behavior cannot be established from evidence; rejects invented behavior and escalates to the user instead of guessing.
