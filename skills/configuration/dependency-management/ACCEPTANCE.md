# Configuration / Dependency Management Acceptance Criteria

## Research
- [ ] Exact Python/package/dependency versions identified.
- [ ] Official package-manager/PyPA documentation read.
- [ ] FastMCP/PydanticAI/Pydantic/SQLAlchemy configuration docs read.
- [ ] Repository CI/container/deployment configuration inspected.
- [ ] Supply-chain guidance checked.
- [ ] Evidence ledger completed.

## Dependencies
- [ ] One authoritative project metadata source exists.
- [ ] Runtime/dev/test/optional dependencies are separated.
- [ ] Every direct dependency has a documented reason.
- [ ] Direct/transitive dependency assumptions are explicit.
- [ ] Version constraints are justified.
- [ ] Lock state is reproducible.
- [ ] No undeclared runtime dependency exists.

## Configuration
- [ ] Supported Python versions are explicit.
- [ ] Required settings are typed/validated where appropriate.
- [ ] Invalid required configuration fails fast.
- [ ] Environment variables are documented.
- [ ] Secrets are external to source control.
- [ ] Unsafe defaults are rejected or explicitly justified.

## Build / supply chain
- [ ] Clean install succeeds from declared metadata/lock state.
- [ ] Build does not depend on developer-global packages.
- [ ] Dependency integrity/provenance policy is explicit.
- [ ] Vulnerability/SBOM strategy is defined.
- [ ] Runtime image contains only required runtime dependencies where applicable.

## Verification
- [ ] Formatter/lint/type checks pass.
- [ ] Tests pass.
- [ ] Configuration failure-path tests pass.
- [ ] Lock consistency is verified.
- [ ] Secret-leak checks pass.
- [ ] Clean-build verification passes where practical.
- [ ] Architecture re-check passes.