---
name: configuration-dependency-management
description: Evidence-first engineering of Python project configuration, dependencies, environments, secrets, reproducible builds and supply-chain controls for FastMCP systems.
---

# Configuration / Dependency Management

## Mission

Make the runtime reproducible, explicit and safe. Configuration, dependency resolution and build metadata are architecture—not incidental setup.

## Mandatory research gate

Before changing configuration or dependencies:
1. Read AGENTS.md and repository engineering contracts.
2. Identify supported Python versions and exact FastMCP/MCP/Pydantic/PydanticAI/SQLAlchemy/server versions.
3. Read official documentation for the project's package/build manager (prefer the repository's established tool; if introducing one, justify it).
4. Read official documentation for dependency groups, lock files, resolution, build isolation, publishing and environment configuration.
5. Read official FastMCP/PydanticAI configuration/deployment guidance relevant to the target version.
6. Inspect repository CI/container/deployment configuration.
7. Inspect authoritative security/supply-chain guidance.
8. Record evidence before implementation.

## Single source of truth

Define one authoritative project metadata/configuration model. Avoid duplicated version declarations, incompatible environment files and undocumented manual setup.

## Dependencies

Every dependency must have a reason and an owner/use boundary. Prefer the smallest sufficient dependency set. Distinguish runtime, development, test, lint/type-check and optional/extras groups. Avoid transitive-dependency reliance when a direct dependency is part of the application's contract.

Pin/constraint versions according to the repository's reproducibility policy. Understand direct vs transitive resolution and lock-file semantics. Do not blindly upgrade packages because a newer version exists.

## uv / package management

When uv is selected or already established, verify exact current uv semantics from official documentation before editing `pyproject.toml`, `uv.lock`, dependency groups, indexes, Python management or sync commands. Never hand-edit a generated lock file unless the tool explicitly documents that workflow.

## Python compatibility

Declare supported Python versions explicitly. Verify all key dependencies against the support range. Avoid relying on behavior newer than the declared minimum. Test at least the repository's critical compatibility boundaries in CI.

## Configuration

Separate:
- immutable application defaults;
- environment-specific configuration;
- secrets/credentials;
- runtime overrides.

Use typed settings validation where appropriate. Fail fast on invalid required configuration. Avoid silently accepting misspelled environment variables or unsafe defaults.

Never commit secrets. Do not place credentials in source, prompts, schemas, fixtures, logs or lock files. Document required variables and safe example values.

## Build reproducibility

A clean checkout must be buildable from declared metadata and lock state. Build environments should be deterministic and should not depend on undeclared globally installed packages or local developer state.

## Supply chain

Evaluate package indexes, trusted publishers/provenance, lock integrity, hashes where supported, dependency confusion risk, malicious packages, transitive dependencies, vulnerability scanning and SBOM requirements. Use private indexes only with explicit trust configuration.

## Containers/deployment

Keep runtime images minimal. Install only runtime dependencies. Run as a non-root user where feasible. Do not copy development secrets or caches into images. Ensure container/runtime configuration matches application configuration contracts.

## CI

CI must verify lock consistency, dependency installation from a clean environment, supported Python versions, static quality, tests and security/dependency checks. Separate intentional dependency-update workflows from normal CI.

## Rejection criteria

Reject if dependency versions are duplicated inconsistently, lock state is stale/unreproducible, required configuration can silently fail, secrets are committed/exposed, runtime depends on undeclared packages, generated lock files are manually corrupted, or a dependency is introduced without architectural justification.

## Deliverables

Configuration/dependency research package, dependency inventory, version compatibility matrix, settings contract, environment contract, secrets policy, reproducible-build procedure, supply-chain controls, implementation, CI verification and architecture re-check.