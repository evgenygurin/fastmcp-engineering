# SQLAlchemy / PostgreSQL Acceptance Criteria

## Research
- [ ] Exact Python, SQLAlchemy, PostgreSQL, driver and migration versions identified.
- [ ] Current official SQLAlchemy Session/AsyncSession/transaction/pooling docs checked.
- [ ] Current PostgreSQL MVCC/isolation/locking/constraint/index/RLS docs checked.
- [ ] Migration and async-driver semantics checked.
- [ ] Official examples/source/tests inspected for ambiguous behavior.
- [ ] Evidence ledger completed.

## Architecture
- [ ] Database dependency direction is explicit.
- [ ] Session lifecycle is explicit.
- [ ] Transaction owner is explicit.
- [ ] Repository/UoW exists only where it adds a real boundary.
- [ ] ORM/Core choice is evidence-driven.
- [ ] Domain is not coupled to SQLAlchemy without deliberate justification.
- [ ] Loading strategy and N+1 risk are explicit.
- [ ] Query projections/pagination are explicit.

## Correctness / Security
- [ ] Critical invariants are backed by database constraints.
- [ ] Isolation/locking strategy is documented where concurrency matters.
- [ ] Serialization/deadlock retry policy is bounded and idempotent.
- [ ] Tenant isolation is enforced outside prompts.
- [ ] RLS behavior and privileged-role exceptions are understood where used.
- [ ] Transactions do not span remote LLM/MCP/HTTP work without justification.

## Operations
- [ ] Pool capacity is bounded and sized for actual worker/process concurrency.
- [ ] Migration locking/table rewrite risks are assessed.
- [ ] Expand/contract strategy exists where required.
- [ ] Index strategy is evidence-based.

## Verification
- [ ] Unit tests pass.
- [ ] Real PostgreSQL integration tests pass.
- [ ] Transaction rollback/commit behavior verified.
- [ ] Constraint behavior verified.
- [ ] Async session lifecycle verified.
- [ ] Concurrency/locking behavior verified where applicable.
- [ ] RLS/tenant isolation verified where applicable.
- [ ] Migration tests verified.
- [ ] Query count/performance checks verified where required.
- [ ] Static quality gates pass.
- [ ] Architecture re-check passes.
- [ ] Stops when database behavior cannot be established from evidence; rejects invented behavior and escalates to the user instead of guessing.
