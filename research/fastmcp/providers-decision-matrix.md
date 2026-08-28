# FastMCP Providers Decision Matrix

## Provider is appropriate when

| Requirement | Provider fit |
|---|---|
| Source/discover MCP components dynamically | Strong |
| Compose components from a source/backend | Strong |
| Expose a changing set of components | Strong, subject to target-version semantics |
| Implement business CRUD | Weak / wrong boundary |
| Encapsulate domain rules | Wrong boundary |
| Coordinate application use cases | Wrong boundary |
| Store/retrieve domain data | Usually Repository/port |
| Apply cross-cutting policy to existing components | Usually Middleware |
| Systematically alter exposed component representation | Usually Transform |
| Inject application dependencies | Usually Context/DI/composition root |

## Provider vs common abstractions

```text
Provider  -> MCP component sourcing/discovery/composition
Repository -> domain/application data access
Service   -> application/domain behavior
Registry  -> generic object registration (use only if truly needed)
DI        -> dependency construction/lifetime
Middleware -> cross-cutting request/component pipeline
Transform -> component representation/composition transformation
```

These definitions are architectural defaults. Exact FastMCP semantics must be verified against the target release.

## Required decision record

```yaml
requirement:
provider_problem:
selected_mechanism:
fastmcp_native_alternatives_checked: []
provider_responsibilities: []
non_responsibilities: []
dynamic_behavior:
visibility:
authorization:
lifecycle:
caching:
concurrency:
error_model:
testing:
version:
evidence: []
```

## Hard rule

Never introduce a Provider because the project already has repositories/services/registries or because Provider is a convenient abstraction name. The problem must be MCP component sourcing/composition.