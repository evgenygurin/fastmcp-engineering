# Context / DI Architecture Boundaries

```text
MCP transport
     |
     v
FastMCP component
     |
     +---- Context: runtime/MCP capabilities
     |
     +---- explicit injected dependency
                 |
                 v
          application port
                 |
                 v
          application service
                 |
                 v
               domain
                 ^
                 |
          infrastructure adapter
                 ^
                 |
       composition/lifespan root
```

## Rules

1. FastMCP Context is not an application dependency container.
2. Application/domain code must not reach arbitrary services through Context.
3. Dependencies are explicit in function signatures, constructors, or the verified DI mechanism.
4. Infrastructure implementations are composed at the outer boundary.
5. Lifespan owns resources that require startup/shutdown according to the exact target-version semantics.
6. Dependency scope and concurrency guarantees must be explicit.
7. Authentication context and authorization policy are distinct responsibilities.

## Review question

For every dependency ask: "Could this application service be unit-tested without constructing a FastMCP Context?" If not, determine whether the boundary is genuinely protocol-specific; otherwise move the dependency behind an application port.
