# FastMCP Transports / Deployment Research Package

## Target
- FastMCP version:
- Python version:
- ASGI server/framework:
- Date:

## Evidence
- Official docs:
- Official examples:
- Source/tests:
- MCP specification/SEP:
- First-party dependency docs:

## Transport findings
| Question | Finding | Evidence | Confidence |
|---|---|---|---|
| Supported transports | | | |
| Endpoint/path | | | |
| Initialization | | | |
| Session semantics | | | |
| Streaming | | | |
| Cancellation | | | |
| Errors | | | |

## Deployment findings
| Question | Finding | Evidence | Confidence |
|---|---|---|---|
| Stateful/stateless | | | |
| Worker model | | | |
| Replica model | | | |
| Shared state | | | |
| Proxy behavior | | | |
| Timeouts | | | |
| Buffering | | | |
| Health/readiness | | | |
| Graceful shutdown | | | |

## Security
- TLS boundary:
- Authentication boundary:
- Authorization boundary:
- Trusted proxy boundary:
- Forwarded headers:

## Topology
```text
client -> [proxy/LB] -> [ASGI/FastMCP] -> [application] -> [state/resources]
```

## Verification
- MCP Client:
- Real transport:
- Proxy integration:
- Streaming:
- Cancellation:
- Shutdown:
- Failure injection:
- Static quality:

## Unknowns

List every behavior not established by first-party evidence. Blocking unknowns must be resolved before implementation.

## Evidence classification

Classify every material claim as `official-doc`, `official-example`, `source`, `test`, `spec`, `first-party-dependency`, or `secondary`. Secondary evidence never silently overrides first-party evidence.