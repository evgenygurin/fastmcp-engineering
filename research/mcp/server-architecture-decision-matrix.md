# MCP / FastMCP Server Architecture Decision Matrix

| Concern | Default architectural decision | Verify when |
|---|---|---|
| Protocol boundary | FastMCP adapter owns MCP concerns | Always |
| Business logic | Application/domain layers | Always |
| Tool handler | Thin adapter to use case | Always |
| Read-only data | Resource | When semantics are passive/readable |
| Action | Tool | When client invokes behavior |
| Reusable instruction | Prompt | When exposing interaction template |
| Request state | Verified Context/dependency mechanism | Exact version |
| App resources | Lifespan | Startup/shutdown ownership required |
| Cross-cutting concerns | Middleware | Ordering/scope must be verified |
| Local integration | STDIO | Client requires local process |
| Remote integration | Streamable HTTP | Remote server |
| Legacy compatibility | SSE only if required | Existing client compatibility |
| Composition | Mount/subserver only with ownership boundary | Multiple server domains |
| Proxy | Proxy only when transparent delegation is required | Remote/aggregated server |

## Hard rules

1. Read the exact FastMCP version's official documentation before using a feature.
2. Read relevant official examples and tests before reproducing an advanced pattern.
3. Do not leak FastMCP/MCP/transport objects into the domain layer.
4. Do not put business logic in decorators or middleware.
5. Do not use model output as an authorization decision.
6. Do not assume middleware order, lifecycle behavior or mounted auth paths.
7. Protocol tests must exercise the protocol boundary.
8. Do not manually recreate FastMCP functionality already provided by the framework.
9. Every extra server/proxy/mount must have a concrete architectural reason.
10. Any undocumented behavior is a blocking unknown until verified from source/tests.