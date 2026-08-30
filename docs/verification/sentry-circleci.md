# Sentry + CircleCI

This repository uses CircleCI for an optional CI/CD path with Sentry release correlation. The repository remains testable without Sentry; the Sentry release job is gated to `main` and version tags.

## CircleCI secrets

Configure these as CircleCI Project Environment Variables or, preferably, in a restricted Context:

- `SENTRY_AUTH_TOKEN` — Sentry authentication token for CI/release operations.
- `SENTRY_ORG` — Sentry organization slug.
- `SENTRY_PROJECT` — Sentry project slug.

Do not commit any token or DSN to `.circleci/config.yml`. CircleCI recommends storing secrets in Project Settings or Contexts; Contexts can additionally restrict which projects/jobs can access them.

## Pipeline behavior

1. `test` runs the repository skill QA suite with Python 3.12.
2. `sentry-release` runs only after tests pass.
3. On `main` and version tags, the job creates a Sentry release using the commit SHA as the release version.
4. Commits are associated automatically with that release.
5. The release is finalized.
6. A `production` deploy is recorded for `main`.

Sentry release versions may be commit hashes, and Sentry supports associating commits and deploys with releases through its release API. The CI token must have a release-capable scope; `org:ci` is the narrow organization-level scope recommended for CI automation.

## Initial setup

1. Create or select the Sentry project.
2. Create a dedicated CI auth token with the minimum required release/CI permissions.
3. Add the three variables above to CircleCI. Prefer a restricted context such as `sentry-ci` once the organization is connected.
4. Follow the repository in CircleCI and enable the project.
5. Push to `main` or create a `v*` tag to exercise the release path.

## Security model

- No secrets are stored in Git.
- The test job does not receive Sentry credentials.
- Sentry credentials are injected only into the release job.
- Release creation is blocked when required Sentry variables are absent.
- Production deploy metadata is emitted only from `main`.
