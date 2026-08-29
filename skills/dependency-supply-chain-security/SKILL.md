---
name: dependency-supply-chain-security
description: Evidence-first dependency, software supply-chain and reproducible-build security for FastMCP projects.
---

# Dependency / Supply-Chain Security

## Mission
Keep the dependency graph intentional, reproducible, auditable and resistant to compromised packages, unsafe upgrades and build-pipeline substitution.

## Mandatory research
Identify exact Python, FastMCP, MCP SDK, Pydantic/PydanticAI, SQLAlchemy, server/runtime and build-tool versions. Read official packaging/build documentation and security advisories for the actual ecosystem. Inspect lockfiles, package metadata, Dockerfiles and CI. Use OSV/GitHub advisories and vendor advisories as evidence. Record an evidence ledger and re-check critical version/security claims before completion.

## Dependency policy
Every runtime dependency must have a demonstrated responsibility. Apply KISS/YAGNI: do not add a package for trivial functionality already safely provided by the standard library or existing dependencies. Prefer mature, maintained libraries with compatible licensing, security history and active maintenance.

Separate runtime, development, test and build dependencies. Do not ship test/build tooling in the production image unless required.

## Pinning / locking
Production dependency resolution must be reproducible from a committed lockfile or equivalent fully resolved artifact. Distinguish direct dependencies from transitive dependencies. Do not silently update lockfiles during production deployment. Record intentional upgrades and security exceptions.

Pinning strategy must match the packaging ecosystem and risk: exact versions where reproducibility requires it, bounded constraints where controlled compatibility is preferable, and immutable container/base-image references for deployment where appropriate.

## Updates
Prefer small, reviewable dependency updates. For each upgrade assess API compatibility, changelog, security advisories, transitive changes, Python/runtime compatibility and performance. Security updates are not automatically safe: run the complete relevant verification suite.

Do not upgrade a dependency merely because a newer version exists. Do not downgrade to evade a vulnerability without documenting the risk and compensating controls.

## Supply-chain threats
Consider typosquatting, dependency confusion, compromised maintainer releases, malicious transitive dependencies, source/build mismatch, poisoned caches, unsafe install scripts, untrusted artifacts and compromised CI actions. Prefer trusted package indexes, verified artifacts and least-privilege CI.

## Build provenance
Build the artifact once, from reviewed source and locked dependencies. Preserve artifact digest, dependency lock state, source revision and build metadata. Generate SBOM/provenance where supported. Deployment must consume the verified artifact rather than rebuilding from mutable inputs.

## Containers
Use minimal trusted base images, pin them according to the deployment policy, remove unnecessary packages and run as non-root where practical. Never copy credentials into image layers. Ensure `.dockerignore` excludes local environments, caches and secrets. Scan images and dependencies with appropriate tools.

## CI actions
Treat third-party GitHub Actions as supply-chain dependencies. Pin actions according to repository policy, prefer trusted maintainers, minimize permissions and review action upgrades. Do not execute untrusted pull-request code with write credentials.

## Vulnerability handling
Maintain a severity-based policy with ownership, affected versions, exploitability/context, remediation deadline, temporary mitigation and exception expiry. Distinguish reachable/runtime vulnerabilities from unused development-only dependencies while still tracking both.

## License / provenance
Track dependency licenses and provenance. Reject dependencies with incompatible licensing or unclear provenance for the project's distribution model. Do not copy code or assets without verifying license obligations.

## Testing
Verify clean-environment installation from the lockfile, dependency integrity, package metadata, import graph and production artifact contents. Run vulnerability scans and license checks where required. Test that forbidden development/test packages are absent from production artifacts.

## Rejection criteria
Reject unpinned/unlocked production resolution, unexplained direct dependencies, mutable deployment inputs, secrets in build context, unreviewed CI actions, ignored critical vulnerabilities, package upgrades without compatibility verification, or production images containing unnecessary build/test tooling.

## Deliverables
Dependency inventory; direct/transitive rationale; lockfile policy; upgrade policy; vulnerability/exception policy; supply-chain threat model; build provenance policy; container policy; CI action policy; license/provenance report; verification matrix; evidence ledger; residual risks.