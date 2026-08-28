# FastMCP Lifespan Decision Matrix

## Core rule

Lifespan owns resources whose lifetime follows the server/runtime lifecycle. It is not a generic initialization hook.

| Need | Preferred mechanism |
|---|---|
| Server/runtime resource startup and cleanup | Lifespan |
| MCP request/session capability | Context |
| Application dependency composition | DI / explicit ports |
| Cross-cutting request behavior | Middleware |
| Component discovery | Provider |
| Component transformation | Transform |
| Business operation | Application service/use case |

## Mandatory resource questions

1. Who owns this resource?
2. What scope does it have?
3. What must exist before it starts?
4. What depends on it?
5. What is the exact cleanup operation?
6. What if a later resource fails during startup?
7. What if shutdown is cancelled?
8. Can cleanup fail, and how is that reported?
9. Is the resource safe to share concurrently?
10. Should it be exposed to Context, and through what verified mechanism?
11. Does an ASGI host need the FastMCP lifespan explicitly propagated?
12. Can multiple servers/providers/extensions share or nest this lifecycle?

## Ordering

If B depends on A:

```text
startup:  A → B
shutdown: B → A
```

Prefer native composable async context managers and `AsyncExitStack` rather than hand-written parallel cleanup when the framework supports them.

## Hard anti-patterns

- Module-import resource initialization.
- Orphaned background `create_task()` calls.
- Request creation of heavyweight server-scoped clients.
- Sharing non-concurrent-safe sessions between requests.
- Dropping `mcp_app.lifespan` when mounting Streamable HTTP into an ASGI application.
- Cleanup that only runs on the happy path.
- Hidden lifecycle state in global variables.
- Treating lifespan as a dependency/service registry.
- Reimplementing FastMCP internal lifecycle machinery without evidence-based need.

## Verification matrix

| Concern | Verification |
|---|---|
| Startup | resources become available in dependency order |
| Failure | previously started resources are cleaned |
| Shutdown | all owned resources close/dispose |
| Cancellation | teardown remains safe under cancellation |
| Ordering | composition follows dependency order |
| HTTP | mounted server has required FastMCP lifecycle |
| Context | intended resources are available through the documented seam |
| Concurrency | shared resources are safe or correctly scoped |
| Background work | tasks are cancelled/drained/closed by owner |
