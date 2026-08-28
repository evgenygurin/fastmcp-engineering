# FastMCP Context / DI Decision Matrix

## Core rule

Context is an MCP runtime capability surface. Dependency injection is dependency composition. They are complementary, not interchangeable.

| Need | Preferred owner |
|---|---|
| MCP request/session/runtime capability | FastMCP Context |
| Application service dependency | Explicit DI / application port |
| Domain dependency | Domain abstraction / explicit dependency |
| Startup/shutdown resource | Lifespan |
| Cross-cutting request behavior | Middleware |
| Configuration | Typed settings/configuration |
| Component discovery | Provider |
| Component transformation | Transform |

## Mandatory questions

1. Does this value describe the current MCP invocation/session or is it an application dependency?
2. Can the application layer operate without importing FastMCP?
3. What is the dependency scope?
4. Who constructs it?
5. Who owns startup/shutdown?
6. Is it mutable?
7. Is it safe to share concurrently?
8. Can tests replace it explicitly?
9. Is the value trusted security identity or merely request metadata?
10. Could this design become a service registry?

## Hard anti-patterns

- `ctx.services.*` service locator.
- Global mutable dependency container.
- Application/domain services accepting `Context` just to reach one dependency.
- Per-request construction of heavyweight clients that should be lifespan-scoped.
- Lifespan resources with undefined cleanup ownership.
- Sharing non-concurrent-safe ORM sessions/clients across requests.
- Treating request metadata as authenticated identity.

## Scope matrix

Every dependency must have an explicit scope and ownership:

```text
application/process
      ↓
lifespan/server
      ↓
session
      ↓
request/invocation
      ↓
transient
```

Only scopes supported by the target FastMCP/DI mechanism may be used; verify exact semantics before implementation.
