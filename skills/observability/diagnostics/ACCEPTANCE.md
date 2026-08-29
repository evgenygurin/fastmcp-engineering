# Observability / Diagnostics Acceptance Criteria

## Research
- [ ] Exact versions identified.
- [ ] Official FastMCP observability/middleware/lifecycle docs read.
- [ ] Official PydanticAI instrumentation docs read where applicable.
- [ ] Official OpenTelemetry docs/semantic conventions read.
- [ ] Relevant official examples/source/tests inspected.
- [ ] Evidence ledger completed.

## Telemetry
- [ ] Trace topology is explicit.
- [ ] Correlation propagates across MCP/application/agent/tool/DB/external boundaries.
- [ ] Logs are structured.
- [ ] Metrics use bounded labels.
- [ ] Error taxonomy is explicit.
- [ ] Sampling/export strategy is explicit.

## Security/privacy
- [ ] Redaction policy is centralized.
- [ ] Secrets never reach logs/traces/metrics.
- [ ] Raw prompts/tool results are not logged by default.
- [ ] User-controlled values are not trusted as trace identity.
- [ ] Sensitive payload tests pass.

## Operations
- [ ] Liveness/readiness are distinct.
- [ ] SLOs are defined from user-visible behavior.
- [ ] Failure signals and alerts are actionable.
- [ ] Telemetry shutdown/flush is handled where required.

## Verification
- [ ] Trace propagation tests pass.
- [ ] Error classification tests pass.
- [ ] Redaction tests pass.
- [ ] Metric cardinality tests pass.
- [ ] Exception/cancellation tests pass.
- [ ] Static quality checks pass.
- [ ] Architecture re-check passes.