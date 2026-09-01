---
name: documentation-evidence-governance
description: Evidence-first research governance for version-sensitive FastMCP/MCP/PydanticAI engineering.
---

# Documentation / Evidence Governance

## Non-negotiable rule
No implementation decision may be based on memory when the behavior is version-sensitive or externally defined. Research the authoritative source first.

## Trigger / Когда применять

**Scope / When to use:** evidence-first research governance for version-sensitive FastMCP/MCP/PydanticAI engineering.
**Trigger:** any version-sensitive or externally-defined behavior where an implementation decision could otherwise be based on memory.
**Upstream / Prerequisite:** an implementation-critical question; authoritative sources available; exact versions to record.
**Mission / Goal:** no implementation decision may be based on memory when the behavior is version-sensitive or externally defined; research the authoritative source first.
**Research / Evidence:** use the source hierarchy — current official specification/API documentation, official repository examples, official source and tests, official release notes/changelog, maintainer-authored material, then high-quality secondary material only as corroboration; record an evidence ledger with claim, source, exact section/API/example, version/date, applicability, confidence and implementation consequence; a secondary article never overrides primary documentation.
**Decision / Selection rules:** map the question → locate authoritative docs → inspect examples → inspect source/tests for ambiguity → record evidence → compare alternatives → make decision → implement → verify against the same contract; search broadly only after primary sources are exhausted; if evidence conflicts, preserve both claims and resolve by version/source authority rather than silently choosing one.
**Version / Compatibility:** record exact versions for FastMCP, MCP SDK, Pydantic, PydanticAI, SQLAlchemy, Python and relevant transports/providers; verify that examples apply to those versions; flag deprecated, experimental and unstable APIs explicitly.

## Deliverables

**Deliverables / Artifacts:** research brief, source map, evidence ledger, version matrix, decision log, rejected alternatives, unresolved questions, and verification checklist.
**Verification / Testing:** implementation agents consume the research package but must independently re-check critical version-sensitive claims before coding; re-check critical claims at the beginning of each implementation session.
**Failure / Stop conditions:** stop when evidence conflicts or the source changed and reassess affected decisions rather than silently carrying stale conclusions; avoid endless browsing — research stops when all implementation-critical questions have authoritative evidence and unresolved items are explicitly classified as non-blocking.
**Positive scenario:** every version-sensitive decision is grounded in authoritative evidence recorded in a version matrix and verified before coding.
**Negative scenario:** an implementation decision is based on memory or stale conclusions are carried after the source changed.

## Source hierarchy
1. Current official specification/API documentation.
2. Official repository examples.
3. Official source and tests when docs are ambiguous.
4. Official release notes/changelog.
5. Maintainer-authored material.
6. High-quality secondary material only as corroboration.

A secondary article never overrides primary documentation.

## Version discipline
Record exact versions for FastMCP, MCP SDK, Pydantic, PydanticAI, SQLAlchemy, Python and relevant transports/providers. Verify that examples apply to those versions. Flag deprecated, experimental and unstable APIs explicitly.

## Research procedure
Map the question → locate authoritative docs → inspect examples → inspect source/tests for ambiguity → record evidence → compare alternatives → make decision → implement → verify against the same contract. Search broadly only after primary sources have been exhausted.

## Evidence ledger
Every non-trivial technical decision must record: claim, source, exact section/API/example, version/date, applicability, confidence, and implementation consequence. If evidence conflicts, preserve both claims and resolve by version/source authority rather than silently choosing one.

## Examples
Examples are evidence of supported usage, not proof of every guarantee. Check whether an example is current, production-oriented, experimental or pedagogical. Never copy an example architecture wholesale without mapping its assumptions to the project.

## Source drift
At the beginning of each implementation session re-check critical version-sensitive claims. If a source changed, stop and reassess affected decisions. Do not silently carry stale conclusions.

## Research stopping rule
Research stops when all implementation-critical questions have authoritative evidence, alternatives have been evaluated, and unresolved items are explicitly classified as non-blocking. Avoid endless browsing.
