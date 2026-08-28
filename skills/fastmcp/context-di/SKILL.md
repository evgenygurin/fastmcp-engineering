---
name: fastmcp-context-di
description: Design FastMCP Context and dependency injection without turning request context into a Service Locator, God Object, or hidden application container.
---

# FastMCP Context / Dependency Injection

## Mission

Use FastMCP Context only for MCP/runtime concerns exposed by the target version and use dependency injection for explicit dependency composition. Preserve a strict boundary between protocol/runtime context and application/domain dependencies.

## Mandatory research gate

Before implementation:

1. Read `AGENTS.md` and engineering contracts.
2. Identify exact FastMCP and Python versions.
3. Read official FastMCP Context and dependency/DI documentation.
4. Inspect relevant official PrefectHQ/fastmcp examples.
5. Inspect source/tests for ambiguous or version-sensitive semantics.
6. Check MCP specification/SEP material where protocol semantics are relevant.
7. Check first-party dependency documentation for involved DI/validation libraries.
8. Record evidence before implementation.

Never infer Context/DI signatures or lifecycle behavior from memory.

## Decision gate

Explicitly distinguish:

- FastMCP `Context` as runtime/request-facing MCP capability;
- dependency injection as dependency composition;
- application services/use cases;
- domain services;
- lifespan-managed resources;
- middleware-established context;
- authentication/authorization context;
- configuration/settings.

Do not use Context merely because it is convenient to reach an object.

## Context boundary

Context may carry or expose runtime concerns supported by the target FastMCP version, such as request/session information, logging, progress/reporting, resource access, lifecycle state, and protocol-aware capabilities.

The exact supported surface is version-sensitive and must be verified.

Do not place arbitrary application state into Context to avoid defining interfaces.

## Dependency boundary

Dependencies should flow inward through explicit abstractions:

```text
FastMCP adapter
      │
      ├── Context/runtime capabilities
      │
      └── injected application ports
                │
                ▼
          application services
                │
                ▼
             domain
```

Infrastructure implementations are composed at the composition root/lifecycle boundary, not discovered dynamically by business code.

## Hard rule: no Service Locator

Reject designs where Context becomes a bag of services such as:

```python
ctx.services.database
ctx.services.user_service
ctx.services.payment_service
ctx.services.anything
```

This hides dependencies, weakens testability, and couples application logic to the MCP runtime.

Prefer explicit constructor/function dependencies and typed application ports.

## Lifespan interaction

If a dependency owns startup/shutdown resources, determine whether it belongs to FastMCP lifespan management. Verify exact lifespan and Context interaction from first-party sources before implementation.

Do not create per-request heavyweight clients if a correctly scoped lifecycle resource is appropriate.

## Scope and concurrency

For every injected dependency document its scope:

- process/application;
- server/lifespan;
- session;
- request/invocation;
- transient.

For mutable or stateful dependencies document concurrency guarantees and ownership. Never assume a client, session, ORM object, or cache is safe to share concurrently.

## Security

Treat identity/authentication context as untrusted input until established by the documented security boundary. Do not let arbitrary Context fields become authorization decisions. Define the policy owner and fail-closed behavior.

## Pydantic and typing

Use typed contracts at boundaries. Prefer Pydantic models for external/data contracts when appropriate and ordinary Python protocols/interfaces for application ports when that provides a cleaner dependency boundary. Do not introduce Pydantic solely to satisfy a pattern.

## Testing

Test both behavior and dependency wiring:

- Context-dependent behavior;
- injected fake/stub implementations;
- missing/invalid dependency cases;
- scope/lifecycle behavior;
- concurrent use where relevant;
- authorization context where relevant;
- MCP Client/in-process behavior;
- startup/shutdown cleanup for lifecycle-managed resources.

## Rejection criteria

Reject if Context is used as a service registry, if application services depend directly on FastMCP Context without an approved boundary, if dependency scope is undefined, if lifecycle ownership is ambiguous, if mutable shared state lacks a concurrency model, or if target-version Context/DI behavior was not verified.

## Deliverables

- version-specific Context/DI research artifact;
- dependency graph and scope map;
- Context-vs-DI decision record;
- implementation;
- wiring tests;
- lifecycle/concurrency verification;
- architecture re-check;
- reproducible evidence.
