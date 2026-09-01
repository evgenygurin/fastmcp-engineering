---
name: api-contract-schema-engineering
description: Evidence-first API and MCP contract engineering with Pydantic v2 and JSON Schema.
---

# API Contract / Schema Engineering

## Mission
Treat every MCP-visible name, description, input schema, output schema, error shape and serialization rule as a versioned public contract.

## Trigger / Когда применять

**Scope / When to use:** any MCP-visible API or contract surface: names, descriptions, input/output schemas, error shapes, serialization rules, defaults, pagination, and structured output.
**Trigger:** defining or changing a public MCP tool/resource/prompt contract, schema, error shape, or serialization rule.
**Upstream / Prerequisite:** identified exact versions of Python, FastMCP, Pydantic, MCP SDK and JSON Schema; contract-first capability inventory.
**Mission / Goal:** treat every MCP-visible name, description, input schema, output schema, error shape and serialization rule as a versioned public contract.
**Research / Evidence:** read the current official MCP specification and FastMCP/Pydantic documentation first; inspect exact-version examples/source/tests; verify the JSON Schema dialect actually emitted and accepted by target MCP clients.
**Decision / Selection rules:** contract-first before implementation; classify changes as additive-compatible, behavior-compatible, potentially breaking, or breaking; prefer stable capability identity and additive evolution over gratuitous `/v1`-style duplication; be deliberate about defaults.
**Version / Compatibility:** identify exact versions; classify every change for compatibility; test generated schemas against representative MCP clients/validators.

## Deliverables

**Deliverables / Artifacts:** contract inventory; schema definitions; JSON Schema compatibility report; serialization policy; error taxonomy; compatibility/versioning policy; pagination contract; structured-output policy; documentation rules; contract test matrix; evidence ledger; rejected alternatives; verification report.
**Verification / Testing:** generate and snapshot schemas; test valid/invalid inputs, nullability, defaults, enum evolution, serialization, errors, pagination, structured outputs and backward compatibility; include protocol-level discovery and invocation tests.
**Failure / Stop conditions:** reject accidental contracts from ORM models, undocumented defaults, breaking changes without migration policy, schema features unsupported by target clients, unstable identifiers, leaked internal fields, unbounded input, and error messages containing sensitive implementation details.
**Positive scenario:** a public API is defined contract-first and its schemas are verified against representative MCP clients before release.
**Negative scenario:** an API contract is derived accidentally from internal ORM/domain classes and silently breaks existing clients.

## Mandatory research
Identify exact Python, FastMCP, Pydantic, MCP SDK and JSON Schema versions. Read current official MCP specification, FastMCP and Pydantic documentation first; inspect exact-version examples/source/tests. Verify JSON Schema dialect/features actually emitted and accepted by the target MCP clients. Secondary sources are supplementary only.

## Contract-first
Before implementation define capability inventory, public names, descriptions, input/output models, nullability, defaults, constraints, error semantics and compatibility policy. Do not derive an API contract accidentally from internal ORM/domain classes.

## Pydantic v2
Use explicit typed models. Distinguish required, nullable and defaulted fields. Validate semantic constraints at the appropriate boundary. Prefer strictness where it prevents ambiguous input, but do not reject legitimate clients without evidence. Avoid `Any`, unbounded dictionaries and implicit coercion when they weaken a contract.

## MCP schemas
Understand what FastMCP exposes from Python annotations/Pydantic models and what the MCP protocol actually transmits. Never assume a Pydantic feature is interoperable merely because it serializes locally. Test generated schemas against representative MCP clients/validators.

## Serialization
Define canonical serialization for dates, UUIDs, enums, decimals, binary/content and discriminated unions. Avoid leaking ORM serialization, internal fields or secrets. Output models are explicit DTO contracts.

## Errors
Define stable application error categories and safe client-facing messages. Distinguish validation errors, authentication/authorization failures, not-found/conflict, dependency failure and internal errors. Never expose stack traces, SQL, credentials or provider internals. Error contracts must be tested.

## Compatibility
Classify changes: additive-compatible, behavior-compatible, potentially breaking and breaking. Adding optional response fields may be compatible for tolerant clients but must be verified. Renaming/removing fields, changing requiredness/type/enum semantics or changing tool/resource identity is potentially breaking. Do not rely on semantic version numbers alone.

## Versioning
Prefer stable capability identity and additive evolution over gratuitous `/v1`-style duplication. If a breaking contract is unavoidable, define explicit migration/deprecation policy and compatibility period. Tool/resource/prompt names are identifiers, not cosmetic labels.

## Defaults
Be deliberate about defaults. A default is part of behavior and therefore part of the contract. Never silently introduce a security-sensitive or side-effecting default.

## Pagination
Define opaque cursor shape, stable ordering, page size limits, empty-page behavior and invalid/expired cursor errors. Do not expose database offsets as a public cursor unless justified. Contract tests must cover concurrent mutations.

## Structured output
When using structured outputs, validate the result against the declared schema and business invariants. Schema-valid data is not automatically semantically valid. Treat model-generated structured data as untrusted.

## Documentation
Descriptions should explain purpose, inputs, outputs, side effects, constraints and important failure modes without duplicating business logic. Keep documentation synchronized with the executable contract.

## Testing
Generate and snapshot schemas where appropriate. Test valid/invalid inputs, nullability, defaults, enum evolution, serialization, errors, pagination, structured outputs and backward compatibility. Include protocol-level discovery and invocation tests rather than only Python unit tests.

## Architecture
MCP adapter contract models → application DTO/use case → domain objects → infrastructure DTOs. Keep contract schemas separate from domain and persistence schemas unless identity is intentionally shared and the coupling is proven safe.