# Context / DI Skill Acceptance Criteria

## Research
- [ ] Exact FastMCP/Python versions identified.
- [ ] Official Context documentation read.
- [ ] Official dependency/DI documentation read.
- [ ] Relevant official examples inspected.
- [ ] Source/tests inspected for ambiguous semantics.
- [ ] MCP specification checked where required.
- [ ] Evidence ledger completed.

## Architecture
- [ ] Runtime Context and application dependencies are distinct.
- [ ] Application/domain code does not depend directly on FastMCP Context without an explicit approved boundary.
- [ ] No Service Locator / God Object was introduced.
- [ ] Dependency graph is explicit.
- [ ] Dependency scopes are explicit.
- [ ] Lifespan ownership is explicit.
- [ ] Infrastructure composition is explicit.

## Runtime / Security
- [ ] Async/concurrency semantics are understood.
- [ ] Mutable shared state has an explicit concurrency model.
- [ ] Resource cleanup is verified.
- [ ] Authentication/authorization ownership is explicit.
- [ ] Context-derived identity is not blindly trusted.

## Verification
- [ ] Focused tests pass.
- [ ] Dependency wiring/overrides are tested where applicable.
- [ ] Lifecycle startup/shutdown is tested where applicable.
- [ ] MCP Client/in-process tests pass where applicable.
- [ ] Static quality checks pass.
- [ ] Architecture re-check passes.
- [ ] Verification evidence is reproducible.