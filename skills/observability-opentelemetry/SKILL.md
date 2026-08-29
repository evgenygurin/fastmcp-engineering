---
name: observability-opentelemetry
description: Evidence-first observability engineering for FastMCP systems using OpenTelemetry, structured logs, metrics and traces.
---

# Observability / OpenTelemetry Engineering

## Mission
Make production behavior explainable across the MCP boundary, application/domain workflows and infrastructure without leaking sensitive data or creating unbounded telemetry cost.

## Mandatory research
Identify exact dependency versions. Read current official OpenTelemetry documentation/specification and exact-version FastMCP, PydanticAI, SQLAlchemy and relevant instrumentation docs/source/tests. Inspect repository conventions. Record an evidence ledger and re-check version-sensitive APIs before completion.

## Three signals
Design traces, metrics and logs as complementary signals. Do not duplicate the same high-cardinality data into all three. Define ownership and correlation between them.

## Tracing
Trace meaningful boundaries: MCP request/session, primitive invocation, application use case, external LLM call, database operation and outbound HTTP/queue operation where instrumentation supports it. Propagate context across async tasks and supported transports. Use stable low-cardinality span attributes. Never put prompts, model outputs, authorization tokens, passwords, secrets, full SQL parameters or arbitrary user content into spans by default.

Use semantic conventions supported by the actual instrumentation version. Do not invent attribute names where an official convention exists.

## Metrics
Define service-level metrics before implementation: request/tool latency, errors, in-flight work, saturation/resource usage and dependency health. Control label cardinality. Never label metrics by user ID, request ID, raw URI, arbitrary tool arguments or unbounded exception text. Prefer bounded dimensions such as operation class, outcome, transport and dependency.

## Structured logs
Use machine-readable logs with consistent timestamp, severity, service, environment, operation, trace/span correlation and stable event names. Redact secrets and sensitive user data at the logging boundary. Avoid duplicate exception logging across layers. Log once at the ownership boundary with actionable context.

## Correlation
Every request should have a trace context where supported. Correlation IDs must not be used as authorization credentials. Preserve trace context across async work and explicitly define correlation for durable jobs/events.

## Errors
Map failures to stable outcome/error categories. Do not use exception message text as a metric label. Capture stack traces only in controlled diagnostic channels. Keep protocol/application/security errors distinguishable.

## Sampling and cost
Define sampling intentionally. Production sampling must not make security/audit requirements disappear. Tail/head sampling decisions must be documented. Telemetry exporters, queues and buffers must be bounded and fail safely; observability failure must not take down the MCP service.

## Privacy/security
Treat telemetry as sensitive infrastructure. Apply data minimization, redaction, access control, retention and export policies. Never emit bearer tokens, cookies, API keys, database credentials, raw authorization headers or secrets. Avoid raw prompts/responses unless explicitly approved and protected.

## Architecture
Instrumentation belongs at stable boundaries, not scattered through domain code. Domain logic should remain independent from OpenTelemetry APIs unless a domain-level business event is intentionally modeled separately. Prefer framework instrumentation and middleware/interceptors over manual spans everywhere.

## Reliability
Telemetry must be asynchronous/bounded where appropriate, have timeout/export failure behavior, and support graceful shutdown/flush. Backpressure in exporters must not become unbounded application memory growth.

## Testing
Test trace propagation, span names/attributes, metric cardinality, log redaction, error classification and graceful exporter shutdown. Use in-memory/test exporters where possible. Include a negative test proving secrets and sensitive payloads are absent. Test failure of telemetry exporters without failing the business operation.

## Deliverables
Observability architecture; signal matrix; semantic-convention mapping; trace/span policy; metric catalog with cardinality budgets; structured-log schema; redaction policy; sampling/retention policy; test matrix; evidence ledger; rejected alternatives; verification report.