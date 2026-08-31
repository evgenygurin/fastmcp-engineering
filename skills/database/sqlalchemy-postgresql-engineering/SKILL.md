---
name: sqlalchemy-postgresql-engineering
description: Evidence-first database engineering for production Python systems using SQLAlchemy 2.x and PostgreSQL, with explicit transaction ownership, async session discipline, schema/migration design, concurrency, RLS, performance and integration testing.
---

# SQLAlchemy 2.x / PostgreSQL Engineering

## Mission
Treat the database as a correctness boundary, not merely persistence plumbing. Design schemas, transactions, queries, concurrency and authorization so correctness is enforced as close to the data as practical without leaking database concerns into domain logic.

## Mandatory research gate
Before implementation:
1. Read repository architecture, security, resilience, testing and configuration contracts.
2. Identify exact Python, SQLAlchemy, PostgreSQL, async driver and migration-tool versions.
3. Read current official SQLAlchemy documentation for Engine, pooling, Session/AsyncSession, transactions, ORM/Core querying, relationships, loading, concurrency and async-specific behavior.
4. Read current PostgreSQL documentation for MVCC, isolation, locks/deadlocks, constraints, indexes, RLS, transactions and query planning relevant to the feature.
5. Read migration-tool documentation and repository migration conventions.
6. Inspect official examples/source/tests for ambiguous behavior.
7. Record evidence, assumptions and unresolved questions.

Do not rely on remembered SQLAlchemy 1.x patterns. Current SQLAlchemy 2.x semantics must be verified from official sources.

## Architecture boundary

```text
Application Use Case
 │
 ▼
Database Port / Repository Contract
 │
 ▼
SQLAlchemy Adapter
 ┌────┴────┐
 │ │
 AsyncSession SQLAlchemy Core/ORM
 │ │
 └────┬────┘
 ▼
 PostgreSQL
```

Domain entities must not inherit from SQLAlchemy or depend on session/query infrastructure unless the architecture explicitly chooses persistence-aware domain modeling with evidence. Keep mapping and database-specific errors at the infrastructure boundary.

## Session and transaction ownership
A Session/AsyncSession represents mutable transactional state. It is not a general cache and must not be shared concurrently. Use session-per-logical-operation/task and make transaction boundaries explicit. Keep transactions short and never hold them open while waiting on LLM, MCP or unrelated network work unless explicitly justified. SQLAlchemy's current guidance states AsyncSession is not safe to share across concurrent asyncio tasks and recommends AsyncSession per task.

Prefer explicit transaction framing such as `async with session.begin()` where appropriate. Understand autobegin, commit/rollback, expiration and nested/SAVEPOINT semantics before choosing a pattern.

## Repository / Unit of Work policy
Do not create generic repositories or Unit of Work abstractions automatically. Introduce a port when it protects application/domain independence, enables a meaningful alternative adapter, or materially improves testing. A repository should express domain/application intent, not duplicate SQLAlchemy's API.

Transaction ownership belongs to the application/use-case boundary or an explicitly documented infrastructure transaction manager. Repositories should not independently commit unless their contract explicitly makes them transaction owners.

## SQLAlchemy 2.x
Prefer SQLAlchemy 2.x `select()`, `insert()`, `update()`, `delete()` and explicit execution APIs. Avoid legacy `Query` patterns. Choose ORM vs Core based on the access pattern, not ideology. Use typed mapped models and explicit relationships/configuration.

Be deliberate about loading strategy. Prevent accidental lazy I/O in async code. Detect and eliminate N+1 queries. Use `selectinload`, `joinedload`, explicit joins or projections according to cardinality and query shape; verify with SQL/query-count tests.

Do not expose ORM entities outside boundaries merely because mapping is convenient. Map to application/domain DTOs where this prevents persistence lifecycle leakage or accidental lazy loads.

## PostgreSQL correctness
Use database constraints for invariants that must hold regardless of application path: primary/foreign keys, unique constraints, check constraints and appropriate NOT NULL constraints. Application validation is complementary, not a replacement for database integrity.

Understand PostgreSQL MVCC and the selected isolation level. Use row-level locks (`SELECT... FOR UPDATE` variants), advisory locks or serializable transactions only for demonstrated concurrency requirements. Design lock ordering to minimize deadlocks. Handle documented serialization/deadlock failures with bounded, idempotent retry at the appropriate application boundary.

## Indexing and query performance
Indexes are workload-specific. Design them from real access predicates, ordering, joins and selectivity. Use EXPLAIN/EXPLAIN ANALYZE in controlled environments. Avoid speculative indexes and redundant indexes. For large production tables, evaluate PostgreSQL `CREATE INDEX CONCURRENTLY` where operationally appropriate; it has different locking/transaction requirements and must be researched before migration use.

Avoid SELECT * when a projection is sufficient. Paginate deterministically. For large datasets choose keyset pagination where offset pagination becomes unsuitable.

## Connection pooling
Configure pool size, overflow, timeouts and recycling based on actual deployment concurrency and PostgreSQL capacity. Never multiply pool sizes blindly across workers/processes. Instrument pool exhaustion and checkout latency. Each AsyncSession/task must release its connection promptly.

## Migrations
Schema changes are versioned artifacts. Follow repository migration conventions. Separate backward-compatible expand/contract changes when zero-downtime deployment requires them. Consider lock duration, table rewrites, index build strategy and rollback feasibility. Never modify production schema manually when the repository migration system is authoritative.

## Row-Level Security / tenancy
When tenant isolation is a requirement, evaluate PostgreSQL RLS as a defense-in-depth data boundary. RLS is default-deny once enabled without applicable policies, but table owners and privileged roles have important exceptions that must be understood.

Application authorization and RLS solve different layers; neither should be assumed to replace the other. Define tenant context propagation and prevent connection/session state leakage between requests.

## Async and concurrency
Never share an AsyncSession across concurrent tasks. If concurrent DB operations are genuinely needed, use independent sessions/transactions and understand the loss of transactional atomicity. SQLAlchemy's own concurrency example warns that gathering ORM statements across multiple sessions adds overhead and can lose transactional safety.

Avoid implicit blocking I/O in async paths. Use the documented async driver and SQLAlchemy async APIs.

## Error handling
Translate infrastructure exceptions at the application boundary. Distinguish integrity violations, not-found conditions, serialization/deadlock failures, connectivity failures, timeouts and programming errors. Do not catch `Exception` and convert everything to a generic database error.

## Testing
Use real PostgreSQL integration tests for transaction, constraint, locking, isolation, RLS, migration and query-plan behavior that mocks cannot prove. Use unit tests for pure mapping/query construction/business orchestration. Test concurrent scenarios explicitly where correctness depends on them.

For tests requiring externally managed transactions, use SQLAlchemy's documented transaction-joining patterns and verify driver/database SAVEPOINT behavior rather than assuming SQLite is equivalent to PostgreSQL.

## Rejection criteria
Reject if sessions are shared across concurrent tasks, repositories commit unexpectedly, transactions span remote LLM/MCP calls without justification, integrity depends only on Python validation, migrations ignore operational locking, tenant boundaries exist only in prompts, N+1/lazy I/O is unexamined, pool capacity is unbounded, or database behavior is claimed based solely on mocks.

## Deliverables
Schema/domain mapping, repository/port decision, transaction map, session lifecycle, concurrency/locking model, migration plan, index/query plan, pooling budget, RLS/tenant policy where applicable, error taxonomy, integration test matrix, implementation and verification report.