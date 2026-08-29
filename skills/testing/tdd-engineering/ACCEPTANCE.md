# Testing / TDD Acceptance Criteria

## Research
- [ ] Exact versions identified.
- [ ] Official pytest/async testing semantics verified.
- [ ] FastMCP testing/client/server behavior verified.
- [ ] PydanticAI TestModel/FunctionModel/override/request-blocking verified.
- [ ] SQLAlchemy/PostgreSQL integration semantics verified.
- [ ] Behaviors mocks cannot prove identified.
- [ ] Evidence ledger completed.

## Test architecture
- [ ] Test taxonomy is explicit.
- [ ] Invariant-to-test matrix exists.
- [ ] Cheapest proving test level selected for each invariant.
- [ ] Unit tests remain deterministic.
- [ ] Contract/protocol tests cover MCP boundaries.
- [ ] Real PostgreSQL tests cover DB-only semantics.
- [ ] Real-provider tests are isolated from normal CI.
- [ ] Security/resilience regressions are covered.
- [ ] Architecture dependency rules are tested where practical.

## Fixtures / async
- [ ] Fixture scopes match lifecycle.
- [ ] No unjustified autouse state.
- [ ] Cleanup is guaranteed.
- [ ] No shared mutable test state.
- [ ] AsyncSession is not shared across concurrent tasks.
- [ ] No sleep-based synchronization.
- [ ] Cancellation and cleanup are tested.

## Quality
- [ ] Tests assert observable contracts.
- [ ] Parametrization is used where it improves coverage.
- [ ] Flaky tests are diagnosed, not hidden.
- [ ] Coverage is used diagnostically.
- [ ] Property/mutation testing is used only where justified.
- [ ] Static quality gates pass.
- [ ] All executed commands/results are recorded.
- [ ] Architecture re-check passes.