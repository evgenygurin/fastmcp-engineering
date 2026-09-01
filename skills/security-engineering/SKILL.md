---
name: security-engineering
description: Evidence-first security engineering for production MCP/FastMCP and PydanticAI systems, covering authentication, authorization, OAuth, trust boundaries, tool security, prompt injection, SSRF, secrets, tenancy and supply-chain risk.
---

# Security Engineering

## Mission
Treat MCP as a security boundary between untrusted model-driven requests, remote tools, identities, data and side effects. Security controls must be deterministic, layered and independently enforceable; prompts are never a security mechanism.

## Trigger / Когда применять

**Scope / When to use:** security engineering for production MCP/FastMCP and PydanticAI systems, covering authentication, authorization, OAuth, trust boundaries, tool security, prompt injection, SSRF, secrets, tenancy and supply-chain risk.
**Trigger:** designing or changing authentication, authorization, OAuth/token validation, trust boundaries, tool security, SSRF protection, secrets handling, tenancy, or supply-chain controls.
**Upstream / Prerequisite:** repository security, architecture, configuration and testing contracts read; identified exact versions; a threat model, evidence ledger and unresolved-risk register produced before implementation.
**Mission / Goal:** treat MCP as a security boundary between untrusted model-driven requests, remote tools, identities, data and side effects; security controls must be deterministic, layered and independently enforceable; prompts are never a security mechanism.
**Research / Evidence:** read current official MCP specification, authorization/security guidance, SEPs and migration notes; read official FastMCP authentication/authorization/security documentation and examples for the exact version; read official PydanticAI security/tool/MCP documentation; read OAuth 2.1/OIDC/JWT guidance relevant to the identity provider and token library; inspect official source/tests for security-sensitive behavior; research dependency and supply-chain security from authoritative sources.
**Decision / Selection rules:** keep authentication (identity), authorization (permission) and application/domain policy (operation enforcement) separate; validate issuer, audience/resource, signature, expiry/not-before, token type and scopes according to the exact protocol; enforce least privilege at the tool/application boundary; assign every tool a risk class; treat tool descriptions, arguments and results as untrusted; apply SSRF restrictions to URL-fetching features; keep credentials outside model-visible context; enforce tenant isolation below the agent/tool layer; pin and audit dependencies; record security-relevant audit decisions.
**Version / Compatibility:** identify exact FastMCP, MCP SDK, PydanticAI, Python, auth-library, SQLAlchemy/DB and deployment versions; MCP authorization changed materially in 2026 (2026-07-28 introduced issuer validation and issuer-bound client credentials) — security implementation must be version-pinned and migration-aware.

## Deliverables

**Deliverables / Artifacts:** threat model, trust-boundary diagram, authn/authz design, OAuth/token validation matrix, tool risk classification, SSRF policy, secret-handling policy, tenant isolation strategy, supply-chain policy, security test matrix, implementation, verification report and residual-risk register.
**Verification / Testing:** mandatory tests include authentication failures, issuer/audience failures, expired/replayed tokens, scope/role violations, tenant isolation, tool authorization bypass, prompt-injection resistance at the application boundary, malicious tool metadata/results, SSRF, secret leakage, unsafe redirects, destructive-operation approval, duplicate side effects and dependency policy checks; use deterministic fakes for most tests and controlled integration tests for actual OAuth/MCP/DB semantics; add regression tests for every discovered vulnerability.
**Failure / Stop conditions:** reject if authorization depends on prompts, tool descriptions or model decisions; tokens are accepted without issuer/audience/resource validation; caller credentials are blindly forwarded; SSRF-capable fetches lack restrictions; secrets enter model-visible context/logs; tenant isolation exists only in the agent layer; mutating tools lack deterministic policy; or version-sensitive MCP auth behavior was not checked against official sources.
**Positive scenario:** an MCP server enforces deterministic, layered security controls verified by the security test matrix.
**Negative scenario:** authorization depends on prompts or model decisions, or tokens are accepted without issuer/audience validation.

## Mandatory research gate
1. Read repository security, architecture, configuration and testing contracts.
2. Identify exact FastMCP, MCP SDK, PydanticAI, Python, auth-library, SQLAlchemy/DB and deployment versions.
3. Read current official MCP specification, authorization/security guidance, SEPs and migration notes.
4. Read official FastMCP authentication/authorization/security documentation and examples for the exact version.
5. Read official PydanticAI security/tool/MCP documentation and examples.
6. Read OAuth 2.1 / OIDC / JWT guidance relevant to the chosen identity provider and token library.
7. Inspect official source/tests for security-sensitive or ambiguous behavior.
8. Research dependency and supply-chain security using authoritative sources.
9. Produce a threat model, evidence ledger and unresolved-risk register before implementation.

