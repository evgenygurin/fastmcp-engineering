# PydanticAI / Agent Integration Research Package

## Target
- Python:
- PydanticAI:
- Pydantic:
- FastMCP:
- MCP:
- Model/provider SDK:
- Date:

## Evidence
- PydanticAI official docs:
- FastMCP official docs/llms:
- Official examples:
- Source/tests:
- MCP specification:
- Provider docs:

## API matrix
| Feature | Verified behavior | Version gate | Evidence | Confidence |
|---|---|---|---|---|
| Agent | | | | |
| Dependencies / RunContext | | | | |
| Output/result | | | | |
| Validators | | | | |
| Tools | | | | |
| Model/provider | | | | |
| Retries | | | | |
| Usage limits | | | | |
| Messages/history | | | | |
| Streaming | | | | |
| Approvals/deferred tools | | | | |
| Instrumentation/evals | | | | |

## Architecture
- MCP boundary:
- Application use case:
- Agent orchestration:
- Domain:
- Infrastructure:

## Security
- Tool authorization:
- Prompt injection:
- Untrusted MCP content:
- Secrets:
- Tenant isolation:

## Reliability
- Timeout:
- Retry:
- Idempotency:
- Cancellation:
- Concurrency:
- Usage limits:
- Failure recovery:

## Verification
- Deterministic model seam:
- Agent unit tests:
- Tool tests:
- Injection fixtures:
- MCP integration:
- Live provider checks (only if actually executed):

## Unknowns
List every behavior not established by first-party evidence. Blocking unknowns must be resolved before implementation.

## Evidence classification
Use `official-doc`, `official-example`, `source`, `test`, `spec`, `first-party-dependency`, or `secondary`. Secondary evidence never overrides contradictory first-party evidence.