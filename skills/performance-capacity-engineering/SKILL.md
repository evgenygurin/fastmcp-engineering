---
name: performance-capacity-engineering
description: Evidence-first performance, capacity and scalability engineering for production FastMCP systems.
---

# Performance / Capacity Engineering

## Mission
Optimize measured user-visible behavior and resource efficiency without sacrificing correctness, security or maintainability. No performance claim is accepted without a baseline and reproducible measurement.

## Mandatory research
Identify exact Python, FastMCP, Pydantic, SQLAlchemy, PydanticAI and relevant runtime/client versions. Read current official documentation first and inspect exact-version examples/source/tests for concurrency, connection pools, async behavior, caching and framework limits. Record evidence and re-check version-sensitive behavior before completion.

## Performance budget
Define measurable budgets for latency, throughput, error rate, memory, CPU, DB connections, external calls and LLM latency/cost where applicable. Tie budgets to user-visible SLIs/SLOs rather than arbitrary microbenchmarks.

## Baseline first
Before optimization establish representative workload, environment, dataset, concurrency, warm/cold state, measurement method and confidence interval/repetition policy. Record p50/p95/p99 where tail latency matters. Do not optimize from intuition or a single timing.

## Bottleneck analysis
Use profiling, traces, query plans, resource metrics and load tests to locate the dominant bottleneck. Distinguish CPU, I/O, lock contention, connection pool exhaustion, serialization, network, database, LLM and queueing effects. Avoid speculative optimization.

## Async/concurrency
Use async concurrency where I/O-bound and supported by dependencies. Bound concurrency explicitly. Avoid blocking calls in async paths. Define cancellation, timeout and backpressure behavior. Never increase concurrency without measuring downstream saturation.

## MCP
Measure MCP discovery and invocation overhead separately from business execution. Set tool-level timeout and concurrency policies according to operation class. Avoid serial orchestration when independent operations can safely run concurrently, but preserve transaction and ordering requirements.

## Database
Use SQLAlchemy query profiling and real PostgreSQL measurements. Eliminate N+1, unnecessary round trips and unbounded result sets. Verify indexes with EXPLAIN/EXPLAIN ANALYZE for critical paths. Tune pool size based on actual workload and DB capacity; more connections are not automatically faster.

## LLM / PydanticAI
Measure time-to-first-token/full completion when relevant, provider latency, retries, token usage and cost. Use model/provider selection, batching, caching or parallelism only when semantic behavior remains correct. Never trade security controls for latency. Treat model output as untrusted.

## Caching
Introduce caching only with a defined key, scope, TTL/invalidation policy, consistency model, memory budget and stampede strategy. Never cache secrets or tenant-specific data across isolation boundaries. Cache correctness is more important than hit rate.

## Batching
Batch only when downstream protocols and semantics support it. Define maximum batch size, latency tradeoff, partial failure behavior and memory bounds. Do not create giant batches that increase tail latency.

## Backpressure
Every potentially unbounded queue must have explicit bounds and overload behavior. Prefer bounded queues, admission control, rate limits and graceful degradation to uncontrolled buffering.

## Resource pools
Treat DB, HTTP, MCP, worker and provider pools as finite resources. Model pool wait time and saturation. Size pools from measured concurrency and downstream capacity. Avoid nested pools that multiply concurrency unexpectedly.

## Memory
Measure allocations, object retention and cache growth. Stream large results where appropriate. Avoid loading unbounded MCP/database/model payloads into memory. Define maximum request/result sizes.

## Load testing
Use representative scenarios for load, stress, spike and soak tests. Identify sustainable throughput, saturation point, recovery time and failure mode. Production-like dependencies are required for conclusions about infrastructure bottlenecks.

## Capacity model
Document expected arrival rate, concurrency, service time, downstream limits, pool sizes and headroom. Use queueing intuition/measurements rather than assuming linear scaling. Revisit the model after major architecture changes.

## Performance regression
Keep stable benchmarks for critical paths and enforce regression thresholds based on noise-aware baselines. Avoid brittle microbenchmark gates when variance is high. Performance CI should fail on meaningful regressions, not normal measurement noise.

## Graceful degradation
When overloaded, prefer bounded failure, reduced optional work, lower concurrency or safe fallback. Define what must remain available and what may be shed. Never silently weaken authorization, validation or audit requirements to improve throughput.

## Observability
Use the observability layer for latency histograms, saturation, queue depth, pool utilization and dependency timing. Do not add high-cardinality metrics merely to diagnose one benchmark.

## Testing
Performance tests must assert correctness as well as speed. Run representative concurrent MCP calls, DB workloads, external dependency failures, cancellation and timeout scenarios. Verify no race, transaction or tenant-isolation regression under load.

## Rejection criteria
Reject optimizations without baseline evidence, unlimited concurrency/queues, unbounded result loading, arbitrary caching, SQLite-only DB performance conclusions, benchmark environments unlike the target deployment, security tradeoffs, and claims based only on average latency.

## Deliverables
Performance budgets; workload model; baseline report; bottleneck analysis; MCP/DB/LLM performance map; concurrency/pool policy; caching policy; batching/backpressure model; memory budget; load/stress/soak plan; capacity model; regression gates; evidence ledger; rejected alternatives; verification report.