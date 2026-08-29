# GitHub Workflow Contract

## Purpose

This contract defines the repository lifecycle for all engineering work. `main` is the only persistent branch.

## Branch invariant

Temporary branches are allowed only while work is actively implemented or reviewed. Every temporary branch MUST have exactly one corresponding PR or be deleted immediately when work is abandoned.

## Lifecycle

```text
main -> short-lived work branch -> local verification -> one PR -> review -> merge -> delete source branch -> verify main -> audit branches
```

## Branch naming

Use `feat/<scope>`, `fix/<scope>`, `refactor/<scope>`, `docs/<scope>`, or `chore/<scope>`.

## One branch, one PR

A work branch MUST NOT accumulate unrelated tasks. A PR is the review and integration unit.

## Review and merge

Before merge, requirements, relevant documentation, applicable tests/static checks, and required security/architecture review must be satisfied. GitHub Actions are optional and are not a prerequisite when unavailable or unfunded.

## Post-merge cleanup

Immediately after merge:

1. Confirm the PR is merged.
2. Confirm `main` contains the merged change.
3. Delete the source branch.
4. Refresh branch state.
5. Verify no orphan PR exists.
6. Verify no stale source branch remains from the completed task.

## Failure handling

If branch deletion is unavailable through current tooling, report cleanup as blocked and do not claim completion. If CI is unavailable, use the strongest applicable local verification and explicitly record unavailable checks.

## Finalization gate

Work is complete only when:

```text
PR merged
AND main verified
AND source branch deleted
AND no orphan PR
AND persistent branch set == {main}
```
