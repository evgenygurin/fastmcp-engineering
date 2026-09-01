---
name: pydantic-schema-engineering
description: Engineer Pydantic v2 and MCP-facing schemas with explicit contracts, strict validation, JSON Schema compatibility, evolution rules, and separation from domain/ORM models.
---

# Pydantic / Schema Engineering

## Mission

Treat schemas as public contracts. Separate MCP transport DTOs, application commands/results, domain models, and SQLAlchemy persistence models. Do not let framework serialization accidentally define architecture.

## Trigger / Когда применять

**Scope / When to use:** Pydantic v2 and MCP-facing schemas with explicit contracts, strict validation, JSON Schema compatibility, evolution rules, and separation from domain/ORM models.
**Trigger:** designing or changing public schemas, validation, JSON Schema generation, or schema evolution.
**Upstream / Prerequisite:** repository engineering contracts and `AGENTS.md` read; identified exact Python, Pydantic, FastMCP and relevant dependency versions; evidence recorded before coding.
**Mission / Goal:** treat schemas as public contracts; separate MCP transport DTOs, application commands/results, domain models, and SQLAlchemy persistence models; do not let framework serialization accidentally define architecture.
**Research / Evidence:** read official Pydantic v2 documentation relevant to the feature; read official FastMCP schema/input/output documentation and llms material; inspect relevant official FastMCP examples; inspect Pydantic/FastMCP source/tests when behavior is ambiguous; check JSON Schema and MCP specification semantics where they affect interoperability.
**Decision / Selection rules:** use verified v2 APIs and semantics; avoid `Any`, unvalidated dictionaries, implicit coercion and custom validation when a precise type can express the invariant; verify how FastMCP derives tool input/output schemas for the exact version and test generated schemas and invocation results; classify every public schema change as additive/backward-compatible, breaking, migration-required, or protocol-version-gated; never treat Pydantic validation as authorization.
**Version / Compatibility:** identify exact Python, Pydantic, FastMCP and relevant dependency versions.

## Deliverables

**Deliverables / Artifacts:** research package, schema decision matrix, implementation, JSON Schema fixtures, compatibility tests, FastMCP integration tests, architecture re-check, and evidence ledger.
**Verification / Testing:** test validation success/failure, coercion/strictness, generated JSON Schema, serialization round trips, unions, boundary cases, malicious inputs, compatibility fixtures, and FastMCP protocol invocation; use property-based tests for complex invariants where useful.
**Failure / Stop conditions:** reject if schema boundaries are implicit, ORM entities are exposed directly, `Any` hides a contract, authorization is confused with validation, generated schemas are unverified, or a breaking change lacks migration/version treatment.
**Positive scenario:** a public schema is validated, verified against FastMCP protocol invocation, and evolves compatibly.
**Negative scenario:** an ORM entity is exposed directly as a public schema or a breaking change lacks migration/version treatment.

## Mandatory research gate

Before implementation:
1. Read repository engineering contracts and AGENTS.md.
2. Identify exact Python, Pydantic, FastMCP and relevant dependency versions.
3. Read official Pydantic v2 documentation relevant to the feature.
4. Read official FastMCP schema/input/output documentation and llms material.
5. Inspect relevant official FastMCP examples.
6. Inspect Pydantic/FastMCP source/tests when behavior is ambiguous.
7. Check JSON Schema and MCP specification semantics where they affect interoperability.
8. Record evidence before coding.

## Boundary model

```text
MCP JSON / JSON Schema
        ↓
MCP DTO / Pydantic adapter model
        ↓
Application command/result
        ↓
Domain model/value object
        ↓
Persistence model
```

A single model may cross layers only with an explicit architectural reason and documented trade-off.

## Pydantic v2

Use verified v2 APIs and semantics. Evaluate:
- BaseModel;
- TypeAdapter;
- Annotated / Field;
- unions and discriminated unions;
- generics and recursive models;
- validators/serializers;
- strictness;
- aliases;
- defaults and factories;
- nullable vs optional semantics;
- model configuration;
- serialization modes;
- JSON Schema generation.

Avoid `Any`, unvalidated dictionaries, implicit coercion, and custom validation when a precise type can express the invariant.

## MCP schema compatibility

Verify how FastMCP derives tool input/output schemas from Python annotations and Pydantic types for the exact version. Do not assume JSON Schema support equals MCP client compatibility. Test generated schemas and actual invocation results.

## Schema evolution

Every public schema change must classify compatibility:
- additive/backward-compatible;
- breaking;
- migration-required;
- protocol-version-gated.

Never silently rename fields, change nullability, change requiredness, alter enum semantics, or change serialization format without an explicit compatibility decision.

## Security

Validate structural and semantic constraints at the appropriate boundary. Never treat Pydantic validation as authorization. Do not accept arbitrary object construction, unsafe deserialization, secrets in repr/schema, or unbounded payloads without limits.

## Testing

Test validation success/failure, coercion/strictness, generated JSON Schema, serialization round trips, unions, boundary cases, malicious inputs, compatibility fixtures, and FastMCP protocol invocation. Use property-based tests for complex invariants where useful.
