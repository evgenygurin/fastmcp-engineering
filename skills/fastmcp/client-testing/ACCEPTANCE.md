# FastMCP Client / Testing Acceptance Criteria

## Research
- [ ] Exact FastMCP/Python versions identified.
- [ ] Official Client/testing documentation read.
- [ ] Relevant official examples inspected.
- [ ] Source/tests inspected for ambiguous behavior.
- [ ] MCP specification checked where required.
- [ ] Evidence ledger completed.

## Test architecture
- [ ] Requirement mapped to the lowest sufficient test layer.
- [ ] MCP-facing behavior uses the documented Client seam where appropriate.
- [ ] In-process tests are not presented as transport/E2E proof.
- [ ] Fixtures have explicit ownership and cleanup.
- [ ] Shared mutable global state is avoided.
- [ ] Synchronization is deterministic.

## Protocol / security
- [ ] Tool discovery/invocation tested where applicable.
- [ ] Resource/prompt contracts tested where applicable.
- [ ] Schemas/structured output tested where applicable.
- [ ] Errors tested.
- [ ] Auth/authz tested through the MCP boundary where applicable.
- [ ] Tenant/isolation behavior tested where applicable.

## Runtime
- [ ] Lifecycle cleanup tested where applicable.
- [ ] Cancellation/timeouts tested where applicable.
- [ ] Tasks/streaming/progress tested where applicable.
- [ ] Concurrency tested where state or race risk exists.
- [ ] Transport-specific guarantees tested on the actual transport.

## Quality
- [ ] Focused tests pass.
- [ ] Integration tests pass.
- [ ] Static checks pass.
- [ ] Architecture re-check passes.
- [ ] No flaky behavior is hidden by weakened assertions.
- [ ] Verification commands/results are reproducible.