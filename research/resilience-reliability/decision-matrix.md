# Resilience / Reliability Decision Matrix

| Concern | Default | Exception requires evidence |
|---|---|---|
| External calls | Explicit timeout/deadline | Truly local non-blocking operation |
| Retry | Bounded + classified | Non-idempotent side effect or deterministic failure |
| Retry owner | One layer per logical operation | Coordinated budget across layers |
| Backoff | Exponential + jitter when contention warrants | Immediate bounded retry for documented semantics |
| Side effects | Idempotency key/constraint/state machine | Explicitly non-retryable operation |
| DB transaction | Short, local transaction | Cross-boundary transaction with explicit design |
| Concurrency | Explicit bounded capacity | Proven safe unbounded work (rare) |
| Queue | Bounded | Explicit durable queue with capacity policy |
| Circuit breaker | Only for useful failure isolation | Simpler bounds sufficient |
| Degradation | Explicit critical/optional classification | No safe degradation |
| Testing | Deterministic fault injection | Real integration for protocol/DB semantics |

## Hard rules

1. No unbounded retries.
2. No retry multiplication across layers.
3. No retry of non-idempotent side effects without replay protection.
4. No unbounded concurrency or queues.
5. No long DB transaction around remote LLM/MCP/HTTP work without explicit justification.
6. No swallowed failures.
7. No misleading success after critical work was dropped.
8. No claim of exactly-once execution without infrastructure proof.
9. Cancellation and deadlines must release resources.
10. Complexity such as circuit breakers is justified by a concrete failure mode, not by fashion.