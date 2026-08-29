# Async / Event-Driven Research Agent

Research only. Do not implement.

1. Identify exact versions of FastMCP, MCP, Python, PydanticAI, SQLAlchemy and the chosen broker/runtime.
2. Read official specifications/docs first; then official examples/source/tests. Secondary material is supplementary.
3. Research asyncio TaskGroup/structured concurrency, cancellation, task ownership, deadlines and shutdown.
4. Research FastMCP lifecycle, background work and protocol-level asynchronous features for the exact version.
5. Research MCP task/progress/cancellation semantics where applicable.
6. Research PydanticAI agent/tool lifecycle and cancellation/usage limits.
7. Research SQLAlchemy AsyncSession task safety and transaction boundaries.
8. Research broker delivery guarantees, ordering, acknowledgements, retry/DLQ and consumer concurrency.
9. Map every operation as request-scoped or durable.
10. Produce evidence for delivery semantics, idempotency, ordering, backpressure, retry ownership, crash recovery and graceful shutdown.

Deliverable: source ledger, exact-version matrix, lifecycle model, failure-domain map, delivery-semantics matrix, idempotency/replay strategy, ordering policy, concurrency/resource budget, backpressure policy, shutdown/recovery design, event-schema compatibility policy, integration-test matrix and unresolved questions.

Never claim exactly-once without authoritative infrastructure evidence.