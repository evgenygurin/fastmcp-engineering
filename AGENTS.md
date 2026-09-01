# FastMCP Engineering — Agent Contract

## Mission

Build production-grade MCP servers through evidence-driven research, explicit architecture, TDD, security review, documentation synchronization, and verification.

## Non-negotiable rules

1. Research official FastMCP documentation before designing or implementing a FastMCP feature.
2. Inspect relevant official FastMCP examples before selecting an implementation mechanism.
3. Verify the MCP protocol semantics relevant to the feature.
4. Identify the supported FastMCP version before using an API; never silently mix version-specific APIs.
5. Prefer native FastMCP mechanisms (Providers, Transforms, Middleware, Context, Lifespans, tasks, auth, client, etc.) when they fit; justify custom infrastructure.
6. Keep domain logic independent of FastMCP, SQLAlchemy, Pydantic, Supabase, HTTP clients, and LLM SDKs unless a deliberate boundary requires otherwise.
7. Keep MCP handlers thin: validate/translate input, invoke an application use case, translate the result.
8. Apply SOLID, KISS, DRY, and YAGNI as constraints, not slogans. Every non-trivial abstraction needs a reason.
9. Use TDD for behavior changes and verify at the appropriate unit, integration, MCP-contract, transport, security, and conformance levels.
10. Never claim completion without fresh verification evidence.
11. Treat documentation as part of the implementation when code, architecture, API, configuration, operational behavior, or agent workflow changes.
12. Do not create persistent work on `main`. Every change must use one short-lived work branch with one corresponding PR.
13. Never leave a branch without a PR. If work is abandoned or no longer needs merging, delete the branch.
14. After a PR is merged, delete its source branch. A merged PR with a surviving source branch is not complete.
15. `main` is the only persistent branch. Branch inventory must be checked at finalization.
16. GitHub Actions are optional. They must never be treated as a prerequisite for development or merge when unavailable or unfunded.
17. When CI is unavailable, perform the strongest applicable local verification: tests, lint, type checks, build, static analysis, protocol checks, and security checks. Record anything that cannot be run.
18. Do not weaken verification merely because CI is unavailable.
19. Before starting work, inspect the current branch, working state, open PRs, and branch inventory. Do not create another branch for work that already has an active branch/PR.
20. After merge, verify that `main` contains the intended change, the PR is merged, the source branch is deleted, and no orphan PR/branch was created by the task.

## Required workflow

Preflight → Requirement → discovery → official research → example/pattern analysis → version check → architecture → architecture gate → contracts → tests → implementation → documentation sync → static analysis → integration/MCP tests → security review → architecture review → PR → review → merge → source-branch deletion → main verification → branch inventory.

## Branch lifecycle

Use short-lived branches named by intent:

- `feat/<scope>` for new behavior;
- `fix/<scope>` for bug fixes;
- `refactor/<scope>` for structural changes without intended behavior change;
- `docs/<scope>` for documentation-only changes;
- `chore/<scope>` for maintenance.

Lifecycle is mandatory:

```text
main
  -> create one short-lived branch
  -> implement and verify
  -> open exactly one PR
  -> review
  -> merge into main
  -> delete source branch
  -> verify main
  -> verify branch inventory
```

A branch must not survive merge. A task must not be reported complete while its source branch remains. If the connected GitHub capability cannot delete the branch, report cleanup as blocked rather than claiming completion.

## Documentation synchronization

When implementation changes externally relevant behavior, architecture, configuration, APIs, testing procedure, operations, or agent workflow, update the relevant documentation in the same PR. If documentation is intentionally unchanged, record the reason in the PR/review evidence.

## Verification policy

CI is an optional evidence source, not the definition of correctness. Local verification is authoritative when CI is unavailable. Use the repository's configured commands and test layers; do not invent passing results. A completion claim requires fresh evidence from the current change.

## Quality principle

A minimal correct design is preferred over a sophisticated design. Framework correctness is not sufficient: responsibility boundaries, failure modes, security, testability, operability, documentation, and maintainability must also be correct.

