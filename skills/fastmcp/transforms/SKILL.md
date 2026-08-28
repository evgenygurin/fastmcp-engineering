---
name: fastmcp-transforms
description: Design and implement FastMCP Transforms for systematic component composition and representation changes while preserving clean application/domain boundaries.
---

# FastMCP Transforms

## Mission

Use a FastMCP Transform when the requirement is to systematically derive, modify, filter, namespace, annotate, or otherwise compose MCP components from another component source, according to the exact semantics of the target FastMCP version.

A Transform is not a generic application service, repository, middleware pipeline, or arbitrary object mapper.

## Mandatory research gate

Before implementation:

1. Read `AGENTS.md` and all applicable engineering contracts.
2. Identify the exact FastMCP version.
3. Read the relevant official FastMCP Transform documentation.
4. Inspect relevant official PrefectHQ/fastmcp examples.
5. Inspect FastMCP source/tests when behavior is ambiguous or version-sensitive.
6. Check MCP specification/SEP material where protocol semantics are involved.
7. Check first-party documentation for directly involved dependencies.
8. Record evidence before implementation.

Never copy a Transform API from another major version without verification.

## Decision gate

First compare the requirement with:

- Tool / Resource / Prompt;
- Provider;
- Middleware;
- Context / DI;
- Lifespan;
- ordinary application composition;
- explicit application DTO mapping.

Choose Transform only when the problem is genuinely a FastMCP component transformation/composition concern.

## Responsibility boundary

Transform code may own MCP component-level adaptation such as systematic exposure, naming, filtering, wrapping, metadata/behavior transformation, or composition supported by the target FastMCP API.

It must not become the home for:

- domain invariants;
- application orchestration;
- persistence policy;
- database transactions;
- authorization business policy;
- external SDK lifecycle;
- arbitrary object-to-object mapping unrelated to MCP component composition.

If authorization is involved, distinguish component exposure/filtering from the application's actual authorization decision. Security policy must have an explicit owner.

## Composition

Document the transformation pipeline explicitly:

```text
Source components
      |
      v
Transform(s)
      |
      v
Exposed MCP components
      |
      v
Client / model
```

When multiple transforms are composed, document ordering and whether transformations are associative, idempotent, stateful, or dependent on prior transformations when those properties matter.

Prefer native FastMCP composition facilities over custom registries or wrapper frameworks.

## Correctness concerns

For every Transform, analyze:

- component identity;
- name/URI preservation or rewriting;
- metadata preservation;
- schema preservation or transformation;
- annotations;
- visibility/filtering;
- authorization interaction;
- error propagation;
- lifecycle/resource ownership;
- caching/freshness;
- ordering/composition;
- idempotency;
- concurrency/thread-safety;
- observability;
- compatibility with FastMCP Client/testing.

Only analyze dimensions relevant to the actual target behavior; do not introduce complexity speculatively.

## Testing

Prefer externally observable MCP behavior. Test:

- transformed component discovery;
- transformed schemas/metadata where applicable;
- success behavior;
- negative/error paths;
- composition order;
- filtering/visibility;
- authorization interaction;
- lifecycle and concurrency where relevant.

Use the documented FastMCP Client/in-process testing seam where practical.

## Rejection criteria

Reject a Transform if:

- it merely renames an application service to satisfy architecture;
- it contains business rules;
- it owns persistence;
- it replaces a simpler DTO mapper or application composition with unnecessary FastMCP machinery;
- Middleware or Provider is the actual semantic fit;
- the target-version API has not been verified;
- component exposure creates an unreviewed security/data-disclosure path.

## Deliverables

- version-specific research artifact;
- transformation decision record;
- responsibility/dependency map;
- implementation;
- focused tests;
- MCP integration tests where applicable;
- verification evidence;
- architecture re-check.
