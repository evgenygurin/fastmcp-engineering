# Dependency / Supply-Chain Acceptance Criteria

- [ ] Exact runtime, framework, package-manager and build versions identified.
- [ ] Official packaging/build/security documentation reviewed.
- [ ] Lockfile is committed and production resolution is deterministic.
- [ ] Runtime/dev/test/build dependency scopes are separated.
- [ ] Every direct dependency has an explicit responsibility.
- [ ] Transitive dependency risk was assessed.
- [ ] Upgrade compatibility and changelog were reviewed.
- [ ] Vulnerabilities have owner, severity, remediation/mitigation and expiry where exceptions exist.
- [ ] Package/artifact provenance is understood.
- [ ] CI actions follow trust and least-privilege policy.
- [ ] Container base and production artifact are appropriately minimized/pinned.
- [ ] Secrets are absent from build context and artifacts.
- [ ] SBOM/provenance requirements are satisfied where applicable.
- [ ] License obligations are checked.
- [ ] Clean installation from the lockfile succeeds.
- [ ] Security/license/build verification is recorded.
- [ ] Current authoritative documentation was re-checked before completion.