# Database / SQLAlchemy Decision Matrix

| Concern | Preferred approach | Verification |
|---|---|---|
| Session scope | Explicit request/use-case/task scope | Lifecycle tests |
| Async concurrency | One AsyncSession per task | Concurrent-task tests |
| Transactions | Application/use-case-owned boundary | Commit/rollback tests |
| Repository | Domain-relevant persistence port | Architecture review |
| ORM | SQLAlchemy 2.x typed mapping | Mapping/integration tests |
| N+1 | Explicit loading/projection | Query-count tests |
| Pagination | Stable ordering; keyset when justified | Boundary/concurrency tests |
| Invariants | DB constraints + application policy | Constraint tests |
| Migrations | Alembic/versioned schema | Clean upgrade tests |
| Pool | Workload/database-limit based | Pool exhaustion tests |
| Concurrency | DB constraints/locking/isolation | Race tests |
| Security | Least privilege/parameterized SQL/tenant controls | Security regression |

## Hard rules

1. Do not share an AsyncSession across concurrent tasks.
2. Repository methods must not silently commit outer application work.
3. Do not use SQLite as proof of PostgreSQL-specific semantics.
4. Do not rely only on Python checks for concurrent invariants.
5. Do not create indexes speculatively; tie them to real access paths.
6. Do not use generic repositories when they add no meaningful boundary.
7. `create_all()` is not a production migration strategy.
8. Critical SQL/transaction/concurrency semantics require real database verification.