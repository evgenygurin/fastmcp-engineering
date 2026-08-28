# Dependency Rules

## Direction

The preferred dependency direction is:

`MCP delivery → Application → Domain`

and:

`Infrastructure → Application/Domain ports`

The composition root may depend on all concrete layers to assemble them.

## Forbidden dependencies

### Domain

Must not import:

- fastmcp
- sqlalchemy
- pydantic
- pydantic_ai
- supabase SDKs
- HTTP clients
- web frameworks
- LLM SDKs

### Application

Must not depend on concrete persistence or external integration implementations. It may depend on domain types and stable ports.

### MCP delivery

Must not directly perform persistence, external API orchestration, or business-rule calculation. It may use FastMCP primitives and application contracts.

## Exceptions

An exception is allowed only when the dependency is itself the intended boundary contract and the decision record explains:

1. why the dependency is needed;
2. which layer owns the dependency;
3. why an adapter is unnecessary or harmful;
4. what coupling is accepted;
5. how the choice affects testing and future replacement.

## Pattern discipline

Do not introduce Repository, Factory, Strategy, Mediator, Event Bus, CQRS, or other patterns merely because they are available. Introduce a pattern only when a demonstrated variability, boundary, or complexity problem requires it.
