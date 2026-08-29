---
name: performance-resource-engineering
description: Evidence-first performance engineering for FastMCP and PydanticAI systems, focused on latency, throughput, resource budgets and measurement.
---

# Performance / Resource Engineering

## Research gate
Read repository skills and identify exact versions. Read official FastMCP, MCP, PydanticAI, SQLAlchemy, async runtime and HTTP client documentation for concurrency, streaming, transport, lifecycle, pooling and limits. Inspect official examples/source/tests where behavior is ambiguous. Measure before optimizing.

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

## Rejection
Reject premature caching, speculative batching, unbounded concurrency, hidden blocking I/O, oversized responses, and complexity whose measured benefit is absent.

## Deliverables
Workload model, SLO/resource budgets, baseline measurements, bottleneck analysis, optimization decision log, benchmarks, regression tests and residual capacity risks.