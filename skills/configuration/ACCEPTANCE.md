# Configuration / Dependency Acceptance Criteria

## Research
- [ ] Exact Python/settings/package-manager versions identified.
- [ ] Official Pydantic Settings source and precedence semantics verified.
- [ ] PyPA `pyproject.toml` and dependency-specifier rules verified.
- [ ] Dependency Groups / PEP 735 verified where used.
- [ ] Exact package-manager lock/sync behavior verified.
- [ ] FastMCP/PydanticAI/SQLAlchemy configuration semantics checked.
- [ ] Supply-chain controls researched.
- [ ] Evidence ledger completed.

## Configuration
- [ ] Typed settings boundary exists.
- [ ] Source precedence is explicit and tested.
- [ ] Environment matrix is explicit.
- [ ] Secrets are separate from ordinary configuration.
- [ ] Missing required production secrets fail fast.
- [ ] No arbitrary environment reads throughout application code.
- [ ] Secrets are absent from logs/prompts/telemetry.

## Dependencies
- [ ] Runtime and development dependencies are separated.
- [ ] One primary package-management workflow is documented.
- [ ] Lockfile policy is explicit.
- [ ] CI/deployment reproduces the locked environment.
- [ ] Supported Python/platform matrix is explicit.
- [ ] Dependency upgrades require upstream/security review.
- [ ] Lockfile changes receive supply-chain review.
- [ ] Arbitrary VCS/URL dependencies are justified or rejected.

## Verification
- [ ] Settings parsing/precedence tests pass.
- [ ] Invalid configuration tests pass.
- [ ] Secret/startup failure tests pass.
- [ ] Clean-environment dependency sync/install passes.
- [ ] Static quality gates pass.
- [ ] Full relevant test suite passes.
- [ ] Architecture/security re-check passes.