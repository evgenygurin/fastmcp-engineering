# PydanticAI / Agent Integration Acceptance Criteria

## Research
- [ ] Exact Python/PydanticAI/Pydantic/FastMCP/provider versions identified.
- [ ] Official PydanticAI docs read.
- [ ] Official FastMCP docs/LLM material read.
- [ ] Relevant official examples inspected.
- [ ] Source/tests inspected for ambiguous behavior.
- [ ] MCP specification checked where relevant.
- [ ] Evidence ledger completed.

## Architecture
- [ ] MCP adapter is distinct from application use cases.
- [ ] Agent orchestration boundary is explicit.
- [ ] Agent does not become domain/application god object.
- [ ] Dependencies are typed and scoped.
- [ ] Provider SDK details do not leak through public layers.
- [ ] Global mutable agent state is absent or explicitly justified.

## Safety/reliability
- [ ] Tool authorization is deterministic.
- [ ] External MCP content/tool results are treated as untrusted.
- [ ] Prompt/tool injection defenses are tested.
- [ ] Output validation is explicit.
- [ ] Domain invariants remain outside LLM validation.
- [ ] Retry policy is replay-safe.
- [ ] Timeouts/cancellation/concurrency are explicit.
- [ ] Usage/token limits are explicit.
- [ ] Secrets are excluded from prompts/schemas/logs.

## Verification
- [ ] Deterministic model seam tests pass.
- [ ] Dependency-scope tests pass.
- [ ] Tool authorization tests pass.
- [ ] Output validation tests pass.
- [ ] Tool failure/retry tests pass.
- [ ] Cancellation/limits tests pass where applicable.
- [ ] MCP integration tests pass.
- [ ] Static quality checks pass.
- [ ] Architecture re-check passes.
- [ ] Stops when agent integration behavior cannot be established from evidence; rejects invented behavior and escalates to the user instead of guessing.
