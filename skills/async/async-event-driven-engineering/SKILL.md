---
name: async-event-driven-engineering
description: Design asynchronous FastMCP systems with correct lifecycle, cancellation, delivery semantics, idempotency, and backpressure — use for async/background work.
---

# Async / Event-Driven Engineering

## Mission
Design asynchronous FastMCP systems without losing lifecycle correctness, cancellation, delivery semantics, idempotency, ordering, backpressure, or observability.

## Trigger / Когда применять

**Scope / When to use:** asynchronous FastMCP systems and async/background or event-driven work.
**Trigger:** designing or changing async/background work, durable jobs, event publishing/consumption, cancellation, delivery semantics, or backpressure.
**Upstream / Prerequisite:** identified exact versions; research evidence on lifecycle, cancellation, and delivery semantics from official sources.
**Mission / Goal:** design asynchronous FastMCP systems without losing lifecycle correctness, cancellation, delivery semantics, idempotency, ordering, backpressure, or observability.
**Research / Evidence:** identify exact versions and read official documentation/specification for FastMCP, MCP, Python asyncio, PydanticAI, SQLAlchemy, the selected broker/queue, and transport/runtime; read official examples and source/tests for ambiguous lifecycle semantics; record evidence and unresolved questions.
**Decision / Selection rules:** separate request-scoped MCP work from durable/background work; prefer structured concurrency with explicit task ownership; treat cancellation as a control signal; use a durable queue/job store for work that must survive request termination; explicitly classify delivery semantics (assume at-least-once unless proven otherwise); evaluate transactional outbox/inbox; require bounded capacity and backpressure; bound retries and define dead-letter behavior.
**Version / Compatibility:** identify exact versions; if protocol-level Tasks are used, verify the exact MCP/FastMCP version and semantics before implementation.

## Deliverables

**Deliverables / Artifacts:** async design with event contracts (versioned public contracts with stable identifiers and schema version), delivery-semantics classification, ordering/backpressure policy, retry/dead-letter policy, shutdown/recovery plan, tests, evidence ledger and unresolved questions.
**Verification / Testing:** test cancellation, client disconnect, timeout, task failure propagation, duplicate delivery, retry exhaustion, poison messages, ordering violations, queue saturation, worker crash, restart recovery, outbox/inbox consistency and graceful shutdown; use real broker/DB integration tests where mocks cannot prove delivery or transaction semantics.
**Failure / Stop conditions:** reject designs with orphaned tasks, unbounded queues, swallowed cancellation, implicit delivery guarantees, non-idempotent consumers under at-least-once delivery, long DB transactions around remote work, infinite poison-message retries, or durable work stored only in process memory.
**Positive scenario:** an async design with structured concurrency and idempotent consumers survives cancellation, duplicate delivery, and crash recovery.
**Negative scenario:** durable work is stored only in process memory and is lost on restart, or a non-idempotent consumer duplicates side effects.

## Mandatory research gate
Before implementation, identify exact versions and read official documentation/specification for FastMCP, MCP, Python asyncio, PydanticAI, SQLAlchemy, the selected broker/queue, and transport/runtime. Read official examples and source/tests for ambiguous lifecycle semantics. Record evidence and unresolved questions. Secondary articles are supplementary only.

## Core model
Separate request-scoped MCP work from durable/background work. An MCP request must not be kept open merely because a durable job can continue asynchronously. If protocol-level Tasks are used, verify the exact MCP/FastMCP version and semantics before implementation.

## Structured concurrency
Prefer Python `asyncio.TaskGroup` or the runtime's documented structured-concurrency primitive. Child tasks have explicit ownership, cancellation and failure propagation. Avoid orphaned `create_task()` calls. Every background task needs an owner, lifecycle, shutdown policy and exception observation.

## Cancellation
Cancellation is a control signal, not an ordinary business exception. Propagate it through application and infrastructure boundaries and ensure cleanup with async context managers/finally. Do not swallow cancellation to force work to finish. Define behavior for client disconnect, request deadline and shutdown.

## Durable work
For work that must survive request termination, use a durable queue/job store rather than in-memory background tasks. Persist state before acknowledging work when required. Define job state transitions, retry policy, idempotency key, deduplication and crash recovery.

## Delivery semantics
Explicitly classify every message/operation as at-most-once, at-least-once, or another proven guarantee. Assume at-least-once unless infrastructure proves otherwise. Exactly-once is not a default property. Consumers must be idempotent where duplicates are possible.

## Transactional boundaries
For DB-backed event publication, evaluate transactional outbox/inbox patterns. Do not publish an event and commit unrelated state in a way that can leave the system inconsistent. Do not hold DB transactions open while waiting on brokers, LLMs, MCP servers or HTTP APIs.

## Ordering
Define ordering key and scope. Do not assume global ordering from a partitioned/distributed broker. If order matters, encode sequence/version and reject or buffer stale/out-of-order events according to a documented policy.

## Backpressure
All producers and consumers require bounded capacity. Prefer bounded queues, worker concurrency limits and explicit overload behavior. Never use an unbounded in-memory queue as a production reliability strategy.

## Retry / poison messages
Retries are bounded and owned by one layer. Use backoff/jitter where justified. Poison messages must not loop forever; define dead-letter/quarantine behavior and operator visibility. Preserve message identity and correlation data.

## Event contracts
Events are versioned public contracts. Use explicit Pydantic models or protocol schemas, stable identifiers, schema version, event type, timestamp, correlation/causation IDs and producer metadata where useful. Validate at boundaries. Prefer additive evolution and define compatibility policy before changing required fields.

## MCP integration
Treat remote MCP servers and tools as external asynchronous dependencies. Bound calls, propagate deadlines, observe cancellation, and isolate resources. Do not let a slow remote server exhaust worker capacity. Use protocol-level asynchronous features only after exact-version research.

## PydanticAI integration
Agent/model calls are bounded work. Tool retries must not duplicate side effects. For long-running agent workflows, separate orchestration state from the MCP request lifecycle and persist state when recovery is required.

## SQLAlchemy integration
An `AsyncSession` is task-scoped and must not be shared concurrently across independent asyncio tasks. Keep transaction scope short. Pass explicit data/results between tasks instead of sharing mutable sessions.

## Shutdown / recovery
Graceful shutdown must stop intake, signal workers, drain bounded work within a deadline, cancel remaining work, close transports/DB pools and persist/requeue unfinished durable jobs according to documented semantics. Startup recovery must reconcile incomplete states and avoid duplicate side effects.

## Testing
Test cancellation, client disconnect, timeout, task failure propagation, duplicate delivery, retry exhaustion, poison messages, ordering violations, queue saturation, worker crash, restart recovery, outbox/inbox consistency and graceful shutdown. Use real broker/DB integration tests where mocks cannot prove delivery or transaction semantics.
