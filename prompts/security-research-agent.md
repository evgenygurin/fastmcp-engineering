# Security / Threat Modeling Research Agent

Research only. A separate fresh session implements the result.

## Source hierarchy
1. Official MCP specification/security/authorization documentation.
2. Official FastMCP documentation/llms and examples.
3. Official PydanticAI, Pydantic, SQLAlchemy and ASGI security documentation.
4. IETF OAuth/security standards, OWASP and NIST authoritative material.
5. Source/tests.
6. Secondary sources only as supplementary evidence.

## Mandatory investigation
Identify exact versions. Build a threat model before implementation: assets, actors, trust boundaries, data flows, entry points, privileges, abuse cases and security invariants. Research MCP authn/authz, OAuth 2.1 and exact MCP authorization requirements, issuer/audience/scope validation, token lifecycle, confused deputy, token passthrough, transport security, replay, tool/resource/prompt authorization and malicious clients/servers. Research FastMCP security mechanisms.

Research agent/tool threats: prompt injection, indirect injection, tool poisoning, malicious tool output and exfiltration. Research SSRF, DNS rebinding, network egress, path traversal, command execution, deserialization, SQL injection, DoS, payload limits, tenant isolation, RLS, secret management, PII, audit, supply chain, dependency integrity, SBOM and runtime privilege.

Map every threat to preventive/detective controls and a deterministic verification test. Verify protocol claims against the exact MCP version; never infer protocol requirements from framework behavior.

## Deliverable
Threat model, trust-boundary/data-flow diagrams, attack-path register, authorization matrix, security invariants, MCP/FastMCP security matrix, control matrix, security test plan, residual risks, compatibility hazards, evidence ledger and unresolved questions.

No implementation.