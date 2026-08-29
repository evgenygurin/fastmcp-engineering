# Testing / TDD Decision Matrix

| Concern | Default | Exception requires evidence |
|---|---|---|
| Pure domain logic | Unit test | Higher-level contract adds unique value |
| Application orchestration | Component test with controlled adapters | Real integration required by semantics |
| MCP schema/protocol | Contract/integration test at MCP boundary | Pure unit only for transformation helpers |
| LLM agent | TestModel/FunctionModel | Real provider integration |
| DB semantics | Real PostgreSQL integration | Unit test only for DB-independent logic |
| Fixtures | Explicit function-scoped mutable state | Broader scope for isolated immutable resources |
| Async | Current documented async plugin mode | Framework-specific alternative |
| External HTTP | Deterministic fake + contract test | Controlled integration |
| Security | Deterministic regression + integration boundary | E2E for critical paths |
| Resilience | Fault injection | Real infrastructure for transport/DB behavior |
| Property testing | Invariants with meaningful generated space | Conventional examples sufficient |
| Mutation testing | High-value domain/security logic | Cost exceeds defect-detection value |

## Hard rules

1. Normal CI must not require live LLM APIs.
2. SQLite/in-memory DB is not evidence for PostgreSQL-specific semantics.
3. Mocks cannot prove protocol, locking, migration, RLS or provider behavior.
4. No sleep-based synchronization.
5. No hidden fixture state that materially changes a test.
6. Tests assert contracts, not incidental private implementation.
7. Every critical invariant maps to at least one proving test.
8. Flaky tests are investigated rather than permanently ignored.
9. Real integration tests are explicitly separated from deterministic suites.
10. Test complexity must be justified by defect-detection value.