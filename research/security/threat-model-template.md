# Security Threat Model Research Package

## Target
- MCP protocol:
- FastMCP:
- Python:
- PydanticAI:
- Pydantic:
- SQLAlchemy:
- ASGI/server:
- Authentication libraries:
- Database:
- Date:

## System/data flow
```text
[Client] -> [Transport] -> [FastMCP] -> [Application] -> [Domain]
                                      |             |
                                      v             v
                                   [Agent]       [Database]
                                      |
                                      v
                               [External Tools/APIs]
```

Replace with verified architecture.

## Trust boundaries
| Boundary | Source | Destination | Data crossing | Trust assumption | Control | Evidence |
|---|---|---|---|---|---|---|

## Assets
| Asset | Classification | Owner | Impact | Required protection |
|---|---|---|---|---|

## Actors / privileges
| Actor | Identity | Capabilities | Tenant scope | Threat potential |
|---|---|---|---|---|

## Attack-path register
| Threat | Preconditions | Attack path | Impact | Likelihood | Control | Verification | Residual risk |
|---|---|---|---|---|---|---|---|

## MCP security matrix
| Area | Exact protocol requirement | FastMCP mechanism | Application control | Evidence |
|---|---|---|---|---|
| Authentication | | | | |
| Authorization | | | | |
| Tokens | | | | |
| Scopes | | | | |
| Audience/issuer | | | | |
| Tool access | | | | |
| Resource access | | | | |
| Transport | | | | |
| Replay | | | | |

## Agent/tool threat matrix
- Prompt injection:
- Indirect injection:
- Tool poisoning:
- Malicious tool output:
- Data exfiltration:
- Tool authorization:
- Credential exposure:

## Network/data threats
- SSRF:
- DNS rebinding:
- Egress:
- Path traversal:
- Command execution:
- Deserialization:
- SQL injection:
- Resource exhaustion:
- PII leakage:

## Security invariants
1.
2.
3.
4.

## Security tests
| Invariant/threat | Test | Expected result | Status |
|---|---|---|---|

## Supply chain
- Dependency lock:
- Integrity/provenance:
- SBOM:
- Container/runtime privilege:
- Vulnerability scanning:

## Evidence ledger
| Claim | Source | Version | Classification | Confidence |
|---|---|---|---|---|

## Blocking unknowns
List every unresolved item that could change the security architecture. Implementation must stop for unresolved critical items.