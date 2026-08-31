---
name: github-actions-engineering
description: Design secure, reproducible GitHub Actions CI/CD for FastMCP/PydanticAI services — use for workflow, OIDC, artifact, and deployment pipeline design.
---

# CI/CD & GitHub Actions Engineering

## Mission
Design secure, reproducible and observable GitHub Actions pipelines for FastMCP/PydanticAI Python services. CI must prove quality; CD must promote an already-tested immutable artifact.

## Mandatory research gate
Before implementation, read repository contracts and verify current official GitHub Actions documentation for workflow syntax, permissions, reusable workflows, environments, concurrency, caching, artifacts, artifact attestations, OIDC, deployment protection and security hardening. Verify every third-party action/version from its authoritative repository and prefer immutable SHA pinning where the policy requires it.

Research exact Python/package-manager/container/deployment versions and their official CI guidance. Inspect official examples/source/docs for ambiguous behavior. Record evidence and unresolved questions.

## Pipeline architecture
Prefer explicit stages:
1. static quality;
2. unit/component tests;
3. integration/security tests;
4. build;
5. artifact/provenance;
6. publish;
7. deployment approval/gate;
8. deploy immutable artifact;
9. smoke/health verification;
10. promotion/rollback.

Do not rebuild a production artifact after tests. Build once, identify by immutable digest, then promote that exact artifact.

## Workflow design
Use reusable workflows for deterministic repeated CI/CD logic. Keep caller workflows thin and parameterized. Pin reusable external workflows/actions according to repository supply-chain policy. Use explicit `permissions` and default to least privilege. Never grant broad write permissions for convenience.

Use `concurrency` deliberately to prevent obsolete deployments and redundant work, but do not accidentally cancel a critical production deployment. Separate PR validation concurrency from deployment concurrency.

Use environments for production secrets and deployment protection where applicable. Do not pass secrets through arbitrary inputs. Never echo secrets or dump complete contexts.

## OIDC
Prefer short-lived OIDC federation over long-lived cloud credentials. Scope trust policies to repository, environment/ref and, where applicable, reusable workflow identity. `id-token: write` is only enabled on the job that needs federation. Keep other permissions minimal.

## Artifacts
Distinguish cache from artifact. Cache dependencies/build acceleration; artifacts carry outputs between jobs/runs. Verify artifact provenance and integrity before deployment. Generate provenance/SBOM attestations for release artifacts where supported and verify them according to the deployment policy.

## Caching
Cache only deterministic, non-secret inputs/outputs. Lockfile-aware cache keys are mandatory. Never cache credentials, environment secrets or mutable production state. Ensure cache poisoning cannot cross trust boundaries.

## Testing gates
CI must run deterministic tests without live provider credentials. Live-provider tests belong in explicit integration jobs with controlled credentials. FastMCP protocol tests, PydanticAI deterministic model tests and real PostgreSQL integration tests must remain distinct where semantics differ.

## Security
Treat workflow YAML, action inputs, PR code and generated artifacts as potentially hostile. Never execute untrusted PR code with production secrets or write-capable deployment credentials. Fork PRs require a separate security model. Restrict `pull_request_target` to narrowly justified cases.

## Deployment
Deployment jobs require explicit environment and branch/tag policy. Deploy by immutable image/package digest, not mutable tags. Run smoke/health checks after deployment. Define rollback criteria and ensure rollback references a known-good immutable artifact.

## Release
Separate PR CI from release/deployment workflows. Tags/releases must have explicit provenance. Avoid release automation that can publish from arbitrary branches. Ensure version and artifact identity are deterministic.

## Verification
Validate workflow syntax, action references, permissions, dependency/cache behavior, artifact transfer, provenance, deployment gates, concurrency and failure paths. Test cancellation and rerun behavior. Verify that a deployment consumes exactly the artifact produced by the tested build.

## Rejection criteria
Reject workflows with broad default write permissions, long-lived cloud credentials when OIDC is available, mutable production artifact references, rebuild-after-test deployment, unbounded secret exposure, untrusted PR access to deployment credentials, cache trust-boundary violations, missing deployment gates, or unverified provenance where provenance is a required control.

## Deliverables
CI/CD topology, workflow dependency graph, permissions matrix, action pinning policy, cache policy, artifact/provenance policy, OIDC trust model, environment/deployment policy, rollback model, verification matrix, implementation and final verification report.