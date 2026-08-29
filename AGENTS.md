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
