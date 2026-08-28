---
name: fastmcp-protocol-compliance
description: Build FastMCP servers with explicit MCP specification compliance, separating protocol guarantees from FastMCP behavior and application conventions.
---

# FastMCP MCP Protocol Compliance

## Mission

Treat MCP as a protocol contract, FastMCP as an implementation framework, and application behavior as a separate architectural layer. Every material behavior must be classified before implementation.

## Mandatory research gate

Before implementation:

1. Read `AGENTS.md` and all repository engineering contracts.
2. Identify exact FastMCP/Python versions.
3. Read official MCP specification material relevant to the feature.
4. Read official FastMCP documentation and `llms.txt`/`llms-full.txt` material relevant to the feature.
5. Inspect all relevant official PrefectHQ/fastmcp examples.
6. Inspect FastMCP source/tests where behavior is ambiguous.
7. Inspect first-party dependency documentation where relevant.
8. Record an evidence ledger and protocol/framework/convention classification.

Never use FastMCP behavior as evidence of an MCP requirement, and never implement an MCP requirement from framework memory.

## Three-level contract

Classify every requirement as exactly one of:

```text
MCP specification guarantee
        │
        ├── FastMCP implementation behavior
        │       │
        │       └── application convention
        │
        └── protocol/client interoperability contract
```

If a framework behavior is stricter or different from the protocol, document the distinction and test the actual target behavior.

## Protocol areas

For every applicable feature investigate:

- JSON-RPC message semantics;
- initialization and negotiated protocol version;
- capability advertisement and capability gating;
- request/response correlation;
- notifications;
- Tools;
- Resources and Resource Templates;
- Prompts;
- structured content/output schemas;
- annotations/metadata;
- progress;
- cancellation;
- Tasks;
- logging;
- sampling;
- elicitation;
- roots;
- authorization/security;
- transport semantics;
- pagination/completion where applicable;
- error codes and error propagation.

Only claim support when the target FastMCP version and MCP protocol version actually establish it.

## Compatibility

Design against interoperable MCP clients, not only FastMCP Client. Where practical verify with protocol-level fixtures and at least one independent/real MCP client or transport implementation.

Do not rely on undocumented framework internals for interoperability.

## Capability discipline

Capabilities must reflect actual supported behavior. Do not advertise optional capabilities that the server cannot correctly service. Do not silently depend on client capabilities without negotiation/verification where the protocol requires it.

## Error discipline

Preserve the distinction between:

- JSON-RPC/protocol errors;
- MCP errors;
- application/domain errors;
- infrastructure errors.

Do not expose internal exceptions, secrets, SQL details, stack traces, or implementation objects through protocol responses.

## Versioning

Record the MCP protocol version, FastMCP version, and any relevant feature/version gate. Treat changes in draft/experimental MCP features as unstable until verified. Do not copy an example from another protocol generation without checking compatibility.

## Testing

Build a protocol verification layer covering:

- initialization/negotiation;
- capability advertisement;
- valid and invalid requests;
- notifications;
- tool/resource/prompt contracts;
- schemas and structured output;
- progress/cancellation where applicable;
- task lifecycle where applicable;
- error mapping;
- pagination/completion where applicable;
- transport behavior;
- authentication/authorization boundaries.

## Rejection criteria

Reject if a protocol claim lacks specification evidence, if framework behavior is mistaken for protocol law, if capabilities are over-advertised, if error layers are conflated, if version compatibility is unspecified, or if interoperability depends on undocumented internals.

## Deliverables

- protocol/version matrix;
- feature compliance matrix;
- specification-to-FastMCP mapping;
- official examples catalog;
- interoperability assumptions;
- error mapping;
- capability matrix;
- implementation;
- protocol tests;
- MCP Client/integration tests;
- architecture re-check;
- evidence ledger.
