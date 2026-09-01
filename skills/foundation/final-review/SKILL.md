---
name: final-review
description: Perform evidence-based final review of a FastMCP change before declaring it complete.
---

# Final Review

## Rule

Never declare completion from code inspection alone. Review the implementation and the verification evidence.

## Trigger / Когда применять

**Scope / When to use:** any FastMCP change before it is declared complete.
**Trigger:** before declaring completion of a change that touches code, contracts, architecture, configuration, operations, or agent workflow.
**Upstream / Prerequisite:** the implemented change plus its verification evidence; review order and evidence standard.
**Mission / Goal:** review the implementation and the verification evidence, never completion from code inspection alone.
**Research / Evidence:** official documentation/version evidence, relevant official examples, and MCP protocol semantics; an evidence standard that reports command, expected result, actual result, evidence/reference, and pass/fail.
**Decision / Selection rules:** return exactly PASS, PASS WITH CONDITIONS, or REJECT based on whether required gates have evidence; a clean test suite does not override a failed architecture or security gate.
**Version / Compatibility:** Привязан к целевому FastMCP/MCP/Python-релизу.

## Deliverables

**Deliverables / Artifacts:** a completion decision (PASS / PASS WITH CONDITIONS / REJECT) backed by the evidence-standard report across the review order.
**Verification / Testing:** for each required verification report command or inspection, expected result, actual result, evidence/reference, and pass/fail; do not convert an unrun check into a pass.
**Failure / Stop conditions:** REJECT when any blocking architecture, security, correctness, contract, or verification defect remains; stop rather than declare completion from code inspection alone.
**Positive scenario:** all required gates have fresh evidence and the change is declared PASS.
**Negative scenario:** a failed architecture or security gate is overridden by a clean test suite and the change is wrongly declared complete.

## Review order

1. Requirement coverage.
2. Official documentation/version evidence.
3. Relevant official examples.
4. MCP protocol semantics.
5. Architecture and dependency direction.
6. Responsibility boundaries.
7. Pattern/YAGNI decisions.
8. Public MCP contracts and schema quality.
9. Error/failure behavior.
10. Authentication/authorization/security.
11. Observability and operational behavior.
12. Unit/integration/MCP/transport/conformance tests.
13. Static analysis and packaging.
14. Documentation.

## FastMCP checks

Confirm that native mechanisms were considered before custom infrastructure. Verify that tools/resources/prompts remain adapters, Providers source components, Transforms modify MCP presentation/composition, Middleware handles cross-cutting concerns, and lifecycle ownership is explicit.

## Evidence standard

For each required verification, report:

- command or inspection performed;
- expected result;
- actual result;
- evidence/reference;
- pass/fail.

Do not convert an unrun check into a pass.

## Decision

Return exactly one:

- `PASS` — all required gates have evidence.
- `PASS WITH CONDITIONS` — no blocking defect, but explicit non-blocking limitations remain.
- `REJECT` — any blocking architecture, security, correctness, contract, or verification defect remains.

A clean test suite does not override a failed architecture or security gate.
