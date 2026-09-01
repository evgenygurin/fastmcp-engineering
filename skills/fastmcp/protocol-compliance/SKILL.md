---
name: fastmcp-protocol-compliance
description: Build FastMCP servers with explicit MCP specification compliance, separating protocol guarantees from FastMCP behavior and application conventions.
---

# FastMCP MCP Protocol Compliance

## Mission

Treat MCP as a protocol contract, FastMCP as an implementation framework, and application behavior as a separate architectural layer. Every material behavior must be classified before implementation.

## Trigger / Когда применять

**Scope / When to use:** FastMCP servers with explicit MCP specification compliance, separating protocol guarantees from FastMCP behavior and application conventions.
**Trigger:** designing or implementing MCP-facing behavior that must comply with the MCP specification.
**Upstream / Prerequisite:** `AGENTS.md` and all repository engineering contracts read; identified exact FastMCP/Python versions; an evidence ledger and protocol/framework/convention classification recorded.
**Mission / Goal:** treat MCP as a protocol contract, FastMCP as an implementation framework, and application behavior as a separate architectural layer; classify every material behavior before implementation.
**Research / Evidence:** read official MCP specification material relevant to the feature; read official FastMCP documentation and `llms.txt`/`llms-full.txt` material; inspect all relevant official PrefectHQ/fastmcp examples; inspect FastMCP source/tests where behavior is ambiguous; inspect first-party dependency documentation where relevant; never use FastMCP behavior as evidence of an MCP requirement.
**Decision / Selection rules:** classify every requirement as exactly one of MCP specification guarantee, FastMCP implementation behavior, or application convention; if a framework behavior is stricter or different from the protocol, document the distinction and test the actual target behavior; design against interoperable MCP clients, not only FastMCP Client; capabilities must reflect actual supported behavior; preserve the distinction between JSON-RPC/protocol, MCP, application/domain and infrastructure errors.
**Version / Compatibility:** identify the exact MCP protocol version, FastMCP version, and any relevant feature/version gate; treat changes in draft/experimental MCP features as unstable until verified; do not copy an example from another protocol generation without checking compatibility.

## Deliverables

**Deliverables / Artifacts:** protocol/version matrix; feature compliance matrix; specification-to-FastMCP mapping; official examples catalog; interoperability assumptions; error mapping; capability matrix; implementation; protocol tests; MCP Client/integration tests; architecture re-check; evidence ledger.
**Verification / Testing:** build a protocol verification layer covering initialization/negotiation, capability advertisement, valid and invalid requests, notifications, tool/resource/prompt contracts, schemas and structured output, progress/cancellation, task lifecycle, error mapping, pagination/completion, transport behavior, and authentication/authorization boundaries.
**Failure / Stop conditions:** reject if a protocol claim lacks specification evidence, framework behavior is mistaken for protocol law, capabilities are over-advertised, error layers are conflated, version compatibility is unspecified, or interoperability depends on undocumented internals.
**Positive scenario:** every material behavior is classified against the protocol and passes protocol-level verification with an independent client.
**Negative scenario:** a protocol claim is made without specification evidence or a framework behavior is mistaken for protocol law.

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
