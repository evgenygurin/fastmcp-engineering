# Research Contract

Before implementing or recommending a FastMCP capability, the agent must produce evidence sufficient to support the decision.

## Required evidence

1. Official FastMCP documentation relevant to the feature.
2. Relevant official FastMCP repository examples.
3. Relevant MCP specification/protocol documentation.
4. Version identification for every API relied upon.
5. Known limitations, compatibility concerns, and production caveats.

## Research record

```yaml
feature: <name>
fastmcp_version: <version/range>
protocol_version: <version if relevant>
official_docs:
  - <source>
official_examples:
  - <source>
mechanisms_considered:
  - <mechanism>
selected_mechanism: <mechanism>
reasons: <why>
limitations: []
production_adaptation: <notes>
confidence: high|medium|low
```

## Prohibited behavior

- Guessing an API from memory.
- Treating a minimal example as a production architecture.
- Mixing v3 and v4 APIs without an explicit compatibility decision.
- Replacing official research with third-party content when official evidence exists.
