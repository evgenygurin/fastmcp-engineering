# Pydantic / Schema Engineering Decision Matrix

| Concern | Preferred boundary | Required evidence |
|---|---|---|
| MCP input contract | Pydantic DTO / adapter | FastMCP + MCP docs |
| Application command | application model | repository architecture |
| Domain invariant | domain type/value object | domain design |
| Persistence row | SQLAlchemy model | SQLAlchemy docs |
| JSON Schema | generated public contract | Pydantic + FastMCP + MCP |
| Authorization | policy layer | security architecture |

## Hard rules

1. Do not expose SQLAlchemy entities as public MCP contracts by accident.
2. Do not use Pydantic validation as authorization.
3. Do not hide contract fields behind `Any` or arbitrary dictionaries.
4. Do not assume Python typing and JSON Schema have identical semantics.
5. Do not assume JSON Schema accepted by Pydantic is automatically accepted by every MCP client.
6. Verify FastMCP schema generation for the target version.
7. Treat requiredness, nullability, defaults, enums and aliases as compatibility-sensitive.
8. Version public schemas deliberately.

## Model flow

```text
MCP payload
   ↓
Pydantic boundary DTO
   ↓
Application command/result
   ↓
Domain model
   ↓
SQLAlchemy persistence model
```

Mappings should be explicit where semantics differ.