## Agent bootstrap

When working in any harness that loads fastmcp-engineering skills, the
`using-fastmcp-engineering` bootstrap skill is injected at session start. It
teaches the agent to invoke a matching fastmcp-engineering skill BEFORE any
response or action. Do not bypass the bootstrap; follow the invoked skill's
procedure, including its research gate, architecture gate, TDD cycle, and
verification requirements.

<!-- gitnexus:start -->
# GitNexus — Code Intelligence

This project is indexed by GitNexus as **fastmcp-engineering** (2708 symbols, 2725 relationships, 0 execution flows). Use the GitNexus MCP tools to understand code, assess impact, and navigate safely.

> Index stale? Run `node .gitnexus/run.cjs analyze` from the project root — it auto-selects an available runner. No `.gitnexus/run.cjs` yet? `npx gitnexus analyze` (npm 11 crash → `npm i -g gitnexus`; #1939).

## Always Do

- **MUST run impact analysis before editing any symbol.** Before modifying a function, class, or method, run `impact({target: "symbolName", direction: "upstream"})` and report the blast radius (direct callers, affected processes, risk level) to the user.
- **MUST run `detect_changes()` before committing** to verify your changes only affect expected symbols and execution flows. For regression review, compare against the default branch: `detect_changes({scope: "compare", base_ref: "main"})`.
- **MUST warn the user** if impact analysis returns HIGH or CRITICAL risk before proceeding with edits.
- When exploring unfamiliar code, use `query({search_query: "concept"})` to find execution flows instead of grepping. It returns process-grouped results ranked by relevance.
- When you need full context on a specific symbol — callers, callees, which execution flows it participates in — use `context({name: "symbolName"})`.
- For security review, `explain({target: "fileOrSymbol"})` lists taint findings (source→sink flows; needs `analyze --pdg`).

## Never Do

- NEVER edit a function, class, or method without first running `impact` on it.
- NEVER ignore HIGH or CRITICAL risk warnings from impact analysis.
- NEVER rename symbols with find-and-replace — use `rename` which understands the call graph.
- NEVER commit changes without running `detect_changes()` to check affected scope.

## Resources

| Resource | Use for |
|----------|---------|
| `gitnexus://repo/fastmcp-engineering/context` | Codebase overview, check index freshness |
| `gitnexus://repo/fastmcp-engineering/clusters` | All functional areas |
| `gitnexus://repo/fastmcp-engineering/processes` | All execution flows |
| `gitnexus://repo/fastmcp-engineering/process/{name}` | Step-by-step execution trace |

## Cross-Repo Groups

This repository is listed under GitNexus **group(s): job-hub** (see `~/.gitnexus/groups/`). For cross-repo analysis, use MCP tools `impact`, `query`, and `context` with `repo` set to `@<groupName>` or `@<groupName>/<memberPath>` (paths match keys in that group’s `group.yaml`). Use `group_list` / `group_sync` for membership and sync. From the project root: `node .gitnexus/run.cjs group list`, `node .gitnexus/run.cjs group sync <name>`, `node .gitnexus/run.cjs group impact <name> --target <symbol> --repo <group-path>` (the `.gitnexus/run.cjs` path is repo-root-relative).

## CLI

| Task | Read this skill file |
|------|---------------------|
| Understand architecture / "How does X work?" | `.claude/skills/gitnexus/gitnexus-exploring/SKILL.md` |
| Blast radius / "What breaks if I change X?" | `.claude/skills/gitnexus/gitnexus-impact-analysis/SKILL.md` |
| Trace bugs / "Why is X failing?" | `.claude/skills/gitnexus/gitnexus-debugging/SKILL.md` |
| Rename / extract / split / refactor | `.claude/skills/gitnexus/gitnexus-refactoring/SKILL.md` |
| Tools, resources, schema reference | `.claude/skills/gitnexus/gitnexus-guide/SKILL.md` |
| Index, status, clean, wiki CLI commands | `.claude/skills/gitnexus/gitnexus-cli/SKILL.md` |

<!-- gitnexus:end -->
