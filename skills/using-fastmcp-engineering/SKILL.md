---
name: using-fastmcp-engineering
description: Use when starting any FastMCP/MCP engineering work - establishes how to find and use fastmcp-engineering skills, requiring skill invocation before ANY response including clarifying questions
---

<SUBAGENT-STOP>
If you were dispatched as a subagent to execute a specific task, ignore this skill.
</SUBAGENT-STOP>

<EXTREMELY-IMPORTANT>
If you think there is even a 1% chance a fastmcp-engineering skill might apply to what you are doing, you ABSOLUTELY MUST invoke the skill.

IF A SKILL APPLIES TO YOUR TASK, YOU DO NOT HAVE A CHOICE. YOU MUST USE IT.

This is not negotiable. You cannot rationalize your way out of this.
</EXTREMELY-IMPORTANT>

## The Rule

**Invoke relevant or requested fastmcp-engineering skills BEFORE any response or action** — including clarifying questions, exploring the codebase, or checking files. If it turns out wrong for the situation, you don't have to use it.

**Before entering plan mode:** if you haven't already brainstormed, invoke the brainstorming skill first.

Then announce "Using [skill] to [purpose]" and follow the skill exactly. If it has a checklist, create a task per item.

## Skill Priority

When multiple skills apply, process skills come first — they set the approach, then implementation skills carry it out. Research-first and engineering-governance are the most common process skills, but the rule holds for any of them.

- "Let's build X" → research-first, then brainstorming/domain skills.
- "Fix this bug" → systematic-debugging first, then domain skills.

## Mission

Make every FastMCP/MCP engineering task evidence-first and architecture-governed: research official documentation before design, gate architecture, define contracts, use TDD, verify before claiming completion. The goal of this skill is to trigger the correct domain skill at the correct moment.

## Scope

This skill applies when the task touches FastMCP servers, MCP protocol semantics, Python/Pydantic contracts, databases, security, observability, deployment, or agent workflows built on these. It does not apply to pure frontend or non-engineering prose work with no framework-sensitive component.

## Trigger

Use when starting any conversation or task that may involve FastMCP/MCP engineering — before any response, exploration, or implementation. Apply before entering plan mode and before writing any code.

## Upstream

Prerequisite context: the task description and the current repository state (branch, contracts, AGENTS.md). Required input is whatever the dispatcher supplied; never substitute memory for current evidence.

## Research

Official documentation is mandatory evidence. Consult current FastMCP docs, the MCP specification, official examples, and primary dependency sources before any design or implementation decision. Never rely on memory-only claims.

## Decision

Selection rules: choose the smallest native FastMCP mechanism that fits; justify custom infrastructure; apply SOLID/KISS/DRY/YAGNI as constraints. When skills conflict, process skills win.

## Verification

Testing is mandatory. Run the repository's configured tests, lint, type checks, and protocol/contract checks before reporting completion. Never claim completion without fresh verification evidence.

## Failure

Stop conditions: if required evidence is unobtainable, the target version is unclear, or behavior cannot be established from official sources — stop and report what is missing. Escalate instead of guessing.

## Deliverables

The artifact required by the invoked domain skill (research record, contract, implementation with tests, verification evidence). Every deliverable cites file:line evidence where applicable.

## Version

FastMCP and MCP APIs are version-sensitive. Identify the exact supported version before using an API; never silently mix version-specific APIs or compatibility across releases.

## Domain skills index

Invoke the matching domain skill when its trigger matches (full inventory lives in the repository `skills/`):

- Research gate: `research-first`, `documentation-evidence-governance`, `fastmcp-research`
- Architecture: `architecture-governor`, `application-domain`, `application-architecture-usecases`, `pattern-selection`
- Components/API: `fastmcp-components`, `api-tool-engineering`, `mcp-primitives-engineering`, `api-contract-schema-engineering`, `api-lifecycle-versioning`, `pydantic-schema-engineering`
- Protocol: `mcp-protocol-engineering`, `fastmcp-protocol-compliance`, `fastmcp-server-architecture`
- FastMCP internals: `fastmcp-auth`, `fastmcp-context-di`, `fastmcp-lifespan`, `fastmcp-middleware`, `fastmcp-providers`, `fastmcp-tasks`, `fastmcp-transforms`, `fastmcp-transports-deployment`, `fastmcp-client-testing`
- Data: `sqlalchemy-engineering`, `sqlalchemy-postgresql-engineering`, `sqlalchemy-persistence-architecture`, `database-persistence-sqlalchemy`, `data-persistence-engineering`, `pydantic-engineering`
- Security: `security-engineering`, `security-threat-modeling`, `security-privacy-governance`, `dependency-supply-chain-security`
- Reliability/performance: `reliability-resilience-engineering`, `resilience-engineering`, `performance-capacity-engineering`, `performance-resource-engineering`, `async-event-driven-engineering`
- Observability: `observability-diagnostics`, `observability-opentelemetry`, `observability-operations`
- Testing/QA: `testing-tdd-engineering`, `testing-verification-engineering`, `testing-quality-engineering`, `final-review`
- Ops: `deployment-operations-engineering`, `packaging-build-deployment`, `ci-cd-github-actions-engineering`, `configuration-environment-engineering`, `dependency-injection-composition-root`

## Platform Adaptation

Per-harness tool mapping (how this skill's actions resolve to real tools) lives in `references/`:

- Claude Code → `references/claude-code-tools.md`
- Cursor → `references/cursor-tools.md`
- Codex → `references/codex-tools.md`
- Copilot CLI → `references/copilot-tools.md`
- Gemini CLI → `references/gemini-tools.md`
- Kimi Code → `references/kimi-tools.md`
- OpenCode → `references/opencode-tools.md`
- pi → `references/pi-tools.md`
