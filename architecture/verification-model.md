# Verification Model

Verification is part of engineering design, not a final ceremonial step.

## Evidence pyramid

```text
                    Acceptance
                       /\
                      /  \
              MCP / Protocol
                    /      \
             Integration  Security
                /            \
             Unit       Operational
                \            /
                 Static Quality
                      /\
                 Contracts
                      /\
                 Requirements
```

Higher layers validate externally meaningful behavior; lower layers provide fast diagnostic feedback.

## Change classification

Before choosing checks, classify the change:

- documentation-only;
- domain behavior;
- application behavior;
- persistence/infrastructure;
- MCP contract;
- MCP runtime/composition;
- authentication/authorization;
- concurrency/background execution;
- AI integration;
- deployment/operations.

Each class activates its applicable verification matrix.

## Verification matrix

| Change | Unit | Integration | MCP/Protocol | Security | Operational |
|---|---:|---:|---:|---:|---:|
| Domain behavior | Required | As needed | No | As needed | No |
| Application behavior | Required | As needed | As needed | As needed | No |
| Persistence | Required | Required | As needed | As needed | As needed |
| MCP contract | As needed | Required | Required | As needed | As needed |
| Middleware/auth | Required | Required | Required | Required | As needed |
| Tasks/concurrency | Required | Required | Required | As needed | Required |
| AI integration | Required | Required | Required if MCP-facing | Required | As needed |
| Deployment | No | Required | Required | Required | Required |

## Test doubles policy

Mock boundaries that are genuinely external or nondeterministic. Do not mock the unit's own internal collaborators merely to make tests easy. For MCP behavior, prefer a real FastMCP Client/in-process integration seam where practical.

## Failure-path requirement

Happy-path tests are insufficient for externally exposed functionality. Verify validation failures, authorization failures, downstream failures, timeouts/cancellation where applicable, and state consistency.

## Regression requirement

Every defect fix must add or update a regression test unless the change is demonstrably non-testable documentation/configuration work. The verification report must state the reason when no regression test is added.

## Reproducibility

Verification commands must be executable by another engineer from the documented project environment. Record environment assumptions and unavailable external services.
