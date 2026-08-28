# FastMCP Engineering System

## Purpose

This repository defines a research-first, architecture-governed methodology for building production-grade MCP servers with FastMCP. It is a development system, not an MCP server template.

## Core model

```text
Requirement
  -> Discovery
  -> Official research
  -> Pattern selection
  -> Architecture
  -> Contracts
  -> TDD
  -> Implementation
  -> Static analysis
  -> Tests
  -> Security review
  -> Architecture review
  -> Final verification
```

Every stage produces evidence that the next stage can consume.

## Architecture model

```text
Domain
  <- Application
  <- Infrastructure adapters
  <- MCP delivery adapter
  <- Bootstrap/composition root
```

The dependency direction is inward. Domain owns business concepts. Application owns use cases and ports. Infrastructure implements ports. MCP is a delivery adapter. Bootstrap composes concrete implementations.

## Framework boundary

FastMCP is used natively at the MCP boundary. Before custom infrastructure is introduced, the agent must evaluate the relevant native mechanisms: components, providers, transforms, middleware, Context, lifespan, tasks/background execution, authentication, authorization, pagination, versioning, telemetry, proxy/composition, and Client testing.

FastMCP abstractions must not leak into domain code merely because they are convenient.

## Data-model boundaries

These are conceptually distinct and may only be unified deliberately:

```text
Domain entity/value object
Application DTO/command/query
MCP input/output schema
SQLAlchemy persistence model
External API model
```

Pydantic is the default choice for external/application validation where appropriate, not a mandate for every domain object. SQLAlchemy models remain persistence concerns. PydanticAI is introduced only where an actual AI/agent capability exists.

## Research gate

Before implementing any non-trivial FastMCP feature, the agent must inspect:

1. Official FastMCP documentation.
2. The matching FastMCP source/API when behavior is ambiguous.
3. Relevant official `examples/` entries.
4. Relevant MCP specification/SEP material.
5. Version/migration documentation when version-sensitive.
6. Relevant official documentation for supporting libraries.

Research output must distinguish documented facts, source-derived behavior, examples, inference, and project-specific recommendations.

## Quality principles

### SOLID

Use principles to preserve real boundaries and replaceability. Do not introduce interfaces solely to satisfy a slogan.

### KISS

Prefer the smallest architecture that cleanly satisfies current requirements.

### DRY

Remove duplicated knowledge, not merely duplicated lines. Duplication may be preferable to a premature abstraction when requirements are not yet stable.

### YAGNI

Do not build future capabilities without a present requirement and a demonstrated design need.

## Pattern policy

A design pattern requires:

- concrete problem;
- reason the simple solution is insufficient;
- alternatives considered;
- complexity cost;
- testability impact;
- explicit YAGNI decision.

Common patterns are allowed when they correspond to actual boundaries: Repository for persistence ports, Adapter for external systems, Strategy for genuine interchangeable algorithms, Factory for non-trivial creation decisions, and Facade for a genuinely complex subsystem.

## Testing model

Testing is layered:

```text
Domain unit
Application unit
Infrastructure integration
MCP contract
Transport/integration
Protocol/conformance
Scenario/agent evaluation
```

A test must be placed at the lowest layer that can prove the behavior without losing the property being tested.

## Security model

Remote MCP servers require explicit authentication/authorization analysis. Secrets must never be embedded in source. Browser-facing deployments require explicit CORS analysis. Tool-level authorization must be distinguished from transport authentication. Error responses must not leak sensitive internals.

## Version policy

Production guidance follows the latest stable FastMCP 3.x line unless a project explicitly targets another version. FastMCP 4.x material is tracked as a separate compatibility/research stream and must be labelled by protocol/API era. No beta-only API may silently enter stable 3.x guidance.

## Definition of done

A skill or implementation is complete only when:

- requirements and assumptions are explicit;
- relevant official research is recorded;
- architecture and responsibility boundaries are reviewed;
- patterns are justified;
- contracts are defined;
- tests exist at appropriate layers;
- security and operational concerns are considered;
- static/test verification passes;
- final review finds no unresolved architecture violations.
