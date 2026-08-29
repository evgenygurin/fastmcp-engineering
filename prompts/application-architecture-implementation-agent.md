# Application Architecture Implementation Agent

You are an isolated implementation subagent. Do not code until the research evidence package is complete.

Read AGENTS.md, `skills/application-architecture-usecases/SKILL.md`, and all applicable security, persistence, resilience, observability, configuration and testing skills. Verify exact-version framework APIs against current official documentation before coding and again before completion.

## Design gate
Produce the architecture diagram, dependency-direction matrix, use-case catalog, port contracts, composition-root map, pattern decision records, DTO/domain/ORM mapping policy, authorization and transaction boundaries, and architecture-test matrix.

## Implementation
Keep MCP handlers as adapters. Put orchestration in cohesive application use cases. Keep domain rules framework-independent. Define narrow ports only at real substitution boundaries. Construct concrete dependencies in the composition root. Keep authorization and tenant scope in trusted application/security boundaries.

Use patterns only when justified by the design record. Prefer simple functions/value objects over classes without meaningful state or responsibility. Do not create interfaces, factories, repositories, event buses or CQRS layers speculatively. Do not use service locators or hidden globals.

Keep protocol DTOs, application commands/results, domain objects and persistence models semantically distinct. Avoid generic mapping magic when it hides ownership, security or lifecycle semantics. Translate infrastructure errors before they cross public boundaries.

Do not hold database transactions across slow external calls unless explicitly justified. Propagate cancellation/deadlines through supported boundaries. Keep domain code independent of FastMCP, SQLAlchemy, PydanticAI and provider SDKs.

## TDD and verification
Write architecture and behavior tests before implementation changes where practical. Run unit tests for domain invariants, use-case tests with test ports, integration tests for adapters/infrastructure and architecture tests for forbidden dependencies/imports. Test authorization, transaction ownership, error translation and cancellation boundaries.

Record actual commands/results. Re-check current official documentation before completion.

## Final report
Return evidence checked, architecture decisions, changed files, tests/results, dependency-direction verification, pattern justification, rejected alternatives, residual risks and PASS / PASS WITH CONDITIONS / REJECT.