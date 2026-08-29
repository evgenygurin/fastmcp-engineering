---
name: observability-diagnostics
description: Design production observability for FastMCP systems with trace/log/metric correlation, OpenTelemetry, safe redaction, MCP/agent/tool/database diagnostics and actionable failure taxonomy.
---

# Observability / Diagnostics

## Mission

Make every production failure diagnosable across the complete request path without logging secrets, credentials, sensitive prompts, private tool results, or uncontrolled payloads.

## Mandatory research gate

Before implementation:
1. Read AGENTS.md and repository engineering contracts.
2. Identify exact FastMCP, Python, OpenTelemetry, ASGI/server, PydanticAI, SQLAlchemy and logging versions.
3. Read official FastMCP observability/middleware/lifecycle documentation and llms material.
4. Read official PydanticAI instrumentation/observability documentation where applicable.
5. Read official OpenTelemetry Python documentation and relevant semantic conventions.
6. Inspect relevant official examples and source/tests when behavior is ambiguous.
7. Record evidence before coding.

## Correlation model

```text
trace_id
  └── MCP request/span
        ├── application use case
        ├── agent run
        │     ├── model call
        │     └── tool call
        ├── database operation
        └── external API operation
```

Use a stable correlation strategy rather than inventing unrelated IDs at every layer. Do not use user-controlled identifiers as trusted trace identity.

## Three signals

Design all three deliberately:

- traces: causality and latency across boundaries;
- metrics: aggregate health, saturation and SLOs;
- structured logs: searchable event detail.

Avoid using logs as a substitute for metrics or traces.

## MCP-specific diagnostics

Capture safe metadata for:
- request method/type;
- protocol version/capability negotiation where useful;
- tool/resource/prompt operation name;
- outcome/error class;
- duration;
- cancellation;
- payload size;
- pagination/streaming lifecycle where applicable.

Never dump complete MCP payloads by default.

## Agent diagnostics

Where PydanticAI is used, correlate agent runs and model/tool operations. Capture provider/model identity, latency, token/usage metadata and outcome when supported, but redact prompt content, credentials, private user data and sensitive tool results. Make high-cardinality labels an explicit design decision.

## Database diagnostics

Correlate database spans with the application trace. Never emit raw secrets or full SQL parameters. SQL statement capture must follow the security posture of the target environment and use safe normalization/redaction.

## Error taxonomy

Distinguish at minimum:
- protocol/client errors;
- validation errors;
- authorization errors;
- domain/business errors;
- dependency failures;
- model/provider failures;
- database failures;
- timeouts/cancellation;
- unexpected programmer errors.

Map each class to appropriate logs, metrics, traces and client-visible errors.

## Redaction

Define a centralized redaction policy. Sensitive fields must be identified by contract, not by ad-hoc logger calls. Prefer allowlisting metadata over denylisting arbitrary keys. Never log API keys, access tokens, cookies, passwords, authorization headers, raw secrets, or unrestricted prompt/tool payloads.

## Metrics

Define bounded labels only. Useful metrics may include request count/error rate, latency distributions, active streams/tasks, tool outcomes, dependency latency/errors, DB pool saturation, agent/model latency and usage, subject to privacy and cardinality constraints.

## Health / SLOs

Separate liveness, readiness and dependency health. Define SLOs from user-visible behavior rather than infrastructure vanity metrics. Alert on symptoms and sustained saturation, not every transient error.

## Testing

Test correlation propagation, redaction, error classification, metric label cardinality, trace creation, cancellation, exception paths and graceful shutdown. Include tests proving sensitive values never reach logs/telemetry exporters.

## Rejection criteria

Reject if trace/log correlation is inconsistent, telemetry leaks secrets or full sensitive payloads, labels are unbounded, error classes are indistinguishable, instrumentation changes business behavior, or observability depends on a single local logger.

## Deliverables

Observability research package, telemetry data model, trace topology, metric catalog, logging schema, redaction policy, error taxonomy, implementation, telemetry tests, operational dashboard/alert specification and architecture re-check.