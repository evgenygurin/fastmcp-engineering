# Observability / OpenTelemetry Acceptance Criteria

## Research
- [ ] Exact FastMCP/OpenTelemetry/PydanticAI/SQLAlchemy/exporter versions identified.
- [ ] Current official OpenTelemetry specification/docs reviewed.
- [ ] Relevant exact-version framework instrumentation docs/source/tests reviewed.
- [ ] Evidence ledger completed.

## Signals
- [ ] Trace boundaries are defined.
- [ ] Context propagation is defined across async and supported transports.
- [ ] Semantic conventions are mapped.
- [ ] Metrics have explicit bounded cardinality.
- [ ] Structured log schema is defined.
- [ ] Correlation between signals is defined.
- [ ] Sampling is intentional and documented.

## Security/reliability
- [ ] Prompts/model outputs are not logged by default.
- [ ] Secrets/tokens/cookies/auth headers are redacted or excluded.
- [ ] Raw SQL parameters and unrestricted user payloads are excluded.
- [ ] Exporter failure cannot take down business operations.
- [ ] Export queues/buffers are bounded.
- [ ] Shutdown/flush is bounded.

## Verification
- [ ] Trace propagation tests pass.
- [ ] Span/attribute tests pass.
- [ ] Metric cardinality tests pass.
- [ ] Log/redaction tests pass.
- [ ] Sensitive-data negative tests pass.
- [ ] Exporter failure tests pass.
- [ ] Cancellation/exception lifecycle tests pass.
- [ ] Current official docs were re-checked before completion.