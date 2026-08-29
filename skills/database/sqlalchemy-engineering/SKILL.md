---
name: database-sqlalchemy-engineering
description: Evidence-first database and SQLAlchemy 2.x engineering for production FastMCP systems, including async ORM, transactions, repositories, migrations, concurrency, pooling, query performance and real database verification.
---

# Database / SQLAlchemy Engineering

## Mission

Treat persistence as a deliberate architectural boundary. Keep domain/application logic independent from ORM details while preserving correct transaction, concurrency and database semantics.

## Mandatory research gate

Before implementation:
1. Read AGENTS.md and repository architecture/data-access contracts.
2. Identify exact Python, SQLAlchemy, SQLAlchemy asyncio extension, database, driver and migration-tool versions.
3. Read the official SQLAlchemy 2.x ORM, Session, transactions, asyncio, relationship/loading, querying, connection pooling and performance documentation for the exact target version.
4. Read official migration-tool documentation (Alembic when used).
5. Read the target database's official documentation for transactions, isolation, constraints, indexes, locking, JSON/array features and concurrency behavior actually used.
6. Read relevant FastMCP lifecycle/context documentation before deciding how DB sessions enter tool execution.
7. Inspect official examples/source/tests where semantics are ambiguous.
8. Record evidence before coding.

## Architecture

Preferred dependency direction:

```text
MCP adapter/tool
      ↓
Application use case
      ↓
Domain model / policies
      ↓
Repository / Unit of Work port
      ↓
SQLAlchemy infrastructure
      ↓
Database
```

MCP handlers must not contain SQL queries, transaction choreography or ORM graph manipulation. Domain objects should not depend on SQLAlchemy where a clean boundary is practical.

## Session lifecycle

A `Session`/`AsyncSession` is mutable, stateful and transaction-oriented. Do not share one instance concurrently across asyncio tasks. Establish an explicit session ownership/lifetime policy. Prefer a short, request/use-case/task-scoped lifetime and make transaction boundaries explicit. Verify exact SQLAlchemy behavior for the target version rather than assuming it.

## Transactions

Define who owns `begin`, `commit`, `rollback`, savepoints and retry behavior. A use case that performs multiple writes should have one explicit transaction boundary unless there is a documented reason otherwise. Never let repository methods unexpectedly commit application work. Handle failures so the session is left in a known state.

Be explicit about transaction isolation when correctness depends on it. For race-sensitive invariants, use database constraints, appropriate locking/isolation and deterministic conflict handling rather than application-level check-then-insert logic alone.

## Repository / Unit of Work

Use repositories for meaningful domain persistence boundaries, not generic CRUD wrappers that leak ORM semantics everywhere. Use a Unit of Work only when it clarifies transaction coordination; avoid ceremony for simple read-only queries.

Repository interfaces belong to the application/domain boundary when they are actual ports. SQLAlchemy implementations belong to infrastructure. Do not create abstractions that merely rename `session.execute()` without providing a useful boundary.

## ORM mapping

Use SQLAlchemy 2.x typed declarative mapping and explicit relationship semantics. Define primary keys, foreign keys, uniqueness, nullability, check constraints and indexes based on invariants. Do not rely on Python validation alone for invariants that must survive concurrent writers.

Avoid accidental bidirectional cascades and uncontrolled relationship graphs. Understand delete/update cascades, orphan behavior and loading semantics before configuring them.

## Querying / performance

Prefer SQLAlchemy 2.x `select()` and explicit result handling. Measure query behavior rather than guessing. Detect N+1 queries. Choose `selectinload`, `joinedload`, lazy strategies and explicit loading based on access patterns and cardinality. Avoid loading large graphs when projections/aggregates are sufficient.

Pagination must be deterministic. Prefer keyset/seek pagination for large mutable datasets when requirements permit; use offset pagination only when its trade-offs are acceptable. Define stable ordering and indexes that support the access path.

## Constraints / indexes

Every important uniqueness, referential-integrity and state invariant must be enforced at the database layer when appropriate. Index based on real query predicates, joins and ordering. Avoid speculative indexes. Verify query plans for critical paths against realistic data volumes.

## Migrations

Schema changes are versioned artifacts. Migrations must be deterministic, reviewable, reversible where practical, and safe for the deployment strategy. Consider expand/contract for incompatible changes and large-table operations. Never treat `create_all()` as a production migration strategy.

## Async

Use SQLAlchemy async APIs consistently at async boundaries. Prevent accidental implicit IO from ORM attribute access where async behavior forbids it. Do not call blocking DB APIs from async tool execution. Verify driver support and pool configuration for the exact database.

## Pooling / resources

Configure engine and pool according to deployment concurrency, database limits and workload. Account for pool timeout, recycle/pre-ping behavior, transaction leaks and graceful shutdown. Never solve connection exhaustion by blindly increasing pool size.

## Concurrency

Model concurrent writes explicitly. Test lost-update, uniqueness races, optimistic/pessimistic locking and retry behavior when relevant. Application-level mutexes are not a substitute for database concurrency guarantees across processes/instances.

## Security

Use least-privilege DB credentials, parameterized SQL, safe identifier handling and tenant isolation. Never construct SQL from untrusted strings. If row-level security is used, verify session identity propagation and fail-closed behavior.

## Testing

Use real supported database integration tests for transaction, constraint, migration, query, isolation and locking semantics. Unit-test pure policies without a database. Verify migration from clean and representative previous states. Include rollback/failure tests and concurrency tests for critical invariants.

## Rejection criteria

Reject if session ownership is ambiguous, repositories commit unexpectedly, ORM details leak across all layers, critical invariants exist only in Python, migrations are not authoritative, async sessions are shared concurrently, N+1 behavior is unexamined, or production correctness depends on SQLite/mock behavior that differs from the target database.

## Deliverables

Database architecture, transaction/session policy, domain persistence ports, ORM mapping strategy, repository/UoW policy, query/performance plan, migration strategy, concurrency model, security controls, integration-test strategy and architecture re-check.