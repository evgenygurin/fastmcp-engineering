---
name: pydantic-engineering
description: Treat Pydantic schemas as executable contracts at system boundaries — use for model validation, serialization, and MCP schema design.
---

# Pydantic / Schema Engineering

## Mission
Treat schemas as executable contracts at system boundaries. Separate transport contracts from application/domain models when responsibilities differ. Never let convenience serialization define an accidental public API.

## Trigger / Когда применять

**Scope / When to use:** Pydantic schemas as executable contracts at system boundaries — model validation, serialization, and MCP schema design.
**Trigger:** designing or changing models, validation, serialization, JSON Schema, or MCP-facing schemas.
**Upstream / Prerequisite:** `AGENTS.md` and repository contracts read; identified exact versions; evidence and compatibility hazards recorded before coding.
**Mission / Goal:** treat schemas as executable contracts at system boundaries; separate transport contracts from application/domain models when responsibilities differ; never let convenience serialization define an accidental public API.
**Research / Evidence:** read official Pydantic v2 documentation for models, validation, serialization, TypeAdapter, JSON Schema, validators, serializers, configuration, strictness, aliases, unions and generics; read official FastMCP documentation/examples for tool input/output schema generation and structured output; read MCP specification sections governing tool schemas/results; inspect official examples and source/tests for ambiguity.
**Decision / Selection rules:** classify every model as MCP input DTO, MCP output DTO, application command/query, domain value object/entity, or persistence model; use annotations and Pydantic constraints for structural validation and validators only for boundary invariants; choose strict vs lax validation intentionally; design validation and serialization separately; treat generated JSON Schema as an externally visible contract and verify the actual MCP-visible schema; prefer discriminated/tagged unions with a stable discriminator; classify public schema changes as additive, conditionally compatible or breaking.
**Version / Compatibility:** identify exact Python, Pydantic, FastMCP, MCP and PydanticAI versions.

## Deliverables

**Deliverables / Artifacts:** schema inventory, model ownership map, validation/serialization strategy, JSON Schema contract, FastMCP integration matrix, evolution policy, implementation, regression tests and architecture re-check.
**Verification / Testing:** schema regression tests must cover valid/invalid inputs, coercion boundaries, missing/null/default semantics, discriminators, serialization, aliases, secret exclusion, compatibility and the actual FastMCP-visible tool schema/structured output for critical tools.
**Failure / Stop conditions:** reject if public schemas depend on accidental ORM serialization, business rules are hidden in validators, security-sensitive values rely on unsafe coercion, schemas change without compatibility analysis, or MCP-visible schemas are assumed rather than verified.
**Positive scenario:** schemas are executable contracts verified against the actual FastMCP-visible schema.
**Negative scenario:** a public schema depends on accidental ORM serialization or unsafe coercion of security-sensitive values.

## Mandatory research gate
1. Read AGENTS.md and repository contracts.
2. Identify exact Python, Pydantic, FastMCP, MCP and PydanticAI versions.
3. Read official Pydantic v2 documentation for models, validation, serialization, TypeAdapter, JSON Schema, validators, serializers, configuration, strictness, aliases, unions and generics relevant to the design.
4. Read official FastMCP documentation/examples for tool input/output schema generation and structured output.
5. Read MCP specification sections governing tool schemas/results where applicable.
6. Inspect official examples and source/tests for ambiguity.
7. Record evidence and compatibility hazards before coding.

## Model boundaries
Classify every model as MCP input DTO, MCP output DTO, application command/query, domain value object/entity, or persistence model. Do not reuse one model across all layers merely to reduce files.

## Validation
Use annotations and Pydantic constraints for structural validation. Use validators only for boundary invariants. Business rules requiring repositories, authorization state or external services belong in application/domain services.

Choose strict vs lax validation intentionally. Do not rely on implicit coercion for security-sensitive identifiers, enums, booleans, numeric values or protocol fields without justification.

## Serialization
Design validation and serialization separately. Use serializers/aliases intentionally. Never expose secrets, internal identifiers, ORM internals or private fields accidentally.

## JSON Schema
Treat generated JSON Schema as an externally visible contract when FastMCP exposes it. Review required/nullable/default semantics, enums, formats, aliases, references and schema stability. Verify both the Python model schema and actual MCP-visible schema.

Pydantic provides `BaseModel.model_json_schema()` and `TypeAdapter.json_schema()` for JSON Schema inspection. The generated schema follows JSON Schema/OpenAPI conventions.

## FastMCP integration
FastMCP derives tool schemas from Python annotations and supports Pydantic models and other JSON-schema-compatible types. Return annotations can generate output schemas; explicit output schemas require matching structured output.

## Unions
Prefer discriminated/tagged unions when variants have a stable discriminator. Pydantic documents their deterministic validation and clearer generated schemas.

## Schema evolution
Treat public MCP schemas as versioned contracts. Classify additive, conditionally compatible and breaking changes. Do not rename/remove required fields or alter enum semantics without an explicit compatibility strategy.

## ORM boundary
Do not blindly expose SQLAlchemy ORM entities as MCP/Pydantic contracts. Define explicit read/write schemas when persistence and API semantics differ.

## Testing
Schema regression tests must cover valid/invalid inputs, coercion boundaries, missing/null/default semantics, discriminators, serialization, aliases, secret exclusion, compatibility and the actual FastMCP-visible tool schema/structured output for critical tools.
