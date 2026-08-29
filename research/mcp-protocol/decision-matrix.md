# MCP Protocol Decision Matrix

| Concern | Default | Exception requires evidence |
|---|---|---|
| Protocol version | Explicit target version | Compatibility range with tested matrix |
| Transport | Native FastMCP transport | Custom transport only for a proven requirement |
| Capabilities | Advertise implemented features only | Explicit compatibility shim |
| State | Explicit lifecycle/session state | Stateless endpoint where protocol semantics permit |
| Tools | Typed validated schemas | Dynamic schema only with documented reason |
| Resources | URI + authorization contract | Ephemeral resources with explicit lifecycle |
| Prompts | Validated arguments | Free-form only when protocol/client contract requires it |
| Errors | Deliberate protocol/application mapping | Raw internal errors never exposed |
| Authorization | Deterministic security/application policy | No model/tool-description authorization |
| Concurrency | Explicit session-state ownership | Shared state only with synchronization/proof |
| Testing | Protocol contract + integration tests | Unit-only for pure mapping logic |

## Hard rules

1. MCP protocol semantics come from the specification, not assumptions about framework internals.
2. Exact protocol and FastMCP versions must be explicit.
3. Capabilities must not be over-advertised.
4. Lifecycle state must be respected.
5. Tools, resources and prompts are distinct protocol primitives.
6. Protocol errors and application errors are not interchangeable.
7. Authentication is not authorization; model behavior is not authorization.
8. External protocol inputs and remote tool results are untrusted.
9. Cancellation and disconnect must release resources.
10. Native FastMCP functionality is preferred over custom protocol plumbing when it satisfies the requirement.