# Research Contract

A research artifact is valid only when it identifies the authoritative evidence used to support the decision.

## Required evidence

For a FastMCP feature, research must cover as applicable:

1. Official FastMCP documentation relevant to the feature.
2. Relevant official FastMCP repository implementation/examples.
3. Relevant MCP specification/protocol documentation.
4. Relevant dependency documentation.
5. Version and stability status for every API relied upon.
6. Migration/deprecation notes when changing or targeting an existing project.

## Research output

```yaml
feature: <name>
fastmcp_version: <version/range>
protocol_version: <version if relevant>
stability: stable|prerelease|unknown
official_docs:
  - <source>
official_examples:
  - <source>
other_authoritative_sources:
  - <source>
mechanisms_considered:
  - <mechanism>
selected_mechanism: <mechanism>
reasons: <why>
limitations: []
production_adaptation: <notes>
confidence: high|medium|low
```

## Rules

- Never guess an API from memory when authoritative documentation can be consulted.
- An official example demonstrates a mechanism; it does not automatically define production architecture.
- Never silently mix FastMCP 3.x and 4.x APIs.
- Third-party articles may provide context, but official sources take precedence when they conflict.
- Unresolved uncertainty must be recorded rather than hidden.
