# Packaging / Build / Deployment Acceptance Criteria

## Research
- [ ] Exact Python/FastMCP/package-manager/Docker/runtime versions identified.
- [ ] Official FastMCP deployment, HTTP and lifespan semantics verified.
- [ ] PyPA packaging/build/reproducibility requirements verified.
- [ ] Docker build/runtime guidance verified.
- [ ] Target deployment platform documented from official sources.
- [ ] Evidence ledger completed.

## Packaging
- [ ] Explicit build backend exists.
- [ ] Runtime and development/build dependencies are separated.
- [ ] Lockfile is enforced in CI/build.
- [ ] Artifact metadata is verified.
- [ ] Build output is reproducible under the declared environment.

## Container
- [ ] Multi-stage build used when it materially reduces runtime attack surface.
- [ ] Build tools are absent from final image.
- [ ] Base images are trusted and pinned appropriately.
- [ ] Production artifact is immutable.
- [ ] Runtime is non-root where supported.
- [ ] No secrets are present in image layers/history.
- [ ] Build context excludes local environments/caches/secrets.

## FastMCP runtime
- [ ] Correct transport and endpoint path verified.
- [ ] Lifespan ownership is correct.
- [ ] Startup resources are deterministic.
- [ ] Shutdown/draining is bounded and tested.
- [ ] Liveness and readiness are separate.
- [ ] Health endpoints reveal no sensitive information.

## CI/CD
- [ ] Quality and tests run before artifact publication.
- [ ] Security/provenance checks run before promotion.
- [ ] Tested artifact is the artifact deployed.
- [ ] Deployment uses immutable artifact identity.
- [ ] Rollback target is an immutable prior artifact.

## Verification
- [ ] Package build passes.
- [ ] Lock consistency passes.
- [ ] Container builds successfully.
- [ ] Container smoke test passes.
- [ ] Runtime user/security checks pass.
- [ ] Health/readiness checks pass.
- [ ] FastMCP endpoint check passes.
- [ ] Lifespan/startup/shutdown checks pass.
- [ ] No secret leakage detected.
- [ ] Deployment verification passes where environment permits.
- [ ] Static quality gates pass.
- [ ] Architecture re-check passes.
- [ ] Stops when packaging/build behavior cannot be established from evidence; rejects invented behavior and escalates to the user instead of guessing.
