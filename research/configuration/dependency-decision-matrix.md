# Configuration / Dependency Decision Matrix

| Concern | Preferred rule | Verification |
|---|---|---|
| Project metadata | One authoritative `pyproject.toml` | Clean build/read metadata |
| Lock state | Package manager generated | Fresh sync/install |
| Runtime deps | Explicit direct dependencies | Import/runtime test |
| Dev/test deps | Separate groups | Production install inspection |
| Settings | Typed validated contract | Failure-path tests |
| Secrets | External secret/config system | Secret scan + tests |
| Python versions | Explicit supported range | CI matrix |
| Build | Reproducible from clean checkout | Clean build |
| Supply chain | Lock/integrity/provenance policy | CI security checks |
| Container | Runtime-only dependency set | Image inspection |

## Hard rules

1. Never infer package-manager semantics from memory.
2. Never hand-edit generated lock files unless officially documented.
3. Do not rely on undeclared transitive dependencies.
4. Do not duplicate dependency versions across unrelated files without a documented reason.
5. Required configuration must fail fast rather than silently degrade.
6. Secrets never belong in source, prompts, schemas, fixtures, logs or lock files.
7. A dependency requires architectural justification, not merely convenience.
8. Clean installation/build must not depend on a developer's global environment.