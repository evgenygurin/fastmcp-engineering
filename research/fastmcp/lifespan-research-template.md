# FastMCP Lifespan Research Package

## Target
- FastMCP version:
- Python version:
- Date:
- Stability channel:

## First-party evidence
- Official docs:
- Official examples:
- FastMCP source:
- FastMCP tests:
- MCP specification/SEP:
- Starlette/FastAPI docs:
- Resource dependency docs:

## Lifespan API findings
| Question | Finding | Evidence | Confidence |
|---|---|---|---|
| User lifespan signature | | | |
| Yielded state | | | |
| Context interaction | | | |
| Provider lifespans | | | |
| Extension lifespans | | | |
| Composition | | | |
| Reference counting | | | |
| Cancellation | | | |
| Cleanup | | | |
| Mounted HTTP behavior | | | |

## Resource matrix
| Resource | Owner | Scope | Startup prerequisites | Consumers | Cleanup | Concurrently shareable? |
|---|---|---|---|---|---|---|
| | | | | | | |

## Lifecycle graph

```text
startup: 
shutdown:
```

## Failure model
- Partial startup:
- Cleanup after failed startup:
- Cleanup failure:
- Cancellation during teardown:
- Re-entry/shared runtime:

## Integration
- Context:
- DI:
- Middleware:
- Providers:
- HTTP/ASGI:
- Background tasks:

## Verification
- Startup tests:
- Failure tests:
- Cleanup tests:
- Cancellation tests:
- Composition tests:
- HTTP integration:
- Concurrency tests:
- Static quality:
- Architecture re-check:

## Unknowns

List every behavior not established by first-party evidence. Blocking unknowns must be resolved before implementation.

## Evidence classification

Classify every material claim as `official-doc`, `official-example`, `source`, `test`, `spec`, `first-party-dependency`, or `secondary`. Secondary evidence never silently overrides first-party evidence.