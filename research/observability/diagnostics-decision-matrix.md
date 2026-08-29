# Observability / Diagnostics Decision Matrix

| Signal | Primary purpose | Must avoid |
|---|---|---|
| Trace | Cross-boundary causality/latency | Sensitive payloads |
| Metric | Aggregate health/SLO/saturation | Unbounded labels |
| Structured log | Event detail/search | Secrets/raw prompts |

## Trace topology

```text
MCP request
  -> FastMCP
  -> application use case
  -> agent/model
  -> tool
  -> SQLAlchemy
  -> external dependency
```

## Hard rules

1. One coherent correlation strategy across boundaries.
2. User-controlled identifiers are not trusted trace identity.
3. Metric labels must be bounded by design.
4. Prefer metadata allowlists over broad log capture.
5. Prompt/tool payloads are not logged by default.
6. Authorization headers, cookies, API keys, tokens and passwords never enter telemetry.
7. Instrumentation must not alter business behavior.
8. Liveness and readiness are separate signals.
9. Error taxonomy is stable enough to support operations and alerting.
10. Privacy/security tests must prove sensitive data does not reach exporters.