---
name: performance-resource-engineering
description: Evidence-first performance engineering for FastMCP and PydanticAI systems, focused on latency, throughput, resource budgets and measurement.
---

# Performance / Resource Engineering

## Research gate
Read repository skills and identify exact versions. Read official FastMCP, MCP, PydanticAI, SQLAlchemy, async runtime and HTTP client documentation for concurrency, streaming, transport, lifecycle, pooling and limits. Inspect official examples/source/tests where behavior is ambiguous. Measure before optimizing.

## Trigger / Когда применять

**Scope / When to use:** performance engineering for FastMCP and PydanticAI systems, focused on latency, throughput, resource budgets and measurement.
**Trigger:** optimizing latency or throughput, defining resource budgets, or planning capacity.
**Upstream / Prerequisite:** repository skills read; identified exact versions; a baseline measurement.
**Mission / Goal:** focus performance engineering on latency, throughput, resource budgets and measurement.
**Research / Evidence:** read official FastMCP, MCP, PydanticAI, SQLAlchemy, async runtime and HTTP client documentation for concurrency, streaming, transport, lifecycle, pooling and limits; inspect official examples/source/tests where behavior is ambiguous; measure before optimizing.
**Decision / Selection rules:** prefer simple architecture over speculative optimization; bound concurrency and resource pools; avoid blocking I/O on async paths; avoid N+1 and unbounded result materialization; stream only when it improves the actual contract; keep DB transactions short; cache only with explicit ownership, invalidation, consistency and memory limits; treat model latency as variable with deadlines and graceful degradation; follow baseline → profile → one variable → benchmark → regression test → document trade-off; measure p50/p95/p99, not averages alone.
**Version / Compatibility:** identify exact versions.

## Deliverables

**Deliverables / Artifacts:** workload model, SLO/resource budgets, baseline measurements, bottleneck analysis, optimization decision log, benchmarks, regression tests and residual capacity risks.
**Verification / Testing:** use reproducible load/benchmark scenarios; test latency, throughput, concurrency, memory, pool exhaustion, large payloads and degradation; track regressions in CI where benchmarks are stable enough; otherwise run scheduled performance tests.
**Failure / Stop conditions:** reject premature caching, speculative batching, unbounded concurrency, hidden blocking I/O, oversized responses, and complexity whose measured benefit is absent.
**Positive scenario:** an optimization is driven by baseline measurement and passes a regression test.
**Negative scenario:** speculative optimization or unbounded concurrency is introduced without a measured benefit.

## Model
Define workload, SLOs, latency percentiles, throughput, concurrency, memory/CPU budgets and dependency bottlenecks. Separate application latency from model/network/database latency.

## Rules
- Prefer simple architecture over speculative optimization.
- Bound concurrency and resource pools.
- Avoid blocking I/O on async paths.
- Avoid N+1 and unbounded result materialization.
- Stream only when it improves the actual contract; do not stream to hide poor architecture.
- Keep DB transactions short.
- Cache only with explicit ownership, invalidation, consistency and memory limits.
- Never cache authorization-sensitive data across tenants without a proven isolation key.
- Avoid duplicate model/MCP calls through deterministic orchestration and memoization only where semantics permit.
- Treat model latency as variable; enforce deadlines and graceful degradation.
- Measure p50/p95/p99, not averages alone.

## Optimization workflow
Baseline → profile → identify dominant cost → formulate hypothesis → change one variable → benchmark → regression test → document trade-off. Do not optimize without evidence.

## Capacity
Define limits for requests, concurrent tool calls, model calls, DB sessions, response size, memory and queues. Derive capacity from measured workload, not arbitrary constants.

## Verification
Use reproducible load/benchmark scenarios. Test latency, throughput, concurrency, memory, pool exhaustion, large payloads and degradation. Track regressions in CI where benchmarks are stable enough; otherwise run scheduled performance tests.
