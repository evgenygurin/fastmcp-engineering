---
name: architecture-governor
description: Enforce layered architecture, dependency direction, responsibility boundaries, and justified complexity for production FastMCP systems.
---

# Architecture Governor

## Mission

Review an MCP server design before implementation and reject architecture that violates responsibility boundaries, dependency direction, or justified-complexity rules.

## Required inputs

- Current requirements and acceptance criteria.
- Research artifact for the relevant FastMCP feature.
- Proposed module/layer diagram.
- Dependency graph.
- Public MCP contracts.
- Persistence/external integration boundaries.
- Pattern decisions and alternatives.

## Mandatory checks

### Layering

Verify:

```text
Domain <- Application <- Infrastructure
                         ^
                         |
                    MCP adapters
```

The arrows represent dependency direction toward inner/application abstractions. Domain must not import infrastructure or framework concerns. Application must not depend on concrete infrastructure implementations.

### Responsibility

Reject:

- business rules in MCP tools/resources/prompts;
- SQLAlchemy queries in MCP handlers;
- external HTTP calls directly from domain/application use cases when an infrastructure port is appropriate;
- authentication logic hidden inside unrelated business functions;
- middleware containing business workflows;
- providers used as generic repositories;
- transforms used to implement domain rules.

### FastMCP-native mechanism check

For each framework concern, explicitly evaluate the native mechanism before custom infrastructure:

- Provider
- Transform
- Middleware
- Context/state
- Lifespan
- Tasks/background execution
- Auth/authorization
- Pagination
- Versioning
- Telemetry
- Proxy/composition
- Client-based testing

If a custom abstraction is selected instead, require a written decision record.

### Pattern gate

Every Factory, Strategy, Repository, Adapter, Facade, Observer, event bus, CQRS layer, or similar abstraction must state:

1. concrete problem;
2. why a simpler solution fails;
3. alternatives;
4. complexity cost;
5. testability benefit/cost;
6. YAGNI decision.

Reject pattern cargo culting.

### Model boundaries

Check that domain models, application DTOs, MCP schemas, persistence models, and external API models are not coupled accidentally. Sharing a model is allowed only when the ownership and lifecycle are genuinely the same.

## Output

Return:

```text
PASS | PASS WITH CONDITIONS | REJECT
```

Then provide:

- violated rules;
- dependency direction findings;
- responsibility findings;
- unnecessary abstractions;
- missing boundaries;
- required changes;
- evidence used.

Do not redesign the whole system merely because an alternative is aesthetically preferable. Apply KISS and YAGNI to the review itself.