Never rely on memory for current MCP authorization semantics. The MCP specification changed materially in 2026: the 2026-07-28 release introduced authorization hardening including issuer validation and issuer-bound client credentials and moved toward Client ID Metadata Documents; these must be checked against the exact target SDK/spec version.

## Security architecture

```text
Untrusted Client / LLM
 ↓
Transport / MCP AuthN
 ↓
Identity + Token Validation
 ↓
Authorization Policy
 ↓
MCP Tool Boundary
 ↓
Application Use Case
 ↓
Domain Policy
 ↓
Ports / Infrastructure
```

Authentication establishes identity. Authorization establishes permission. Application/domain policy enforces the actual operation. Never collapse these into one prompt, decorator or middleware check.

## OAuth / token validation

Validate issuer, audience/resource, signature, expiry/not-before, token type and required scopes/claims according to the exact protocol and identity provider. Bind credentials to the correct authorization server/resource. Do not accept a valid JWT merely because its signature verifies.

Do not forward caller tokens blindly to downstream APIs. Use explicit token exchange/downstream credentials or a server-owned credential when appropriate. The current MCP security direction explicitly hardens issuer validation and issuer-bound credentials.

## Authorization

Enforce least privilege at the tool/application boundary. Authorization must consider authenticated principal, tenant, resource ownership, operation, sensitivity and requested side effect. Use capability/policy objects or a dedicated policy layer when complexity warrants it.

A model selecting a tool is not authorization. A tool annotation describing risk is not authorization. An MCP server must enforce policy independently of model behavior.

## MCP-specific threats

Threat-model at minimum:
- prompt injection and indirect prompt injection;
- tool poisoning / malicious tool descriptions;
- malicious or compromised remote MCP servers;
- confused deputy and token forwarding;
- SSRF through URLs, metadata, OAuth discovery or fetch tools;
- credential exfiltration;
- excessive tool exposure;
- cross-tenant data access;
- unsafe destructive operations;
- malicious resources/prompts/results;
- replay and duplicate side effects;
- dependency/supply-chain compromise.

MCP authorization is evolving rapidly; the 2026-07-28 specification also introduced a stateless core and header-based routing, while deprecating older mechanisms. Security implementation must therefore be version-pinned and migration-aware.

## Tool security

Assign every tool a risk class: read-only, sensitive-read, mutating, destructive or privileged. Tool metadata/annotations may inform UX and policy but cannot replace enforcement. Require explicit approval or stronger authorization for consequential operations where appropriate.

Validate inputs at the boundary with strict typed schemas. Validate outputs before trusting them downstream. Treat tool descriptions, arguments and results as untrusted data.

## SSRF

Any feature that fetches a user/model/tool-supplied URL is a security-sensitive network primitive. Apply scheme/host/IP restrictions, DNS rebinding defenses, redirect policy, size/time limits and private-network blocking as appropriate to the deployment. OAuth/client-metadata discovery can itself create SSRF risk; the MCP project explicitly calls out blocking internal network access, timeouts and size limits for such fetches.

## Secrets

Keep credentials outside model-visible context and MCP messages whenever possible. Use server-side secret stores and scoped credentials. Never log tokens, API keys, authorization codes, cookies or raw secret-bearing payloads. Prefer secure browser-based credential acquisition where the protocol provides it; MCP's URL-mode elicitation was designed specifically to avoid sending credentials through the client.

## Tenancy / data isolation

Tenant isolation must be enforced below the agent/tool layer. Where appropriate, combine application authorization with database constraints/RLS. Never rely solely on a tenant ID supplied by the model or client. Test horizontal and vertical privilege escalation explicitly.

## Local servers / deployment

Treat local MCP servers as privileged software. Minimize filesystem/network/process permissions, validate command/URL inputs, pin dependencies and isolate processes where practical. Remote and local deployment models require different threat assumptions; record them explicitly.

## Supply chain

Pin and audit dependencies, verify trusted package sources, minimize dependency surface, review transitive dependencies and run automated vulnerability/license/policy checks. MCP server catalogs/registries are discovery mechanisms, not trust authorities by default; define provenance and allowlisting policy.

## Logging / audit

Record security-relevant decisions with correlation IDs: principal, tenant, server/tool, authorization outcome, policy version and operation result. Redact secrets and sensitive data. Distinguish audit records from ordinary debug logs and protect audit integrity/access.

## Security testing

Mandatory tests include authentication failures, issuer/audience failures, expired/replayed tokens, scope/role violations, tenant isolation, tool authorization bypass, prompt-injection resistance at the application boundary, malicious tool metadata/results, SSRF, secret leakage, unsafe redirects, destructive-operation approval, duplicate side effects and dependency policy checks.

Use deterministic fakes for most tests and controlled integration tests for actual OAuth/MCP/DB semantics. Add regression tests for every discovered vulnerability.
