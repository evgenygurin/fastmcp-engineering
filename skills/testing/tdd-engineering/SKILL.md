---
name: testing-tdd-engineering
description: Evidence-first testing and TDD engineering for FastMCP, PydanticAI, SQLAlchemy and production Python services.
---

# Testing / TDD Engineering

## Mission
Build a test system that proves behavior, contracts, failure handling and architecture without making the suite slow, flaky, provider-dependent or coupled to implementation details.

## Mandatory research gate
Before implementation:
1. Read repository architecture, security, reliability and configuration contracts.
2. Identify exact Python, pytest, FastMCP, PydanticAI, SQLAlchemy and database-driver versions.
3. Read official pytest documentation for fixtures, parametrization, markers, collection, monkeypatching, async testing and plugin behavior.
4. Read official PydanticAI testing documentation and source/tests for TestModel, FunctionModel, Agent.override and request blocking.
5. Read official FastMCP testing/client/server documentation and examples for the exact version.
6. Read SQLAlchemy testing/async transaction documentation and PostgreSQL integration requirements.
7. Inspect official examples/source/tests for version-sensitive behavior.
8. Record evidence and unresolved questions.

Do not infer framework testing semantics from generic pytest knowledge when official framework guidance exists.

## TDD
For behavior-changing implementation, write a failing test that expresses the desired contract, implement the minimum behavior, then refactor. Do not write meaningless tests solely to satisfy coverage. When research or architecture work cannot sensibly start with a test, document why and establish contract tests before implementation.

## Test taxonomy
Use explicit categories:
- unit: pure domain/application logic;
- component: application components with controlled adapters;
- contract: MCP/tool/API/schema contracts;
- integration: real DB/transport/framework behavior;
- end-to-end: critical user/system workflows;
- resilience/failure: timeout, cancellation, retry, duplicate, overload;
- security: authorization, tenant isolation, injection and tool trust boundaries;
- property-based/fuzz: parsers, schemas, invariants where valuable.

Do not confuse a mock-heavy unit test with an integration test.

## Test pyramid and boundaries
Keep the fast deterministic suite broad. Keep expensive real-provider, network and end-to-end tests narrow and separately selectable. Tests should fail for behavioral regressions, not refactors that preserve contracts.

## pytest fixtures
Fixtures must be explicit, modular and scoped to lifecycle needs. Prefer function scope for mutable state. Use broader scopes only for genuinely immutable/isolated resources. Avoid autouse fixtures that hide important setup. Cleanup must be guaranteed through fixture finalization/context managers.

Parametrize behavior rather than duplicating test bodies. Give important parameter sets readable IDs. Avoid shared mutable parameter objects.

## Async testing
Use the current documented pytest-asyncio/async testing mode for the exact stack. Never share an AsyncSession across concurrent tasks. Test cancellation and cleanup explicitly.

## PydanticAI
Normal CI must not make live model requests. Use TestModel or FunctionModel for deterministic tests and `Agent.override` for controlled replacement of models/dependencies/toolsets. Configure documented request blocking such as `ALLOW_MODEL_REQUESTS=False` where appropriate. Verify tool availability, arguments, structured output, validation/retry paths, usage limits and failures. Real providers belong in controlled integration tests.

## FastMCP
Test tool/resource/prompt schemas and behavior at the MCP boundary using the documented FastMCP testing/client mechanisms. Add protocol/contract tests where client/server interoperability matters. Test authentication/authorization independently from handler business logic. Test lifecycle, cancellation and error mapping.

## Database
Use mocks for repository-independent application behavior, but use a real PostgreSQL integration environment for SQL semantics, constraints, transactions, isolation, locking, RLS, migrations and query behavior that SQLite/in-memory fakes cannot prove. Ensure each test owns its transaction/data lifecycle and parallel tests cannot contaminate one another.

## Assertions
Assert externally meaningful behavior: returned data, state changes, emitted domain events, authorization decisions, tool contracts and error taxonomy. Avoid asserting private attributes, exact call counts or incidental implementation structure unless that interaction is itself a contract.

## Determinism / flakiness
No sleeps as synchronization. Control clocks, randomness, IDs and external responses. Detect order dependence. Bound all external operations. Isolate environment variables and process-global state. Re-run flaky tests and identify the race before changing timing.

## Coverage
Coverage is a diagnostic, not a quality target. Require meaningful coverage of critical branches, authorization, failure paths, transaction boundaries and security-sensitive behavior. Do not lower quality by gaming line coverage.

## Architecture tests
Where practical, enforce dependency direction and forbidden imports with architecture checks. A test suite must detect accidental framework/database leakage into domain layers.

## Mutation/property testing
Use mutation testing selectively on high-value domain/security logic. Use property-based tests for invariants and parsers where generated cases provide meaningful defect detection. Do not introduce expensive tooling everywhere without evidence of value.

## Verification
Run formatting, linting, typing, unit/component tests, contract/integration tests and targeted failure/security suites according to the repository's gates. Record exact commands and real results. Separate tests skipped because infrastructure/provider access is unavailable from passing tests.

## Rejection criteria
Reject if CI requires live LLMs, tests rely on sleeps/races, integration behavior is claimed from mocks, fixtures leak state, AsyncSession is shared across concurrent tasks, security boundaries are untested, failures are swallowed, or tests assert implementation details instead of contracts without justification.

## Deliverables
Test strategy, test taxonomy, fixture/lifecycle policy, TDD plan, provider-isolation strategy, MCP contract tests, DB integration strategy, resilience/security test matrix, architecture tests, implementation, verification report and residual-risk register.