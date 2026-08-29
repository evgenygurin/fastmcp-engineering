---
name: application-domain-architecture
description: Evidence-first design of layered Python application/domain architecture for FastMCP and PydanticAI systems, with explicit use cases, ports, adapters, policies, transaction ownership and dependency direction.
---

# Application / Domain Architecture

## Mission
Keep MCP, agent, transport, persistence and external integrations at the edges. Business rules and application workflows must remain deterministic, testable and independent of FastMCP/PydanticAI/SQLAlchemy whenever practical.

## Mandatory research gate
Before implementation:
1. Read AGENTS.md and all repository architecture/security/testing contracts.
2. Read the existing FastMCP, PydanticAI, Pydantic and SQLAlchemy skills and research packages.
3. Identify exact versions and verify framework lifecycle/DI semantics from official documentation.
4. Research Clean Architecture, Hexagonal Architecture/Ports & Adapters, dependency inversion, domain modeling and transaction boundaries using authoritative sources.
5. Inspect official FastMCP/PydanticAI examples relevant to adapter boundaries.
6. Inspect repository structure and existing conventions before proposing abstractions.
7. Record evidence, alternatives and unresolved questions.

Do not cargo-cult Clean Architecture. Layers are justified by independent responsibilities and change boundaries, not by file-count targets.

## Target dependency direction

```text
          Transport / MCP / CLI / HTTP
                     │
                     ▼
              Interface Adapters
                     │
                     ▼
              Application Use Cases
                     │
          ┌──────────┴──────────┐
          ▼                     ▼
       Domain              Output Ports
          ▲                     │
          │                     ▼
          └──────────── Infrastructure Adapters
```

Dependencies point inward toward stable policies. Infrastructure implements ports; domain does not import FastMCP, PydanticAI, SQLAlchemy sessions or provider SDKs merely to express business rules.

## Domain
Domain contains business concepts, invariants, policies and domain services that are genuinely domain-level. Keep it framework-light. Do not create an anemic domain merely to satisfy a folder structure, and do not create domain abstractions for CRUD with no domain behavior.

Domain invariants must be deterministic. Authorization policy that determines whether an operation is allowed must not depend on an LLM response.

## Application
Application use cases orchestrate a business operation: load required state through ports, enforce application policy, invoke domain behavior, coordinate external capabilities and define transaction ownership. Application code should not know MCP transport details.

One use case should have one coherent business purpose. Avoid god services and generic `Manager`/`Helper` classes.

## Ports
Define ports only at meaningful architectural boundaries. Input ports represent application use cases; output ports represent dependencies such as repositories, external services, clocks, event publishers or model gateways when those dependencies need substitution or isolation.

Do not create an interface for every class. A port must protect a change boundary, testing boundary or dependency direction.

## Adapters
MCP/FastMCP handlers are input adapters. PydanticAI agents are orchestration adapters/capabilities. SQLAlchemy repositories are output adapters. Provider SDK clients and HTTP clients remain infrastructure. Mapping between transport schemas and application/domain types belongs at the boundary.

## Dependency injection
Prefer explicit constructor/function dependencies. Composition roots assemble concrete implementations. Avoid service locators, module-level mutable singletons and hidden imports. Request-scoped resources must follow their documented lifecycle.

## Transactions
Transaction ownership belongs to the application/use-case boundary or an explicitly documented unit-of-work abstraction. MCP handlers and domain entities must not independently commit arbitrary transactions. Domain code must not depend on a live SQLAlchemy session.

## Unit of Work / Repository
Use Repository when persistence semantics are meaningful to the domain/application boundary. Use Unit of Work when a use case needs atomic coordination across multiple persistence operations. Do not introduce these patterns merely because they are conventional.

## Mapping
Keep external/ORM representations from leaking inward when doing so protects a real boundary. Avoid excessive DTO/entity duplication when the boundary is not independently evolving. Mapping code must be explicit about identity, nullability, ownership and collections.

## Errors
Define a stable application/domain error taxonomy. Translate infrastructure/provider/MCP errors at the adapter boundary. Never expose raw database exceptions, provider errors or internal stack traces as an application contract.

## Time, randomness and external effects
Inject clocks/randomness/external effect ports when deterministic behavior matters. Keep side effects at explicit boundaries. Use idempotency for operations that can be retried or replayed.

## Agent boundary
PydanticAI may reason and orchestrate tools, but application/domain policy remains authoritative. Agent tools call application capabilities; they do not bypass repositories, authorization or transaction ownership.

## MCP boundary
FastMCP tools/resources/prompts are protocol adapters. They validate transport input, resolve request context, call an application use case and map the result to the MCP contract. Do not place domain workflows inside decorators.

## Anti-patterns
Reject god services, anemic-but-overabstracted domains, generic repositories, interface-per-class designs, service locators, circular dependencies, framework imports in domain policy, transaction commits in adapters, duplicated authorization, and abstractions without a demonstrated change/testing boundary.

## Testing
Domain tests are pure and fast. Application tests use deterministic ports/fakes where appropriate. Adapter tests verify framework/protocol behavior. Persistence tests use the real DB for DB semantics. Architecture tests may enforce dependency direction and forbidden imports. Do not make every layer require an end-to-end test.

## Deliverables
Architecture diagram, responsibility matrix, dependency rule, use-case catalog, port/adapter matrix, transaction policy, error taxonomy, composition-root design, rejected alternatives, architecture tests, implementation and verification report.