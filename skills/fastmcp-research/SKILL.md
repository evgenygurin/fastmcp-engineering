---
name: fastmcp-research
description: Produce reproducible, version-aware research artifacts for FastMCP projects — use before any framework-sensitive implementation decision.
---

# FastMCP Research Skill

## Purpose

Produce reproducible, version-aware research artifacts before implementation decisions are made for a FastMCP project.

This skill is a research procedure, not a tutorial and not an implementation shortcut.

## Scope

Use when a task involves FastMCP APIs, MCP protocol behavior, transports, authentication, authorization, providers, transforms, middleware, lifecycle, tasks, client behavior, composition, Apps, serialization, or other framework capabilities.

## Non-goals

- Do not implement production code.
- Do not infer undocumented behavior from memory.
- Do not treat an official example as a production architecture.
- Do not silently mix FastMCP major versions.

## Mandatory source hierarchy

Research in this order:

1. FastMCP version-specific official documentation.
2. FastMCP official repository source and tests.
3. FastMCP official examples.
4. MCP specification and relevant SEP documents.
5. First-party documentation for directly involved dependencies.
6. High-quality secondary sources only for additional context or unresolved practical issues.

If a claim cannot be supported by an appropriate source, mark it as unverified instead of presenting it as fact.

## Version gate

Before researching an API:

1. Identify the project's target FastMCP version.
2. Identify the latest stable version.
3. Identify prerelease versions separately.
4. Record whether each finding is stable, deprecated, prerelease, or version-independent.
5. Never apply v4 prerelease guidance to a v3 production target without an explicit compatibility decision.

As of the current research snapshot, the official installation documentation states that 3.x remains the latest stable line while FastMCP 4 is prerelease. Verify this again at execution time because this is time-sensitive.

## Research procedure

### Phase 1 — Define the question

Create a precise research question with:

- desired behavior;
- relevant FastMCP component;
- target version;
- runtime/transport context;
- security implications;
- expected artifact.

### Phase 2 — Map official documentation

Use the official documentation sitemap/LLM documentation where available. Identify all directly relevant pages, not only the first matching page.

Record:

- canonical URL;
- title;
- version badge/status;
- relevance;
- APIs referenced;
- prerequisites;
- related pages.

### Phase 3 — Inspect source and tests

When behavior matters, inspect the FastMCP repository implementation and tests. Source inspection is mandatory for:

- lifecycle semantics;
- middleware ordering;
- provider/transform composition;
- client behavior;
- authentication/authorization;
- serialization;
- concurrency/background task behavior;
- undocumented edge cases;
- APIs whose documentation is ambiguous.

Tests are evidence of intended behavior, but distinguish implementation behavior from public API guarantees.

### Phase 4 — Inspect examples

Search the official `examples/` tree for every relevant pattern.

For each example record:

- path;
- mechanism demonstrated;
- important API calls;
- assumptions;
- intentionally omitted production concerns;
- reusable pattern;
- anti-pattern risks;
- version relevance.

Do not copy an example's architecture merely because it is official.

### Phase 5 — MCP protocol research

Determine whether the behavior is FastMCP-specific or protocol-defined. If protocol-defined, inspect the relevant MCP specification/SEP and record the boundary.

### Phase 6 — Dependency research

If implementation would involve Pydantic, SQLAlchemy, PydanticAI, Supabase, HTTP clients, auth libraries, or other dependencies, research their current first-party guidance separately. Do not infer dependency semantics from FastMCP examples.

### Phase 7 — Synthesize patterns

Produce:

- capability matrix;
- version matrix;
- decision table;
- pattern catalog entries;
- anti-patterns;
- production adaptation notes;
- unresolved questions.

### Phase 8 — Confidence and evidence

Every significant conclusion must have an evidence class:

- `official-docs`
- `official-source`
- `official-tests`
- `official-example`
- `mcp-spec`
- `first-party-dependency`
- `secondary`
- `inference`

Do not present `inference` as official behavior.

## Required output

The completed research artifact MUST contain:

1. Research question.
2. Target versions.
3. Sources inspected.
4. Relevant official documentation.
5. Relevant official examples.
6. Source/test findings where required.
7. MCP specification findings where required.
8. Capability/version matrix.
9. Recommended mechanisms.
10. Rejected alternatives and reasons.
11. Production risks.
12. Security considerations.
13. Testing implications.
14. Open questions.
15. Evidence references.

## Decision rule

Research is incomplete if the agent can explain how an API works but cannot explain:

- why that mechanism is appropriate;
- what responsibility owns it;
- what alternatives were considered;
- what version it belongs to;
- how it should be tested;
- what production concerns the minimal example omits.

## Stop conditions

Stop and escalate to Architecture Governor when:

- requirements conflict with project architecture;
- two native FastMCP mechanisms appear equally valid and the trade-off is architectural;
- required behavior depends on undocumented internals;
- version compatibility is unclear;
- security behavior cannot be established from authoritative evidence.

## Completion criterion

The skill is complete only when another agent can use the resulting artifact to make the implementation decision without repeating the entire research process.