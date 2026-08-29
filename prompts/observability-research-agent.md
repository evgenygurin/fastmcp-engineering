# Observability / Operations Research Agent

Research only. Implementation occurs in a fresh session.

## Source hierarchy
1. Official OpenTelemetry documentation/specifications.
2. Official FastMCP documentation, llms material, examples, source/tests.
3. Official PydanticAI observability/logging documentation and source/tests.
4. Official ASGI/server, SQLAlchemy and deployment-platform documentation.
5. Authoritative SRE/observability guidance.
6. Secondary sources only as supplementary evidence.

## Mandatory investigation
Identify exact versions. Research FastMCP middleware/lifecycle/context/observability hooks, PydanticAI instrumentation, OpenTelemetry tracing/metrics/logging, context propagation, semantic conventions, ASGI instrumentation, SQLAlchemy instrumentation, MCP request/session correlation, agent/model/tool telemetry, streaming/cancellation, errors, graceful shutdown, exporters, sampling, baggage, cardinality and privacy.

Map critical production workflows to signals and failure diagnostics. Identify sensitive fields in prompts, tool arguments/results, DB values, tokens and headers. Determine what can be captured safely and what must be redacted or omitted.

Research SLI/SLO candidates, alerting, dependency outage behavior, graceful degradation, retry budgets and runbook requirements. Inspect source/tests where docs are ambiguous.

Every material claim must include source, version and confidence.

## Deliverable
Observability architecture, correlation/data-flow map, signal schema, telemetry sensitivity matrix, metric/cardinality matrix, health/readiness policy, SLI/SLO matrix, sampling/retention policy, failure-mode diagnostics, dashboard/runbook plan, testing matrix, evidence ledger and blocking unknowns.

No implementation.