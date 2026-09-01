---
name: observability-telemetry-engineering
description: Evidence-first observability and telemetry engineering for production FastMCP systems using OpenTelemetry.
---

# Observability / Telemetry Engineering

## Mission
Make system behavior diagnosable in production without coupling domain logic to telemetry vendors or leaking secrets, personal data or high-cardinality dimensions.

## Trigger / Когда применять

**Scope / When to use:** observability and telemetry engineering for production FastMCP systems using OpenTelemetry.
**Trigger:** designing or changing spans, metrics, logs, context propagation, redaction, sampling, health/readiness, or SLI/SLO telemetry.
**Upstream / Prerequisite:** identified exact versions; evidence recorded and re-checked before completion.
**Mission / Goal:** make system behavior diagnosable in production without coupling domain logic to telemetry vendors or leaking secrets, personal data or high-cardinality dimensions.
**Research / Evidence:** identify exact Python, FastMCP, OpenTelemetry API/SDK, Pydantic, SQLAlchemy, PydanticAI and exporter/backend versions; read current official OpenTelemetry, FastMCP, SQLAlchemy and PydanticAI documentation; inspect exact-version instrumentation examples/source/tests; verify semantic conventions and framework instrumentation actually supported by installed versions.
**Decision / Selection rules:** place instrumentation at adapters, application boundaries and infrastructure integrations; keep domain logic free of OpenTelemetry, logging backends and vendor SDKs; use the three core signals deliberately; use OpenTelemetry APIs/SDK with standard semantic conventions; create meaningful spans and avoid span-per-loop unless cardinality is safe; never record complete prompts, arguments or outputs by default; use low-cardinality metric dimensions only; sample deliberately; define centralized redaction before export; separate liveness from readiness; define SLIs from user-visible outcomes; ensure telemetry never makes the business operation fail.
**Version / Compatibility:** identify exact versions; verify semantic conventions and framework instrumentation actually supported by the installed versions.

## Deliverables

**Deliverables / Artifacts:** observability architecture; signal matrix; instrumentation boundary map; semantic-convention map; MCP/DB/LLM telemetry policy; logging schema; context-propagation policy; metric/cardinality budget; sampling strategy; redaction policy; health/readiness model; SLI/SLO catalog; telemetry failure model; test matrix; evidence ledger; rejected alternatives; verification report.
**Verification / Testing:** test span/metric/log creation at architectural boundaries, context propagation, error status, redaction, cardinality-sensitive labels, sampling behavior where deterministic, health/readiness semantics and graceful exporter failure; assert meaningful telemetry contracts without coupling tests to exporter internals.
**Failure / Stop conditions:** reject domain-level telemetry dependencies, high-cardinality labels, full payload logging by default, secret-bearing spans/logs, exporter availability affecting business success, liveness checks coupled to optional dependencies, arbitrary metric proliferation and duplicate instrumentation.
**Positive scenario:** production behavior is diagnosable with low-cardinality, redacted telemetry that degrades gracefully when exporters fail.
**Negative scenario:** domain logic couples to a telemetry vendor or full payloads and secrets leak by default.

## Mandatory research
Identify exact Python, FastMCP, OpenTelemetry API/SDK, Pydantic, SQLAlchemy, PydanticAI and exporter/backend versions. Read current official OpenTelemetry, FastMCP, SQLAlchemy and PydanticAI documentation first; inspect exact-version instrumentation examples/source/tests. Verify semantic conventions and framework instrumentation actually supported by installed versions. Record evidence and re-check version-sensitive behavior before completion.

## Architecture
Instrumentation belongs at adapters, application boundaries and infrastructure integrations. Domain logic must not import OpenTelemetry, logging backends or vendor SDKs. Prefer automatic instrumentation where it is reliable and supplement it with deliberate business spans/metrics at meaningful boundaries.

