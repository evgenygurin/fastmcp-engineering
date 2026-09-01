---
name: fastmcp-middleware
description: Design and implement FastMCP middleware for cross-cutting request/component behavior with explicit ordering, context, error, security, performance, and lifecycle boundaries.
---

# FastMCP Middleware

## Mission

Use middleware for genuinely cross-cutting behavior that applies around MCP execution or protocol/component processing. Do not use middleware as a hidden service layer or a substitute for domain/application architecture.

## Trigger / Когда применять

**Scope / When to use:** FastMCP middleware for cross-cutting request/component behavior with explicit ordering, context, error, security, performance, and lifecycle boundaries.
**Trigger:** designing or adding middleware for cross-cutting behavior around MCP execution or protocol/component processing.
**Upstream / Prerequisite:** `AGENTS.md` and all applicable engineering contracts read; identified exact FastMCP version; evidence recorded before implementation.
**Mission / Goal:** use middleware for genuinely cross-cutting behavior around MCP execution or protocol/component processing; do not use it as a hidden service layer or substitute for domain/application architecture.
**Research / Evidence:** read official FastMCP middleware documentation; inspect relevant official PrefectHQ/fastmcp examples; inspect source/tests for ambiguous or version-sensitive behavior; check MCP specification/SEP material where protocol semantics are relevant; check first-party documentation for directly involved dependencies; never rely on remembered middleware hooks or signatures.
**Decision / Selection rules:** explicitly compare middleware with application service, domain service, Tool/Resource/Prompt implementation, Provider, Transform, Context/DI, Lifespan, framework-native logging/tracing/auth, and infrastructure proxy; middleware wins only when behavior is cross-cutting and belongs at the MCP request/component execution boundary; document ordering whenever more than one middleware is involved; do not add retries, caching or buffering without concrete semantic justification.
**Version / Compatibility:** identify the exact FastMCP version; verify the target-version middleware API.

## Deliverables

**Deliverables / Artifacts:** version-specific research artifact; middleware decision record; chain/order diagram; responsibility and security boundaries; implementation; focused and integration tests; verification evidence; architecture re-check.
**Verification / Testing:** test middleware through observable behavior — downstream invocation, short-circuit behavior, success/exception paths, ordering, context propagation, cancellation/timeouts, security policy behavior, concurrent execution where state exists, and streaming/task behavior where relevant; use documented FastMCP Client/in-process testing mechanisms where appropriate.
**Failure / Stop conditions:** reject if middleware hides feature-specific business logic, persistence, application orchestration, or a missing architecture boundary; if ordering is undocumented where relevant; if a retry can duplicate non-idempotent work; if security semantics are ambiguous; or if the target-version API was not verified.
**Positive scenario:** cross-cutting middleware is placed at the MCP boundary with documented ordering and passes focused tests.
**Negative scenario:** middleware is used to hide feature-specific business logic or a missing architecture boundary.

## Research gate

Before implementation:

1. Read `AGENTS.md` and all applicable engineering contracts.
2. Identify the exact FastMCP version.
3. Read official FastMCP middleware documentation.
4. Inspect relevant official PrefectHQ/fastmcp examples.
5. Inspect source/tests for ambiguous or version-sensitive behavior.
6. Check MCP specification/SEP material where protocol semantics are relevant.
7. Check first-party documentation for directly involved dependencies.
8. Record evidence before implementation.

Never rely on remembered middleware hooks or signatures.

## Decision gate

Explicitly compare middleware with:

- application service/use case;
- domain service;
- Tool/Resource/Prompt implementation;
- Provider;
- Transform;
- FastMCP Context/DI;
- Lifespan;
- framework-native logging/tracing/auth mechanisms;
- infrastructure proxy/gateway.

Middleware wins only when the behavior is cross-cutting and belongs at the MCP request/component execution boundary.

## Responsibility boundary

Appropriate middleware concerns can include cross-cutting concerns such as logging, tracing, metrics, request correlation, policy enforcement, rate limiting, retries where semantically safe, request/response instrumentation, and protocol-aware adaptation when supported by the target API.

Do not put these in middleware merely for convenience:

- domain invariants;
- use-case orchestration;
- persistence queries;
- transaction business policy;
- feature-specific business logic;
- arbitrary dependency construction;
- application DTO mapping unrelated to middleware behavior.

## Chain semantics

Model the chain explicitly:

```text
Inbound request
    ↓
Middleware A
    ↓
Middleware B
    ↓
Component / application boundary
    ↓
Middleware B response/error path
    ↓
Middleware A response/error path
    ↓
Outbound response
```

Document ordering whenever more than one middleware is involved. Identify whether middleware executes before/after downstream behavior, what happens on short-circuit, and how exceptions/results propagate.

## Security

Authentication, authorization, rate limiting, tenant isolation, redaction, and audit behavior have different responsibilities. Do not collapse them into an unspecified `SecurityMiddleware`.

If middleware makes a security decision, document the policy owner, identity source, trust boundary, failure behavior, and whether downstream code may rely on established security context.

## Reliability and performance

Analyze:

- idempotency before retries;
- timeout/deadline propagation;
- cancellation propagation;
- backpressure;
- concurrency safety;
- statefulness;
- memory growth;
- logging/metrics overhead;
- exception handling;
- streaming behavior;
- task/background execution where applicable.

Do not add retries, caching, or buffering without a concrete semantic justification.

## Testing

Test middleware through observable behavior where practical. Include:

- downstream invocation;
- short-circuit behavior;
- success path;
- exception path;
- ordering;
- context propagation;
- cancellation/timeouts where relevant;
- security policy behavior;
- concurrent execution where state exists;
- streaming/task behavior where relevant.

Use documented FastMCP Client/in-process testing mechanisms where appropriate.
