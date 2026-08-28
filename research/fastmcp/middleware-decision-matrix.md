# FastMCP Middleware Decision Matrix

Middleware is selected for cross-cutting behavior at the MCP request/component execution boundary, not because it is an easy place to put shared code.

| Requirement | Preferred mechanism |
|---|---|
| Feature-specific business operation | Application use case |
| Domain invariant | Domain layer |
| MCP component behavior | Tool / Resource / Prompt |
| MCP component discovery/composition | Provider |
| Systematic MCP component transformation | Transform |
| Cross-cutting execution/request behavior | Middleware |
| Dependency construction | Context / DI / composition root |
| Resource initialization/cleanup | Lifespan |

## Mandatory design questions

1. What is cross-cutting about this concern?
2. What exact FastMCP lifecycle/hook does it intercept?
3. Where does it sit in the middleware chain?
4. Does ordering affect correctness?
5. Can it short-circuit?
6. How are errors and cancellations propagated?
7. What context does it read or establish?
8. Is it stateful? If so, what is the concurrency model?
9. Does it affect streaming or task execution?
10. Does it make a security decision? Who owns the policy?
11. Does it retry? If yes, is downstream work idempotent?
12. What is the simplest non-middleware implementation?

## Hard anti-patterns

- Business logic hidden in middleware.
- Database access hidden in middleware.
- A giant `SecurityMiddleware` mixing authentication, authorization, tenant policy, audit and rate limiting without explicit boundaries.
- Generic exception swallowing.
- Blind retries of non-idempotent tools.
- Global mutable state without a concurrency model.
- Middleware used to compensate for an incorrect application architecture.
- Reimplementing native FastMCP features without a documented reason.

## Verification matrix

| Concern | Verification |
|---|---|
| Chain | exact ordering and nesting |
| Short-circuit | downstream is not invoked when policy says stop |
| Errors | expected propagation/translation |
| Cancellation | cancellation reaches downstream and cleanup occurs |
| Context | expected values propagate |
| Security | allow/deny behavior and fail-closed semantics |
| State | concurrent calls do not corrupt state |
| Retry | no unsafe duplicate work |
| Streaming/tasks | behavior remains correct when applicable |
| Performance | overhead is measured/justified where material |
