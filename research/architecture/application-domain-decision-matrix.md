# Application / Domain Architecture Decision Matrix

| Concern | Preferred decision | Reason |
|---|---|---|
| Business rules | Domain | Deterministic stable policy |
| Workflow orchestration | Application use case | Explicit business operation boundary |
| MCP transport | Input adapter | Protocol concern |
| Agent orchestration | Application-facing adapter/capability | Probabilistic concern isolated from policy |
| Persistence | Output adapter | Infrastructure concern |
| External API | Output adapter | Infrastructure concern |
| Repository | Only when persistence boundary is meaningful | Avoid speculative abstraction |
| Unit of Work | Only when atomic multi-operation coordination is required | Explicit transaction ownership |
| DI | Composition root + explicit dependencies | Avoid hidden coupling |
| Mapping | At boundaries where representations independently evolve | Prevent leakage without duplication by default |
| Errors | Stable application/domain taxonomy | Hide infrastructure contracts |
| Architecture tests | Forbidden imports/dependency direction | Executable architecture rule |

## Hard rules

1. Dependencies point inward toward stable policies.
2. Domain code does not require FastMCP, PydanticAI, SQLAlchemy sessions or provider SDKs to express business rules.
3. MCP handlers do not own business workflows or arbitrary transaction commits.
4. LLM output never establishes authorization or domain truth.
5. Ports require a real boundary; interfaces are not created merely for style.
6. Repository/UoW are optional patterns, not mandatory layers.
7. Composition roots own concrete wiring.
8. Infrastructure exceptions do not become stable application contracts accidentally.
9. Side effects must have explicit retry/idempotency semantics.
10. Architecture must be verified by executable checks where practical.