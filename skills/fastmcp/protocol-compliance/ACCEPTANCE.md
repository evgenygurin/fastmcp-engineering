# Acceptance — FastMCP Protocol Compliance

## Positive scenario

- [ ] **Happy path:** for a feature with an applicable MCP specification requirement, the implementation maps the requirement to the target FastMCP behavior and produces protocol/conformance verification evidence.

## Negative scenario

- [ ] **Failure mode:** if protocol behavior is unsupported, ambiguous, or version-sensitive, the implementation does not guess; it records the limitation and expected outcome, and the work is escalated or rejected as appropriate.

## Contract checks

- [ ] Maps implementation behavior to the applicable MCP specification requirements.
- [ ] Verifies protocol lifecycle, schemas, capabilities, errors, and transport assumptions relevant to the feature.
- [ ] Distinguishes MCP protocol requirements from FastMCP implementation details.
- [ ] Identifies unsupported, ambiguous, or version-sensitive behavior instead of guessing.
- [ ] Produces protocol/conformance verification evidence.

## Stop condition

- [ ] **Reject/stop** the change when a protocol claim lacks specification evidence, framework behavior is presented as protocol law, capabilities are over-advertised, error layers are conflated, version compatibility is unspecified, or interoperability depends on undocumented internals.
