---
name: fastmcp-providers
description: Design and implement FastMCP Providers as component sources/composition boundaries, without confusing them with repositories, services, dependency injection containers, or business-logic layers.
---

# FastMCP Providers

## Mission

Use FastMCP Providers when the problem is fundamentally about sourcing, discovering, exposing, composing, or dynamically controlling MCP components. Do not use Providers as generic application-service containers.

## Trigger / Когда применять

**Scope / When to use:** FastMCP Providers as component sources/composition boundaries, without confusing them with repositories, services, dependency injection containers, or business-logic layers.
**Trigger:** designing or changing how MCP components are sourced, discovered, exposed, composed, or dynamically controlled.
**Upstream / Prerequisite:** target FastMCP version independently verified; evidence recorded before implementation.
**Mission / Goal:** use FastMCP Providers when the problem is fundamentally about sourcing, discovering, exposing, composing, or dynamically controlling MCP components; do not use Providers as generic application-service containers.
**Research / Evidence:** independently verify the target FastMCP version and read the relevant official documentation, official examples, and source/tests when behavior is ambiguous; check MCP specification material where protocol semantics matter; check first-party dependency documentation; do not implement from memory or from examples belonging to another major version.
**Decision / Selection rules:** ask whether the problem is about where MCP components come from, whether dynamic discovery/loading/composition is required, and whether the provider is responsible for component lifecycle/exposure rather than business execution; if the problem is business persistence or orchestration, a Provider is probably the wrong abstraction; inspect built-in providers and composition mechanisms before custom code and prefer native composition.
**Version / Compatibility:** independently verify the target FastMCP version before implementation.
**Deliverables / Artifacts:** research/evidence artifact; provider decision record; responsibility/dependency map; implementation; focused tests; MCP integration tests where relevant; verification report; architecture re-check.
**Verification / Testing:** test provider behavior at the MCP boundary — component discovery/listing, lookup, composition, authorization visibility, failures, and lifecycle behavior; use the documented FastMCP Client/testing seam rather than testing only private implementation details.
**Failure / Stop conditions:** reject if a Provider exists only to satisfy a pattern preference, contains business invariants, directly owns business transactions, is a disguised service locator for arbitrary application dependencies, a simpler native FastMCP mechanism solves the requirement, version-sensitive behavior was not researched, or dynamic exposure creates an unreviewed authorization/data-exposure path.
**Positive scenario:** a Provider sources and composes MCP components natively and passes MCP-boundary tests.
**Negative scenario:** a Provider is used as a disguised service locator or contains business invariants.
