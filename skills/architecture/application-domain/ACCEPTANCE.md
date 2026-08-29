# Application / Domain Architecture Acceptance Criteria

## Research
- [ ] Existing repository dependency graph inspected.
- [ ] Official FastMCP/PydanticAI/Pydantic/SQLAlchemy lifecycle semantics checked.
- [ ] Clean/Hexagonal/Ports & Adapters principles researched from authoritative sources.
- [ ] Evidence ledger completed.
- [ ] Rejected alternatives documented.

## Architecture
- [ ] Dependency direction points toward stable policies.
- [ ] Domain is framework-light and deterministic.
- [ ] Application use cases own orchestration and transaction boundaries.
- [ ] MCP/transport code is an input adapter.
- [ ] Persistence/providers are output adapters.
- [ ] Ports exist only at meaningful change/testing boundaries.
- [ ] Composition root assembles concrete implementations.
- [ ] No service locator/global mutable dependency mechanism.
- [ ] Agent does not own authorization or domain invariants.
- [ ] Error translation is explicit.
- [ ] Idempotency is defined for retryable side effects.

## Anti-overengineering
- [ ] No interface-per-class pattern without justification.
- [ ] No generic repository without a concrete boundary.
- [ ] No unnecessary DTO/entity duplication.
- [ ] No speculative layers.
- [ ] No god service/helper/manager.

## Verification
- [ ] Architecture/dependency checks pass.
- [ ] Formatter/lint/type checks pass.
- [ ] Domain tests pass.
- [ ] Application tests pass.
- [ ] Persistence tests cover real DB semantics where required.
- [ ] MCP/PydanticAI adapter tests cover actual framework contracts.
- [ ] Transaction behavior is verified.
- [ ] No circular dependency remains.
- [ ] Architecture re-check passes.