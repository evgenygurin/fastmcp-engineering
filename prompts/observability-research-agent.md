# Observability / Diagnostics Research Agent

Research only; implementation happens in a fresh session.

## Source hierarchy
1. Official FastMCP documentation/llms.
2. Official PydanticAI documentation.
3. Official OpenTelemetry Python documentation and semantic conventions.
4. Official ASGI/server, SQLAlchemy and relevant dependency docs.
5. Official examples and source/tests.
6. Secondary sources only as supplementary evidence.

## Mandatory investigation
Identify exact versions. Research FastMCP middleware/lifecycle/context/observability hooks, PydanticAI instrumentation, OpenTelemetry tracing/metrics/logging, context propagation, semantic conventions, ASGI instrumentation, SQLAlchemy instrumentation, streaming/cancellation, errors, graceful shutdown, exporters, sampling, baggage, cardinality and privacy. Design safe correlation across MCP request → application → agent/model/tool → DB/external APIs. Determine what metadata is safe to capture and what must be redacted.

Build an error taxonomy, telemetry schema, metric catalog, trace topology, redaction policy, SLO/health strategy, testing strategy and operational failure matrix. Inspect source/tests where docs are ambiguous.

Every material claim must include source, version and confidence. No implementation.