# Pydantic Schema Decision Matrix

| Concern | Default | Verification |
|---|---|---|
| MCP input | Explicit transport DTO | MCP schema inspection |
| MCP output | Explicit public contract | structured-output test |
| Application command | Separate when semantics differ | use-case tests |
| Domain model | Domain-owned invariants | domain tests |
| Persistence | ORM-owned model | DB integration |
| Structural validation | Pydantic boundary | validation tests |
| Business invariants | Domain/application | unit/integration |
| Variant payloads | Discriminated union | schema + validation test |
| Public schema | Generated and reviewed | schema regression |
| Serialization | Explicit aliases/serializers | serialization tests |

## Hard rules

1. A Pydantic model is not automatically a domain model.
2. An ORM entity is not automatically an MCP DTO.
3. Validation is not authorization.
4. Business rules requiring external state do not belong in Pydantic validators.
5. Public JSON Schema is a contract and must be reviewed.
6. Critical MCP tools require verification of the actual FastMCP-visible schema.
7. Avoid accidental coercion for security-sensitive values.
8. Prefer discriminated unions when variants have stable discriminators.
9. Never expose secrets/internal ORM fields through serialization by accident.
10. Schema changes require compatibility analysis.