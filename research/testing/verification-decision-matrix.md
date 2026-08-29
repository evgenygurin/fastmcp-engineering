# Testing / Verification Decision Matrix

| Invariant | Preferred test | Why |
|---|---|---|
| Pure business rule | Unit | Fast/deterministic |
| Application orchestration | Component | Verifies real collaboration |
| SQL/transaction semantics | Integration + real DB | Mocks cannot prove DB behavior |
| MCP wire/protocol behavior | Protocol/contract | Direct calls bypass protocol |
| PydanticAI orchestration | Deterministic agent tests | Avoid live-model nondeterminism |
| Security boundary | Security regression | Explicit attack proof |
| Broad input invariant | Property-based | Explores input space |
| Assertion effectiveness | Mutation | Detects weak tests |
| Critical user workflow | E2E | Verifies complete contract |

## Hard rules

1. Do not mock the behavior that is actually under test.
2. Direct function calls are not MCP protocol tests.
3. A live LLM is not a normal unit-test dependency.
4. Real DB tests are mandatory where correctness depends on DB semantics.
5. Every critical security invariant needs an executable regression test.
6. Sleeps are not synchronization.
7. Flaky tests require diagnosis, not permanent suppression.
8. Coverage percentage is not evidence of behavioral correctness by itself.
9. Expensive tests must have an explicit CI placement and purpose.
10. Tests must protect contracts/invariants rather than incidental implementation details.