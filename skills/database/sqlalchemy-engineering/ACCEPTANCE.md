# Database / SQLAlchemy Engineering Acceptance Criteria

## Research
- [ ] Exact Python/SQLAlchemy/database/driver/migration/FastMCP versions identified.
- [ ] Official SQLAlchemy 2.x Session/transaction/asyncio/query/loading/pooling docs read.
- [ ] Official target database and driver docs read.
- [ ] Migration-tool docs read where applicable.
- [ ] FastMCP lifecycle/context docs read.
- [ ] Relevant source/tests inspected.
- [ ] Evidence ledger completed.

## Architecture
- [ ] Dependency direction is explicit.
- [ ] Session ownership/lifetime is explicit.
- [ ] Transaction ownership is explicit.
- [ ] Repository/UoW abstraction is justified.
- [ ] ORM details do not leak into domain/application unnecessarily.
- [ ] Relationship/cascade policy is explicit.

## Database correctness
- [ ] Constraints enforce critical invariants.
- [ ] Indexes support real access paths.
- [ ] Loading strategy avoids known N+1 paths.
- [ ] Pagination ordering is deterministic.
- [ ] Migration path is authoritative and reviewed.
- [ ] Pool/resource lifecycle is bounded.
- [ ] Concurrency behavior is modeled and tested where required.
- [ ] Tenant/security boundaries are enforced.

## Async
- [ ] AsyncSession is not shared across concurrent tasks.
- [ ] Blocking DB operations are absent from async paths.
- [ ] Implicit async IO hazards are handled.

## Verification
- [ ] Unit tests pass.
- [ ] Real target-database integration tests pass.
- [ ] Transaction rollback/failure tests pass.
- [ ] Migration tests pass.
- [ ] Constraint/security tests pass.
- [ ] Query/performance checks pass where required.
- [ ] Concurrency tests pass where required.
- [ ] Static quality gates pass.
- [ ] Architecture re-check passes.
- [ ] Stops when database behavior cannot be established from evidence; rejects invented behavior and escalates to the user instead of guessing.
