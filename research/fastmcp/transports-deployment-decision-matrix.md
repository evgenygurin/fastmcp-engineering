# FastMCP Transports / Deployment Decision Matrix

## Core rule

Transport is an infrastructure/protocol boundary. Deployment topology must be derived from verified protocol and lifecycle semantics, not from a local development success case.

| Concern | Decision owner |
|---|---|
| MCP protocol transport | FastMCP transport layer |
| TLS/network perimeter | infrastructure |
| MCP authentication | FastMCP/auth boundary |
| Application authorization | application policy |
| Session/task shared state | explicit state store |
| Startup/shutdown resources | lifespan |
| Cross-cutting request behavior | middleware |
| Business behavior | application/domain |

## Mandatory questions

1. Which exact transport is supported by the target FastMCP version?
2. What endpoint/path and HTTP semantics does it use?
3. Is execution/session state process-local, server-local, or externally persisted?
4. Can multiple workers/replicas serve the same client safely?
5. What does the proxy do to streaming, buffering and timeouts?
6. Which component owns authentication and trusted proxy interpretation?
7. What happens to requests, streams, sessions and tasks during shutdown?
8. What health/readiness signal is actually meaningful?
9. Which state must survive worker replacement or deployment?
10. What assumptions need integration tests rather than unit tests?

## Deployment anti-patterns

- Scaling a stateful process-local MCP server horizontally without a state strategy.
- Assuming HTTP proxies preserve streaming semantics by default.
- Trusting forwarded identity headers from arbitrary clients.
- Inventing custom MCP routes instead of using the verified native integration.
- Treating liveness as readiness.
- Killing workers without defining in-flight request/stream behavior.
- Hard-coding development timeouts into production.
- Coupling application/domain code to transport details.
