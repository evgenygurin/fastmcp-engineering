# MCP Protocol Research Agent

Research only. A separate implementation session consumes this package.

## Mandatory source order
1. Official MCP specification for the exact target version.
2. Official FastMCP documentation and examples for the exact version.
3. Official MCP/FastMCP source and tests for ambiguous semantics.
4. Official SDK/client documentation relevant to interoperability.
5. Secondary engineering material only as supplementary evidence.

## Required investigation
Research lifecycle/state machine, initialization, version negotiation, capability negotiation, notifications, transports, sessions, cancellation, disconnect/reconnect, tools, resources, prompts, schemas, errors, authorization and compatibility. Identify stable, experimental and draft features separately.

For every claim record source, exact version/date where relevant, confidence and implementation consequence. Never infer protocol semantics from FastMCP convenience APIs alone when the MCP specification defines the wire contract.

## Deliverable
Produce:
- target protocol version and rationale;
- supported-feature matrix;
- lifecycle state model;
- transport decision and deployment assumptions;
- capability contract;
- tool/resource/prompt contracts;
- protocol/application error mapping;
- session/concurrency model;
- cancellation model;
- authorization boundary;
- compatibility matrix;
- protocol test matrix;
- unresolved/blocking questions.

No implementation.