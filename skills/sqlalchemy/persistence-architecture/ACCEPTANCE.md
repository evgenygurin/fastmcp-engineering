# SQLAlchemy Persistence Acceptance Criteria

## Research
- [ ] Exact versions identified.
- [ ] Official SQLAlchemy docs read.
- [ ] Database/driver/migration docs read.
- [ ] Relevant FastMCP lifecycle/Context docs/examples read.
- [ ] Ambiguous behavior checked against source/tests.
- [ ] Evidence ledger completed.

## Architecture
- [ ] Persistence is behind application/domain boundaries.
- [ ] Repository ports have explicit responsibilities.
- [ ] Unit of Work is justified, not a service locator.
- [ ] Session ownership is explicit.
- [ ] Transaction ownership is explicit.
- [ ] ORM models do not accidentally become public DTOs.

## Database
- [ ] AsyncEngine/pool lifecycle is explicit.
- [ ] AsyncSession scope is explicit and concurrency-safe.
- [ ] Loading strategy prevents accidental N+1/implicit IO.
- [ ] Pagination/unbounded reads are controlled.
- [ ] Concurrency/isolation strategy is explicit.
- [ ] Retry policy is narrow and replay-safe.
- [ ] Migrations are versioned and deployment-safe.
- [ ] Database constraints support integrity.
- [ ] Security/RLS policy is explicit where applicable.

## Verification
- [ ] Unit tests pass.
- [ ] Real database integration tests pass where SQL behavior matters.
- [ ] Rollback/transaction tests pass.
- [ ] Constraint tests pass.
- [ ] Concurrency tests pass where applicable.
- [ ] Migration tests pass.
- [ ] Static quality checks pass.
- [ ] Architecture re-check passes.