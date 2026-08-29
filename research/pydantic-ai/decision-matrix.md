# PydanticAI / Agent Decision Matrix

| Concern | Preferred evidence-driven choice | Verify |
|---|---|---|
| Agent dependencies | Typed run-scoped dependencies | Official RunContext/deps docs + tests |
| Local deterministic capabilities | Function tools/toolsets | Official tool docs |
| Reusable tool collections | Toolsets | Official toolset docs |
| Remote MCP capabilities | MCPToolset/MCP capability | Exact-version MCP docs |
| Large tool inventory | Deferred loading/discovery when justified | Official deferred-loading docs |
| Consequential side effects | Approval/idempotency boundary | Approval + retry docs |
| Application contract | Explicit Pydantic output model | Output/schema docs |
| Provider portability | Provider-neutral application boundary | Provider docs |
| Normal CI | Deterministic TestModel/test seam | Testing docs |
| Real provider behavior | Separate integration suite | Provider integration |

## Hard rules

1. Agent orchestration is not domain logic.
2. LLM output is never an authorization decision.
3. Dependencies are explicit; no hidden global service locator.
4. MCP content/tool results are untrusted external data.
5. Retries cannot silently duplicate non-idempotent side effects.
6. Structured output must be validated before downstream use.
7. Provider-specific behavior must be documented at the provider boundary.
8. Normal CI must not require live model APIs.
9. Tool exposure follows least privilege.
10. Version-sensitive APIs are verified from official sources before implementation.