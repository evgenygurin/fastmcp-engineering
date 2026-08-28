---
name: fastmcp-providers
description: Design and implement FastMCP Providers as component sources/composition boundaries, without confusing them with repositories, services, dependency injection containers, or business-logic layers.
---

# FastMCP Providers

## Mission

Use FastMCP Providers when the problem is fundamentally about sourcing, discovering, exposing, composing, or dynamically controlling MCP components. Do not use Providers as generic application-service containers.

## Mandatory research

Before implementation, independently verify the target FastMCP version and read the relevant official documentation, official examples, and source/tests when behavior is ambiguous. Check MCP specification material where protocol semantics matter. Check first-party dependency documentation for involved dependencies.

Do not implement from memory or from examples belonging to another major version.

## Decision gate

Ask:

1. Is the problem about where MCP components come from?
2. Is dynamic discovery/loading/composition required?
3. Is the provider responsible for component lifecycle or exposure rather than business execution?
4. Would a Tool/Resource/Prompt, Transform, Middleware, Context/DI, or ordinary application composition be simpler?

If the problem is business persistence or business orchestration, a Provider is probably the wrong abstraction.

## Responsibility boundary

A Provider may own component sourcing, discovery, lookup, listing, and provider-specific composition semantics according to the target FastMCP API.

A Provider must not silently become:

- a Repository;
- an Application Service;
- a Domain Service;
- a dependency-injection container;
- a transaction manager;
- an authorization policy engine;
- a generic service locator.

## Repository distinction

```text
Repository
  answers: "How do I access domain/application data?"

Provider
  answers: "Which MCP components are available and how are they sourced/composed?"
```

A provider may internally depend on an application port or infrastructure adapter when that is required to discover components. It should not absorb domain persistence policy.

## Composition rules

Before custom provider code, inspect built-in providers and composition mechanisms in the target FastMCP version. Prefer native composition over an invented registry or plugin framework.

When dynamic components are involved, explicitly document:

- discovery semantics;
- lookup semantics;
- identity and naming;
- visibility;
- authorization implications;
- caching/freshness;
- lifecycle ownership;
- error behavior;
- concurrency behavior;
- cleanup/resource ownership.

## Testing

Test provider behavior at the MCP boundary where practical. Verify component discovery/listing, lookup, composition, authorization visibility, failures, and lifecycle behavior relevant to the implementation. Use the documented FastMCP Client/testing seam rather than testing only private implementation details.

## Deliverables

- research/evidence artifact;
- provider decision record;
- responsibility/dependency map;
- implementation;
- focused tests;
- MCP integration tests where relevant;
- verification report;
- architecture re-check.

## Rejection criteria

Reject if:

- Provider exists only to satisfy a pattern preference;
- Provider contains business invariants;
- Provider directly owns business transactions;
- Provider is a disguised service locator for arbitrary application dependencies;
- a simpler native FastMCP mechanism solves the requirement;
- version-sensitive behavior was not researched;
- dynamic exposure creates an unreviewed authorization/data-exposure path.
