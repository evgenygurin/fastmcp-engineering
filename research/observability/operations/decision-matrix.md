# Observability Decision Matrix

| Concern | Preferred rule | Verification |
|---|---|---|
| Correlation | Stable request/run/tool IDs propagated through boundaries | Trace/log tests |
| Tracing | Meaningful architectural boundaries | Trace topology |
| Metrics | Low-cardinality dimensions | Cardinality test |
| Logs | Structured, actionable events | Schema tests |
| LLM telemetry | Metadata by default, content only by explicit policy | Redaction tests |
| Health | Liveness separated from readiness | Failure tests |
| Sampling | Explicit cost/privacy policy | Exporter tests |
| Retention | Data-classification driven | Configuration review |
| Shutdown | Flush/close without blocking service exit indefinitely | Lifecycle tests |

## Hard rules

1. Never put secrets, tokens or unrestricted sensitive model content into ordinary telemetry.
2. Never use user-controlled values as unbounded metric labels.
3. Liveness must not depend on every external dependency.
4. Correlation must survive async and MCP/application boundaries.
5. Telemetry must be diagnostically useful without becoming a second application data store.
6. Normal CI must not require a production telemetry backend.
7. Instrument meaningful boundaries, not every function.
8. Sampling and retention are explicit privacy/cost decisions.