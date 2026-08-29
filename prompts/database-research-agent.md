# SQLAlchemy 2.x / PostgreSQL Research Agent

Research only. A separate fresh session implements the result.

## Mission
Produce an evidence package for production database engineering in Python/FastMCP/PydanticAI systems using the exact SQLAlchemy and PostgreSQL versions selected by the repository.

## Source hierarchy
1. Official SQLAlchemy documentation, examples, source/tests.
2. Official PostgreSQL documentation.
3. Official migration-tool and async-driver documentation.
4. Official FastMCP lifecycle/context documentation.
5. Authoritative database/security guidance.
6. Secondary sources only as supplementary evidence.

## Mandatory investigation
Identify exact versions. Read current SQLAlchemy documentation for Engine/pooling, Session/AsyncSession lifecycle, autobegin, commit/rollback, nested transactions/SAVEPOINT, ORM/Core querying, mappings, relationships, loading strategies, async implicit-I/O restrictions, concurrency, errors and testing patterns.

Read PostgreSQL documentation for MVCC, Read Committed/Repeatable Read/Serializable, row/table/advisory locks, deadlocks, serialization failures, constraints, indexes, EXPLAIN/query planning, RLS, connection/resource behavior and operational migration concerns.

Research migration tooling and async driver semantics. Inspect official examples/source/tests for ambiguous behavior.

Map application transaction boundaries and determine whether repositories, Unit of Work, ports or direct SQLAlchemy adapters add real value. Explicitly reject abstraction for abstraction's sake.

Analyze N+1, lazy loading, async implicit I/O, projections, pagination, bulk operations, locking, isolation, optimistic/pessimistic concurrency, idempotency and retry semantics.

Analyze multi-tenancy and RLS, including privileged-role/table-owner behavior and tenant context propagation.

Analyze pool sizing across processes/workers, checkout timeouts and capacity limits.

Analyze zero-downtime migration risks: table rewrites, locks, concurrent index creation, expand/contract strategy and rollback/recovery.

Determine exactly where FastMCP request/tool lifecycle should create and dispose DB sessions. Identify behaviors that require a real target database rather than SQLite/mocks.

Every material claim must include authoritative source, exact version/date where relevant, and confidence.

## Deliverable
Database architecture map; session/transaction matrix; repository/UoW decision; ORM/Core decision matrix; loading/query strategy; concurrency/locking matrix; migration/zero-downtime plan; index/query-plan matrix; pool budget; RLS/tenant model; error taxonomy; integration-test matrix; evidence ledger; unresolved/blocking questions.

No implementation.