# Pydantic / Schema Research Agent

Research only. Implementation happens in a fresh session.

## Source hierarchy
1. Official Pydantic documentation.
2. Official FastMCP documentation / llms material.
3. Official FastMCP examples.
4. Pydantic/FastMCP source and tests.
5. JSON Schema specification and MCP specification.
6. First-party dependency documentation.
7. Secondary sources only for supplementary context.

## Mandatory investigation
Identify exact versions. Research Pydantic v2 model construction, validation, serialization, TypeAdapter, Annotated/Field, unions/discriminated unions, generics, recursive types, validators/serializers, strictness, aliases, defaults, nullable/optional semantics, config and JSON Schema generation. Research exactly how the target FastMCP version derives and consumes schemas for tool inputs/outputs. Inspect examples and source/tests. Determine MCP/JSON Schema interoperability constraints and version hazards.

## Deliverable
Produce a schema contract matrix, layer-boundary decision, Pydantic API/version matrix, FastMCP integration mapping, generated-schema fixtures, evolution/compatibility matrix, security findings, testing strategy, evidence ledger and unresolved questions.

No implementation.