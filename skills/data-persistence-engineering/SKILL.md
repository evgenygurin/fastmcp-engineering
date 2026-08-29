---
name: data-persistence-engineering
description: Evidence-first PostgreSQL and persistence engineering for production FastMCP systems.
---

# Data / Persistence Engineering

## Mission
Make persistence correct, secure, observable, performant and evolvable. PostgreSQL is the reference relational system when relational persistence is required; conclusions about transactional behavior must use the actual production-class database.

## Mandatory research
Identify exact Python, SQLAlchemy, PostgreSQL, migration-tool and driver versions. Read current official PostgreSQL and SQLAlchemy documentation first, then exact-version migration/driver/framework source and tests. Verify transaction, isolation, locking, pooling, async and migration behavior rather than relying on memory.

## Data ownership
Every table/entity has an explicit owner and lifecycle. Separate domain concepts from persistence models. Do not leak ORM/session objects across architectural boundaries. Define identity, uniqueness, nullability and referential integrity explicitly.

## Transactions
Define transaction boundaries at the application/use-case level. A transaction must have a clear owner. Keep transactions short and deterministic. Never hold a DB transaction across external network/LLM calls unless there is an explicit, justified design and timeout strategy.

## Unit of Work
Use a Unit of Work abstraction only when it clarifies transaction ownership across multiple repositories/operations. Repositories must not silently commit independently when the use case requires atomicity. Rollback behavior must be explicit.

## Isolation / concurrency
Choose isolation levels based on required invariants. Analyze lost updates, write skew, phantom reads, deadlocks and serialization failures. Use optimistic/pessimistic locking intentionally. Retry only documented transient serialization/deadlock failures and only when the operation is safe to retry.

## Schema integrity
Enforce critical invariants in the database with NOT NULL, UNIQUE, CHECK, FOREIGN KEY and appropriate indexes. Application validation improves UX but must not be the only protection for invariants that concurrent writers can violate.

## Migrations
All schema changes are versioned, deterministic and reviewable. Migrations must be safe for the deployment strategy and dataset size. Separate expand/contract changes when zero-downtime compatibility is required. Never edit an already-applied migration silently. Test migrations on representative schemas/data.

## PostgreSQL-first verification
SQLite or in-memory databases may be useful for narrow unit tests but cannot prove PostgreSQL-specific semantics. Integration tests requiring transactions, RLS, locking, query plans, JSONB, extensions or PostgreSQL types must run against PostgreSQL.

## Queries
Avoid N+1 queries, accidental Cartesian products and unbounded result sets. Select only required columns where material. Use stable pagination. Critical queries require EXPLAIN/EXPLAIN ANALYZE evidence under representative data. Indexes must have a query/use case rationale and write/storage cost considered.

## Pagination
Prefer deterministic keyset pagination for large/changing datasets where appropriate. Offset pagination is acceptable for bounded/simple cases. Every paginated query must have a stable ordering and bounded page size. Never accept arbitrary client-controlled page sizes without limits.

## Connection pools
One application-level engine/pool per intended process/lifetime. Size pools from measured workload and PostgreSQL capacity. Monitor pool wait time and saturation. Never create engines/sessions inside repositories or per-request without an explicit lifecycle reason.

## Async SQLAlchemy
Use SQLAlchemy async APIs correctly for the installed version. `AsyncSession` is a unit-of-work resource and must not be concurrently shared across independent asyncio tasks. Define commit/rollback/close ownership explicitly.

## RLS / tenant isolation
When tenant isolation is required, enforce it in PostgreSQL RLS or an equivalent database boundary in addition to application authorization. Test direct/indirect access paths, joins, background jobs and elevated roles. Never rely on a caller-supplied tenant ID as proof of authorization.

## Soft delete / history
Soft deletion is not automatically superior. If used, define uniqueness, foreign-key, query-default, restoration and retention semantics. Audit/history tables need explicit event ownership, immutable fields and retention policy. Avoid accidental exposure of deleted/archived records.

## Idempotency
Sensitive or externally-triggered writes need an idempotency strategy where duplicate delivery is possible. Prefer database-enforced uniqueness/idempotency keys over in-memory deduplication. Define behavior for concurrent duplicate requests and ambiguous outcomes.

## External side effects
Do not assume DB transaction rollback can undo external side effects. For DB + message/event workflows consider transactional outbox/inbox patterns. Define delivery semantics, deduplication and recovery before implementing distributed workflows.

## Backups / recovery
Define backup strategy, retention, encryption/access, restore procedure, RPO and RTO. A backup is not considered reliable until restore is tested. Migration compatibility with rollback/restore procedures must be considered.

## Data lifecycle
Define retention, archival, deletion and legal/security requirements. Minimize stored sensitive data. Deletion must cover indexes, caches, search projections and derived stores where applicable.

## Test data
Factories/builders must create valid domain state without hidden global fixtures. Production data must never be copied into tests without approved anonymization. Integration tests must isolate state and be order-independent.

## Security
Never log credentials, tokens, sensitive bind values or full sensitive rows. Parameterize SQL. Restrict DB roles by least privilege. Separate application roles from migration/admin roles. Secrets arrive through configuration boundaries, not repositories.

## Observability
Instrument query latency, pool saturation, transaction failures, deadlocks and migration health through the observability layer. Avoid high-cardinality SQL text or parameter logging.

## Performance / reliability
Persistence decisions must satisfy performance and resilience policies: bounded queries/results, timeouts, retry-safe transient failure handling, backpressure and graceful degradation. Never retry arbitrary transactions containing non-idempotent side effects.

## Rejection criteria
Reject ORM-only integrity assumptions, per-repository commits that break atomicity, shared async sessions, unbounded queries/pages, untested PostgreSQL-specific behavior, unsafe migrations, application-only tenant isolation where DB isolation is required, blind retries and untested backups/restores.

## Deliverables
Data ownership model; schema/invariant catalog; transaction/UoW map; isolation/locking policy; migration strategy; PostgreSQL verification matrix; query/index plan; pagination policy; pool/session lifecycle; RLS/tenant model; idempotency/outbox strategy; backup/restore plan; data lifecycle policy; test matrix; evidence ledger; rejected alternatives; verification report.