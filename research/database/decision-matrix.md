# SQLAlchemy / PostgreSQL Decision Matrix

| Concern | Default | Requires explicit evidence to deviate |
|---|---|---|
| Session | Session/AsyncSession per logical operation/task | Deliberate longer lifecycle with ownership proof |
| Transaction | Application/use-case boundary | Explicit alternative transaction owner |
| Repository | Intent-focused port when boundary value exists | Direct SQLAlchemy adapter when abstraction adds no value |
| UoW | Only when coordinating a meaningful transaction boundary | Omit when application transaction context is sufficient |
| ORM/Core | Workload-driven | No ideological preference |
| Loading | Explicit strategy | Lazy loading only when safe and understood |
| Pagination | Deterministic ordering | Offset only when workload permits |
| Invariants | Database constraints + application validation | Application-only for non-integrity presentation rules |
| Concurrency | Explicit isolation/locking model | Default isolation when race is proven irrelevant |
| Tenant security | Application authorization + RLS where justified | One layer only requires threat-model evidence |
| Migration | Versioned expand/contract where required | Direct migration when operational risk is negligible |
| Index | Query/workload evidence | No speculative indexes |
| Integration tests | Real PostgreSQL | Mock/SQLite only for concerns independent of DB semantics |

## Hard rules

1. Never share AsyncSession concurrently.
2. Never silently commit inside a repository that is not the transaction owner.
3. Never hold a DB transaction across remote LLM/MCP/HTTP calls without explicit justification.
4. Never rely solely on Python validation for database integrity invariants.
5. Never substitute SQLite for PostgreSQL-specific semantics without proof of equivalence for the tested behavior.
6. Never claim zero-downtime migrations without analyzing PostgreSQL locking/rewrites.
7. Never add Repository/UoW layers merely for pattern compliance.
8. Never use tenant prompts as an authorization boundary.
9. Never retry serialization/deadlock failures without bounded, replay-safe semantics.
10. Never claim performance from intuition; measure query count/plans for critical paths.