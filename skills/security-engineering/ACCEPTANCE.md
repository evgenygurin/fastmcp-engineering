# Security Engineering Acceptance Criteria

## Research
- [ ] Exact stack versions identified.
- [ ] Current MCP authorization/security specification verified.
- [ ] FastMCP authn/authz and transport security verified.
- [ ] PydanticAI tool/MCP/approval boundaries verified.
- [ ] OAuth/OIDC/token validation semantics verified from first-party sources.
- [ ] Threat model and evidence ledger completed.

## Architecture
- [ ] Authentication and authorization are separate.
- [ ] Authorization is deterministic and independent of model output.
- [ ] Tool risk classification exists.
- [ ] Least privilege is enforced at the application/tool boundary.
- [ ] OAuth issuer/resource/audience validation is explicit.
- [ ] Caller credentials are not blindly forwarded.
- [ ] Secrets are isolated from model context and logs.
- [ ] Tenant isolation is enforced below the agent layer.
- [ ] SSRF controls exist for network-fetch primitives.
- [ ] Destructive operations have appropriate approval/policy.
- [ ] Supply-chain policy is defined.

## Verification
- [ ] Authn failure tests pass.
- [ ] Issuer/audience/resource/token validation tests pass.
- [ ] Scope/role/tenant isolation tests pass.
- [ ] Tool authorization bypass tests pass.
- [ ] Malicious MCP content/tool result tests pass.
- [ ] SSRF and redirect tests pass.
- [ ] Secret leakage tests pass.
- [ ] Replay/duplicate side-effect tests pass.
- [ ] Destructive-operation approval tests pass.
- [ ] Dependency policy checks pass.
- [ ] Real OAuth/MCP/DB semantics are integration-tested where necessary.
- [ ] Static quality gates pass.
- [ ] Architecture/security re-check passes.
- [ ] Stops when security behavior cannot be established from evidence; rejects invented behavior and escalates to the user instead of guessing.
