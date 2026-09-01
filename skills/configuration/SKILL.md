---
name: configuration-dependency-management
description: Evidence-first configuration, dependency and reproducible-environment engineering for production Python/FastMCP systems.
---

# Configuration & Dependency Management

## Mission
Make runtime configuration explicit, validated, environment-aware and secret-safe; make dependencies reproducible, auditable and deliberately upgraded.

## Trigger / Когда применять

**Scope / When to use:** configuration, dependency and reproducible-environment engineering for production Python/FastMCP systems.
**Trigger:** designing or changing runtime configuration, settings models, secrets handling, dependency declarations, lockfiles, or upgrade/reproducibility workflows.
**Upstream / Prerequisite:** repository architecture, security, testing and deployment contracts read; exact Python and package-manager versions identified; evidence recorded.
**Mission / Goal:** make runtime configuration explicit, validated, environment-aware and secret-safe; make dependencies reproducible, auditable and deliberately upgraded.
**Research / Evidence:** read official Pydantic Settings documentation for the exact version (settings models, sources, precedence, env parsing, nested settings, secrets files, CLI/custom sources); read PyPA specifications for `pyproject.toml`, dependency specifiers and dependency groups; read the exact package manager documentation for lockfiles, resolution, sync and reproducibility; read FastMCP/PydanticAI/SQLAlchemy configuration documentation relevant to the versions used; research dependency security/supply-chain controls.
**Decision / Selection rules:** use a typed settings boundary with explicit source precedence; separate static configuration, deployment configuration, credentials/secrets, request-scoped data and mutable business state; use `BaseSettings`/current documented settings APIs; use standards-based `pyproject.toml`; commit a lockfile and install/sync from it; upgrade deliberately rather than blind mass upgrades; choose one primary toolchain workflow and document it.
**Version / Compatibility:** identify exact versions of Python and the package manager; verify configuration precedence and package-manager behavior against the installed version rather than memory.

## Deliverables

**Deliverables / Artifacts:** configuration contract, source-precedence matrix, environment matrix, secrets policy, dependency policy, lock/reproducibility policy, upgrade procedure, supply-chain controls, tests, implementation and verification report.
**Verification / Testing:** test settings source precedence, aliases, parsing, required secrets, invalid combinations, environment isolation and startup failure; verify lockfile synchronization and clean installation in CI; configuration tests must not require production secrets.
**Failure / Stop conditions:** reject if modules read environment variables directly throughout the codebase, configuration is untyped, secrets are logged/stored in code, precedence is undocumented, production dependencies are unlocked without justification, CI silently re-resolves dependencies, dependency upgrades lack review, or multiple package-management workflows conflict.
**Positive scenario:** typed configuration with documented precedence fails fast at startup when a required production secret is missing.
**Negative scenario:** modules read environment variables directly and a secret is logged or stored in source code.

## Mandatory research gate
Before implementation:
1. Read repository architecture, security, testing and deployment contracts.
2. Identify exact Python and package-manager versions.
3. Read official Pydantic Settings documentation for the exact version: settings models, sources, precedence, env parsing, nested settings, secrets files, CLI/custom sources where applicable.
4. Read PyPA specifications for `pyproject.toml`, dependency specifiers and dependency groups.
5. Read the exact package manager documentation (prefer the repository's chosen tool; evaluate uv when appropriate) for lockfiles, dependency groups, resolution, environments, sync and reproducibility.
6. Read FastMCP/PydanticAI/SQLAlchemy configuration documentation relevant to the versions used.
7. Research dependency security/supply-chain controls from authoritative sources.
8. Record evidence, decisions and unresolved questions.

Do not assume configuration precedence or package-manager behavior from memory.

## Configuration architecture
Use a typed settings boundary. Parse external strings once into validated types. Keep configuration separate from domain entities and business state. Define a composition root that constructs settings and dependencies; do not let arbitrary modules read environment variables directly.

Define explicit precedence, normally from lowest to highest priority according to the selected settings source model. Document every source actually enabled. Avoid hidden custom sources.

Separate:
- static application configuration;
- deployment/environment configuration;
- credentials/secrets;
- request-scoped data;
- mutable business state.

Never put secrets in source code, default values, logs, exception messages, prompts, model-visible context or telemetry.

## Pydantic Settings
Use `BaseSettings`/current documented settings APIs for typed configuration when appropriate. Validate cross-field invariants with current Pydantic mechanisms. Prefer immutable/frozen settings after composition when practical. Do not use settings objects as global mutable service locators.

If nested models, environment prefixes, aliases, JSON decoding, secrets directories, CLI sources or custom sources are used, verify exact semantics against the installed version and test precedence explicitly.

## Environments
Keep dev/test/staging/prod differences explicit. Avoid branching business logic on arbitrary environment strings. Test configuration in isolation. A missing production secret should fail fast at startup rather than produce a latent runtime failure.

## Dependency declarations
Use standards-based `pyproject.toml` metadata and dependency specifiers. Separate runtime dependencies from development/test/docs groups. Use dependency groups for internal development dependencies where supported by the chosen tool/specification.

Avoid unnecessary direct dependencies. Do not add a library for functionality already supplied by the standard library or an existing first-party stack unless the benefit is demonstrated.

## Locking and reproducibility
Applications should use a committed lockfile when the selected package manager supports it. Locking must capture a reproducible resolution for supported platforms/Python versions. CI and deployment should install/sync from the lockfile rather than silently re-resolve.

Distinguish direct dependency constraints from the resolved transitive graph. Review lockfile changes as supply-chain changes.

## Dependency upgrades
Upgrade deliberately:
1. identify motivation/security/advisory;
2. read upstream changelog and migration guide;
3. inspect breaking changes;
4. update lockfile;
5. run targeted tests;
6. run full quality/security suite;
7. review transitive changes;
8. record residual compatibility risk.

Never perform blind mass upgrades in a production task.

## Supply-chain security
Pin or constrain according to the application's reproducibility/security requirements. Prefer trusted indexes and explicit index configuration. Avoid arbitrary VCS/URL dependencies unless justified and reviewed. Review package provenance, maintainers, advisories and release integrity for security-sensitive dependencies.

Do not confuse a lockfile with proof that a package is trustworthy: a lockfile primarily fixes resolution; it does not eliminate malicious or compromised packages.

## Toolchain policy
Choose one primary project/dependency workflow and document it. Do not mix uv/Poetry/Pipenv/pip-tools ad hoc. Developer and CI commands must be reproducible from a clean checkout.

## Testing
Test settings source precedence, aliases, parsing, required secrets, invalid combinations, environment isolation and startup failure. Verify lockfile synchronization and clean installation in CI. Configuration tests must not require production secrets.

