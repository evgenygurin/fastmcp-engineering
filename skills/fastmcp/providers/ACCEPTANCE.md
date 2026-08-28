# FastMCP Providers Acceptance Criteria

## Research
- [ ] Exact FastMCP/Python versions identified.
- [ ] Official Provider documentation read.
- [ ] Relevant official examples inspected.
- [ ] Source/tests inspected for ambiguous behavior.
- [ ] MCP specification checked where required.
- [ ] Evidence ledger completed.

## Architecture
- [ ] Provider is justified against simpler native mechanisms.
- [ ] Provider is limited to MCP component sourcing/discovery/composition.
- [ ] Business/domain logic remains outside Provider.
- [ ] Repository/application-service/DI/service-locator responsibilities are not hidden in Provider.
- [ ] Application and infrastructure boundaries are explicit.

## Dynamic behavior
- [ ] Discovery trigger is explicit.
- [ ] Lookup/listing semantics are verified.
- [ ] Identity/key semantics are verified.
- [ ] Collision/precedence behavior is explicit.
- [ ] Visibility and authorization are distinct.
- [ ] Cache/freshness/invalidation semantics are explicit when applicable.
- [ ] Timeout/cancellation/failure behavior is explicit.
- [ ] Concurrency and mutable state are analyzed.
- [ ] Lifecycle/resource ownership is explicit.

## Verification
- [ ] Discovery/listing tests pass.
- [ ] Lookup tests pass.
- [ ] Composition/collision tests pass where applicable.
- [ ] Security/visibility tests pass where applicable.
- [ ] External failure/timeout tests pass where applicable.
- [ ] FastMCP Client/in-process tests pass where applicable.
- [ ] Static quality checks pass.
- [ ] Architecture re-check passes.
- [ ] Evidence is reproducible.
