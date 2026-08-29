# CI/CD & GitHub Actions Acceptance Criteria

## Research
- [ ] Current official GitHub Actions workflow/security documentation read.
- [ ] Reusable workflow semantics verified.
- [ ] OIDC claims and trust conditions verified.
- [ ] Artifact attestation/provenance and SBOM behavior verified.
- [ ] Permissions and fork/PR trust model verified.
- [ ] Cache/artifact distinction and cache trust risks verified.
- [ ] Every third-party action reference verified.
- [ ] Evidence ledger completed.

## Architecture
- [ ] CI and CD responsibilities are separated.
- [ ] Workflow dependency graph exists.
- [ ] Per-job least-privilege permissions exist.
- [ ] Reusable workflow boundaries are explicit.
- [ ] Production artifact is built once and promoted immutably.
- [ ] Artifact provenance/integrity policy exists.
- [ ] OIDC trust is scoped to intended repository/ref/environment/workflow.
- [ ] Production environments have explicit protection policy.
- [ ] Deployment concurrency is safe.
- [ ] Rollback points to a known immutable artifact.

## Security
- [ ] No unnecessary write permissions.
- [ ] No long-lived cloud credentials where OIDC is viable.
- [ ] Untrusted PR code cannot access production credentials.
- [ ] `pull_request_target` is absent or explicitly justified.
- [ ] Cache cannot cross trust boundaries unsafely.
- [ ] Secrets are not printed or embedded in artifacts/images.
- [ ] External actions/workflows follow pinning policy.

## Verification
- [ ] Workflow syntax/behavior verified.
- [ ] Permission tests/review completed.
- [ ] Reusable workflow inputs/secrets verified.
- [ ] Cache behavior verified.
- [ ] Artifact identity verified across jobs.
- [ ] Provenance/attestation verification tested where required.
- [ ] OIDC trust path verified.
- [ ] Environment/deployment gates verified.
- [ ] Cancellation/rerun/concurrency behavior tested.
- [ ] Fork PR behavior tested/reviewed.
- [ ] Deployment smoke test verified.
- [ ] Rollback verified.
- [ ] Static/security gates pass.
- [ ] Architecture re-check passes.