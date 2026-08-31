---
name: fastmcp-tasks
description: Design FastMCP background task execution with verified MCP semantics, explicit ownership, idempotency, cancellation, persistence, and failure boundaries.
---

# FastMCP Tasks / Background Execution

## Mission

Use FastMCP/MCP task capabilities only when the operation genuinely requires asynchronous or deferred execution. Do not equate a protocol task with `asyncio.create_task()` or a generic job queue.

## Mandatory research gate

Before implementation:

1. Read `AGENTS.md` and all engineering contracts.
2. Identify the exact FastMCP and Python versions.
3. Read official FastMCP task/background execution documentation and current `llms` material.
4. Inspect all relevant official PrefectHQ/fastmcp task examples.
5. Inspect FastMCP source and tests for task state, polling, storage, cancellation, expiry, result retrieval, and lifecycle semantics.
6. Check the MCP specification/SEP material governing tasks.
7. Check first-party dependency documentation for any selected task backend.
8. Record evidence before implementation.

Version-sensitive task behavior is blocking until verified. Never implement from memory.

## Architectural distinction

Keep these concepts separate:

- MCP protocol task;
- FastMCP task abstraction;
- Python coroutine/background task;
- application command/use case;
- durable job;
- queue message;
- worker execution;
- task result store.

A protocol task may coordinate execution, but it does not automatically provide durable distributed job processing.

## Decision gate

Choose deferred execution only when there is a concrete requirement such as long-running work, asynchronous polling, or protocol-level task semantics. For every task design document:

- execution owner;
- task state machine;
- result ownership;
- persistence/durability guarantee;
- cancellation semantics;
- timeout/deadline;
- expiry/TTL;
- retry policy;
- idempotency key or equivalent protection;
- worker/process boundary;
- shutdown behavior;
- observability;
- authorization on creation, polling, and result access.

## State machine

Model task state explicitly from target-version evidence. Do not invent states or transitions.

```text
accepted
 ↓
queued / working
 ├── completed
 ├── failed
 ├── cancelled
 └── expired
```

The actual state set and transitions must come from the verified FastMCP/MCP contract where protocol tasks are involved.

## Cancellation

Cancellation is a semantic operation, not merely calling `Task.cancel()`. Determine what cancellation guarantees exist at the protocol, framework, worker, downstream API, and database layers.

Never report cancellation as successful if downstream work can continue and the contract does not distinguish cancellation request from completed cancellation.

## Retries and idempotency

Never add automatic retries by default. Before retrying determine:

- whether the operation is idempotent;
- whether external side effects can be duplicated;
- whether the task has a stable idempotency identity;
- whether the failure is retryable;
- who owns retry policy.

At-least-once execution must never silently become duplicate business effects.

## Persistence and durability

Explicitly distinguish:

- in-memory state;
- process-local state;
- server-lifespan state;
- shared database state;
- durable queue state;
- externally managed worker state.

Do not claim durability, crash recovery, or cross-worker visibility unless verified and tested.

For multi-worker HTTP deployments, determine whether task state is shared and whether the architecture requires sticky sessions or a shared backend. FastMCP's HTTP deployment model and stateless/session semantics must be checked against the target version.

## Ownership and lifecycle

A background task must have a clear owner. Lifespan shutdown must define what happens to accepted, running, queued, and result-producing tasks.

Never create untracked background work that can outlive the server without an explicit ownership and recovery model.

## Security

Authorization applies to task creation and, separately, task status/result retrieval. A task identifier must not become an authorization bypass or tenant enumeration primitive.

Bind task access to the verified principal/tenant where required. Avoid leaking task arguments, progress, errors, or results across authorization boundaries.

## Observability

Long-running tasks require correlation identifiers and structured state/error telemetry. Do not log credentials, bearer tokens, secrets, or sensitive task arguments/results.

## Testing

At minimum, where applicable test:

- task creation;
- immediate/deferred result behavior;
- state transitions;
- polling;
- completion;
- failure;
- cancellation;
- timeout/deadline;
- expiry/TTL;
- retry/idempotency;
- authorization on status/result;
- concurrent polling;
- worker/process boundaries;
- restart/shutdown behavior;
- persistence recovery;
- MCP Client behavior.

Use FastMCP's documented in-process Client for deterministic protocol tests where appropriate. The current official Client documentation explicitly positions it as a testing seam.

## Hard anti-patterns

- `asyncio.create_task()` with no ownership.
- Treating protocol tasks as a durable queue.
- Automatic retries without idempotency analysis.
- Task IDs that are globally enumerable and authorization-free.
- Storing task state only in process memory while claiming multi-worker durability.
- Letting shutdown silently abandon work.
- Catching every exception and marking tasks successful.
- Putting business retry policy into MCP transport code.

## Deliverables

- version-specific task research package;
- protocol/framework state machine;
- execution ownership model;
- durability matrix;
- cancellation/retry/idempotency decision record;
- security model;
- implementation;
- protocol/client tests;
- lifecycle/restart verification;
- architecture re-check.
