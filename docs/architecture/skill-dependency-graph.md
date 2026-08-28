# Skill Dependency Graph

Specialized skills are developed in isolated sessions, but they consume shared upstream contracts rather than inventing their own methodology.

```text
research-first
      |
      +--> architecture-governor
      |        |
      |        +--> pattern-selection
      |
      +--> fastmcp-research
      |
      +--> library-research
               |
               +--> pydantic
               +--> sqlalchemy
               +--> pydantic-ai
               +--> supabase

architecture-governor
      |
      +--> domain-design
      +--> application-design
      +--> infrastructure-design
      +--> mcp-components
      +--> providers
      +--> transforms
      +--> middleware
      +--> auth
      +--> authorization
      +--> state-context
      +--> testing
      +--> observability
      +--> deployment

all implementation skills
      |
      +--> security-review
      +--> final-review
```

## Rule

A downstream skill may add domain-specific knowledge, but it may not weaken the foundation contracts. If a specialized skill requires a different boundary, it must produce an architecture decision explaining why.

## Session isolation

Every new skill-development session receives:

1. the skill specification;
2. relevant foundation contracts;
3. relevant research artifacts;
4. dependency/version policy;
5. explicit task scope;
6. required output artifacts;
7. verification requirements.

The subagent must not assume hidden context from previous sessions.

## Development order

Foundation first. Then research skills. Then architecture/domain/application boundaries. Then FastMCP-specific mechanisms. Then integrations and infrastructure. Finally testing, security, observability, deployment, and review orchestration.
