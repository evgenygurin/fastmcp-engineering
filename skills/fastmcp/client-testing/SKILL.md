---
name: fastmcp-client-testing
description: Build evidence-first FastMCP verification using the official Client, protocol-level integration tests, transport tests, security tests, and deterministic architecture verification.
---

# FastMCP Client / Testing

## Mission

Verify an MCP server at the correct abstraction level. Unit tests prove local logic; FastMCP Client tests prove MCP-facing contracts; transport tests prove deployment boundaries; security and lifecycle tests prove operational guarantees.

## Trigger / Когда применять

**Scope / When to use:** FastMCP verification using the official Client, protocol-level integration tests, transport tests, security tests, and deterministic architecture verification.
**Trigger:** verifying an MCP server at the correct abstraction level; before implementation or test design.
**Upstream / Prerequisite:** `AGENTS.md` and all engineering contracts read; identified exact FastMCP and Python versions; evidence recorded before writing tests.
**Mission / Goal:** verify an MCP server at the correct abstraction level — unit tests prove local logic, Client tests prove MCP-facing contracts, transport tests prove deployment boundaries, security and lifecycle tests prove operational guarantees.
**Research / Evidence:** read official FastMCP testing/client documentation; inspect relevant official PrefectHQ/fastmcp examples; inspect source/tests where semantics are ambiguous; check MCP specification/SEP material for protocol assertions; check first-party dependency testing guidance; never invent Client APIs, transport semantics, session behavior, or lifecycle guarantees from memory.
**Decision / Selection rules:** use the cheapest test that proves the requirement but do not substitute lower-level tests for protocol behavior; use the documented FastMCP Client as the primary MCP contract seam; test only transports the product actually supports; use fixtures with explicit ownership and avoid global mutable state; do not weaken assertions merely to eliminate flakiness.
**Version / Compatibility:** identify exact FastMCP and Python versions; verify the exact target-version Client methods and lifecycle behavior first.

## Deliverables

**Deliverables / Artifacts:** a verification report recording exact versions, sources inspected, test layers executed, exact commands, pass/fail results, known gaps, flaky behavior and diagnosis, architecture verification, security verification, and transport limitations.
**Verification / Testing:** test initialize/session negotiation, tools/list and tools/call, resources and templates, prompts, schemas and structured output, errors, authentication, progress/cancellation/tasks, subscriptions/streaming, and pagination where applicable; never claim a test passed unless it was actually executed.
**Failure / Stop conditions:** reject tests that only assert private implementation details for MCP contracts, mocking FastMCP so extensively that no MCP behavior is exercised, sleep-based synchronization when an observable readiness primitive exists, shared global state across unrelated tests, weakened assertions, coverage percentage treated as proof of correctness, calling an in-process test an E2E test, and testing auth only at the service layer while leaving MCP discovery/invocation untested.
**Positive scenario:** an MCP server is verified at the correct abstraction level with Client and transport tests that actually pass.
**Negative scenario:** an in-process test is called an E2E test and protocol/transport/security behavior goes unverified.

## Mandatory research gate

Before implementation or test design:

1. Read `AGENTS.md` and all engineering contracts.
2. Identify exact FastMCP and Python versions.
3. Read official FastMCP testing/client documentation.
4. Inspect relevant official PrefectHQ/fastmcp examples.
5. Inspect source/tests where semantics are ambiguous.
6. Check MCP specification/SEP material for protocol assertions.
7. Check first-party dependency testing guidance.
8. Record evidence before writing tests.

Never invent Client APIs, transport semantics, session behavior, or lifecycle guarantees from memory.

## Verification pyramid

```text
                  E2E / deployed
                       ▲
                 transport tests
                       ▲
              MCP Client integration
                       ▲
          component/application tests
                       ▲
              domain unit tests
```

Use the cheapest test that proves the requirement, but do not substitute lower-level tests for protocol behavior.

## FastMCP Client

Use the documented FastMCP Client as the primary MCP contract seam where practical. Verify the exact target-version methods and lifecycle behavior first.

Test protocol-visible behavior including:

- initialize/session negotiation;
- tools/list and tools/call;
- resources/list, resources/read and templates where applicable;
- prompts/list and prompts/get;
- schemas and structured output;
- annotations/metadata where relevant;
- errors;
- authentication;
- progress/cancellation/tasks where supported;
- subscriptions/streaming where supported;
- pagination where applicable.

## Transport matrix

Test only transports that the product actually supports, but establish the transport contract explicitly:

| Boundary | What it proves |
|---|---|
| In-process | server behavior without network noise |
| stdio | process/stream protocol integration |
| Streamable HTTP | HTTP transport, sessions/auth/lifecycle |
| deployed HTTP | real deployment boundary |

Do not claim an in-process test proves HTTP deployment correctness.

## Fixtures and determinism

Fixtures must have explicit ownership and cleanup. Avoid global mutable state. Prefer isolated server instances, unique test data, deterministic clocks/IDs where needed, and controlled dependency overrides.

Do not weaken assertions merely to eliminate flakiness. Diagnose shared state, timing, concurrency, network, or lifecycle causes.

## Contract testing

For each MCP-facing component define:

- discovery contract;
- input schema contract;
- output contract;
- error contract;
- authorization contract;
- lifecycle assumptions;
- side-effect/idempotency contract.

Test the contract rather than implementation details.

## Security testing

At the MCP boundary test:

- unauthenticated access;
- invalid credentials;
- expired credentials;
- insufficient scopes/roles;
- tenant isolation;
- tool/resource discovery leakage;
- authorization at invocation time;
- malformed/untrusted input;
- token/header redaction in logs;
- fail-closed behavior.

## Lifecycle / concurrency

Where applicable test startup/shutdown, resource cleanup, cancellation, timeout, concurrent requests, background tasks, and graceful termination. Never rely on process-local tests to prove distributed durability.

## Property / fuzz testing

Use property-based or fuzz testing where input-space risk justifies it: schema validation, URI parsing, pagination tokens, malformed protocol inputs, authorization edge cases, and serialization boundaries. Do not add property tests solely for coverage metrics.

## Test anti-patterns

Reject:

- tests that only assert private implementation details for MCP contracts;
- mocking FastMCP itself so extensively that no MCP behavior is exercised;
- sleep-based synchronization when an observable readiness/completion primitive exists;
- shared global server/client state across unrelated tests;
- tests that pass only because assertions were weakened;
- treating coverage percentage as proof of correctness;
- calling an in-process test an E2E test;
- testing auth only at the service layer while leaving MCP discovery/invocation untested.

## Verification report

Every implementation session must report:

- exact versions;
- sources inspected;
- test layers executed;
- exact commands;
- pass/fail results;
- known gaps;
- flaky behavior and diagnosis;
- architecture verification;
- security verification;
- transport limitations.

Never claim a test passed unless it was actually executed.