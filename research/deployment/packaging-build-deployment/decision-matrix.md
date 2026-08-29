# Packaging / Build / Deployment Decision Matrix

| Concern | Default | Exception requires evidence |
|---|---|---|
| Build | Standard pyproject build backend | Legacy build only for proven compatibility |
| Dependency resolution | One locked workflow | Migration with explicit decision |
| Container | Multi-stage | Single stage if attack surface/build constraints are demonstrably equivalent |
| Runtime image | Minimal compatible trusted image | Larger image for required runtime capabilities |
| Image identity | Immutable digest/tag | Mutable tags only for development |
| Secrets | Runtime secret injection | None baked into image/artifacts |
| User | Non-root | Root only with explicit operational requirement |
| FastMCP HTTP | Documented transport/startup API | Custom ASGI integration with verified lifespan semantics |
| Health | Separate liveness/readiness | Combined endpoint only if platform requires it and semantics remain correct |
| Promotion | Promote tested immutable artifact | Rebuild only in controlled, reproducibly equivalent pipeline |
| Deployment | Simplest platform meeting requirements | More complex orchestrator only with demonstrated need |

## Hard rules

1. Do not deploy an artifact different from the tested artifact.
2. Do not put secrets in image layers.
3. Do not rely on mutable `latest` as a production release identity.
4. Do not break FastMCP lifespan when mounting ASGI applications.
5. Do not make liveness depend on optional downstream services.
6. Do not introduce a second package manager without an explicit migration decision.
7. Do not claim reproducibility without locked dependencies and pinned runtime/build inputs.
8. Do not add deployment infrastructure for fashion; justify operational complexity.