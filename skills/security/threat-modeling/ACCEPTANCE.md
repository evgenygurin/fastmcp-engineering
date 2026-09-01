# Security / Threat Modeling Acceptance Criteria

## Research
- [ ] Exact dependency/protocol versions identified.
- [ ] MCP security/authorization specification read.
- [ ] Official FastMCP security/auth docs and examples read.
- [ ] Relevant PydanticAI/Pydantic/SQLAlchemy/server security docs read.
- [ ] Authoritative OAuth/OWASP/NIST material checked where relevant.
- [ ] Source/tests inspected for ambiguity.
- [ ] Evidence ledger completed.

## Threat model
- [ ] Assets and data classification documented.
- [ ] Actors and privileges documented.
- [ ] Trust boundaries documented.
- [ ] Data flows documented.
- [ ] Entry points documented.
- [ ] Abuse cases and attack paths documented.
- [ ] Security invariants documented.
- [ ] Residual risks documented.

## Controls
- [ ] Authentication and token validation are explicit.
- [ ] Authorization matrix is explicit.
- [ ] Tool/resource/prompt access is policy-controlled.
- [ ] Model output cannot authorize access.
- [ ] External MCP content is untrusted.
- [ ] Tenant isolation is enforced.
- [ ] Network egress is bounded.
- [ ] Payload/resource limits are bounded.
- [ ] Secrets use secure configuration and never enter prompts/logs.
- [ ] Database privileges are least-privilege.
- [ ] Supply-chain controls are defined.

## Verification
- [ ] Authentication failure tests pass.
- [ ] Authorization bypass tests pass.
- [ ] Tenant isolation tests pass.
- [ ] Prompt-injection/tool-poisoning fixtures pass.
- [ ] SSRF/path traversal/resource-exhaustion tests pass where applicable.
- [ ] Secret-leakage tests pass.
- [ ] Security regression suite passes.
- [ ] Static/security tooling passes.
- [ ] Architecture/security re-check passes.
- [ ] Stops when threat-model behavior cannot be established from evidence; rejects invented behavior and escalates to the user instead of guessing.
