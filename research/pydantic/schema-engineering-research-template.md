# Pydantic / Schema Engineering Research Package

## Target
- Python:
- Pydantic:
- FastMCP:
- MCP protocol:
- Date:

## First-party evidence
- Pydantic docs:
- FastMCP docs/llms:
- FastMCP examples:
- Source/tests:
- JSON Schema specification:
- MCP specification:

## API matrix
| Feature | Pydantic behavior | FastMCP behavior | MCP/JSON Schema constraint | Evidence | Confidence |
|---|---|---|---|---|---|
| BaseModel | | | | | |
| TypeAdapter | | | | | |
| Annotated/Field | | | | | |
| Unions | | | | | |
| Validators | | | | | |
| Serializers | | | | | |
| Strict mode | | | | | |
| Aliases | | | | | |
| Defaults | | | | | |
| Optional/null | | | | | |
| JSON Schema | | | | | |
| Structured output | | | | | |

## Boundary decisions
- MCP DTO:
- Application command/result:
- Domain:
- Persistence:
- Mapping strategy:

## Evolution
| Change | Compatibility | Migration/version gate | Evidence |
|---|---|---|---|
| Add field | | | |
| Remove field | | | |
| Rename field | | | |
| Requiredness change | | | |
| Nullability change | | | |
| Enum change | | | |

## Security
- Payload limits:
- Validation:
- Authorization boundary:
- Secret handling:

## Verification
- Generated schema fixtures:
- Validation tests:
- Serialization tests:
- FastMCP invocation:
- Compatibility tests:
- Property-based tests:

## Unknowns
List every behavior not established by first-party evidence. Blocking unknowns must be resolved before implementation.

## Evidence classification
Use `official-doc`, `official-example`, `source`, `test`, `spec`, `first-party-dependency`, or `secondary`. Secondary evidence never overrides contradictory first-party evidence.