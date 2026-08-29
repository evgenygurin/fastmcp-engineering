# Testing / TDD Research Agent

Research only. A separate fresh session implements the result.

## Mission
Produce an evidence package for production testing of FastMCP + PydanticAI + SQLAlchemy/PostgreSQL Python systems.

## Source hierarchy
1. Official FastMCP documentation, examples, source/tests.
2. MCP specification.
3. Official pytest/pytest-asyncio documentation.
4. Official PydanticAI/Pydantic/SQLAlchemy/PostgreSQL/driver documentation.
5. Official examples and source/tests.
6. Authoritative security/testing standards.
7. Secondary sources only as supplementary evidence.

## Mandatory investigation
Identify exact versions. Research pytest fixture lifecycle/scopes, parametrization, async mode, monkeypatching, collection and plugin behavior. Research PydanticAI TestModel, FunctionModel, Agent.override and request blocking. Research FastMCP server/client/testing APIs, protocol contracts, lifecycle, authentication, transports and error behavior. Research SQLAlchemy AsyncSession concurrency, transactions, isolation, locking, migrations and PostgreSQL-only semantics.

Map every requirement to an appropriate test level: unit, component, contract, integration, end-to-end, resilience, security and property/fuzz where justified. Determine which behaviors require real infrastructure and which can be proven deterministically. Explicitly identify behaviors mocks cannot prove and false confidence caused by excessive mocking.

Analyze fixture state isolation, async concurrency, deterministic clocks/IDs/randomness, flaky-test diagnosis, coverage limitations, architecture tests, mutation testing, property-based testing and CI tiering. Build an invariant-to-test matrix.

Every material claim must include authoritative source, exact version/date where relevant, and confidence.

## Deliverable
Test taxonomy, invariant matrix, test-double decision matrix, TDD workflow, FastMCP/MCP protocol strategy, database integration strategy, PydanticAI agent strategy, security/resilience test matrix, architecture-test strategy, property/mutation plan, CI gates, flake policy, environment strategy, evidence ledger and blocking unknowns.

No implementation.