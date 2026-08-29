# Contributing

## Branch and PR lifecycle

`main` is the only persistent branch.

For every coherent change:

1. Start from an up-to-date `main`.
2. Create one short-lived `feat/*`, `fix/*`, `refactor/*`, `docs/*`, or `chore/*` branch.
3. Make the change and synchronize relevant documentation.
4. Run the strongest applicable local verification.
5. Open exactly one PR for the branch.
6. Review the PR.
7. Merge into `main`.
8. Delete the source branch immediately.
9. Verify `main` and audit the remaining branch inventory.

Do not leave branches without PRs. Do not leave merged source branches. Do not commit routine work directly to `main`.

## Verification

GitHub Actions are optional. If CI is unavailable, do not wait for it and do not invent its results. Run repository-local tests, lint, type checks, builds, static analysis, protocol/conformance checks, and security checks that are applicable and available.

## Documentation

If a change affects behavior, architecture, API, configuration, operations, testing, or agent workflow, update the corresponding documentation in the same PR. If no documentation change is needed, explain why in the PR.
