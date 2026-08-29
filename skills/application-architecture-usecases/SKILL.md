---
name: application-architecture-usecases
description: Evidence-first layered application architecture for FastMCP services using explicit use cases, dependency inversion and domain boundaries.
---

# Application Architecture / Use Cases

## Mission
Keep MCP protocol concerns, application orchestration, domain rules and infrastructure independently understandable, testable and replaceable.

## Mandatory research
Identify exact versions of FastMCP, Python, Pydantic/PydanticAI and relevant framework libraries. Read current official documentation and exact-version examples/source/tests before deciding architecture or APIs. Inspect all repository skills and existing architecture. Record evidence and re-check version-sensitive claims before completion.

## Layers
Use a deliberate dependency direction:

`MCP adapter → Application → Domain`

`Application → Ports ← Infrastructure`

Infrastructure implements ports; domain does not import FastMCP, SQLAlchemy, PydanticAI, HTTP clients or provider SDKs. Pydantic models belong at boundaries unless they are explicitly chosen as domain value objects for a justified reason.

## MCP adapter
MCP handlers translate protocol input/context into application commands and translate application results/errors into protocol responses. They do not contain business rules, SQL, provider calls, transaction orchestration or authorization policy beyond invoking the trusted authorization boundary.

## Application layer
A use case represents one coherent business capability and owns orchestration: authorization context, transaction boundary, domain operations, port calls and output mapping. Keep use cases cohesive and explicit. Do not create a use-case class for every trivial getter merely to satisfy a pattern; apply the abstraction where it protects a real boundary.

## Domain
Domain objects express invariants and business behavior independent of infrastructure. Prefer rich domain behavior where invariants belong together; avoid anemic data bags when behavior is genuinely domain-specific. Do not turn domain objects into service locators or dependency containers.

## Ports / dependency inversion
Define narrow ports around capabilities the application actually needs. Depend on interfaces/protocols at the application boundary, not concrete database/HTTP/LLM clients. Do not create speculative interfaces for dependencies that have no meaningful substitution boundary.

## Composition root
Construct concrete infrastructure and wire dependencies in one composition root/startup boundary. Dependency injection must be explicit. Avoid global service registries, hidden singletons and runtime imports used to bypass dependency direction.

## OOP / patterns
Use patterns only when they remove real complexity: Strategy for interchangeable policies, Factory when construction has meaningful variation, Adapter for external APIs, Repository for persistence abstraction, Unit of Work for transaction coordination, Specification only when query/business predicates genuinely benefit. Prefer simple functions/value objects when a class adds no responsibility or state.

## SOLID / KISS / DRY / YAGNI
Single Responsibility means one reason to change, not one method per class. Open/Closed should not become speculative plugin architecture. Liskov requires substitutable contracts. Interface Segregation favors small capability ports. Dependency Inversion protects application/domain boundaries. DRY applies to knowledge/rules, not merely repeated syntax. KISS and YAGNI override speculative abstraction.

## Command/query separation
Separate state-changing use cases from reads when it clarifies authorization, transactions and performance. Do not introduce CQRS/event sourcing solely because they are fashionable. Read models may use optimized queries without exposing ORM models to MCP contracts.

## Mapping
Keep protocol DTOs, application commands/results, domain objects and persistence models conceptually distinct. Avoid generic magic mappers when mapping hides security-sensitive fields, lifecycle semantics or ownership. Mapping code should be deterministic and tested.

## Errors
Domain/application exceptions express business failures. Infrastructure exceptions are translated at the application boundary. MCP protocol error mapping belongs to the adapter. Never leak provider, SQL or internal stack details through public responses.

## Authorization
Authorization is a trusted application/security concern. A use case must receive verified caller/tenant context and enforce resource scope. Model-generated intent, prompt text and MCP metadata are never authorization mechanisms.

## Transactions and side effects
The application owns transactional orchestration. Do not hold DB transactions open across slow LLM/HTTP calls unless explicitly justified. For reliable cross-system effects use outbox/workflow/idempotency patterns from the persistence/reliability skills.

## Async
Use async where the dependency and workload benefit from it. Do not make domain code async merely because the MCP adapter is async. Avoid blocking I/O in async application paths and propagate cancellation/deadlines through ports where supported.

## Testing
Test domain invariants without infrastructure. Test use cases with fake/test ports and explicit authorization/transaction boundaries. Use integration tests for MCP adapters and real infrastructure semantics. Test architecture boundaries so forbidden imports/dependencies do not silently return.

## Rejection criteria
Reject god services, god handlers, service locators, hidden globals, domain imports of infrastructure/frameworks, speculative abstraction layers, generic mapper magic that hides semantics, repository-owned business transactions and use cases that merely proxy one dependency without a real boundary.

## Deliverables
Architecture diagram; dependency-direction rules; use-case catalog; port contracts; composition-root map; pattern decision record; mapping/error policy; authorization/transaction boundaries; architecture test matrix; evidence ledger; rejected alternatives; verification report.