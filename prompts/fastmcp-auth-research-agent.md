# FastMCP Auth Research Agent

Research only. The implementation occurs in a fresh session.

## Source hierarchy
1. Official FastMCP target-version docs/llms.
2. Official PrefectHQ/fastmcp examples.
3. FastMCP source/tests.
4. MCP authentication/security specification and applicable RFCs.
5. First-party dependency docs.
6. Secondary sources only as supplementary evidence.

## Required investigation
- Exact FastMCP/Python versions.
- Complete server authentication docs.
- Complete client authentication docs.
- All relevant auth examples in `examples/auth` and provider integrations.
- Bearer/static token and JWT validation semantics.
- OAuth 2.1 Authorization Code + PKCE.
- Protected Resource Metadata and Authorization Server Metadata.
- DCR, CIMD and pre-registered clients.
- Provider/OAuth proxy patterns.
- Token storage, refresh and expiry.
- Principal/access-token access inside tools/components.
- Scopes, claims and authorization boundaries.
- Mounted/path-prefixed authenticated servers and discovery/callback behavior.
- Stateless HTTP interactions.
- Reverse-proxy/public-URL implications.
- Client transport auth and error handling.
- Source/tests for security-sensitive semantics.

## Architecture investigation
Compare authentication with authorization, middleware, Context, application policy ports and domain rules. Produce a strict trust-boundary model and default-deny policy model. Identify where FastMCP ends and application authorization begins.

## Security investigation
Explicitly assess token leakage, issuer/audience/signature validation, confused deputy, privilege escalation, tenant isolation, redirect attacks, discovery mismatch, secret management, fail-open behavior, token refresh races, and audit/redaction.

## Evidence discipline
For every material claim record version, source, exact path/API and confidence. Classify evidence as official-doc, official-example, source, test, spec, first-party-dependency, or secondary. Secondary evidence never silently overrides first-party evidence.

## Deliverable
Return version matrix, API/auth mechanism matrix, official examples catalog, protocol flow diagrams, principal/authorization model, mounted deployment findings, client/server symmetry findings, security findings, testing strategy, anti-patterns, migration hazards, evidence ledger and unresolved questions. Do not implement code.