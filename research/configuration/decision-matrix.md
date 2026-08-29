# Configuration & Dependency Decision Matrix

| Concern | Default | Exception requires evidence |
|---|---|---|
| Runtime config | Typed Pydantic Settings boundary | Truly static compile-time constant |
| Environment access | Composition root/settings sources | Framework-required adapter boundary |
| Secrets | Secret store/environment injection | Explicitly documented local development mechanism |
| Dependencies | `pyproject.toml` standards | Tool-specific metadata required by selected backend |
| Dev dependencies | Dependency groups | Published extras when consumers need them |
| Resolution | Committed lockfile for applications | Distribution workflow with a different explicit policy |
| CI/deploy | Sync/install from lock | Explicit controlled resolver policy |
| Package manager | One primary workflow | Migration with documented transition |
| Upgrade | Deliberate reviewed change | Emergency security response with follow-up review |
| VCS/URL dependency | Reject by default | Explicitly justified, reviewed and reproducible |

## Hard rules

1. Configuration is typed at the boundary.
2. Application modules do not freely read environment variables.
3. Secrets never enter source control, logs, prompts or telemetry.
4. Configuration precedence is documented and tested.
5. Runtime and development dependencies are separated.
6. Lockfile changes are supply-chain changes.
7. CI/deployment must not silently re-resolve production dependencies.
8. One primary dependency-management workflow is used.
9. Dependency upgrades require upstream/security review.
10. A lockfile proves resolution reproducibility, not package trustworthiness.