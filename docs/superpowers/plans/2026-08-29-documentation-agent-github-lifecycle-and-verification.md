# Documentation, Agent Rules, GitHub Lifecycle and Verification Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development or superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Synchronize documentation and agent rules with the consolidated repository and enforce a deterministic branch/PR lifecycle with CI-independent verification.

**Architecture:** Repository policy is split into the agent contract, a GitHub lifecycle contract, and the engineering-system specification. Local verification is authoritative when GitHub Actions are unavailable.

**Tech Stack:** Markdown, GitHub branches/PRs, repository-local verification.

**Spec:** `docs/specs/engineering-system.md`

## Global Constraints

- `main` is the only persistent branch.
- Every non-main change uses one short-lived work branch and exactly one PR.
- After merge, the source branch must be deleted before completion.
- GitHub Actions are optional and never a prerequisite for development or merge.
- Local verification is mandatory when technically possible.
- Documentation changes belong in the same PR when code, architecture, behavior, or agent workflow changes require them.

## Tasks

1. Update `AGENTS.md` with branch lifecycle, documentation sync, and CI-independent verification rules.
2. Add `contracts/github-workflow-contract.md`.
3. Update `docs/specs/engineering-system.md`.
4. Update `README.md` and add `CONTRIBUTING.md`.
5. Add GitHub lifecycle, documentation, and finalization agent prompts.
6. Review repository documentation for contradictions and run all applicable local verification.
7. Merge the PR and verify source-branch cleanup.
