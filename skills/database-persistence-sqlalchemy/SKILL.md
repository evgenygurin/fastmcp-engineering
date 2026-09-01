---
name: database-persistence-sqlalchemy
description: Evidence-first persistence engineering for FastMCP applications using SQLAlchemy 2.x and PostgreSQL/Supabase.
---

# Database / Persistence Engineering

## Mission
Keep persistence correct, transactional, observable and replaceable while preventing ORM concerns from leaking into the domain model.

## Trigger / Когда применять

**Scope / When to use:** persistence engineering for FastMCP applications using SQLAlchemy 2.x and PostgreSQL/Supabase.
**Trigger:** designing or changing persistence, ORM models, repositories, transactions, sessions, pooling, migrations, or Supabase integration.
**Upstream / Prerequisite:** identified exact Python, SQLAlchemy, async driver, PostgreSQL and Supabase versions; repository migrations/models/tests inspected; evidence recorded.
**Mission / Goal:** keep persistence correct, transactional, observable and replaceable while preventing ORM concerns from leaking into the domain model.
**Research / Evidence:** identify exact versions; read current official SQLAlchemy, PostgreSQL and relevant Supabase documentation first; inspect repository migrations/models/tests; research exact-version examples/source/tests for async sessions, transactions, pooling, ORM loading, locking and migrations; record evidence and re-check version-sensitive behavior.
**Decision / Selection rules:** keep domain entities/value objects independent of SQLAlchemy; place persistence models, repositories, Unit of Work and transaction adapters at infrastructure/application boundaries; use one clear session lifecycle per operation; define transaction boundaries from business invariants; use explicit SQLAlchemy 2.x APIs with intentional loading; enforce important invariants in the database; use a single authoritative migration mechanism with expand/contract; use an outbox for DB+event consistency; configure pooling from deployment constraints.
**Version / Compatibility:** identify exact versions of Python, SQLAlchemy, async driver, PostgreSQL and Supabase; use explicit 2.x APIs and typed mappings for the installed version.

## Deliverables

**Deliverables / Artifacts:** persistence architecture; model/schema map; transaction/UoW policy; repository contracts; locking/isolation policy; query/index analysis; pool configuration; migration plan; outbox/inbox decision; Supabase integration policy; persistence test matrix; evidence ledger; rejected alternatives; verification report.
**Verification / Testing:** use fast unit tests for domain/application behavior and real PostgreSQL integration tests for transaction, constraint, query, locking and migration behavior; SQLite is not a drop-in substitute for PostgreSQL semantics; test rollback, unique/FK/check violations, concurrent updates, N+1-sensitive paths, pagination and migration compatibility.
**Failure / Stop conditions:** reject domain classes importing ORM types, repository-level hidden commits, implicit async lazy I/O, unbounded pools, SQLite-only proof of PostgreSQL behavior, missing constraints for critical invariants, unsafe migration rewrites, blind transaction retries and DB/network atomicity assumptions.
**Positive scenario:** persistence is layered behind the domain with real PostgreSQL verification of transactions and migrations.
**Negative scenario:** ORM types leak into domain classes and PostgreSQL-specific behavior is proven only against SQLite.

## Mandatory research
Identify exact Python, SQLAlchemy, async driver, PostgreSQL and Supabase versions. Read current official SQLAlchemy documentation, PostgreSQL documentation and relevant Supabase documentation first; inspect repository migrations/models/tests. Research exact-version examples/source/tests for async sessions, transactions, pooling, ORM loading, locking and migrations. Record evidence and re-check version-sensitive behavior before completion.

## Architecture
Domain entities/value objects must not depend on SQLAlchemy. Persistence models, repositories, Unit of Work and transaction adapters belong to infrastructure/application boundaries. MCP handlers never access sessions or repositories directly. Application use cases own transaction boundaries unless a deliberately wider workflow requires orchestration.

## SQLAlchemy 2.x
Prefer explicit 2.x APIs and typed mappings. Define relationships intentionally. Avoid implicit lazy I/O in async code. Make loading strategy explicit (`selectinload`, `joinedload`, explicit queries) and test query counts for critical paths. Do not use ORM models as API schemas.

## Session / Unit of Work
Use one clear session lifecycle per application operation/request where appropriate. Transactions must be explicit. Do not pass sessions deep into domain logic. Commit at the application transaction boundary; repositories should not secretly commit unless the architecture explicitly defines that policy. Rollback and close must be deterministic.

## Transactions
Define transaction boundaries from business invariants, not repository methods. Analyze isolation level, read/write dependencies, deadlocks, retries and partial failure. Never assume a transaction protects external HTTP/LLM side effects; use an outbox/workflow pattern when atomicity across systems is required.

## Concurrency
Choose optimistic locking/version columns or PostgreSQL row locks based on contention and invariant requirements. Document lock ordering to reduce deadlocks. Test concurrent updates. Do not use locks as a substitute for constraints.

## Constraints
Enforce important invariants in the database: primary/foreign keys, unique constraints, checks, not-null and appropriate indexes. Application validation improves UX but must not be the only protection against races or concurrent writes.

## Query performance
Prevent N+1 queries. Select only required data for read-heavy paths where justified. Index based on real query predicates/orderings and inspect query plans for critical paths. Avoid premature indexes and ORM micro-optimizations without evidence. Pagination must use a stable ordering; keyset pagination is preferred for large/changing datasets when applicable.

## Async
Async SQLAlchemy is not automatically faster. Avoid blocking database drivers inside async paths. Do not share `AsyncSession` concurrently across independent tasks unless exact documented usage permits it; use separate sessions/transaction scopes as required. Bound connection pools and account for database connection limits.

## Pooling
Configure pool size, overflow, timeout, recycle/health behavior from deployment constraints. Analyze Supabase connection/pooling mode and application concurrency before choosing pool settings. Never blindly increase pool size.

## Migrations
Use a single authoritative migration mechanism. Every schema change must be forward-deployable and reviewed for lock duration, data volume and backward compatibility. Prefer expand/contract migrations for zero/minimal downtime: add compatible schema → deploy dual-compatible code → backfill → switch reads/writes → remove old schema later.

## Outbox / integration consistency
When a DB state change must reliably produce an external event/job, use an outbox or equivalent transactional handoff rather than DB commit + network call without recovery. Consumers need idempotency/inbox semantics when duplicate delivery is possible.

## Supabase
Treat Supabase as PostgreSQL plus its enabled platform services, not as a reason to couple the domain to Supabase APIs. Verify actual project settings, connection mode, RLS/auth behavior and operational limits from current official Supabase documentation. If using RLS, define policies as defense-in-depth and test them; application authorization remains explicit.

## Testing
Use fast unit tests for domain/application behavior and real PostgreSQL integration tests for transaction, constraint, query, locking and migration behavior. SQLite is not a drop-in substitute for PostgreSQL semantics. Test rollback, unique/FK/check violations, concurrent updates, N+1-sensitive paths, pagination and migration compatibility.

## Reliability
Handle transient DB failures according to the resilience skill. Retries must be transaction-safe and only applied where operations are idempotent or protected by deduplication. Never retry blindly after an ambiguous commit outcome.

## Security
Use parameterized SQL/SQLAlchemy expressions. Apply least-privilege DB roles. Never log credentials or sensitive query parameters. Test tenant isolation and authorization at repository/use-case/database policy boundaries.