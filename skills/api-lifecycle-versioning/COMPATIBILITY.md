# Compatibility Matrix

## Dimensions

Evaluate each public change independently across:

- MCP protocol version negotiation
- transport/session behavior
- tool/resource/prompt discovery
- input schema
- output/structured content
- protocol/application errors
- authentication/authorization
- pagination
- dependency/runtime behavior

## Classification

**Additive:** existing valid clients continue to work without changes.

**Conditionally compatible:** compatibility depends on a documented client capability, negotiated feature, or explicit behavior.

**Breaking:** an existing supported client can fail validation, discovery, authorization, invocation, parsing, or semantic expectations.

## Potentially breaking changes

- removing/renaming public tools, resources, or prompts
- changing meaning while preserving a name
- tightening required fields or validation bounds
- changing defaults
- changing nullability or enum semantics
- changing pagination or ordering guarantees
- changing error categories or machine-readable fields
- adding mandatory authorization requirements
- changing negotiated protocol/capability behavior

## Required migration sequence

For breaking changes:

1. introduce replacement;
2. document migration;
3. support overlap where required;
4. measure/verify remaining consumers when possible;
5. remove old contract only after explicit criteria.

Protocol version and application API version must never be conflated.