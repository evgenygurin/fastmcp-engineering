# Security Decision Matrix

| Concern | Required decision | Evidence |
|---|---|---|
| Identity | Exact auth mechanism/profile | MCP + framework docs |
| Authorization | Deterministic policy boundary | Architecture + tests |
| MCP trust | Explicit server/client trust decision | MCP/FastMCP docs |
| Tool access | Least privilege | Tool inventory |
| Side effects | Idempotency/approval policy | Application design |
| URLs | Scheme/host/egress policy | SSRF threat model |
| Files | Canonical root/sandbox policy | Filesystem threat model |
| DB | Least privilege + tenant boundary | DB policy |
| Secrets | External storage + redaction | Secret policy |
| Availability | Bounded resources | Load/abuse model |
| Supply chain | Lock/provenance/scanning | Dependency policy |

## Hard rules

1. Protocol requirements are verified, never guessed.
2. Authentication and authorization are separate concerns.
3. Prompts are not authorization controls.
4. Model output is untrusted.
5. Remote MCP is a separate trust domain unless explicitly established otherwise.
6. Sensitive tools follow least privilege.
7. Non-idempotent side effects require replay protection or approval.
8. Secrets never enter model-visible context or ordinary logs.
9. Critical threats require executable regression tests.
10. Security exceptions must be explicit, scoped and documented.