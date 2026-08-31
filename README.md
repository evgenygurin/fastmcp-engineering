# FastMCP Engineering

Engineering methodology, research artifacts, skills, prompts, contracts, and quality gates for building production-grade MCP servers with FastMCP.

## Core principles

- Research official documentation and official examples before making framework decisions.
- Separate domain, application, infrastructure, and MCP delivery responsibilities.
- Prefer the simplest architecture that satisfies real requirements.
- Use SOLID, KISS, DRY, and YAGNI as decision criteria, not as reasons to add abstractions.
- Prefer native FastMCP capabilities before custom infrastructure.
- Keep Pydantic, SQLAlchemy, PydanticAI, Supabase, and other technologies behind appropriate boundaries.
- Verify behavior with tests, protocol checks, security review, and architecture review.
- Treat documentation and repository hygiene as part of correctness.

## Engineering workflow

Preflight → Requirement → Discovery → Documentation Research → Example Research → Architecture → Design Gate → Contracts → TDD → Implementation → Documentation Sync → Static Analysis → Tests → Security Review → Architecture Review → PR Review → Merge → Delete Source Branch → Verify `main` → Branch Audit.

## GitHub workflow

`main` is the only persistent branch. Work is performed on one short-lived intent-named branch with exactly one PR:

```text
main → feat/fix/refactor/docs/chore branch → PR → review → merge → delete branch → verify main
```

A branch without a PR is orphan work. A merged PR whose source branch survives is incomplete work. If branch deletion is unavailable through the current tooling, completion must be reported as blocked.

## Verification without CI

GitHub Actions are optional and are not a prerequisite for development or merge. When CI is unavailable, run the strongest applicable local checks: tests, lint, type checks, builds, static analysis, protocol/conformance checks, and security checks. Never invent CI results and never lower the verification standard because CI is unavailable.

## Documentation synchronization

Changes to externally relevant behavior, architecture, API, configuration, operations, testing procedures, or agent workflow must update the relevant documentation in the same PR. Intentional documentation non-changes must be explained in the review evidence.

## Version policy

FastMCP version-specific claims must identify their version and stability level. Stable and prerelease APIs must never be silently mixed.

## Status

Consolidated engineering foundation. The repository contains canonical skills, prompts, contracts, architecture guidance, research artifacts, and verification rules. New implementation work follows the branch/PR lifecycle above.

## opencode integration

Global exposure of this repository's capabilities in opencode:

- **Skills**: global `skills.paths` → this clone (frontmatter `name`+`description` required)
- **Reference**: `references.fastmcp-eng` — whole repo readable in any project
- **Plugin hint**: `~/.config/opencode/plugin/fastmcp-engineering.ts` (verified PASS 2026-08-30)
- **fm-* role agents**: `opencode/agents/` — research/implementation/audit/review/governor subagents; they load `prompts/<token>-<role>-agent.md` at runtime (auto-sync, no duplication)
- **Commands**: `opencode/commands/` — `/fm` dispatcher, `/fm-prompts` inventory

Setup on a new machine (symlinks into global config, run from repo root):

    ln -s "$PWD/opencode/agents/fm-research.md" ~/.config/opencode/agents/fm-research.md
    ln -s "$PWD/opencode/agents/fm-implementation.md" ~/.config/opencode/agents/fm-implementation.md
    ln -s "$PWD/opencode/agents/fm-audit.md" ~/.config/opencode/agents/fm-audit.md
    ln -s "$PWD/opencode/agents/fm-review.md" ~/.config/opencode/agents/fm-review.md
    ln -s "$PWD/opencode/agents/fm-governor.md" ~/.config/opencode/agents/fm-governor.md
    ln -s "$PWD/opencode/commands/fm.md" ~/.config/opencode/commands/fm.md
    ln -s "$PWD/opencode/commands/fm-prompts.md" ~/.config/opencode/commands/fm-prompts.md

Design: `docs/superpowers/specs/2026-08-31-opencode-fastmcp-maximal-design.md`
