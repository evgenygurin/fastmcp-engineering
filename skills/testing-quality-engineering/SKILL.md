---
name: testing-quality-engineering
description: Evidence-first testing and quality engineering for production FastMCP systems.
---

# Testing / Quality Engineering

## Mission
Build confidence from executable evidence, not coverage numbers or green unit tests. Test at the lowest useful level and reserve real infrastructure for behavior that cannot be proven with fakes.

## Trigger / Когда применять

**Scope / When to use:** testing and quality engineering for production FastMCP systems.
**Trigger:** designing or changing test strategy, TDD, the test pyramid, MCP protocol tests, contract tests, quality gates, or CI design.
**Upstream / Prerequisite:** identified exact versions; evidence recorded and re-checked before completion.
**Mission / Goal:** build confidence from executable evidence, not coverage numbers or green unit tests; test at the lowest useful level and reserve real infrastructure for behavior that cannot be proven with fakes.
**Research / Evidence:** identify exact Python, FastMCP, Pydantic, SQLAlchemy, MCP SDK, pytest and relevant plugin versions; read current official pytest/FastMCP/Pydantic/SQLAlchemy/MCP documentation and exact-version examples/source/tests before designing tests; record evidence.
**Decision / Selection rules:** use the test pyramid — domain unit tests, application tests, infrastructure integration tests, MCP protocol tests, and end-to-end tests for critical journeys; write a failing test that expresses the contract before behavior-changing implementation; mock at architectural boundaries, not arbitrary internal classes; prefer protocol-level tests for public MCP contracts; use real PostgreSQL for transaction/constraint/locking/query/migration/RLS semantics; use property-based testing for meaningful invariants; snapshot public schemas deliberately; apply mutation testing selectively; treat coverage as diagnostic; keep fixtures explicit, minimal and isolated; test dependency failure modes and security controls at trusted boundaries.
**Version / Compatibility:** identify exact Python, FastMCP, Pydantic, SQLAlchemy, MCP SDK, pytest and relevant plugin versions.

## Deliverables

**Deliverables / Artifacts:** test strategy; test-level matrix; TDD evidence; fixture/factory policy; MCP contract tests; DB integration strategy; property/mutation testing plan; coverage policy; failure/security test matrix; CI quality gates; flakiness policy; evidence ledger; rejected alternatives; verification report.
**Verification / Testing:** before merge run formatting, lint, type checking, unit/integration/contract tests, security checks and any required mutation/property suites; capture exact commands and results; do not suppress failures merely to obtain green CI.
**Failure / Stop conditions:** reject tests that assert implementation details unnecessarily, over-mock framework behavior, depend on ordering, use arbitrary sleeps, only check coverage, blindly update snapshots, omit cleanup, or prove PostgreSQL behavior only with SQLite.
**Positive scenario:** confidence is built from executable evidence across the test pyramid with meaningful contract and integration tests.
**Negative scenario:** coverage numbers or green unit tests are treated as proof while integration behavior is mocked away.

## Mandatory research
Identify exact Python, FastMCP, Pydantic, SQLAlchemy, MCP SDK, pytest and relevant plugin versions. Read current official pytest/FastMCP/Pydantic/SQLAlchemy/MCP documentation and exact-version examples/source/tests before designing tests. Record evidence and re-check version-sensitive behavior before completion.

## Test pyramid
Use domain unit tests for deterministic business rules; application tests for orchestration/authorization/transaction policies; infrastructure integration tests for PostgreSQL/HTTP/queues; MCP protocol tests for discovery/schema/invocation; end-to-end tests for critical user journeys. Do not replace integration behavior with mocks when the behavior depends on real infrastructure semantics.

## TDD
For behavior changes: write a failing test that expresses the contract, implement the smallest correct change, then refactor. Tests must fail for the right reason before implementation when practical. Avoid writing tests after implementation merely to encode existing behavior.

## Test boundaries
Mock at architectural boundaries, not arbitrary internal classes. Prefer fakes/in-memory adapters for application tests when they preserve the port contract. Avoid mocking SQLAlchemy internals, Pydantic internals or FastMCP framework internals unless testing an adapter specifically.

## MCP protocol tests
Test server discovery, tool/resource/prompt metadata, generated schemas, valid and invalid calls, structured outputs, error mapping, authorization and side effects. Prefer protocol-level tests over calling Python functions directly for public MCP contracts.

## Async
Use pytest async facilities appropriate to the installed stack. Ensure each async test has deterministic lifecycle and cleanup. Never share unsafe mutable async resources across tests or tasks. Test cancellation/timeouts and background-task cleanup where applicable.

## Database
Use real PostgreSQL for transaction, constraint, locking, query, migration and RLS semantics. Keep fixtures isolated and deterministic. Test rollback and failure paths. Add query-count assertions for N+1-sensitive operations and EXPLAIN-based checks for genuinely critical queries where practical.

## Property-based testing
Use property-based testing when the input domain has meaningful invariants or combinatorial edge cases: parsers, pagination cursors, validation, normalization, state transitions and idempotency. Properties must describe business invariants, not merely generate random values.

## Contract testing
Snapshot or otherwise assert generated public schemas deliberately. Detect accidental breaking changes. Validate representative client compatibility. Keep snapshots reviewed: never blindly update them to make CI green.

## Mutation testing
Use mutation testing selectively on high-value domain/application modules to detect weak assertions. Do not impose mutation testing on generated/framework glue where signal is poor. Treat surviving meaningful mutants as evidence of missing tests.

## Coverage
Coverage is diagnostic, not a target by itself. Require coverage of critical branches/invariants and meaningful mutation/property evidence rather than arbitrary global percentages. A 100% covered bad test suite is still bad.

## Fixtures
Fixtures must be explicit, minimal and isolated. Prefer factories/builders for complex data over giant shared fixtures. Never depend on test execution order. Make time, randomness, IDs and external calls controllable.

## Failure testing
Test dependency timeout, connection loss, malformed dependency response, rate limit, cancellation, duplicate delivery, ambiguous commit, exporter failure and partial side effects where relevant. Verify graceful degradation and cleanup.

## Security tests
Include unauthorized access, cross-tenant access, injection, secret leakage, sensitive telemetry, resource exhaustion and prompt-injection/indirect-exfiltration cases where applicable. Security controls must be tested at trusted boundaries, not only through happy-path MCP calls.

## Quality gates
Before merge run formatting, lint, type checking, unit/integration/contract tests, security checks and any required mutation/property suites. Capture exact commands and results. Do not suppress failures merely to obtain green CI.

## CI design
Keep fast deterministic checks on every change; partition expensive integration/e2e/security jobs deliberately. Pin or constrain dependency versions reproducibly. Ensure CI uses the same important database/runtime semantics as production.

## Flakiness
A flaky test is a defect in the test system. Quarantining must be explicit, temporary and tracked. Never add arbitrary sleeps as synchronization. Use deterministic polling/events and bounded timeouts.
