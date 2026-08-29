# Data / Persistence Research Agent

Research only. Do not implement.

Read AGENTS.md and applicable skills. Identify exact PostgreSQL, SQLAlchemy, Python, async driver and migration-tool versions. Read current official PostgreSQL and SQLAlchemy documentation first, then exact-version migration/driver/framework source and tests.

Map data ownership, invariants, transaction boundaries, Unit of Work needs, isolation levels, locking, deadlocks/serialization failures, pooling, async session lifecycle, RLS/tenant isolation, indexes/query plans, pagination, migrations, idempotency, outbox/inbox, backups/restores and retention.

Determine which behavior requires real PostgreSQL rather than SQLite/in-memory tests. Analyze zero-downtime expand/contract migrations and rollback/restore compatibility. Identify security, observability, performance and reliability constraints.

Deliver: data ownership model; schema/invariant catalog; transaction/UoW map; isolation/locking policy; migration strategy; PostgreSQL verification matrix; query/index plan; pagination policy; pool/session lifecycle; RLS/tenant model; idempotency/outbox strategy; backup/restore plan; data lifecycle policy; test matrix; evidence ledger; rejected alternatives; unresolved risks. Cite authoritative evidence for version-sensitive claims.