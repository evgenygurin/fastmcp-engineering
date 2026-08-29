---
name: api-tool-engineering
description: Evidence-first design of production MCP tools, resources and prompts as stable public APIs.
---

# API / Tool Engineering

## Mission
Design MCP tools, resources and prompts as deliberate public contracts, not thin wrappers around database tables or internal methods.

## Mandatory research gate
Before implementation, read the repository architecture/security/testing/configuration/reliability skills and identify exact versions. Then read the current official MCP specification and FastMCP documentation/examples for the exact version, especially tools, resources, prompts, annotations, structured output, pagination, elicitation and error semantics. Inspect official source/tests when documentation is ambiguous. Research Pydantic/PydanticAI schema and validation behavior where used.

Create an evidence ledger and compatibility matrix. Do not rely on blog posts when primary documentation exists.

## Contract design
For every public capability define:
- stable name and semantic purpose;
- input schema and constraints;
- output schema/content type;
- errors and retryability;
- authorization policy;
- side effects and idempotency;
- pagination/filter/sort semantics where applicable;
- consistency guarantees;
- observability fields;
- compatibility/deprecation policy.

Names describe user-facing capabilities, not database tables or implementation classes.

## Tool granularity
One tool should represent one coherent capability with a bounded responsibility. Avoid both mega-tools with dozens of modes and one-tool-per-column CRUD noise. Split when authorization, transaction boundary, risk, latency or semantic responsibility differs.

## Schemas
Use explicit Pydantic models where they improve the contract. Constrain inputs; reject ambiguous values. Avoid exposing ORM models as public schemas. Keep internal/domain models separate from MCP wire schemas. Treat model-generated arguments as untrusted input and validate again at the application boundary.

## Structured output
Prefer typed structured output when clients can consume it reliably. Define backward-compatible evolution rules. Never rely on prose parsing for machine-critical data.

## Errors
Separate protocol errors from application/domain errors. Never leak stack traces, SQL, credentials or internal topology. Make errors actionable without exposing sensitive implementation details. Document whether callers may retry.

## Authorization
Authorization is deterministic and outside the LLM. Every side-effecting or tenant-sensitive tool must resolve identity, tenant and capability through the application security boundary. Tool descriptions/annotations are metadata, not access control.

## Side effects
Classify tools as read-only, reversible mutation, irreversible/consequential mutation. Require explicit idempotency/replay semantics for mutations. Do not rely on the agent to avoid duplicate calls.

## Resources
Use resources for addressable/read-oriented contextual data rather than disguising commands as resources. Define URI semantics, MIME/type behavior, freshness/consistency and access control. Avoid embedding authorization decisions in resource contents.

## Prompts
Treat prompts as versioned user-facing templates. Keep policy/instructions separate from untrusted resource data. Never assume prompt text is a security boundary.

## Pagination and large results
Never return unbounded collections. Define stable cursors or documented pagination semantics. Ensure ordering is deterministic and pagination remains correct under concurrent writes according to the documented consistency model.

## Backward compatibility
Maintain a contract matrix for clients and server versions. Add optional fields rather than silently changing meaning. Deprecate deliberately. Removing/renaming a public tool, resource URI or required input is a breaking change unless the protocol/version policy explicitly permits it.

## KISS / YAGNI
Do not add pagination, caching, filtering, versioning, generic CRUD abstractions or elaborate schema machinery without a demonstrated contract need. Complexity must have a concrete reason.

## Verification
Test schemas, protocol serialization, authorization, errors, idempotency, pagination, compatibility and dangerous side effects. Use official FastMCP/MCP testing mechanisms where available plus application integration tests. Test adversarial/invalid inputs and large result boundaries.

## Rejection criteria
Reject if a public tool bypasses application authorization, exposes ORM/domain internals, has unbounded output, conflates protocol/application errors, permits unsafe replay, uses descriptions as security controls, has ambiguous semantics, or introduces abstraction without evidence.

## Deliverables
Capability inventory, contract matrix, schema definitions, authorization/risk classification, compatibility matrix, pagination strategy, error taxonomy, evidence ledger, implementation, contract tests and verification report.