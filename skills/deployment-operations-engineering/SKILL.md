---
name: deployment-operations-engineering
description: Evidence-first production deployment and operations engineering for FastMCP systems.
---

# Deployment / Operations Engineering

## Mission
Deliver reproducible, secure, observable and recoverable production deployments. Deployment machinery is infrastructure; domain/application code must remain independent of it.

## Mandatory research
Identify exact Python, FastMCP, container/runtime, CI/CD platform, database, migration-tool and deployment-target versions. Read current official documentation first for every version-sensitive mechanism, then inspect exact-version examples/source/tests. Verify commands and platform semantics rather than relying on memory.

## Build reproducibility
Build immutable artifacts from pinned, reviewable inputs. Keep dependency lockfiles and build configuration under version control. Separate build-time and runtime configuration. Do not embed secrets in images or source artifacts.

## Container security
Prefer minimal images, non-root runtime users, explicit filesystem permissions, bounded resources and deterministic entrypoints. Pin or otherwise govern base images. Scan dependencies and images where tooling supports it. Generate SBOM/provenance where required. Never treat a scanner result as proof of application security.

## CI/CD gates
Pipeline stages should include formatting/lint/type checks, unit/integration/MCP-contract tests, security checks, artifact creation and deployment verification as applicable. Do not allow deployment from an unverified artifact. Keep promotion tied to the exact artifact digest/identity.

## Environments
Separate local, test, staging and production configuration. Promote artifacts rather than rebuilding per environment. Configuration and secrets enter through the Configuration/Secrets boundary. Production credentials must never be used by ordinary CI tests.

## Database migrations
Coordinate deployment with persistence migrations. Prefer backward-compatible expand/contract changes for rolling or zero-downtime deployments. Never deploy application code that requires a schema unavailable to still-running instances. Migration failures need explicit stop/rollback/forward-fix behavior.

## Startup / readiness / liveness
Use liveness to indicate process health and readiness to indicate ability to serve traffic. Do not make liveness depend on optional downstream systems. Readiness should reflect dependencies genuinely required for serving the configured workload. Probes must be cheap, bounded and non-recursive.

## Graceful shutdown
Handle SIGTERM/cancellation correctly. Stop accepting new work, allow safe in-flight work to finish within a deadline, cancel background tasks deterministically and close resources through their lifecycle owners. Verify behavior rather than assuming framework defaults.

## Deployment strategies
Choose rolling, canary, blue/green or another strategy based on compatibility and risk. Define health gates, observation windows and rollback criteria. Zero-downtime is a property to verify, not a label to claim.

## Rollback
Distinguish code rollback from schema rollback. Prefer forward-compatible schema changes so application rollback remains possible. Define rollback ownership, data compatibility, traffic reversal and migration recovery. Never blindly downgrade a production database schema.

## Concurrency
Prevent conflicting deployments/migrations through explicit locks or CI concurrency controls. Ensure retries do not trigger duplicate migrations or unsafe promotion. Deployment jobs must be idempotent where practical.

## Runtime resources
Define CPU, memory, file descriptor, connection, worker and request limits. Resource limits must align with performance/capacity budgets and reliability policies. Avoid unlimited queues and process growth.

## Secrets/configuration
Inject secrets at runtime through approved secret/configuration mechanisms. Do not print them during builds or startup. Verify environment/config validation before traffic is accepted. Rotate credentials without requiring source changes where supported.

## Security
Apply least privilege to runtime identity, container capabilities, network egress and deployment credentials. Separate migration/admin privileges from application runtime privileges. Protect CI/CD tokens and deployment surfaces.

## Observability
Deployment and runtime must expose health, logs, metrics and traces through the Observability layer. Record deployment identity/version and correlate incidents with changes. Avoid logging secrets or full request/model payloads.

## Verification
Every deployment needs post-deploy verification appropriate to risk: health/readiness, smoke tests, MCP contract checks, critical-path checks and telemetry inspection. Verification must target the deployed artifact/environment, not merely CI.

## Failure / recovery
Define behavior for failed builds, failed migrations, unhealthy instances, dependency outages, partial rollout, deployment interruption and operator cancellation. Recovery must be bounded and observable.

## Disaster recovery
Coordinate deployment with backup/restore and RPO/RTO. Verify that a restored database can run a compatible application version. Test recovery procedures periodically; configuration documentation alone is insufficient.

## Rejection criteria
Reject mutable/untracked artifacts, secrets in images/logs, production credentials in ordinary tests, rebuild-per-environment promotion, unsafe schema rollback, unbounded runtime resources, missing graceful shutdown, deployment without verification, and rollback plans that ignore data compatibility.

## Deliverables
Build/artifact policy; CI/CD gate map; environment/promotion model; container hardening policy; migration/deployment compatibility matrix; probe model; shutdown model; deployment strategy; rollback/forward-fix plan; resource limits; secrets/config boundary; runtime security policy; observability/deployment telemetry; post-deploy verification; recovery/DR plan; evidence ledger; rejected alternatives; verification report.