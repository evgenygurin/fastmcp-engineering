---
name: resilience-reliability-engineering
description: Evidence-first reliability engineering for FastMCP, PydanticAI, database and external-service workflows, covering deadlines, retries, idempotency, concurrency, backpressure, degradation and recovery.
---

# Resilience / Reliability Engineering

## Mission
Design explicit failure boundaries so transient failures do not become duplicated side effects, resource exhaustion, cascading failures or silent data corruption.

## Mandatory research gate
Before implementation:
1. Read repository architecture, security, testing and configuration contracts.
2. Identify exact versions of Python, FastMCP, PydanticAI, HTTP/DB clients and runtime infrastructure.
3. Read official documentation for timeout/deadline, cancellation, connection pooling, retry and concurrency semantics of every relevant dependency.
4. Read FastMCP/FastMCP Client transport and lifecycle documentation for the exact version.
5. Read PydanticAI model/tool retry, usage-limit and cancellation semantics.
6. Read database/driver transaction and pooling documentation.
7. Inspect official examples/source/tests for ambiguous behavior.
8. Record evidence, failure assumptions and unresolved questions.

Never add generic retries without mapping the actual failure domain and side-effect semantics.

## Reliability model
For every external boundary define:
- deadline/timeout;
- cancellation behavior;
- retryability;
- retry budget;
- backoff/jitter;
- idempotency strategy;
- concurrency limit;
- resource limit;
- error classification;
- observability;
- fallback/degradation;
- recovery behavior.

## Failure domains
Treat MCP transport, remote MCP server, LLM provider, HTTP API, database, queue and local process as distinct failure domains. A failure in one must not automatically exhaust unrelated resources.

## Deadlines and timeouts
Prefer end-to-end deadlines propagated through request-scoped context over unrelated nested timeouts. Every network/DB/model operation must have an intentional bound unless the API explicitly requires another lifecycle. Cancellation must reach underlying operations and release resources.

## Retries
Retry only transient failures with bounded attempts/time/budget and exponential backoff plus jitter where appropriate. Do not retry validation errors, authorization failures, deterministic business rejections or non-idempotent side effects unless an explicit idempotency mechanism makes replay safe.

Avoid retry multiplication across layers. One logical operation should have a clear retry owner/budget.

## Idempotency / deduplication
Any operation that can produce an external or persistent side effect must define replay semantics. Use idempotency keys, unique constraints, state machines or transactional outbox/inbox patterns where justified. Never claim exactly-once execution when the infrastructure only provides at-least-once behavior.

## Concurrency / resource isolation
Bound concurrent model calls, MCP calls, HTTP calls, DB work and expensive CPU operations. Use semaphores/pools/queues only with documented ownership and metrics. Avoid unbounded task creation. Keep DB sessions request/task scoped.

## Backpressure / load shedding
Define behavior when capacity is exhausted: queue, reject, shed optional work or degrade. Do not hide overload behind unbounded queues. Preserve critical operations over optional enrichment.

## Circuit breakers / bulkheads
Introduce circuit breakers or bulkheads only where the failure mode and traffic pattern justify their state complexity. Define open/half-open/closed semantics, probe limits and recovery. Do not implement a circuit breaker as decorative retry logic.

## Graceful degradation
Classify capabilities as critical, optional and best-effort. Degrade explicitly and observably. Never return apparently successful authoritative data after silently dropping a critical operation.

## FastMCP / MCP
Respect transport lifecycle, cancellation and client/server ownership. Remote MCP calls are untrusted external dependencies and may fail, hang, return malformed data or change availability. Bound their execution and isolate their resources. Do not let remote tool failures bypass application authorization.

## PydanticAI
Bound model calls, tool calls and usage. Ensure model/tool retries cannot duplicate side effects. Use deterministic application-level idempotency rather than relying on the LLM to remember that an operation already happened.

## Database
Transactions must have bounded scope. Never hold DB transactions open while waiting for an LLM, remote MCP server or unrelated network operation unless explicitly justified. Handle deadlocks/serialization conflicts according to the database/driver's documented retry semantics.

## Recovery
Define startup recovery, shutdown behavior, in-flight operation cancellation, retry exhaustion, partial failure and replay. Durable state transitions must be explicit.

## Testing
Test each failure mode deterministically: timeout, cancellation, transient failure, permanent failure, retry exhaustion, duplicate delivery, concurrent contention, pool exhaustion, overload, partial dependency failure and recovery. Use fault injection/fakes at boundaries and real integration tests for DB/transport semantics where mocks cannot prove behavior.

## Rejection criteria
Reject if timeouts are absent at external boundaries, retries are unbounded or duplicated across layers, side effects lack replay semantics, concurrency is unbounded, queues can grow without bound, transactions span unrelated remote calls, failures are swallowed, or degradation returns misleading success.

## Deliverables
Failure-domain map, deadline budget, retry matrix, idempotency model, concurrency/resource budget, overload policy, degradation strategy, recovery model, failure-injection tests, implementation and verification report.