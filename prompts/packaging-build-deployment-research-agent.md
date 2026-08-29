# Packaging / Build / Deployment Research Agent

Research only. A separate implementation session consumes this package.

## Mission
Produce evidence for reproducible Python packaging, container builds and production deployment of FastMCP services.

## Mandatory sources
Use current official sources first: FastMCP docs/source/examples; Python Packaging User Guide/PyPA specifications; selected package manager docs; Docker docs; target deployment platform docs. Inspect official source/tests for version-sensitive lifecycle and HTTP behavior.

## Mandatory investigation
Identify exact versions. Research pyproject/build backend, package artifacts, lock/reproducibility semantics, dependency groups, Python runtime constraints, Docker multi-stage builds, build context and cache, image pinning/digests, non-root execution, runtime filesystem, SBOM/provenance, secrets, FastMCP HTTP transport/path, custom routes, authentication boundaries, lifespan ownership, graceful shutdown, readiness/liveness, deployment scaling, immutable promotion and rollback.

Research the actual target deployment platform rather than assuming Kubernetes, serverless or a VM. Compare alternatives against startup time, concurrency, networking, persistence, cost, operational complexity and security.

Verify whether FastMCP's current mounted HTTP application requires lifespan propagation and what custom-route authentication semantics are. Never rely on old FastMCP deployment examples without checking their version.

## Deliverable
Version matrix; packaging/build decision; Docker design; runtime image decision; supply-chain/provenance matrix; FastMCP transport/lifespan findings; health/readiness design; CI/CD pipeline; deployment topology comparison; immutable promotion strategy; rollback plan; verification matrix; evidence ledger; blocking unknowns.

No implementation.