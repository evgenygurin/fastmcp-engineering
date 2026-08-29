# Observability / Operations Acceptance Criteria

## Research
- [ ] Exact telemetry/framework versions identified.
- [ ] FastMCP lifecycle/observability docs and examples read.
- [ ] PydanticAI observability docs read.
- [ ] OpenTelemetry specs/semantic conventions read.
- [ ] ASGI/SQLAlchemy instrumentation docs checked.
- [ ] Source/tests inspected for ambiguity.
- [ ] Evidence ledger completed.

## Architecture
- [ ] Trace topology documented.
- [ ] Correlation contract documented.
- [ ] Structured log schema documented.
- [ ] Metric catalog and cardinality policy documented.
- [ ] Telemetry sensitivity/redaction policy documented.
- [ ] Health/readiness semantics documented.
- [ ] SLI/SLOs and operational runbooks documented.

## Security / privacy
- [ ] Tokens/credentials are excluded from telemetry.
- [ ] Sensitive prompts/tool payloads are excluded or explicitly redacted.
- [ ] User-controlled data cannot become unbounded metric labels.
- [ ] Telemetry access/retention is defined.

## Verification
- [ ] Correlation propagation tests pass.
- [ ] Log schema/redaction tests pass.
- [ ] Trace/error status tests pass.
- [ ] Metric cardinality tests pass.
- [ ] Health/readiness tests pass.
- [ ] Cancellation/shutdown tests pass where applicable.
- [ ] Static quality gates pass.
- [ ] Architecture/security re-check passes.