# Skill Development Order

The project is developed in dependency order. A downstream skill must not silently redefine an upstream contract.

```text
foundation
  ├── research-governance
  ├── architecture-governor
  ├── pattern-selection
  ├── skill-context
  └── verification
          |
          v
fastmcp-components
          |
          +--> providers
          +--> transforms
          +--> middleware
          +--> context-di
          +--> lifecycle
          +--> auth
          +--> tasks
          +--> client-testing
          |
          v
persistence / integrations
  ├── sqlalchemy
  └── supabase
          |
          v
ai
  ├── pydantic
  └── pydantic-ai
          |
          v
security / observability / performance / deployment
          |
          v
final production review
```

This order is a default dependency graph, not a prohibition on parallel research. A feature may use a subset of the graph; irrelevant skills must not be introduced solely for architectural symmetry.