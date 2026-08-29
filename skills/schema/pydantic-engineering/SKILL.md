---
name: pydantic-schema-engineering
description: Evidence-first Pydantic v2 schema and API contract engineering for FastMCP, including validation, serialization, JSON Schema, discriminated unions and schema evolution.
---

# Pydantic / Schema Engineering

## Mission
Treat schemas as executable contracts at system boundaries. Separate transport contracts from application/domain models when their responsibilities differ. Never let convenience serialization define an accidental public API.

## Mandatory research gate

Before implementation:
1. Read AGENTS.md and repository contracts.
2. Identify exact Python, Pydantic, FastMCP, MCP and PydanticAI versions.
3. Read official Pydantic v2 documentation for models, validation, serialization, TypeAdapter, JSON Schema, validators, serializers, configuration, strictness, aliases, unions and generics relevant to the design.
4. Read official FastMCP documentation for tool input/output schema generation and structured output.
5. Read MCP specification sections governing tool schemas/results where applicable.
6. Inspect official examples and source/tests for ambiguous integration behavior.
7. Record evidence and compatibility hazards before coding.

## Boundary model

Explicitly classify every model as one or more of:
- MCP/transport input DTO;
- MCP/transport output DTO;
- application command/query;
- domain value object/entity;
- persistence model.

Do not reuse one model across all layers merely to reduce files. Reuse only when semantics, lifecycle and compatibility requirements genuinely match.

## Validation

Use type annotations and Pydantic constraints for structural validation. Use field/model validators only for invariants that belong at the schema boundary. Business rules requiring repositories, authorization state or external services belong in application/domain services, not Pydantic validators.

Choose strict vs lax validation intentionally. Do not rely on implicit coercion for security-sensitive identifiers, enums, booleans, numeric values or protocol fields without justification.

## Serialization

Design input validation and output serialization separately. Use serializers/aliases intentionally. Never expose secrets, internal identifiers, ORM internals or private fields accidentally. Verify `model_dump`, JSON serialization and schema generation for the exact target version.

## JSON Schema

Treat generated JSON Schema as an externally visible contract when FastMCP exposes it. Review titles, descriptions, required/nullable semantics, defaults, enums, formats, aliases, `$defs`/references and union representation. Avoid implementation-driven schema noise.

Pydantic generates JSON Schema from Python/Pydantic types; `BaseModel.model_json_schema()` and `TypeAdapter.json_schema()` are authoritative APIs for inspection. citeturn0search2turn0search6

## FastMCP integration

FastMCP derives tool schemas from Python annotations and supports Pydantic models and other JSON-schema-compatible types. Output schemas can be generated from return annotations; explicit output schemas must match returned structured output. citeturn0search0turn0search1

Therefore verify both the Python model contract and the actual MCP-visible schema. Do not assume that a valid Pydantic model automatically yields the desired MCP contract.

## Unions

Prefer discriminated/tagged unions where variants have a stable discriminator. They make validation deterministic and produce clearer schemas; Pydantic documents that they validate against the selected variant rather than attempting every branch. citeturn0search3

## Schema evolution

Treat public MCP schemas as versioned contracts. Identify backward-compatible, conditionally compatible and breaking changes. Never remove/rename required fields or alter enum semantics without an explicit compatibility strategy. Additive changes must still consider strict clients and generated schemas.

## ORM boundary

Do not blindly expose SQLAlchemy ORM entities as MCP/Pydantic contracts. Define explicit read/write schemas when persistence and API semantics differ. Prevent lazy-loading surprises and accidental relationship traversal.

## Testing

Snapshot or structurally assert important JSON Schemas. Test valid/invalid inputs, coercion boundaries, missing/null/default semantics, discriminators, serialization, aliases, secret exclusion and backwards compatibility. Test the actual FastMCP-visible tool schema and structured output for critical tools.

## Rejection criteria

Reject if public schemas depend on accidental ORM serialization, business rules are hidden in validators, security-sensitive values rely on unsafe coercion, schemas are changed without compatibility analysis, or MCP-visible schemas are assumed rather than verified.

## Deliverables

Schema inventory, boundary/model ownership map, validation strategy, serialization strategy, JSON Schema contract, FastMCP integration matrix, evolution policy, implementation, schema regression tests and architecture re-check.