# Pydantic Schema Acceptance Criteria

- Exact Python/Pydantic/FastMCP/MCP versions identified.
- Official Pydantic documentation and relevant FastMCP/MCP material read.
- MCP input/output, application, domain and persistence model ownership is explicit.
- Structural validation and business invariants have separate ownership.
- Strict/lax behavior and security-sensitive coercion are intentional.
- Serialization, aliases and secret exclusion are tested.
- Generated JSON Schema is reviewed.
- Actual FastMCP-visible schemas are verified for critical tools.
- Structured output behavior is tested where applicable.
- Discriminated unions are tested where applicable.
- Required/null/default semantics are tested.
- Schema evolution and compatibility are assessed.
- Formatter, lint, type checks and tests pass.
- Architecture re-check passes.
- [ ] Stops when schema behavior cannot be established from evidence; rejects invented behavior and escalates to the user instead of guessing.
