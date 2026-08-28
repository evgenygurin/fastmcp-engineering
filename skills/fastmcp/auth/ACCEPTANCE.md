# FastMCP Auth Acceptance Criteria

## Research
- [ ] Exact FastMCP/Python versions identified.
- [ ] Complete target-version auth docs read.
- [ ] Relevant official auth examples inspected.
- [ ] Server and client auth flows researched.
- [ ] Source/tests inspected for ambiguous security semantics.
- [ ] MCP security specification/RFCs checked where applicable.
- [ ] Evidence ledger completed.

## Authentication
- [ ] Credential validation mechanism is explicit.
- [ ] Issuer/audience/signature validation is explicit where applicable.
- [ ] Principal identity is derived only from verified data.
- [ ] Token lifetime/refresh/revocation behavior is explicit.
- [ ] Secrets and tokens are never logged.

## Authorization
- [ ] Authentication and authorization are separate.
- [ ] Policy owner is explicit.
- [ ] Enforcement point is explicit.
- [ ] Default-deny behavior is verified.
- [ ] Scope/role/tenant boundaries are explicit.
- [ ] Application/domain layers do not depend directly on FastMCP token internals.

## OAuth / Deployment
- [ ] Discovery behavior is verified.
- [ ] Callback/redirect URLs are verified for actual mount topology.
- [ ] Client and server flows are both tested where applicable.
- [ ] PKCE/registration/CIMD/pre-registration behavior is verified where applicable.
- [ ] Reverse-proxy/public-URL assumptions are explicit.

## Verification
- [ ] Positive authentication tests pass.
- [ ] Negative/expiry tests pass.
- [ ] Authorization denial tests pass.
- [ ] Tenant/security-boundary tests pass where applicable.
- [ ] Secret-redaction tests pass where applicable.
- [ ] Client/server integration tests pass where applicable.
- [ ] Static quality checks pass.
- [ ] Architecture/security re-check passes.
- [ ] Verification evidence is reproducible.
