---
name: reliability-resilience-engineering
description: Evidence-first reliability and resilience engineering for production FastMCP systems.
---

# Reliability / Resilience Engineering

## Mission
Keep critical capabilities correct and recoverable under dependency failure, overload, partial failure, restart, duplication and network uncertainty. Resilience mechanisms must preserve security, consistency and bounded resource use.

## Mandatory research
Identify exact Python, FastMCP, SQLAlchemy, PydanticAI, MCP SDK, HTTP client, queue and deployment/runtime versions. Read current official documentation first, then exact-version failure-handling, timeout, cancellation, retry, connection and lifecycle guidance. Record evidence and re-check version-sensitive behavior before completion.

## Reliability model
Define critical user-visible capabilities, dependencies, failure domains, recovery objectives, availability targets and acceptable degraded modes. Distinguish transient, permanent, overload, protocol and data-consistency failures.

## Timeouts
Every remote or potentially blocking operation must have an explicit bounded timeout appropriate to the operation. Propagate deadlines where supported. Never use infinite waits. Timeout values must leave enough budget for cleanup and response handling.

## Retries
Retry only operations that are demonstrably safe or idempotent. Use bounded attempts, exponential backoff and jitter. Respect provider/server retry guidance and `Retry-After` where applicable. Never blindly retry authentication failures, validation failures or known permanent errors.

## Idempotency
Any operation that can create, charge, publish, enqueue, mutate or otherwise cause an external side effect must have an explicit duplicate/replay policy. Use idempotency keys, unique constraints or transactional state where appropriate. Ambiguous outcomes must be handled conservatively.

## Circuit breaking / bulkheads
Use circuit breakers only where they improve failure containment and with clearly defined open/half-open behavior. Isolate scarce or failure-prone dependencies with bounded concurrency, pools, queues or separate worker capacity. Do not add a circuit breaker merely as ceremony.

## Backpressure
All unbounded work sources require admission control, bounded queues or explicit shedding. Under overload prefer predictable bounded failure to memory exhaustion. Preserve authentication, authorization and critical audit behavior during degradation.

## Graceful degradation
Define feature priority and fallback behavior before failures occur. Optional dependencies may be shed; security controls and correctness invariants may not. Fallback data must have explicit freshness/consistency semantics.

## Distributed consistency
Assume network calls can succeed remotely while the local caller times out. Model ambiguous commit/outcome states explicitly. Use transactional outbox/inbox, reconciliation, idempotency or durable state when cross-system consistency requires it. Never claim distributed atomicity without a real protocol providing it.

## Database resilience
Handle transaction rollback, deadlocks, serialization failures, connection loss and pool exhaustion according to PostgreSQL/SQLAlchemy semantics. Retry only safe transaction scopes. Keep transactions bounded and do not hold them across slow external calls.

## Async cancellation
Cancellation is a control signal, not an ordinary exception to swallow. Ensure cleanup runs, resources are released and partially completed side effects have a defined policy. Do not let shielded cleanup become an unbounded shutdown blocker.

## Startup / shutdown
Define readiness separately from liveness. Startup must fail clearly when critical dependencies cannot be initialized. Shutdown must stop intake, drain or cancel owned work, close resources and finish within a bounded budget. Partial startup must clean up already-created resources.

## Recovery
Define restart behavior, durable state recovery, replay handling and reconciliation. Stateless recovery is preferred where practical. Never assume process memory survives a crash.

## Queues / workers
Define delivery semantics: at-most-once, at-least-once or effectively-once through idempotency. Specify visibility timeout/ack behavior, poison-message handling, dead-letter policy and retry limits when queues exist.

## External providers / LLMs
Treat provider outages, throttling, malformed responses, model unavailability and latency spikes as normal failure modes. Bound retries and fallback. Never let fallback providers bypass security, tenant isolation or policy checks. Model-generated content remains untrusted.

## MCP resilience
Protect tool invocations from dependency stalls and overload. Define per-operation timeouts, cancellation and retry policies. Do not expose internal retry storms to MCP clients. Return stable, safe errors while preserving correlation for diagnosis.

## Chaos / fault injection
Test representative failures deliberately: dependency timeout, connection reset, HTTP 5xx, rate limit, malformed response, DB deadlock/serialization failure, process restart, duplicate delivery, cancellation and exporter outage. Prefer targeted deterministic fault injection before broad chaos experiments.

## SLO / error budget
Reliability targets must be tied to user-visible SLIs. Use error budgets to prioritize reliability work and consciously trade feature velocity against reliability. Do not optimize availability by hiding failures or returning incorrect data.

## Observability
Use the observability skill to measure retries, timeout rate, circuit state, queue depth, saturation, recovery time, duplicate operations and degraded-mode usage. Never use high-cardinality failure labels.

## Testing
Test happy path, transient failure, permanent failure, timeout, cancellation, duplicate execution, ambiguous outcome, overload, restart/recovery and degraded mode. Verify invariants after failure, not just returned errors.

## Rejection criteria
Reject infinite timeouts, unbounded retries, retrying unsafe side effects without idempotency, transactions held across remote calls, unbounded queues, swallowed cancellation, fallbacks that bypass policy, fake distributed atomicity and resilience mechanisms without measured failure-containment value.

## Deliverables
Reliability model; dependency/failure matrix; timeout/deadline policy; retry/idempotency policy; circuit/bulkhead design; backpressure/degradation model; distributed-consistency model; DB resilience policy; async cancellation policy; startup/shutdown recovery model; queue semantics; fault-injection plan; SLI/SLO/error-budget model; test matrix; evidence ledger; rejected alternatives; verification report.