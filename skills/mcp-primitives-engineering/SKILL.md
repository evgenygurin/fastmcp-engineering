---
name: mcp-primitives-engineering
description: Evidence-first engineering rules for MCP tools, resources, prompts and advanced protocol primitives in FastMCP.
---

# MCP Primitives Engineering

## Mission
Choose and implement the correct MCP primitive for each capability while preserving protocol semantics, clean architecture, security, compatibility and testability.

## Trigger / Когда применять

**Scope / When to use:** MCP tools, resources, prompts and advanced protocol primitives in FastMCP.
**Trigger:** choosing or implementing an MCP primitive for a capability — tool, resource, prompt, or an advanced protocol feature.
**Upstream / Prerequisite:** identified exact MCP/FastMCP versions; evidence recorded with source, version/date, claim and confidence.
**Mission / Goal:** choose and implement the correct MCP primitive for each capability while preserving protocol semantics, clean architecture, security, compatibility and testability.
**Research / Evidence:** identify exact MCP/FastMCP versions; read the current official MCP specification/changelog and relevant exact-version FastMCP docs, examples, source and tests; research Pydantic/PydanticAI and transport/runtime semantics where relevant; re-check version-sensitive documentation before completion.
**Decision / Selection rules:** use a tool for an executable operation, a resource for addressable/readable data, a prompt for reusable templates; document owner, audience, side effects, authorization, latency, cacheability, mutability, identity/addressing, error semantics and lifecycle for every primitive; verify exact protocol/FastMCP support for advanced features; do not implement a custom substitute for a standard MCP primitive unless research proves the standard mechanism cannot satisfy the requirement.
**Version / Compatibility:** identify exact MCP/FastMCP versions.

## Deliverables

**Deliverables / Artifacts:** primitive-selection matrix; public contract inventory; architecture/data-flow diagram; security classification; schemas; compatibility impact; test matrix; evidence ledger; rejected alternatives; verification report.
**Verification / Testing:** test discovery/listing as well as invocation; for each primitive test valid/invalid schemas, authorization, errors, structured output, cancellation, pagination and relevant capability negotiation; use real MCP integration tests for protocol semantics that mocks cannot prove; test old-client compatibility when the public contract changes.
**Failure / Stop conditions:** reject ambiguous primitive choice, fat handlers, business logic in MCP decorators, model-controlled authorization, custom protocol reinvention without evidence, unstable pagination contracts, undocumented advanced features, leaked internal errors, and untested public contract changes.
**Positive scenario:** the correct MCP primitive is chosen and passes discovery, invocation and integration tests.
**Negative scenario:** an ambiguous primitive choice hides domain operations in resources or reinvents a standard protocol primitive without evidence.

## Mandatory research
Before implementation identify exact MCP/FastMCP versions. Read the current official MCP specification/changelog and relevant exact-version FastMCP docs, examples, source and tests. Research Pydantic/PydanticAI and transport/runtime semantics where relevant. Record evidence with source, version/date, claim and confidence. Re-check version-sensitive documentation before completion.

## Primitive selection
Use a **tool** for an executable operation/action whose behavior is initiated by the model/client. Use a **resource** for addressable/readable contextual data. Use a **prompt** for reusable user/model-facing prompt templates or workflows. Do not expose domain operations as resources merely to avoid tool design, and do not turn static/contextual data into tools without a semantic reason.

For every primitive document owner, audience, side effects, authorization, latency, cacheability, mutability, identity/addressing, error semantics and lifecycle.

## Tools
Design narrow, cohesive tools with explicit typed input/output contracts. Keep handlers thin and delegate to application use cases. Validate input at the boundary. Model business invariants in the domain/application layer. Return structured output when the contract benefits from machine-readable results. Treat tool names, descriptions, schemas, annotations and output shapes as public API.

Classify side effects: read-only, reversible mutation, irreversible/destructive, external side effect. Apply authorization and confirmation policy outside model-generated intent. Never infer authorization from tool annotations or descriptions.

## Resources
Use stable, meaningful URIs/URI templates. Define MIME/media semantics where applicable, encoding and size limits. Separate resource identity from retrieval implementation. Avoid embedding credentials, secrets or authorization decisions in resource URIs. For dynamic resources define freshness/cache semantics explicitly. For subscriptions or updates, verify the exact MCP/FastMCP support and lifecycle semantics before use.

## Prompts
Prompts are user/model-facing templates, not authorization or application business logic. Give prompts stable names and typed arguments where supported. Keep policy and security decisions outside prompt text. Do not duplicate a complex application workflow inside prompt templates.

## Advanced primitives
Before using any advanced feature, verify exact current protocol/FastMCP support and client interoperability. Research and test as applicable:
- resource templates;
- resource subscriptions;
- pagination;
- completion/autocomplete;
- elicitation;
- progress notifications;
- cancellation;
- task/deferred execution semantics;
- sampling;
- structured content/output;
- annotations and hints.

Do not implement a custom substitute for a standard MCP primitive unless the research package proves the standard mechanism cannot satisfy the requirement.

## Pagination
Pagination is a contract, not an implementation detail. Define cursor opacity, stability, ordering, limits, expiration and behavior under concurrent mutations. Never expose database primary keys as cursors unless explicitly designed and safe.

## Progress/cancellation
Progress is observational; it must not be treated as completion. Cancellation must propagate to underlying work and release resources. Long-running durable work belongs in the async/durable-job architecture rather than being hidden inside a request lifecycle.

## Errors
Distinguish protocol errors from application/domain failures. Do not leak internal exception messages, SQL, credentials or stack traces. Error responses must be stable enough for supported clients and documented where machine consumption is expected.

## Architecture
MCP layer: protocol translation, schemas, context and authorization integration.
Application layer: use cases and orchestration.
Domain layer: business rules/invariants.
Infrastructure: database, HTTP, LLM, filesystem, queues.
MCP primitives must not become repositories, service locators or god objects.

## Testing
Test discovery/listing as well as invocation. For each primitive test valid/invalid schemas, authorization, errors, structured output, cancellation, pagination and relevant capability negotiation. Use real MCP integration tests for protocol semantics that mocks cannot prove. Test old-client compatibility when the public contract changes.
