---
name: dependency-injection-composition-root
description: Evidence-first dependency injection, lifecycle and composition-root engineering for production FastMCP applications.
---

# Dependency Injection / Composition Root

## Mission
Make the dependency graph explicit, typed, testable and lifecycle-safe. Dependencies are assembled at the application boundary; domain and use cases consume capabilities rather than constructing infrastructure.

## Trigger / Когда применять

**Scope / When to use:** dependency injection, lifecycle and composition-root engineering for production FastMCP applications.
**Trigger:** designing or changing the dependency graph, composition root, dependency lifetimes, request context, or resource lifecycle.
**Upstream / Prerequisite:** identified exact Python, FastMCP, Pydantic, SQLAlchemy, PydanticAI and relevant client/library versions; evidence recorded.
**Mission / Goal:** make the dependency graph explicit, typed, testable and lifecycle-safe; dependencies are assembled at the application boundary.
**Research / Evidence:** identify exact versions; read current official documentation first, then exact-version examples/source/tests for FastMCP lifespan/server construction, dependency/context mechanisms, SQLAlchemy async lifecycle, PydanticAI dependency injection and all selected DI/container libraries; do not introduce a DI framework merely because one exists.
**Decision / Selection rules:** have one discoverable composition root; keep dependency direction explicit; prefer constructor injection for stable required dependencies; use `Protocol`/interfaces only where a consumer needs substitution, isolation, or a stable boundary; classify every dependency lifetime; use FastMCP-native lifespan mechanisms; define create/health/use/failure/shutdown/cancellation for every resource; keep request context in explicit trusted context; construct engine/session factory at the appropriate application lifetime.
**Version / Compatibility:** identify exact versions; use FastMCP-native lifespan/startup/shutdown mechanisms verified for the exact version.

## Deliverables

**Deliverables / Artifacts:** dependency graph; lifetime matrix; composition-root design; ports/protocols; FastMCP lifespan mapping; SQLAlchemy lifecycle; PydanticAI dependency mapping; external-client lifecycle; startup/shutdown failure model; test wiring strategy; evidence ledger; rejected alternatives; verification report.
**Verification / Testing:** application tests construct the dependency graph with fakes/test adapters; integration tests wire real infrastructure selectively; add composition-root tests that detect missing bindings, invalid lifecycle order and unsafe singleton/scoped combinations; test startup failure and shutdown cleanup.
**Failure / Stop conditions:** reject global mutable containers, service locators, hidden imports that instantiate services, repository-created sessions, handlers creating infrastructure, domain imports of FastMCP/SQLAlchemy/PydanticAI, singleton request state, and generic `Container.get()` calls scattered throughout code.
**Positive scenario:** an explicit composition root assembles the dependency graph with correct lifetimes and passes composition-root tests.
**Negative scenario:** a service locator or hidden global container hides dependencies and breaks lifecycle safety.

## Mandatory research
Identify exact Python, FastMCP, Pydantic, SQLAlchemy, PydanticAI and relevant client/library versions. Read current official documentation first, then exact-version examples/source/tests for FastMCP lifespan/server construction, dependency/context mechanisms, SQLAlchemy async lifecycle, PydanticAI dependency injection and all selected DI/container libraries. Do not introduce a DI framework merely because one exists.

## Composition root
There must be one discoverable composition root responsible for configuration resolution, infrastructure construction, adapter wiring, application service/use-case construction and MCP server assembly. Keep business logic out of this layer. Make startup failures explicit.

## Dependency direction
Domain → abstractions owned by the consuming layer where appropriate. Application depends on domain and ports. Infrastructure implements ports. MCP adapters depend on application contracts. Composition root is allowed to know concrete implementations and wire them together. Never reverse this direction through imports or hidden globals.

## Explicit injection
Prefer constructor injection for stable required dependencies. Use function parameters for narrow request-scoped collaborators. Avoid service locator, ambient global containers and hidden dependency lookup. A dependency must be visible from the object's construction or documented framework context.

## Protocols / ports
Use `Protocol` or abstract interfaces only where a consumer needs substitution, isolation, or a stable boundary. Keep interfaces small and behavior-oriented. Do not create one interface per class. Type contracts must describe what consumers need, not mirror implementations.

## Lifetimes
Classify every dependency as process-singleton, application-lifetime, request/task-scoped, transaction-scoped or transient. Verify framework semantics rather than assuming them. Never share unsafe mutable resources across concurrent tasks. `AsyncSession` requires a safe per-task/session lifecycle; it is not a global singleton.

## FastMCP lifecycle
Use FastMCP-native lifespan/startup/shutdown mechanisms when appropriate and verified for the exact version. Construct resources before serving traffic; close them deterministically. Lifespan should coordinate resources, not contain domain workflows. Do not create DB clients/HTTP clients/LLM clients lazily inside handlers without an explicit lifecycle policy.

## Resource lifecycle
For every resource define create, health/readiness, use, failure, shutdown and cancellation behavior. Ensure partial startup rolls back already-created resources. Shutdown should be idempotent and bounded. Background tasks must have explicit ownership and cancellation semantics.

## Request context
Keep authenticated principal, correlation/request IDs, tenant scope and other request-local data in explicit trusted context. Do not use mutable module globals or thread-local assumptions in async code. Context propagation must be tested across spawned tasks/background work.

## PydanticAI
When PydanticAI is used, follow its documented dependency/dependency-injection mechanisms. Keep model/provider configuration and agent dependencies outside domain objects. Do not let an LLM agent construct repositories, sessions or privileged clients. Model output remains untrusted.

## SQLAlchemy
Construct engine/session factory at the appropriate application lifetime. Inject session/unit-of-work boundaries into application operations. Never let repositories create arbitrary engines or global sessions. Do not share `AsyncSession` concurrently between independent tasks.

## External clients
HTTP, MCP, queues, LLM providers and storage clients are infrastructure adapters. Inject narrow ports where application logic depends on them. Centralize timeout, retry, auth and lifecycle policies. Never instantiate SDK clients deep inside use cases.

## Configuration
Configuration is resolved once at the composition boundary using the configuration skill. Do not let dependencies read environment variables directly. Secrets enter through explicit configuration/secret providers and never through prompts or model context accidentally.

## Testing
Application tests should construct the dependency graph with fakes/test adapters. Integration tests should wire real infrastructure selectively. Add composition-root tests that detect missing bindings, invalid lifecycle order and unsafe singleton/scoped combinations. Test startup failure and shutdown cleanup.

## Circular dependencies
Break cycles through dependency inversion, ports, domain events or application orchestration. Do not use lazy imports or runtime service lookup merely to hide architectural cycles.

## Anti-patterns
Reject global mutable containers, service locators, hidden imports that instantiate services, repository-created sessions, handlers creating infrastructure, domain imports of FastMCP/SQLAlchemy/PydanticAI, singleton request state, and generic `Container.get()` calls scattered throughout code.