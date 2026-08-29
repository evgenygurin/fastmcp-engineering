---
name: engineering-governance
description: Meta-orchestration and governance for evidence-driven engineering across all project skills.
---

# Engineering Governance / Meta-Orchestration

## Mission
Coordinate engineering work by risk, evidence and architectural dependencies. Governance is a control system, not bureaucracy: trivial changes take a short path; architectural changes take the full path.

## Mandatory workflow
Classify change risk first: trivial, bounded, architectural or breaking. Select required skills from the dependency graph. For version-sensitive work, research current official documentation and exact installed versions before design or implementation.

Required lifecycle for architectural/breaking work:
1. Research and evidence collection.
2. Design gate.
3. Implementation plan.
4. TDD/tests where behavior changes.
5. Implementation.
6. Verification.
7. Security review when relevant.
8. Performance/reliability review when relevant.
9. Documentation/ADR update.
10. PR review.
11. Merge only after required gates pass.
12. Post-merge verification when operationally relevant.

## Evidence gate
Every version-sensitive claim must identify source, version and verification status. Prefer official documentation and exact-version source/tests. Do not represent inference, memory or an unverified assumption as fact.

## Design gate
Architectural changes require an explicit design before implementation. The design must state goals, non-goals, boundaries, dependencies, invariants, failure modes, security implications, performance implications, migration/rollback and rejected alternatives. Approval is required before implementation.

## Verification gate
Never claim a change is complete, fixed, passing or merged without current verification evidence. Record exact commands/checks and outcomes. A green unit suite is not sufficient when integration, protocol, security, performance or operational behavior is relevant.

## Skill dependency graph
Treat skills as composable controls. Security constraints cannot be weakened by application, performance or reliability guidance. Testing verifies behavior specified by architecture/contracts/security. Observability supports performance/reliability diagnosis. Deployment must satisfy security, reliability and observability requirements. Data changes require contract, security, migration and recovery consideration.

## Change classification
- Trivial: documentation/cosmetic/no runtime behavior; lightweight verification.
- Bounded: isolated behavior with known interfaces; focused tests and relevant skill gates.
- Architectural: dependency/lifecycle/protocol/data/security/operational boundary changes; full design and cross-skill review.
- Breaking: incompatible public behavior/schema/protocol/data contract; migration, compatibility and rollback analysis required.

## Cross-skill precedence
When requirements conflict, preserve higher-risk safety properties first: security/integrity, correctness, data durability, reliability, observability, performance, convenience. No optimization may bypass validation/authz/audit. No resilience mechanism may weaken security. No telemetry may leak protected data.

## Exception policy
Exceptions must state the violated rule, reason, risk, compensating control, owner and expiry/revisit condition. Never silently bypass a gate. Temporary exceptions must be tracked.

## ADR / decision records
Record consequential architectural decisions with context, decision, alternatives, consequences, risks and rollback/migration notes. Link the decision to the affected skills and evidence.

## Definition of Ready
Scope and acceptance criteria are clear; change classification is known; relevant dependencies/skills are identified; constraints and security/data implications are known; required research/design approvals exist.

## Definition of Done
Implementation matches approved design; required tests and quality gates pass; relevant security/performance/reliability checks pass; docs/ADR are updated; exact verification evidence is recorded; PR review is complete; merge/post-merge checks are complete when required.

## PR discipline
PRs should be small enough to review, explain the architectural intent, list evidence and verification, identify residual risks and explicitly state skipped gates with justification. Do not merge known failing required checks.

## Automation
Agents may execute independent research/review work in parallel, but shared-state implementation and sequential gates remain ordered. Never parallelize writes to the same artifact when order or current SHA matters.

## Audit
A governance audit checks that the selected skills were appropriate, required gates were actually performed, evidence is current, exceptions are explicit and no later change silently invalidated earlier controls.

## Rejection criteria
Reject work with missing design approval for architectural changes, unverifiable completion claims, blind dependency/version assumptions, hidden exceptions, skipped mandatory security/data/reliability checks, failing required tests, or cross-skill conflicts resolved by silently weakening safety controls.

## Deliverables
Change classification; skill dependency graph; research/evidence ledger; design gate; implementation plan; verification record; security/performance/reliability review; ADR/decision record; exception register; PR checklist; post-merge verification; final governance audit.