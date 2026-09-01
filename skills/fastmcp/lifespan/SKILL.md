---
name: fastmcp-lifespan
description: Design FastMCP lifecycle management with explicit resource ownership, startup/shutdown ordering, cleanup, composition, cancellation, concurrency, and integration boundaries.
---

# FastMCP Lifespan / Resource Management

## Mission

Use FastMCP lifespan for resources whose ownership follows the server/runtime lifecycle. Treat startup and shutdown as architecture, not incidental plumbing.

## Trigger / Когда применять

**Scope / When to use:** FastMCP lifecycle management with explicit resource ownership, startup/shutdown ordering, cleanup, composition, cancellation, concurrency, and integration boundaries.
**Trigger:** designing or changing lifespan-managed resources, startup/shutdown ordering, cleanup, composition, cancellation, or concurrency.
**Upstream / Prerequisite:** `AGENTS.md` and all engineering contracts read; identified exact FastMCP and Python versions; evidence recorded before implementation.
**Mission / Goal:** use FastMCP lifespan for resources whose ownership follows the server/runtime lifecycle; treat startup and shutdown as architecture, not incidental plumbing.
**Research / Evidence:** read official FastMCP lifespan documentation and `llms` material; inspect relevant official PrefectHQ/fastmcp examples; inspect FastMCP lifespan source and tests for lifecycle, reference counting, nesting, cancellation, and cleanup semantics; inspect Starlette/FastAPI lifecycle documentation when HTTP mounting is involved; check MCP specification/SEP material; check first-party dependency documentation.
**Decision / Selection rules:** document owner, creation point, scope, startup prerequisites, consumers, shutdown ordering, cleanup, failure/cancellation behavior and concurrency guarantees for every resource; compose lifespans predictably by entering resources in dependency order and releasing them in reverse; treat startup failure as requiring cleanup of partially initialized resources; do not create heavyweight clients per tool invocation when their correct scope is server/lifespan-scoped.
**Version / Compatibility:** identify exact FastMCP and Python versions; the current implementation uses an `AsyncExitStack`, composes lifespans, and provides `combine_lifespans` — verify exact target-version semantics rather than copying from memory.

## Deliverables

**Deliverables / Artifacts:** version-specific lifespan research; resource ownership matrix; lifecycle dependency graph; startup/shutdown sequence; failure/cancellation model; implementation; lifecycle integration tests; architecture re-check; reproducible evidence.
**Verification / Testing:** test lifecycle as observable behavior — startup success, startup failure and partial cleanup, shutdown cleanup, cleanup failure, cancellation during teardown, repeated/shared lifecycle entry, composed lifespans and ordering, mounted FastMCP HTTP applications, dependency availability through the Context/DI seam, and concurrent consumers.
**Failure / Stop conditions:** reject if resource ownership is ambiguous, cleanup is not guaranteed, shutdown ordering is undocumented, background tasks are orphaned, request-scoped objects are shared incorrectly, FastMCP HTTP lifespan is dropped during mounting, or implementation depends on unverified version-specific lifecycle behavior.
**Positive scenario:** lifespan-managed resources start, compose and clean up in documented order and pass lifecycle integration tests.
**Negative scenario:** a partially initialized resource is left alive after startup failure or the FastMCP HTTP lifespan is dropped during mounting.

## Mandatory research gate

Before implementation:

1. Read `AGENTS.md` and all engineering contracts.
2. Identify the exact FastMCP and Python versions.
3. Read official FastMCP lifespan documentation and `llms` material.
4. Inspect relevant official PrefectHQ/fastmcp examples.
5. Inspect FastMCP lifespan source and tests for lifecycle, reference counting, nesting, cancellation, and cleanup semantics.
6. Inspect relevant Starlette/FastAPI lifecycle documentation when HTTP mounting is involved.
7. Check MCP specification/SEP material when protocol lifecycle semantics matter.
8. Check first-party dependency documentation for resources being managed.
9. Record evidence before implementation.

The current FastMCP implementation uses an `AsyncExitStack`, composes lifespans, and contains explicit lifecycle handling for mounted/runtime trees; exact behavior is version-sensitive and must be verified rather than copied from memory.

## Resource ownership

For every resource document:

- owner;
- creation point;
- scope;
- startup prerequisites;
- consumers;
- shutdown ordering;
- cleanup operation;
- failure behavior;
- cancellation behavior;
- concurrency guarantees;
- whether it may be shared.

Typical candidates include database engines/pools, HTTP clients, SDK clients, queues/workers, caches, telemetry exporters, and other long-lived infrastructure.

Do not create heavyweight clients per tool invocation when their correct scope is server/lifespan-scoped.

## Composition

Lifespans must compose predictably. Enter resources in dependency order and release them in reverse order. Prefer `AsyncExitStack`/native composition mechanisms where appropriate rather than manually duplicating cleanup logic.

FastMCP provides `combine_lifespans`; the current implementation enters lifespans in order and exits them LIFO, merging yielded mappings with later values overriding earlier keys. Verify exact target-version semantics before relying on this.

When integrating Streamable HTTP with Starlette/FastAPI, preserve the FastMCP app lifespan. Official documentation explicitly requires passing `mcp_app.lifespan` to the outer application because nested lifespans are not automatically recognized in that integration model.

## Failure semantics

Analyze each startup step:

```text
resource A startup
 ↓
resource B startup
 ↓
resource C startup
 ↓
server ready
```

If C fails, A and B must be cleaned up according to the verified lifecycle semantics. Never leave partially initialized resources alive.

Shutdown must remain safe when:

- startup partially failed;
- shutdown is called more than once through framework-managed lifecycle paths;
- cancellation occurs during teardown;
- a cleanup operation itself fails;
- multiple consumers share the runtime tree.

Current FastMCP source explicitly shields teardown from cancellation to allow async cleanup to complete; treat this as evidence to verify against the target release, not a generic rule to reimplement.

## Scope and concurrency

Classify resources as process/application, server/lifespan, session, request, or transient. Verify which scopes are actually supported by the target architecture.

Do not share mutable clients, ORM sessions, transactions, or other non-concurrent-safe objects merely because they are available from lifespan state. Engines/pools and sessions have different ownership models.

## FastMCP Context interaction

Lifespan-owned resources may be exposed through the target version's verified Context/lifecycle mechanism, but the Context must not become a service locator. Application code should depend on explicit ports/interfaces and receive the required dependency explicitly.

## Database rule

For SQLAlchemy:

- normally manage `AsyncEngine`/pool at lifespan scope;
- create `AsyncSession` according to request/unit-of-work scope;
- never share an active session across concurrent requests unless its concurrency semantics explicitly permit it;
- dispose the engine/pool during shutdown.

Exact patterns must be validated against the installed SQLAlchemy version and application architecture.

For Supabase or other SDK clients, determine whether the client is safe and intended for process/server reuse before making it lifespan-scoped. Verify first-party client documentation.

## Background work

Background tasks/workers require explicit ownership. Define startup, cancellation signal, join/drain behavior, timeout policy, and failure reporting. Do not launch orphaned `asyncio.create_task()` work from module import or tool calls.

## Testing

Test lifecycle as observable behavior:

- startup success;
- startup failure and partial cleanup;
- shutdown cleanup;
- cleanup failure;
- cancellation during teardown;
- repeated/shared lifecycle entry where supported;
- composed lifespans and ordering;
- mounted FastMCP HTTP applications;
- dependency availability through the intended Context/DI seam;
- concurrent consumers where shared resources exist.
