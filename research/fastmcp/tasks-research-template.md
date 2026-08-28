# FastMCP Tasks Research Package

## Target
- FastMCP version:
- Python version:
- Date:
- Stability channel:

## First-party evidence
- Official docs / llms:
- Official examples:
- Source:
- Tests:
- MCP specification / SEP:
- First-party dependencies:

## Task API
| Question | Finding | Evidence | Confidence |
|---|---|---|---|
| Task declaration | | | |
| Accepted/background semantics | | | |
| State machine | | | |
| Polling | | | |
| Result retrieval | | | |
| Cancellation | | | |
| Timeout/deadline | | | |
| TTL/expiry | | | |
| Progress | | | |
| Errors | | | |

## Execution model
- Owner:
- Storage:
- Durability:
- Worker boundary:
- Multi-worker behavior:
- Restart recovery:
- Shutdown behavior:

## Reliability
- Retry semantics:
- Idempotency:
- Failure classification:
- Backpressure/concurrency:

## Security
- Creation authorization:
- Status authorization:
- Result authorization:
- Tenant binding:
- Sensitive data handling:

## Architecture decision
- Why protocol task:
- Why not synchronous:
- Why not asyncio background task:
- Why not queue/workflow engine:
- Interaction with Context:
- Interaction with Middleware:
- Interaction with Lifespan:
- Interaction with Auth:

## Verification
- Protocol/client tests:
- Lifecycle tests:
- Failure/cancellation tests:
- Persistence/recovery tests:
- Security tests:
- Static quality:
- Architecture re-check:

## Unknowns

List every behavior not established by first-party evidence. Blocking unknowns must be resolved before implementation.

## Evidence classification

Classify every material claim as `official-doc`, `official-example`, `source`, `test`, `spec`, `first-party-dependency`, or `secondary`. Secondary evidence never silently overrides first-party evidence.