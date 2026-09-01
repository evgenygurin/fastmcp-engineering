---
name: api-lifecycle-versioning
description: Evidence-first API lifecycle, schema evolution and compatibility engineering for FastMCP/MCP servers.
---

# API Lifecycle / Versioning & Compatibility

## Mission
Design MCP APIs that can evolve without silently breaking clients, agents, integrations, persisted data, or protocol interoperability.

## Trigger / Когда применять

**Scope / When to use:** MCP API lifecycle, schema evolution, and compatibility across protocol, transport, discovery, schemas, errors, auth, persistence, and dependencies.
**Trigger:** designing or changing an MCP API surface, schema, protocol negotiation, deprecation, or migration policy.
**Upstream / Prerequisite:** identified exact versions; a research evidence ledger with source/version/date/claim/confidence; defined compatibility dimensions.
**Mission / Goal:** design MCP APIs that can evolve without silently breaking clients, agents, integrations, persisted data, or protocol interoperability.
**Research / Evidence:** read, in order, the current MCP specification and changelog; official FastMCP documentation/examples/source/tests for the exact version; Pydantic/PydanticAI documentation; serialization/schema dependencies; and the repository compatibility policy; re-check documentation immediately before implementation and verification.
**Decision / Selection rules:** prefer additive changes (optional inputs with safe defaults, additive output fields, new tools/resources, explicit deprecation); version only externally observable contracts; choose the least complex versioning strategy that solves the compatibility requirement.
**Version / Compatibility:** identify exact versions; protocol version negotiation follows the actual MCP specification; never invent custom protocol semantics when a standard capability exists.

## Deliverables

**Deliverables / Artifacts:** compatibility matrix; public-contract inventory; versioning decision record; schema evolution rules; deprecation/removal policy; migration plan; golden fixtures; contract tests; evidence ledger; unresolved questions; final verification report.
**Verification / Testing:** maintain golden request/response/error fixtures and compatibility tests for supported client versions; test discovery and invocation; verify schema evolution, capability negotiation, protocol errors, auth failures and deprecation behavior.
**Failure / Stop conditions:** reject silent breaking changes, undocumented schema changes, protocol-version assumptions unsupported by evidence, custom semantics duplicating MCP features, deprecations without migration paths, and compatibility claims without tests.
**Positive scenario:** an MCP API evolves additively and every supported client version passes the golden compatibility fixtures.
**Negative scenario:** a breaking change is shipped silently without a migration path and existing clients break.

## Mandatory research gate
Before implementation identify exact versions and read, in order: current MCP specification and changelog; official FastMCP documentation/examples/source/tests for the exact version; relevant Pydantic/PydanticAI documentation; serialization/schema dependencies; repository compatibility policy. Secondary articles are supplementary only.

Produce an evidence ledger with source, version/date, claim, applicability and confidence. Re-check documentation immediately before implementation and verification.

## Compatibility dimensions
Analyze independently:
- MCP protocol/version compatibility;
- transport compatibility;
- tool/resource/prompt discovery compatibility;
- input schema compatibility;
- output/structured-content compatibility;
- error compatibility;
- authentication/authorization compatibility;
- persistence/event schema compatibility;
- dependency/runtime compatibility.

Never call an API "backward compatible" without defining the client population and compatibility dimension.

## Evolution rules
Prefer additive changes: optional inputs with safe defaults, additive output fields where clients tolerate unknown fields, new tools/resources for incompatible semantics, and explicit deprecation before removal. Treat renaming, changing meaning, tightening validation, changing defaults, enum removal, pagination semantics, auth requirements, and error shapes as potentially breaking.

Do not version every internal class or database table. Version externally observable contracts where compatibility requires it.

## MCP-specific contract
Protocol version negotiation follows the actual MCP specification, not application assumptions. Do not invent custom protocol semantics when a standard capability exists. Distinguish protocol version from application/API version. Capabilities must be negotiated and feature availability must be explicit.

Tools/resources/prompts are public contracts. Names, descriptions, schemas and annotations are compatibility surfaces. Never rely on prompt wording as a stable machine contract.

## Schema evolution
Pydantic models are implementation contracts unless exposed through MCP. For exposed schemas define required/optional semantics, defaults, nullability, unknown-field behavior, enums, formats and bounds. Validate both old-client requests and new-server behavior with contract fixtures.

## Deprecation
Every deprecation needs owner, reason, replacement, first-deprecated version/date, migration guidance, telemetry/usage measurement where available, and removal criteria. Do not remove based only on source-code search if external consumers exist.

## Versioning strategy
Choose the least complex strategy that solves the compatibility requirement: unversioned additive evolution, explicit protocol negotiation, namespaced/new tool, or separately versioned API surface. Reject URL/path/version headers copied from HTTP conventions unless the actual transport/application boundary requires them.

## Contract testing
Maintain golden request/response/error fixtures and compatibility tests for supported client versions. Test discovery as well as invocation. Verify schema evolution, capability negotiation, protocol errors, auth failures and deprecation behavior.

## Migration
For breaking changes define a staged migration: introduce replacement → support old and new → communicate/measure → migrate consumers → remove old contract only after explicit criteria. Data migrations must use the database skill's expand/contract rules and must not be coupled to an MCP client rollout without justification.

