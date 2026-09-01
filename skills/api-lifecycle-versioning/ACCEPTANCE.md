# API Lifecycle / Versioning Acceptance Criteria

## Research
- [ ] Exact MCP/FastMCP/Pydantic versions identified.
- [ ] Current official MCP specification and changelog reviewed.
- [ ] Relevant official FastMCP docs/examples/source/tests reviewed.
- [ ] Evidence ledger completed.

## Contract
- [ ] Public tools/resources/prompts inventoried.
- [ ] Protocol version is distinguished from application API version.
- [ ] Capability negotiation is evidence-based.
- [ ] Schema compatibility is explicitly classified.
- [ ] Error/auth/discovery compatibility is considered.
- [ ] Additive changes are preferred where possible.
- [ ] Breaking changes have explicit migration paths.
- [ ] Deprecations include owner, replacement and removal criteria.

## Verification
- [ ] Golden fixtures exist for public contracts.
- [ ] Discovery tests pass.
- [ ] Invocation contract tests pass.
- [ ] Old-client/new-server compatibility is tested where supported.
- [ ] Error/auth compatibility is tested.
- [ ] Migration/deprecation behavior is tested.
- [ ] Current official documentation was re-checked before completion.
- [ ] Stops when API compatibility and versioning behavior cannot be established from evidence; rejects invented behavior and escalates to the user instead of guessing.