## Signals
Use the three core signals deliberately: traces for causality/timing, metrics for aggregate health/capacity/SLOs, logs/events for detailed diagnostic context. Do not duplicate the same information across every signal without a diagnostic reason.

## OpenTelemetry
Use OpenTelemetry APIs/SDK and standard semantic conventions where supported. Keep exporter/backend configuration outside business code. Avoid vendor lock-in in application instrumentation. Instrumentation must degrade gracefully when exporters are unavailable.

## Trace boundaries
Create meaningful spans for MCP invocation, authentication/authorization, application use cases, external HTTP/MCP calls, SQL queries and LLM/provider calls. Avoid span-per-loop/item unless the cardinality and volume are demonstrably safe. Record status and exceptions consistently.

## MCP telemetry
Track tool/resource/prompt invocation latency, outcome, errors and relevant stable capability identity. Never record complete prompts, arguments or outputs by default. Sensitive payloads require explicit redaction policy and strong justification.

## LLM / PydanticAI telemetry
Capture provider/model identity, latency, token usage and cost metrics when available and safe. Treat prompts, model output, tool arguments and retrieved context as potentially sensitive. Do not put full content into traces or logs by default. Instrument retries and fallback providers distinctly.

## Database telemetry
Use SQLAlchemy-supported instrumentation where appropriate. Never log raw credentials or sensitive bind values. Prefer normalized statement metadata and bounded attributes. DB telemetry must not become a second application-level query logger.

## Structured logging
Use structured events with stable field names and severity. Include correlation/trace identifiers through context propagation. Messages should be actionable. Avoid logging secrets, authorization tokens, full request bodies, model prompts, model outputs, SQL parameters or arbitrary user content.

## Context propagation
Propagate trace/correlation context through async tasks, HTTP calls and background jobs using documented mechanisms. Do not use mutable globals or thread-local assumptions for async request identity. Define behavior when context is missing or invalid.

## Metrics
Define low-cardinality dimensions only: operation, outcome, protocol capability, dependency class, bounded status category and environment as appropriate. Never use user ID, request ID, raw URL, prompt text or unbounded exception text as metric labels. Use histograms for latency and counters for events; gauges only for values with meaningful current-state semantics.

## Cardinality / volume
Every new telemetry attribute must have an estimated cardinality and volume impact. Sampling, aggregation and retention are part of the design. Do not solve telemetry cost by disabling the only useful diagnostic signal.

## Sampling
Use trace sampling deliberately and document head/tail or parent-based behavior. Preserve important error/slow traces where the backend supports it. Sampling must not make security/audit records disappear when those records have separate compliance requirements.

## Redaction
Define centralized redaction rules for credentials, authorization headers, cookies, API keys, tokens, PII, prompts, model output and database parameters. Redaction should happen before export whenever possible. Test redaction against realistic nested payloads and exception paths.

## Health / readiness
Separate liveness from readiness. Readiness should reflect dependencies required to serve traffic; liveness should not restart an otherwise healthy process merely because a downstream dependency is unavailable. Avoid health checks that create expensive load or recursively depend on telemetry itself.

## SLI / SLO
Define SLIs from user-visible outcomes: successful MCP operation rate, latency, availability, dependency failure rate and task completion where applicable. SLOs need an owner, window and error-budget policy. Do not declare arbitrary infrastructure metrics to be user-facing SLIs.

## Resilience
Telemetry must never make the business operation fail merely because an exporter/backend is unavailable. Bound exporter queues, shutdown flush time and resource consumption. Instrumentation exceptions must be contained.

## Testing
Test span/metric/log creation at architectural boundaries, context propagation, error status, redaction, cardinality-sensitive labels, sampling behavior where deterministic, health/readiness semantics and graceful exporter failure. Assert meaningful telemetry contracts without coupling tests to exporter internals.

## Security / privacy
Treat telemetry as a sensitive data store. Define retention, access, encryption and export policy at the deployment boundary. Do not assume observability systems are safe destinations for application secrets merely because they are internal.
