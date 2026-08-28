---
name: fastmcp-providers
description: Design and implement FastMCP Providers as component sources/composition boundaries, without confusing them with repositories, services, dependency injection containers, or business-logic layers.
---

# FastMCP Providers

Use FastMCP Providers when the problem is fundamentally about sourcing, discovering, exposing, composing, or dynamically controlling MCP components. Do not use Providers as generic application-service containers.

## Mandatory research

Before implementation, independently verify the exact target FastMCP version and read relevant official documentation, official PrefectHQ/fastmcp examples, and source/tests when behavior is ambiguous. Check MCP specification material where protocol semantics matter. Check first-party dependency documentation for involved dependencies.

The current official FastMCP server documentation describes Providers as supplying Tools, Resources, and Prompts dynamically, and says providers are queried at request time. This remains version-sensitive and must be verified against the target release before relying on it. citeturn0search9

Do not implement from memory or from examples belonging to another major version.

## Decision gate

Ask:
1. Is the problem about where MCP components come from?
2. Is dynamic discovery/loading/composition required?
3. Is the provider responsible for component exposure rather than business execution?
4. Would a Tool/Resource/Prompt, Transform, Middleware, Context/DI, Lifespan, or ordinary application composition be simpler?

If the problem is business persistence or orchestration, a Provider is probably the wrong abstraction.

## Responsibility boundary

A Provider may own component sourcing, discovery, lookup, listing, filtering, delegation, and provider-specific composition semantics according to the target FastMCP API.

A Provider must not silently become a Repository, Application Service, Domain Service, dependency-injection container, transaction manager, authorization policy engine, or generic service locator.

## Repository distinction

```text
Repository
  answers: "How do I access domain/application data?"

Provider
  answers: "Which MCP components are available and how are they sourced/composed?"
```

A provider may internally depend on an application port or infrastructure adapter when required to discover components. It should not absorb domain persistence policy.

## Dynamic discovery

For every dynamic provider document: source of truth, discovery trigger/request-time behavior, lookup key, filtering, freshness, caching, invalidation, failure behavior, timeout/deadline propagation, cancellation, concurrency, and lifecycle ownership.

Do not introduce caching without understanding freshness and authorization implications. Do not turn component listing into uncontrolled remote fan-out.

## Identity and composition

Before custom provider code, inspect built-in providers and composition mechanisms in the target version. Prefer native composition over an invented registry or plugin framework.

Verify canonical component identity/key semantics before implementing deduplication or collision handling. Test duplicate identities, overlapping providers, precedence, mounts, transforms, visibility, and replacement/override behavior where supported.

## Security

Discovery can disclose capabilities. Separate discoverability, read/invoke/render permission, returned-data authorization, tenant/user scope, and policy ownership. Hiding a component is not equivalent to authorization.

## State, lifecycle, and concurrency

For stateful providers document scope and concurrency guarantees. Never assume shared mutable state is safe during concurrent discovery. External clients, DB sessions, caches, and other heavyweight resources need explicit ownership and should normally be lifecycle-managed rather than constructed per lookup when appropriate.

## Performance and resilience

Analyze discovery latency, N+1 remote calls, pagination/fan-out, cache staleness, authorization staleness, timeout/deadline propagation, cancellation, backpressure, retry safety, failure isolation, and memory growth.

## Testing

Use the documented FastMCP Client/in-process seam where practical. Cover discovery/listing, lookup, empty/missing components, duplicate identity, precedence/composition, visibility, authorization-sensitive discovery, external-source failure, timeout/cancellation, concurrent access, caching where applicable, and lifecycle cleanup.

## Deliverables

- version-specific research/evidence artifact;
- provider decision record;
- discovery/source-of-truth map;
- identity/collision policy;
- security boundary;
- lifecycle/scope model;
- implementation;
- Client/in-process integration tests;
- performance/reliability verification;
- architecture re-check;
- evidence ledger.

## Rejection criteria

Reject disguised repositories/service locators, business invariants in providers, direct business transaction ownership, guessed component identity, undefined freshness/failure semantics, visibility-as-authorization, shared mutable state without a concurrency model, custom registries when native FastMCP composition suffices, and implementation based on unverified target-version behavior.
