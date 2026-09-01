---
name: packaging-build-deployment
description: Evidence-first packaging, container build and production deployment engineering for FastMCP Python services.
---

# Packaging / Build / Deployment Engineering

## Mission
Produce reproducible, minimal, observable and safely deployable FastMCP services without coupling application architecture to a particular deployment platform.

## Trigger / Когда применять

**Scope / When to use:** packaging, container build and production deployment engineering for FastMCP Python services.
**Trigger:** designing or changing packaging, build reproducibility, container design, FastMCP runtime transport, lifespan/shutdown, CI/CD, deployment topology, or rollback.
**Upstream / Prerequisite:** repository architecture, security, resilience, testing and configuration contracts read; identified exact versions; evidence, assumptions and unresolved questions recorded.
**Mission / Goal:** produce reproducible, minimal, observable and safely deployable FastMCP services without coupling application architecture to a particular deployment platform.
**Research / Evidence:** read current official FastMCP deployment, HTTP transport, lifespan and custom-route documentation; read official Python packaging/PyPA build and reproducible-environment specifications; read official package-manager documentation for lockfile and container workflows; read official Docker documentation for multi-stage builds, build cache, image security and runtime configuration; read deployment-platform documentation; inspect official examples/source/tests for lifecycle, HTTP and packaging behavior.
**Decision / Selection rules:** use the standard `pyproject.toml` build interface and an explicit build backend; pin and lock dependencies and assert lock consistency; prefer multi-stage builds with compilers/package managers kept out of the runtime image; generate provenance/SBOM and prefer immutable image references; use the documented FastMCP startup mechanism and exact transport semantics; separate liveness from readiness; own startup resources in an explicit lifespan; promote the exact immutable artifact that was tested; choose deployment topology from requirements, not convention.
**Version / Compatibility:** identify exact Python, FastMCP, PydanticAI, SQLAlchemy, package-manager, Docker and runtime versions; verify version-sensitive lifecycle, HTTP and packaging behavior.

## Deliverables

**Deliverables / Artifacts:** packaging contract, build reproducibility contract, Docker/image design, runtime/lifespan model, health/readiness model, CI/CD pipeline, deployment topology, supply-chain controls, rollback model, verification matrix and residual risks.
**Verification / Testing:** verify clean reproducible build, lockfile consistency, package artifact metadata, image runs as non-root, no secrets in image/history, health/readiness behavior, FastMCP transport path, lifespan startup/shutdown, graceful termination, migration/dependency ordering, deployment smoke test, provenance/SBOM where required, and rollback to previous immutable artifact.
**Failure / Stop conditions:** reject builds with mutable production artifacts, hidden dependency resolution, secrets in image layers, missing shutdown semantics, broken FastMCP lifespan, unaudited deployment-specific assumptions, unbounded health checks, or production artifacts that differ from tested artifacts.
**Positive scenario:** a reproducible, minimal image built once passes verification and is promoted as an immutable artifact.
**Negative scenario:** a production artifact differs from the tested bytes or contains secrets in an image layer.

## Mandatory research gate
Before implementation:
1. Read repository architecture, security, resilience, testing and configuration contracts.
2. Identify exact Python, FastMCP, PydanticAI, SQLAlchemy, package-manager, Docker and runtime versions.
3. Read current official FastMCP deployment, HTTP transport, lifespan and custom-route documentation.
4. Read official Python packaging/PyPA build and reproducible-environment specifications.
5. Read official package-manager documentation for lockfile and container workflows.
6. Read official Docker documentation for multi-stage builds, build cache, image security and runtime configuration.
7. Read deployment-platform documentation for the actual target platform.
8. Inspect official examples/source/tests for lifecycle, HTTP and packaging behavior that is version-sensitive.
9. Record evidence, assumptions and unresolved questions.

## Packaging
Use the standard `pyproject.toml` build interface and an explicit build backend. Build distributions with the selected package tool and verify artifacts before release. Keep runtime dependencies separate from development/build dependencies. Do not publish source-only assumptions as package guarantees.

## Reproducibility
Pin and lock dependencies according to the selected package workflow. CI and production builds must assert lock consistency rather than silently resolving a new graph. Pin base images and critical build tools by immutable digest where reproducibility/security requires it. Record Python/runtime/platform constraints.

## Container design
Prefer multi-stage builds. Keep compilers, package managers and development dependencies out of the final runtime image. Run as non-root where supported. Use a minimal compatible runtime image, explicit working directory, deterministic environment and a narrow entrypoint. Never bake secrets into layers, ARGs or the image filesystem.

Separate dependency installation from source copying to maximize safe build caching. Ensure `.venv`, caches, credentials and local artifacts are excluded from the build context. Use BuildKit cache mounts only where they do not compromise reproducibility.

## Supply chain
Generate and retain image/package provenance and SBOM where the deployment environment supports them. Verify trusted base images and package sources. Review dependency changes. Prefer immutable image references for production promotion. Do not treat a mutable `latest` tag as a release identifier.

## FastMCP runtime
Use the documented FastMCP startup mechanism and exact transport semantics. For HTTP deployments, understand the MCP endpoint path, custom routes, authentication middleware boundaries and lifespan ownership. Health/readiness routes must not accidentally expose sensitive application state. If FastMCP is mounted into Starlette/FastAPI, preserve the documented lifespan context required by the transport.

Separate liveness from readiness. Liveness should answer whether the process/runtime is alive; readiness should reflect whether the service can safely receive work. Do not make liveness depend on every downstream dependency.

## Lifespan and shutdown
Own startup resources in an explicit application lifespan. Initialize and dispose DB pools, MCP clients, HTTP clients and other shared resources deterministically. Propagate graceful shutdown and cancellation. Allow in-flight work to finish within a bounded termination window and reject new work when draining.

## Runtime configuration
Configuration is injected at startup through the configuration boundary. Secrets come from the runtime secret mechanism, never from source code or image layers. Production configuration must fail fast when required values are invalid or missing.

## CI/CD
Pipeline stages should be explicit: quality → tests → build → security/provenance checks → artifact publication → deployment → smoke/health verification. Promote the exact immutable artifact that was tested. Do not rebuild different bytes for production after tests pass.

## Deployment
Deployment topology is chosen from requirements: process model, HTTP transport, concurrency, statefulness, startup time, persistent storage, network access, secrets and scaling. Do not introduce Kubernetes or another orchestrator merely because it is conventional.

## Verification
Verify:
- clean reproducible build;
- lockfile consistency;
- package artifact metadata;
- image runs as non-root;
- no secrets in image/history;
- health/readiness behavior;
- FastMCP transport path;
- lifespan startup/shutdown;
- graceful termination;
- migration/dependency ordering;
- deployment smoke test;
- provenance/SBOM where required;
- rollback to previous immutable artifact.