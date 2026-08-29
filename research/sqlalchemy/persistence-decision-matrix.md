# SQLAlchemy Persistence Decision Matrix

| Concern | Default direction | Evidence required |
|---|---|---|
| Engine | Application infrastructure singleton/process resource | SQLAlchemy async/pooling docs |
| Session | Request/use-case scoped | SQLAlchemy async session docs |
| Transaction | Application use-case boundary | SQLAlchemy transaction docs |
| Repository | Explicit application port | Architecture + use-case needs |
| Unit of Work | Only when coordination adds value | Pattern review + transaction semantics |
| ORM model | Persistence representation | SQLAlchemy docs |
| Domain model | Independent where domain semantics warrant it | Architecture |
| Public MCP DTO | Separate Pydantic contract | Pydantic/FastMCP docs |
| Loading | Explicit per use case | SQLAlchemy relationship/loading docs |
| Retry | Narrow, transient, replay-safe | DB/driver docs + operation semantics |
| Migration | Versioned migration artifact | Migration tool docs |

## Hard rules

1. Repositories do not silently commit.
2. AsyncSession is not shared concurrently across unrelated tasks.
3. Domain/application layers do not import SQLAlchemy merely to query data.
4. Public MCP schemas do not expose ORM entities by accident.
5. Database constraints supplement, not replace, application authorization.
6. Every unbounded query is a design defect until justified.
7. Every retry requires a replay/idempotency analysis.
