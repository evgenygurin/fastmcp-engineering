---
name: security-threat-modeling
description: Security engineering and threat modeling for production FastMCP systems, covering MCP boundaries, authn/authz, agents, tools, resources, databases, external dependencies and supply chain.
---

# Security / Threat Modeling

## Mission
Security is an architectural property. Before implementation, establish trust boundaries, assets, actors, capabilities, attack paths and security invariants. Never begin with an authentication library before understanding the threat model.

## Mandatory research gate
1. Read AGENTS.md and repository security/engineering contracts.
2. Identify exact Python, FastMCP, MCP, PydanticAI, Pydantic, SQLAlchemy, ASGI/server and auth dependency versions.
3. Read the official MCP specification and relevant authorization/security documentation.
4. Read official FastMCP security/auth documentation and llms material.
5. Read official PydanticAI security-relevant documentation.
6. Read official framework/dependency security documentation.
7. Inspect relevant official examples and source/tests.
8. Consult authoritative OAuth/IETF, OWASP and NIST guidance where relevant.
9. Record evidence before implementation.

## Threat-model first
Produce before coding: system/data-flow diagram, trust boundaries, assets/data classification, actors/privileges, entry points, threat scenarios, abuse cases, security invariants, mitigations, residual risk and verification plan.

## MCP security
Explicitly evaluate authentication/authorization, OAuth 2.1 or the exact relevant authorization profile, issuer/audience/scope validation, token lifecycle, confused deputy, token passthrough, tool/resource/prompt authorization, capability exposure, transport security, replay/request integrity, malicious or untrusted MCP servers/clients and cross-tenant access. Do not invent protocol requirements; verify each claim against the exact MCP version.

## Agent/tool security
Treat model instructions, MCP tool descriptions, tool results, resources and external content as untrusted. Evaluate prompt injection, indirect prompt injection, tool poisoning, malicious tool output and data exfiltration. Model output is never an authorization decision.

Authorization must be deterministic, policy-driven and independent of model-generated arguments for security-sensitive decisions. Validate tool arguments structurally and enforce business authorization in application/domain layers.

## Network/data security
Evaluate SSRF, DNS rebinding, unrestricted egress, URL validation, path traversal, file access, command execution, unsafe deserialization, SQL injection and oversized payloads. Use allowlists and capability-scoped clients where practical.

Protect PII and secrets. Apply data minimization, retention and redaction. Never place credentials in prompts, source code, schemas or logs.

## Database/tenancy
Use least-privilege DB credentials. Define tenant identity propagation. If RLS is used, verify policy enforcement and failure modes. Application authorization and DB isolation should provide defense in depth, not contradictory policy layers.

## Supply chain
Pin/lock dependencies according to repository policy. Review transitive dependencies, provenance, package integrity, SBOM, image base, OS packages and runtime privileges. Do not blindly copy security-sensitive code from secondary sources.

## Resilience/security limits
Define authentication rate limits, payload limits, concurrency limits, tool timeouts, outbound network limits and resource budgets. Ensure limits cannot be bypassed through alternate tool/resource paths.

## Testing
Security tests must cover authentication failures, authorization bypass, tenant isolation, confused deputy, replay, malformed tokens, tool poisoning, prompt injection fixtures, SSRF, path traversal, oversized input, data exfiltration, secret leakage and database access boundaries. Prefer deterministic regression fixtures.

## Rejection criteria
Reject if trust boundaries are undefined, authorization depends on LLM output, tokens are accepted without exact validation requirements, untrusted tool content is treated as trusted instructions, credentials cross inappropriate boundaries, network egress is unrestricted without justification, or critical threats lack verification.

## Deliverables
Threat model, security architecture, authorization matrix, trust-boundary map, attack-path register, security controls, implementation, regression tests, supply-chain/security checklist, residual-risk register and architecture re-check.