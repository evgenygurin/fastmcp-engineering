# Verification Contract

No completion claim without evidence.

## Verification layers

1. Formatting/linting.
2. Static typing.
3. Unit tests.
4. Component/integration tests.
5. MCP contract tests using a real FastMCP Client where appropriate.
6. Transport tests for deployed transports.
7. Security checks.
8. Architecture/dependency checks.
9. Protocol/conformance checks when applicable.
10. Scenario/evaluation tests for agent-facing behavior when applicable.

## Failure policy

A failed check is a blocker. Do not weaken the test, skip the check, or claim success without documenting and resolving the failure.

## Evidence record

```yaml
verification:
  status: passed|failed|blocked
  commands: []
  results: []
  skipped: []
  known_failures: []
  residual_risks: []
```
