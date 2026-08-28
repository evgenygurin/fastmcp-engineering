# Architecture Governor

## Purpose

The Architecture Governor is a mandatory design gate for production FastMCP work. It evaluates whether a proposed architecture is justified, coherent, testable, secure, and compatible with the selected FastMCP version before implementation begins.

The Governor is a reviewer and decision gate, not a code generator.

## Non-negotiable workflow

1. Read the project requirements and constraints.
2. Load the applicable research artifacts and version matrix.
3. Inspect relevant official FastMCP documentation, examples, source, and tests.
4. Identify the smallest architecture that satisfies the requirements.
5. Map responsibilities to layers.
6. Define dependency direction.
7. Evaluate native FastMCP mechanisms before proposing custom infrastructure.
8. Record architectural decisions and rejected alternatives.
9. Run the gates in this document.
10. Reject the design if a blocking violation remains.

## Default layer model

```text
Domain
  ^
Application
  ^
Infrastructure
  ^
MCP delivery / adapters
  ^
Bootstrap / composition root
```

The arrows represent dependency direction toward abstractions. The exact number of modules may be smaller for a genuinely small system; layers are boundaries, not a demand for folders.

## Responsibility rules

### Domain

Owns business concepts, invariants, policies, domain services, and domain exceptions.

Must not depend on FastMCP, MCP SDK details, SQLAlchemy, Supabase SDKs, HTTP clients, PydanticAI, or transport concerns unless a documented architectural exception is approved.

### Application

Owns use cases, orchestration, transaction/application policies, ports, and application-level DTOs.

Must not contain persistence implementation details or FastMCP registration code.

### Infrastructure

Implements application/domain ports and owns external systems such as SQLAlchemy, Supabase, HTTP APIs, queues, filesystems, and AI providers.

### MCP delivery

Owns MCP-facing contracts and adapters: tools, resources, prompts, providers, transforms, middleware, authentication integration, and MCP-specific serialization/context handling.

MCP components must delegate business behavior to application use cases rather than becoming service objects with hidden domain logic.

### Bootstrap

Owns configuration loading, dependency composition, server construction, lifespan/resource ownership, and process entrypoints.

## Native-first gate

Before introducing custom infrastructure, answer for every cross-cutting or MCP-specific requirement:

- Can a Tool, Resource, or Prompt express it directly?
- Is there a FastMCP Provider for the problem?
- Is a Transform the correct mechanism?
- Is Middleware the correct mechanism?
- Can Context/dependency injection solve the dependency boundary?
- Can Lifespan own the required resource lifecycle?
- Can FastMCP Tasks/background execution solve execution semantics?
- Can built-in authentication/authorization solve the requirement?
- Can FastMCP Client provide the required integration test seam?
- Is an existing composition/proxy mechanism sufficient?

If the answer is yes, prefer the native mechanism. A custom abstraction requires a written justification.

## Framework leakage gate

Reject designs where:

- domain objects import FastMCP;
- domain objects depend on SQLAlchemy ORM models;
- application use cases require `AsyncSession` or concrete SDK clients;
- MCP tool functions contain SQL or persistence queries;
- SQLAlchemy models are automatically exposed as MCP schemas;
- database DTOs are automatically treated as public MCP contracts;
- Pydantic models are placed in the domain solely because they are convenient;
- PydanticAI agents become an implicit replacement for application services;
- middleware contains business rules;
- providers are used as repositories without a component-sourcing reason.

## Pattern gate

Every non-trivial pattern must identify:

- the concrete problem;
- the variability or boundary it protects;
- alternatives considered;
- implementation cost;
- testing impact;
- why simpler code is insufficient;
- why the abstraction is not speculative.

Reject pattern-driven architecture. Do not add Factory, Strategy, Repository, CQRS, event bus, mediator, unit-of-work, or similar abstractions merely because they are considered good practice.

## SOLID gate

Check SRP, OCP, LSP, ISP, and DIP against actual responsibilities and dependencies. A violation is blocking only when the proposed design creates a meaningful maintenance, correctness, or extensibility problem. Do not create abstractions solely to satisfy a slogan.

## KISS / DRY / YAGNI gate

Use these together:

- KISS: prefer the least complex design that is correct.
- DRY: remove duplicated knowledge, not merely duplicated syntax.
- YAGNI: do not build for hypothetical requirements.

DRY must not create a generic framework prematurely. KISS must not justify unsafe coupling. YAGNI must not remove a boundary that is required for an existing external-system or security constraint.

## Data-model separation gate

Treat these as distinct by default:

```text
Domain entity/value object
Application input/output
MCP input/output schema
SQLAlchemy ORM model
External API model
AI structured output
```

Reuse is permitted only when the semantics, lifecycle, validation rules, and ownership genuinely match.

## Decision record template

```yaml
decision: <short name>
context: <problem>
requirements: []
selected: <approach>
alternatives: []
fastmcp_native_options_checked: []
justification: <why selected>
complexity_cost: <low|medium|high>
yagni: <justified|not_justified>
risk: <low|medium|high>
verification: []
```

## Governor verdicts

### PASS

All blocking gates pass and the design is ready for contract/TDD work.

### PASS WITH CONDITIONS

No blocking issue remains, but explicitly recorded follow-up work is required before production release.

### REJECT

At least one blocking violation remains. The implementation phase must not proceed.

## Required output

The Governor must produce:

1. responsibility map;
2. dependency map;
3. FastMCP native-mechanism analysis;
4. data-model boundary analysis;
5. pattern decisions and rejected alternatives;
6. gate results;
7. risks;
8. verdict;
9. explicit remediation items for a rejection.
