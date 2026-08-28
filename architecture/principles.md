# Engineering Principles

## Boundary rule

Frameworks and infrastructure are adapters. Domain policy belongs in domain/application layers unless there is a documented reason otherwise.

## Layer model

```text
Domain
  ↑
Application
  ↑
Infrastructure adapters
  ↑
MCP delivery adapters
  ↑
Bootstrap/composition
```

The arrows describe dependency direction: inner layers do not depend on outer implementation details.

## Technology boundaries

- FastMCP: MCP delivery/runtime concerns.
- Pydantic: external/application contracts and validation where appropriate; do not automatically make every domain object a Pydantic model.
- SQLAlchemy: persistence implementation.
- Supabase: external platform/infrastructure adapter unless the project explicitly chooses Supabase as its application boundary.
- PydanticAI: agent/LLM capability adapter; not an automatic dependency of every MCP server.

## Pattern rule

Use a design pattern only when it solves an identified problem such as variability, dependency inversion, integration, or lifecycle complexity. Do not introduce patterns for ceremony.

## Decision rule

For every abstraction that adds indirection, record the problem, alternatives considered, expected benefit, and YAGNI assessment.
