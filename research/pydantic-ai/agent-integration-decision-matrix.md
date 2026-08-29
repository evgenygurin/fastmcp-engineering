# PydanticAI / Agent Integration Decision Matrix

| Concern | Preferred boundary | Rule |
|---|---|---|
| MCP protocol | FastMCP adapter | No business logic |
| Use case | Application layer | Owns orchestration |
| Agent | Agent orchestration layer | Model reasoning only |
| Dependencies | Typed RunContext/dependencies | Explicit run scope |
| Tools | Capability boundary | Deterministic authorization |
| Output | Typed Pydantic contract | Validate before application use |
| Domain invariants | Domain/application | Never delegated to LLM |
| Provider SDK | Infrastructure | Must not leak upward |
| Secrets | Infrastructure/config | Never prompts or schemas |
| Retry | Application/infrastructure | Must be replay-safe |

## Hard rules

1. Model-generated intent is never an authorization decision.
2. MCP tool output is untrusted external input.
3. Agent state is never accidentally shared across independent requests.
4. Provider-specific types do not become application contracts.
5. Normal CI does not require a paid/live LLM.
6. Side-effecting tools require an idempotency/replay analysis before retries.
7. Structured output validation does not replace domain validation.
8. Agent orchestration does not become a substitute for application services.
