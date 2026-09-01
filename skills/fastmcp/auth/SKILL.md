---
name: fastmcp-auth
description: Design FastMCP authentication and authorization as explicit security boundaries — use for OAuth, JWT, and MCP auth implementation.
---

# FastMCP Authentication / Authorization

## Mission

Design authentication and authorization as explicit security boundaries. Authentication establishes who/what is calling; authorization decides what that principal may do. Never collapse identity, credential validation, policy, and application business rules into one abstraction.

## Trigger / Когда применять

**Scope / When to use:** FastMCP authentication and authorization as explicit security boundaries — OAuth, JWT, and MCP auth implementation.
**Trigger:** designing or changing authentication or authorization boundaries, token/secret handling, or client/server auth flows.
**Upstream / Prerequisite:** `AGENTS.md` and all engineering contracts read; identified exact FastMCP and Python versions; an evidence ledger recorded before coding.
**Mission / Goal:** design authentication and authorization as explicit security boundaries; never collapse identity, credential validation, policy, and application business rules into one abstraction.
**Research / Evidence:** read complete target-version FastMCP authentication documentation; inspect all relevant official PrefectHQ/fastmcp auth examples; inspect FastMCP source/tests when semantics are ambiguous; read applicable MCP authentication/security specification material; read first-party dependency/security-library documentation; no remembered OAuth/JWT/API behavior is acceptable evidence.
**Decision / Selection rules:** select only mechanisms verified for the target release; authentication is not authorization — define principal model, permissions, policy enforcement, default-deny and audit; prefer explicit application authorization ports/policies; validate security-critical claims and never treat unverified claims as trusted identity; research both client and server sides.
**Version / Compatibility:** identify exact FastMCP and Python versions; select only mechanisms verified for the target release.

## Deliverables

**Deliverables / Artifacts:** target-version research; OAuth/protocol flow diagrams; Principal and authorization model; trust-boundary map; implementation; negative security tests; client/server integration verification; security review; architecture re-check; reproducible evidence ledger.
**Verification / Testing:** use documented FastMCP client/in-process testing seams; test authentication and authorization separately with positive, negative, boundary, expiry and policy cases; never use real third-party credentials in automated tests; test OAuth discovery, redirect construction, PKCE/registration, refresh and protected requests with deterministic providers/mocks.
**Failure / Stop conditions:** reject if identity is inferred from unverified input, authorization is fail-open, authentication and authorization are conflated, secrets are logged/stored insecurely, token validation is guessed, mounted OAuth discovery is unverified, or application/domain layers directly depend on FastMCP auth internals without an adapter boundary.
**Positive scenario:** authentication and authorization are separated as explicit boundaries and pass negative security tests.
**Negative scenario:** authorization is fail-open or identity is inferred from unverified input.

## Mandatory research gate

Before implementation:
1. Read `AGENTS.md` and all engineering contracts.
2. Identify exact FastMCP and Python versions.
3. Read complete target-version FastMCP authentication documentation.
4. Inspect all relevant official PrefectHQ/fastmcp auth examples.
5. Inspect FastMCP source/tests when semantics are ambiguous.
6. Read applicable MCP authentication/security specification material.
7. Read first-party dependency/security-library documentation for components actually used.
8. Record an evidence ledger before coding.

No remembered OAuth/JWT/API behavior is acceptable evidence.

## Security model

Document the complete trust flow:

```text
Client / Agent
      |
      v
Authentication boundary
      |
      | verified principal / claims
      v
Authorization boundary
      |
      v
FastMCP component
      |
      v
Application use case
      |
      v
Domain / infrastructure
```

Explicitly identify issuer, audience, signing/validation mechanism, token source, credential lifetime, scopes/claims, principal identity, trust boundaries, and policy owner.

## Authentication mechanisms

Select only mechanisms verified for the target release. Investigate where applicable: bearer/static tokens, JWT validation, OAuth 2.1 Authorization Code + PKCE, client credentials, authorization-server metadata, protected-resource metadata, Dynamic Client Registration, CIMD, pre-registered clients, provider integrations/OAuth proxy patterns, mounted/path-prefixed servers, client OAuth handling, token storage and refresh.

Do not assume every OAuth provider satisfies MCP discovery/registration requirements. Provider-specific adapters may be required.

## Authorization

Authentication is not authorization. Define principal model, permissions/scopes/roles, resource/tool-level policy, tenant boundaries, policy enforcement point, default-deny behavior, error semantics and audit requirements.

Prefer explicit application authorization ports/policies rather than scattering role checks through MCP handlers.

## Token and secret handling

Never log access tokens, refresh tokens, client secrets, private keys, authorization codes, or full Authorization headers. Redact credentials in telemetry and errors.

Validate security-critical claims according to protocol/provider requirements. Never treat unverified claims as trusted identity. Define credential lifetime and refresh/revocation behavior.

## MCP-specific boundary

Remote MCP servers should be authenticated according to target-version guidance. HTTP transport, OAuth discovery, mounted servers, stateless mode, reverse proxies, and public URLs can affect authentication behavior and metadata endpoints. For mounted authenticated servers, verify path-aware discovery and callback URLs for the exact deployment topology.

## Client/server symmetry

Research both sides: server credential validation and protected-resource metadata; client OAuth discovery, browser flow, PKCE, registration/CIMD, pre-registered credentials, token caching/refresh, transport auth headers, and expired/invalid credential handling.

A server design is incomplete if its intended client cannot perform the required authentication flow.

## Application architecture

MCP handlers should adapt the authenticated principal into an application-level identity/authorization request. Domain logic must not import FastMCP authentication internals.

```text
FastMCP auth -> verified Principal -> AuthorizationPort -> Application use case -> Domain
```

## Security failure modes

Explicitly test: missing/malformed credentials, expired tokens, invalid issuer/audience/signature, insufficient scope, confused deputy, tenant breakout, privilege escalation, token leakage, callback mismatch, discovery mismatch, path-prefix mistakes, insecure secret configuration, fail-open authorization, and stale identity after refresh.

## Testing

Use documented FastMCP client/in-process testing seams. Test authentication and authorization separately with positive, negative, boundary, expiry and policy cases. Never use real third-party credentials in automated tests. For OAuth, test discovery, redirect construction, PKCE/registration where supported, refresh, and protected requests with deterministic providers/mocks.