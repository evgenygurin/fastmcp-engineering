# FastMCP Protocol Compliance Decision Matrix

## Core rule
MCP specification, FastMCP implementation, and application conventions are separate contracts.

| Question | Evidence required | Result |
|---|---|---|
| Is this mandated by MCP? | Specification | |
| Is this a FastMCP feature? | Official docs/examples/source | |
| Is this application policy? | Repository architecture | |
| Is capability negotiation required? | Specification + implementation | |
| Is behavior version-sensitive? | Versioned docs/source/tests | |
| Does an error belong to JSON-RPC, MCP, application, or infrastructure? | Specification + framework behavior | |

## Hard rules

1. Never infer protocol requirements from a framework decorator.
2. Never infer framework guarantees from the protocol specification.
3. Never advertise an unsupported capability.
4. Never expose internal exceptions, secrets, SQL details, or stack traces through MCP responses.
5. Never depend on undocumented framework internals for interoperability.
6. Record the MCP protocol version and FastMCP version for every feature decision.
7. Experimental/draft protocol features require explicit version and stability treatment.
8. Protocol adaptation belongs at the MCP boundary; business rules belong in application/domain layers.

## Error boundary

```text
JSON-RPC transport/protocol
        ↓
MCP semantic error
        ↓
application/domain error
        ↓
infrastructure failure
```

Map errors deliberately. Do not flatten all failures into a generic exception or leak implementation details.

## Compatibility gate

A feature is not considered interoperable merely because FastMCP Client can exercise it. Where interoperability is material, verify against protocol-level fixtures or an independent MCP implementation/client.