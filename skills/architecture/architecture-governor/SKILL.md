---
name: architecture-governor
description: Enforce layered architecture, dependency direction, responsibility boundaries, and justified complexity for production FastMCP systems.
---

# Architecture Governor

## Mission

Review an MCP server design before implementation and reject architecture that violates responsibility boundaries, dependency direction, or justified-complexity rules.

## Trigger / Когда применять

**Scope / When to use:** reviewing an MCP server design before implementation for responsibility boundaries, dependency direction, and justified complexity.
**Trigger:** before implementation of an MCP server design that needs architecture review.
**Upstream / Prerequisite:** current requirements and acceptance criteria; a research artifact for the relevant FastMCP feature; proposed module/layer diagram; dependency graph; public MCP contracts; persistence/external integration boundaries; pattern decisions and alternatives.
**Mission / Goal:** review an MCP server design before implementation and reject architecture that violates responsibility boundaries, dependency direction, or justified-complexity rules.
**Research / Evidence:** run the mandatory checks: layering (Domain ← Application ← Infrastructure with MCP adapters), responsibility boundaries, the FastMCP-native mechanism check, the pattern gate, and model boundaries; record evidence used.
**Decision / Selection rules:** for each framework concern evaluate the native mechanism (Provider, Transform, Middleware, Context, lifespan, tasks, auth, pagination, versioning, telemetry, proxy, client-based testing) before custom infrastructure and require a written decision record for any custom abstraction; every pattern must state the concrete problem, why a simpler solution fails, alternatives, complexity cost, testability benefit/cost, and YAGNI decision.
**Version / Compatibility:** Привязан к целевому FastMCP/MCP/Python-релизу.

## Deliverables

**Deliverables / Artifacts:** an output of PASS, PASS WITH CONDITIONS, or REJECT plus violated rules, dependency-direction findings, responsibility findings, unnecessary abstractions, missing boundaries, required changes, and evidence used.
**Verification / Testing:** apply the mandatory checks to the design and record evidence; do not redesign the whole system merely because an alternative is aesthetically preferable — apply KISS and YAGNI to the review itself.
**Failure / Stop conditions:** reject architecture that violates responsibility boundaries, dependency direction, or justified-complexity rules; reject business rules in MCP tools/resources/prompts, SQLAlchemy queries in MCP handlers, external HTTP calls from domain/application use cases when a port is appropriate, and pattern cargo culting.
**Positive scenario:** a design that respects dependency direction and justified complexity passes the governor review as PASS.
**Negative scenario:** a design places business rules in MCP handlers or imports framework concerns into domain and is rejected.

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


