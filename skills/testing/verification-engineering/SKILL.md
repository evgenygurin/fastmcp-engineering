---
name: testing-verification-engineering
description: Evidence-first testing and verification engineering for production FastMCP systems across unit, integration, contract, protocol, database, agent, security, property, mutation and end-to-end layers.
---

# Testing / Verification Engineering

## Mission

Tests are executable architecture constraints. Verification must establish correctness at the cheapest layer that can prove the invariant, while reserving real infrastructure for behavior that mocks cannot faithfully establish.

## Trigger / Когда применять

**Scope / When to use:** testing and verification engineering for production FastMCP systems across unit, integration, contract, protocol, database, agent, security, property, mutation and end-to-end layers.
**Trigger:** designing or changing verification strategy, test classes, test doubles, database/async verification, CI gates, or flake control.
**Upstream / Prerequisite:** `AGENTS.md` and repository engineering/testing contracts read; identified exact versions; evidence recorded before changing tests or production code.
**Mission / Goal:** treat tests as executable architecture constraints; verification must establish correctness at the cheapest layer that can prove the invariant, while reserving real infrastructure for behavior that mocks cannot faithfully establish.
**Research / Evidence:** identify exact Python, FastMCP, Pydantic, PydanticAI, SQLAlchemy, database, driver, test framework and server versions; read official documentation for every testing mechanism used; read relevant FastMCP official testing/examples and MCP protocol material; read PydanticAI, SQLAlchemy and dependency testing guidance; inspect source/tests for ambiguous behavior.
**Decision / Selection rules:** use the verification pyramid — the lowest level that can prove the invariant; define explicit test classes (unit, component, integration, contract, protocol, agent, security, property-based, mutation, E2E); choose test doubles by the invariant and prefer simple fakes/stubs; verify DB semantics against a real supported database; test cancellation, timeouts and race-sensitive invariants; test failure modes for each critical dependency; treat coverage as evidence, not the goal; define deterministic CI stages and fail closed on required quality gates; treat every flaky test as a defect until diagnosed.
**Version / Compatibility:** identify exact Python, FastMCP, Pydantic, PydanticAI, SQLAlchemy, database, driver, test framework and server versions.

## Deliverables

**Deliverables / Artifacts:** verification strategy, test taxonomy, invariant-to-test matrix, fixture/fake strategy, integration environment, contract/protocol tests, agent test strategy, security regression suite, property/mutation plan, CI quality gates, flake policy and final verification report.
**Verification / Testing:** define deterministic CI stages such as formatting/lint/type checks, unit tests, component tests, integration tests, security tests and selected E2E; separate expensive/live-provider suites explicitly; fail closed on required quality gates.
**Failure / Stop conditions:** reject if tests assert implementation details instead of contracts, integration behavior is mocked away, protocol compliance is inferred from direct function calls, live LLM/network dependencies are required for normal unit CI, failures are swallowed, flaky tests are permanently ignored, or critical security/database invariants have no executable verification.
**Positive scenario:** verification establishes correctness at the cheapest layer that proves each invariant.
**Negative scenario:** protocol compliance is inferred from direct function calls and integration behavior is mocked away.

## Mandatory research gate

Before implementation:
1. Read AGENTS.md and repository engineering/testing contracts.
2. Identify exact Python, FastMCP, Pydantic, PydanticAI, SQLAlchemy, database, driver, test framework and server versions.
3. Read official documentation for every testing mechanism used.
4. Read relevant FastMCP official testing/examples and MCP protocol material.
5. Read PydanticAI, SQLAlchemy and dependency testing guidance.
6. Inspect source/tests for ambiguous behavior.
7. Record evidence before changing tests or production code.

## Verification pyramid

```text
                 E2E / production-like
                / protocol / security \
               / integration / contract \
              / component / agent / DB  \
             /       unit tests          \
            ------------------------------
             cheapest deterministic proof
```

Use the lowest level that can prove the invariant. Do not create integration tests merely to test pure logic; do not mock away the behavior that is actually under test.

## Test classes

### Unit
Pure domain/application logic, mappings, policies and deterministic transformations. No network/database/LLM.

### Component
A coherent application component with controlled infrastructure seams. Verify lifecycle and interaction contracts without turning every dependency into a mock.

### Integration
Use real supported database/server/framework behavior when SQL, transactions, serialization, protocol or lifecycle semantics matter.

### Contract
Verify MCP schemas, tool/resource/prompt contracts, external API assumptions and compatibility boundaries. Contracts must be derived from authoritative specifications or actual provider contracts.

### Protocol
Exercise the actual FastMCP/MCP transport and message semantics where protocol compliance matters. Do not substitute direct Python function calls for protocol tests.

### Agent
Use deterministic model seams for normal CI. Test dependencies, tools, structured outputs, validators, retries, usage limits, approvals and failure behavior. Live-provider tests belong in a separately controlled suite.

### Security
Test authentication, authorization, tenant isolation, injection, tool poisoning, SSRF, secret leakage and resource limits according to the threat model.

### Property-based
Use when broad input spaces and invariants justify generative testing. Properties must be meaningful, bounded and reproducible.

### Mutation
Use mutation testing selectively to validate whether important assertions actually detect behavioral changes. Do not optimize for a vanity mutation score.

### E2E
Use production-like infrastructure for critical user-visible workflows. Keep the suite small, deterministic and independently diagnosable.

## Test doubles

Choose among stub, fake, mock, spy and real dependency based on the invariant. Prefer simple fakes/stubs over interaction-heavy mocks. Never mock the framework behavior whose correctness is the purpose of the integration test.

## Database verification

Verify migrations, constraints, transaction commit/rollback, isolation/concurrency behavior, loading strategies, pagination, uniqueness and authorization/RLS against a real supported database where semantics differ from Python mocks.

## Async/concurrency verification

Test cancellation, timeouts, task isolation, session ownership, race-sensitive invariants and bounded concurrency where applicable. Never rely on sleeps as synchronization when deterministic synchronization primitives are available.

## Failure testing

For each critical dependency, test timeout, cancellation, malformed response, transient failure, permanent failure and retry/idempotency behavior where applicable. Verify error translation without destroying root-cause observability.

## Coverage

Coverage is evidence, not the goal. Track branch/condition coverage for critical policies and enforce meaningful thresholds only after understanding generated/unreachable code. Review untested architectural paths, not only line percentages.

## CI gates

Define deterministic stages such as formatting/lint/type checks, unit tests, component tests, integration tests, security tests and selected E2E. Separate expensive/live-provider suites explicitly. Fail closed on required quality gates.

## Flake control

Every flaky test is a defect in the test system until diagnosed. Identify nondeterminism source, reproduce, fix root cause and quarantine only with an owner and expiration policy.
