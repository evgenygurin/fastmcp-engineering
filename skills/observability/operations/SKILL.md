---
name: observability-operations
description: Evidence-first observability, reliability and production operations for FastMCP systems, including traces, metrics, logs, correlation, LLM/tool telemetry, redaction, health, readiness, SLOs and incident diagnostics.
---

# Observability / Operations

## Mission
Make production behavior diagnosable without leaking secrets or sensitive model data. Observability must explain MCP requests, application use cases, database work, model runs and tool calls across async boundaries.

## Trigger / Когда применять

**Scope / When to use:** observability, reliability and production operations for FastMCP systems, including traces, metrics, logs, correlation, LLM/tool telemetry, redaction, health, readiness, SLOs and incident diagnostics.
**Trigger:** designing or changing traces, metrics, logs, correlation, LLM/tool telemetry, redaction, health/readiness, SLOs, or incident diagnostics.
**Upstream / Prerequisite:** `AGENTS.md` and architecture/security/testing contracts read; identified exact versions; evidence and unresolved questions recorded.
**Mission / Goal:** make production behavior diagnosable without leaking secrets or sensitive model data; observability must explain MCP requests, application use cases, database work, model runs and tool calls across async boundaries.
**Research / Evidence:** read official FastMCP logging/instrumentation/server lifecycle documentation; read official PydanticAI observability/logging/instrumentation guidance; read OpenTelemetry semantic conventions and SDK/exporter docs relevant to the stack; inspect official examples/source/tests for version-sensitive behavior; inspect deployment/runtime logging and monitoring configuration.
**Decision / Selection rules:** use logs, metrics and traces as complementary signals; avoid high-cardinality metric labels and put identifiers in trace/log context; define stable correlation identifiers propagated across async boundaries; trace meaningful boundaries rather than every trivial function; treat prompt/completion/tool payloads as sensitive by default with redaction and retention controls; separate liveness from readiness; define SLI/SLOs for critical operations; classify telemetry with retention, sampling, access and deletion controls.
**Version / Compatibility:** identify exact FastMCP, MCP, PydanticAI, ASGI/server, SQLAlchemy and telemetry versions.

## Deliverables

**Deliverables / Artifacts:** observability architecture, signal/event schema, correlation contract, redaction policy, metric/SLO matrix, health/readiness design, dashboards/runbooks, implementation, verification and residual-risk register.
**Verification / Testing:** test correlation propagation, structured log schema, redaction, trace creation/status, metrics labels, health/readiness semantics and failure/cancellation paths; use in-memory/test exporters or documented SDK test facilities; do not depend on a production telemetry backend for normal CI.
**Failure / Stop conditions:** reject if telemetry can leak credentials/sensitive content, correlation breaks across async/MCP boundaries, metrics have unbounded cardinality, liveness depends on external services, readiness has no explicit policy, critical operations have no diagnostic signals, or observability changes materially alter application behavior without justification.
**Positive scenario:** production behavior is diagnosable with correlated signals and no secret or sensitive model data leaks.
**Negative scenario:** telemetry leaks credentials or liveness depends on an external service.

## Mandatory research gate
Before implementation:
1. Read AGENTS.md and architecture/security/testing contracts.
2. Identify exact FastMCP, MCP, PydanticAI, ASGI/server, SQLAlchemy and telemetry versions.
3. Read official FastMCP logging/instrumentation/server lifecycle documentation.
4. Read official PydanticAI observability/logging/instrumentation guidance.
5. Read OpenTelemetry semantic conventions and SDK/exporter docs relevant to the stack.
6. Inspect official examples/source/tests for version-sensitive behavior.
7. Inspect deployment/runtime logging and monitoring configuration.
8. Record evidence and unresolved questions.

## Three signals
Use logs, metrics and traces as complementary signals:
- traces explain one request/run across boundaries;
- metrics show aggregate health, latency, volume and saturation;
- structured logs provide searchable event detail and diagnostic context.

Avoid high-cardinality metrics labels. Put request/run identifiers in trace/log context rather than metric dimensions.

## Correlation
Define stable identifiers for request, MCP session where applicable, application operation, agent run and tool invocation. Propagate context across async tasks, DB calls and outbound HTTP/MCP calls without leaking credentials.

## Tracing
Trace meaningful boundaries: transport request, authentication/authorization, application use case, agent run/model call, tool invocation, external MCP call and database transaction/query where supported. Do not create spans for every trivial function. Capture latency/status/error attributes and bounded operational metadata.

## LLM/tool telemetry
Measure model latency, call count, token/usage data when available, retries, tool calls, validation failures and outcome. Prompt/completion/tool payloads are sensitive by default: capture content only under explicit policy, with redaction/minimization and retention controls.

## Logging
Use structured logs with stable event names. Log actionable state transitions, failures and security decisions. Never log tokens, passwords, API keys, raw authorization headers or unrestricted model context. Redact sensitive fields centrally rather than relying on every caller.

## Metrics
Define service-level indicators such as request rate, error rate, latency distributions, saturation, active sessions, tool/model failure rate and DB pool health. Use histograms for latency. Establish bounded label cardinality.

## Health / readiness
Separate liveness from readiness. Liveness answers whether the process can run; readiness answers whether it can safely serve traffic. Do not make liveness depend on every external dependency. Define dependency-specific readiness policy and timeouts.

## Reliability / SLOs
Define SLI/SLOs for critical operations. Establish latency/error/availability targets, alert thresholds, retry budgets and degradation behavior. Alerts should be actionable and tied to user impact or capacity risk.

## Async / lifecycle
Ensure instrumentation survives cancellation and exceptions and closes spans/resources correctly. Verify background tasks, lifespan startup/shutdown, DB pools and MCP transports are observable and cleanly terminated.

## Privacy / retention
Classify telemetry. Define retention, sampling, access controls and deletion requirements. Prefer metadata over raw content. Treat prompts, tool results, DB values and PII as sensitive unless explicitly classified otherwise.

## Testing
Test correlation propagation, structured log schema, redaction, trace creation/status, metrics labels, health/readiness semantics and failure/cancellation paths. Use in-memory/test exporters or documented SDK test facilities; do not depend on a production telemetry backend for normal CI.

## Operations
Provide dashboards/runbooks for critical SLOs and common failure modes. Document graceful degradation, dependency outages, model/provider failures, MCP server failures, DB saturation and rate-limit behavior.
