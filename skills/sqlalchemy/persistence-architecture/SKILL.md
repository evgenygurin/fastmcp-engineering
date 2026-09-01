---
name: sqlalchemy-persistence-architecture
description: Engineer SQLAlchemy 2.x persistence behind explicit application transaction boundaries, repositories, unit of work, async lifecycle, concurrency, migrations, and database security.
---

# SQLAlchemy / Persistence Architecture

## Mission

Treat persistence as infrastructure. Domain and application code must not depend on SQLAlchemy session mechanics, ORM entities, or database-specific accidental behavior unless explicitly justified.

## Trigger / Когда применять

**Scope / When to use:** SQLAlchemy 2.x persistence behind explicit application transaction boundaries, repositories, unit of work, async lifecycle, concurrency, migrations, and database security.
**Trigger:** designing or changing persistence, transaction boundaries, repositories, unit of work, async sessions, concurrency, migrations, or database security.
**Upstream / Prerequisite:** `AGENTS.md` and repository contracts read; identified exact versions; evidence recorded before coding.
**Mission / Goal:** treat persistence as infrastructure; domain and application code must not depend on SQLAlchemy session mechanics, ORM entities, or database-specific accidental behavior unless explicitly justified.
**Research / Evidence:** read official SQLAlchemy 2.x documentation relevant to the feature, especially asyncio, sessions, transactions, pooling, ORM loading and concurrency; read official migration-tool/database documentation; read relevant FastMCP lifecycle/Context documentation and official examples; inspect SQLAlchemy/FastMCP source/tests where semantics are ambiguous.
**Decision / Selection rules:** let the application use case own the business transaction boundary and define explicitly who begins, commits, rolls back and closes a transaction; prefer one coherent unit of work per use-case operation; never share an `AsyncSession` concurrently between independent asyncio tasks — prefer task/request-scoped sessions; choose loading strategy deliberately to prevent N+1 and accidental lazy IO; keep repositories as persistence-oriented ports rather than generic CRUD mirrors; use Unit of Work only where it clarifies coordination; scope retries narrowly; treat schema changes as versioned artifacts; use least-privilege credentials and parameterized queries.
**Version / Compatibility:** identify exact Python, SQLAlchemy, database driver, database, migration tool and FastMCP versions.

## Deliverables

**Deliverables / Artifacts:** evidence package, persistence decision matrix, transaction/session ownership map, implementation, migration artifacts, repository/UoW tests, database integration tests, concurrency tests, architecture re-check and evidence ledger.
**Verification / Testing:** test repository queries against a real supported database when SQL semantics matter; use unit tests for application/domain behavior with repository ports; test transactions, rollback, constraints, concurrent updates, loading behavior, pagination and migration compatibility; avoid mocks that reproduce ORM behavior inaccurately.
**Failure / Stop conditions:** reject if transaction ownership is ambiguous, sessions are shared unsafely, repositories commit unexpectedly, ORM entities leak across public boundaries without justification, queries create N+1/unbounded loads, migration state is untracked, or retry semantics can duplicate non-idempotent work.
**Positive scenario:** persistence is infrastructure behind explicit transaction boundaries verified against a real supported database.
**Negative scenario:** transaction ownership is ambiguous or sessions are shared unsafely across concurrent tasks.

## Mandatory research gate

Before implementation:
1. Read AGENTS.md and repository contracts.
2. Identify exact Python, SQLAlchemy, database driver, database, migration tool and FastMCP versions.
3. Read official SQLAlchemy 2.x documentation relevant to the feature, especially asyncio, sessions, transactions, pooling, ORM loading and concurrency.
4. Read official migration-tool/database documentation.
5. Read relevant FastMCP lifecycle/Context documentation and official examples.
6. Inspect SQLAlchemy/FastMCP source/tests where semantics are ambiguous.
7. Record evidence before coding.

## Layering

```text
FastMCP adapter
      ↓
Application use case
      ↓
Repository / Unit of Work ports
      ↓
Infrastructure adapters
      ↓
SQLAlchemy AsyncSession
      ↓
Database
```

ORM entities are persistence models, not automatically domain entities or MCP DTOs.

## Transaction boundary

The application use case owns the business transaction boundary. Repository methods should not unexpectedly commit. Define explicitly who begins, commits, rolls back and closes a transaction.

Prefer one coherent unit of work per use-case operation unless the domain explicitly requires multiple independent transactions.

## Async SQLAlchemy

Verify exact async semantics for:
- AsyncEngine;
- AsyncSession;
- async sessionmaker;
- transaction context managers;
- connection pooling;
- `expire_on_commit` behavior;
- implicit IO/lazy loading;
- concurrent task/session safety.

Never share an `AsyncSession` concurrently between independent asyncio tasks unless the exact documented semantics and architecture explicitly permit it. Prefer task/request-scoped sessions.

## Query and loading discipline

Prevent N+1 and accidental lazy IO. Choose loading strategy deliberately (`selectinload`, `joinedload`, explicit queries, etc.) based on verified SQLAlchemy behavior and cardinality. Paginate large collections. Avoid unbounded relationship traversal.

## Repository pattern

Repositories express persistence-oriented application ports, not generic CRUD for its own sake. Do not create abstractions that merely mirror every SQLAlchemy method. Keep query intent explicit.

## Unit of Work

Use Unit of Work only where it clarifies transaction coordination. It must not become a service locator or god object. Its lifecycle and ownership must be explicit.

## Concurrency

Research and test:
- isolation levels;
- optimistic concurrency/version columns;
- pessimistic locks where required;
- unique constraints;
- deadlocks;
- serialization failures;
- retries and idempotency;
- transaction boundaries;
- connection pool exhaustion.

Retries must be narrowly scoped and only applied to errors proven transient and safe to replay.

## Migrations

Schema changes are versioned artifacts. Review forward migration, downgrade strategy where supported, data migration/backfill, locking, deployment ordering and backward compatibility. Never modify production schema manually as an untracked workaround.

## Database security

Use least-privilege credentials. Parameterize queries through SQLAlchemy APIs. Treat database constraints as a second line of integrity protection, not a replacement for application authorization. If PostgreSQL RLS/multi-tenancy is used, document policy ownership and identity propagation.

## Testing

Test repository queries against a real supported database when SQL semantics matter. Use unit tests for application/domain behavior with repository ports. Test transactions, rollback, constraints, concurrent updates, loading behavior, pagination and migration compatibility. Avoid mocks that reproduce ORM behavior inaccurately.
