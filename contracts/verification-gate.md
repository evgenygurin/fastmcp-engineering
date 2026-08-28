# Verification Gate Contract

Verification is a mandatory evidence-producing gate. A claim that work is complete is invalid unless the applicable checks have actually been executed or explicitly marked unavailable.

## Verification layers

```text
Requirements
    ↓
Architecture
    ↓
Contracts
    ↓
Static quality
    ↓
Unit tests
    ↓
Component tests
    ↓
MCP integration / protocol tests
    ↓
Security
    ↓
Operational checks
    ↓
Documentation
    ↓
Final acceptance
```

The applicable layers depend on the change. Omitting a layer requires an explicit reason.

## Evidence rule

Every verification claim must have:

- command or inspection performed;
- scope;
- result;
- relevant output or artifact reference;
- timestamp/session context where useful;
- limitations.

Never report a check as passing because it was expected to pass.

## Required test categories

At minimum, evaluate whether the change needs:

- domain unit tests;
- application/use-case tests;
- infrastructure integration tests;
- FastMCP Client tests;
- transport tests;
- authentication/authorization tests;
- concurrency/background-task tests;
- schema/contract tests;
- failure-path tests.

## MCP-specific verification

For MCP-facing changes verify, where applicable:

- tool/resource/prompt registration;
- input and output schemas;
- error semantics;
- context/session behavior;
- middleware ordering;
- provider/transform composition;
- authentication and authorization;
- pagination;
- task/background execution semantics;
- transport behavior;
- protocol compatibility.

Prefer FastMCP's documented testing/client mechanisms over brittle implementation-level mocks for MCP integration behavior.

## Static quality

Run the project's configured formatter, linter, type checker, and test suite. If a tool is not configured, do not invent a pass; record it as absent and assess whether it is required by the project standard.

## Security gate

Security-sensitive changes require explicit review of:

- authentication;
- authorization;
- credential/token handling;
- input validation;
- output/data exposure;
- prompt injection/tool misuse where AI is involved;
- SSRF and outbound network access where relevant;
- logging of secrets or sensitive data;
- dependency vulnerabilities where tooling is available.

## Architecture re-check

After implementation, rerun the relevant architecture checks. Implementation drift can invalidate an earlier architecture approval.

## Verdicts

`PASS` — all required checks have evidence and no blocking issue remains.

`PASS WITH CONDITIONS` — no release-blocking issue remains, but conditions are recorded.

`REJECT` — one or more required checks failed, evidence is missing, or a blocking issue remains.

## Required verification report

```markdown
# Verification Report

## Change

## Requirements Verified

## Architecture Re-check

## Static Analysis

## Tests

## MCP / Protocol Verification

## Security Verification

## Documentation Verification

## Evidence

## Failures / Limitations

## Verdict
PASS | PASS WITH CONDITIONS | REJECT

## Follow-up
```
