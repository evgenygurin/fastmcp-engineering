# MCP Testing Pyramid

```text
                    deployed E2E
                        ▲
                 transport contract
                        ▲
                  FastMCP Client
                        ▲
             application/component
                        ▲
                    domain unit
```

## Rule

Each layer proves a different boundary. A lower layer cannot silently stand in for a higher-layer guarantee.

- Domain tests prove business invariants.
- Application/component tests prove orchestration and adapters.
- FastMCP Client tests prove the MCP-facing contract.
- Transport tests prove stdio/HTTP/session/auth behavior at that transport.
- Deployed E2E tests prove the actual deployment topology.

## Required review

For every requirement, state the lowest sufficient layer and any higher layer required by the risk. If a test uses an in-process server, do not label it HTTP/E2E. If auth is security-critical, exercise the actual MCP security boundary rather than only unit-testing the policy function.
