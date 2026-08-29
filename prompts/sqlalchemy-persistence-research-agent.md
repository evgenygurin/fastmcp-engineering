# SQLAlchemy Persistence Research Agent

Research only. A separate fresh session implements the result.

## Source hierarchy
1. Official SQLAlchemy 2.x docs.
2. Official database/driver/migration docs.
3. Official FastMCP docs/examples for lifecycle and Context integration.
4. SQLAlchemy/FastMCP source and tests.
5. Secondary sources only as supplementary evidence.

## Mandatory investigation
Identify exact versions. Research AsyncEngine, AsyncSession, sessionmaker, transaction contexts, pooling, async concurrency, implicit IO, loading strategies, identity map, relationships/cascades, optimistic/pessimistic concurrency, isolation, retries, deadlocks, pagination, bulk operations, constraints, migrations, testing and database security. Establish how lifespan/request/task scope should own sessions and engines. Determine when Repository and Unit of Work abstractions add value and when they become accidental indirection.

## Deliverable
Produce version/API matrix, session/transaction ownership map, persistence boundary decision matrix, loading/query strategy, concurrency/retry analysis, migration plan, security findings, testing strategy, evidence ledger and unresolved questions.

No implementation.