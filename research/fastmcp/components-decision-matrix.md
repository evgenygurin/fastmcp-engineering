# FastMCP Components Decision Matrix

## Scope

This artifact defines how an agent chooses among MCP Tools, Resources, and Prompts before implementing an MCP-facing capability. It is a decision aid, not a substitute for current official FastMCP documentation.

## Mandatory research

Before applying this matrix, verify the target FastMCP version against official documentation and inspect relevant official examples. If behavior is version-sensitive, inspect source/tests as well.

## Component selection

| Requirement shape | Preferred MCP component | Reason |
|---|---|---|
| Model should invoke an operation/action | Tool | Represents executable capability |
| Client/model should retrieve addressable/read-oriented data | Resource | Represents contextual data rather than an action |
| Reusable user/model instruction or workflow template | Prompt | Represents reusable prompt content |
| Cross-cutting behavior around many components | Middleware | Not a component substitute |
| Dynamic/component discovery or composition | Provider | Component source/composition concern |
| Systematic transformation of exposed components | Transform | Presentation/composition transformation |

## Tool rules

A Tool should be a thin MCP delivery adapter. It should:

- validate/accept the public MCP input schema;
- establish MCP-specific context when required;
- invoke an application use case or explicitly justified boundary;
- translate application/domain outcomes into MCP-facing results/errors.

A Tool should not:

- execute SQL directly;
- own transactions that belong to the application boundary;
- contain business invariants;
- instantiate infrastructure clients;
- become a hidden service layer;
- expose internal persistence models as a public contract by accident.

## Resource rules

Choose Resource when the primary semantics are retrieval of contextual/addressable data rather than an action. Define URI semantics, parameterization, freshness/caching requirements, authorization, and error behavior explicitly.

Do not force mutations into Resources simply because a read can trigger side effects.

## Prompt rules

Choose Prompt for reusable prompt content and explicit user/model guidance. Keep domain decisions in application/domain code. Prompt templates are not a substitute for authorization or business rules.

## Schema boundary

Treat the MCP schema as a public protocol contract. It may be backed by Pydantic, but the choice must follow the public contract and validation semantics rather than convenience. Do not automatically reuse SQLAlchemy models or domain entities as MCP schemas.

## Result and error boundary

Define:

- success shape;
- structured output requirements;
- validation failures;
- domain/application failures;
- authorization failures;
- infrastructure failures;
- whether errors are exposed, translated, or redacted.

The exact FastMCP error/result API must be verified against the target version before implementation.

## Decision record

```yaml
component: <tool|resource|prompt>
requirement: <statement>
selected: <component>
alternatives_considered: []
native_fastmcp_evidence: []
public_contract: <summary>
application_boundary: <use case / port>
security: <summary>
testing: []
version: <target>
```

## Anti-patterns

- "Everything is a Tool."
- CRUD database endpoints exposed one-to-one as MCP components without semantic design.
- Tool functions containing domain logic.
- Resource used as a generic RPC endpoint.
- Prompt used as a place to encode authorization/business invariants.
- Pydantic/SQLAlchemy model reuse without contract analysis.
