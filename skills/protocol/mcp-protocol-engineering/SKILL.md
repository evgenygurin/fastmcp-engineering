---
name: mcp-protocol-engineering
description: Evidence-first MCP protocol engineering for FastMCP servers and clients, including lifecycle, transports, capabilities, sessions, tools/resources/prompts, errors, compatibility, and protocol testing.
---

# MCP Protocol Engineering

## Mission
Implement MCP integrations from the protocol contract outward. FastMCP is the implementation framework; MCP protocol semantics remain the interoperability contract.

## Mandatory research gate
Before design or code:
1. Read the exact MCP specification version targeted by the project, including lifecycle, transports, authorization, tools, resources, prompts, notifications, capabilities, errors and version negotiation.
2. Read exact-version FastMCP documentation and relevant examples.
3. Inspect official FastMCP/MCP source and tests where documentation is ambiguous.
4. Identify supported/stable versus experimental/draft features. Never silently mix versions.
5. Record protocol assumptions and compatibility matrix.

## Lifecycle
For handshake-era versions, model initialize/negotiation, capability agreement, normal operation and shutdown/disconnect as explicit states. For the modern `2026-07-28` protocol, do not invent a protocol-level initialize handshake or session requirement: the core is stateless and requests are designed to be routable across instances. Reject operations invalid for the targeted protocol lifecycle and respect notification semantics.

## Capabilities
Advertise only capabilities actually implemented. Discovery/capability information is an interoperability contract, not a feature flag decoration. Unknown/unsupported capabilities must be handled according to the target specification.

## Transports
Choose transport from deployment requirements and exact FastMCP support. For modern Streamable HTTP, account for `Mcp-Method`/`Mcp-Name` routing headers and ordinary load balancing. Define cancellation, disconnect behavior, proxy/load-balancer requirements, keepalive/streaming semantics where applicable and security boundaries. Do not write custom transport code when native FastMCP support satisfies the requirement.

## Primitives
Design tools, resources and prompts according to their distinct semantics. Tools perform operations; resources expose contextual data; prompts provide reusable prompt templates. Do not collapse these into one generic abstraction.

Tool schemas must be explicit and validated. Under `2026-07-28`, tool schemas use JSON Schema 2020-12; bound validation depth/time and reject unsafe/unbounded schema processing. Resource URIs must have deterministic ownership and authorization semantics. Prompt arguments must be validated and must not become an authorization mechanism.

## Errors
Preserve the distinction between protocol-level errors and application/tool errors as defined by the target MCP version. Map internal exceptions deliberately. Do not leak stack traces, credentials, SQL or internal topology. Error responses must remain useful to clients without exposing sensitive internals. Track version-specific error-code changes rather than matching obsolete literals blindly.

## State and concurrency
For handshake-era versions define session lifetime and per-session state explicitly. For modern stateless protocol versions keep application state explicit and independently scoped. Do not share mutable state across concurrent requests without synchronization and documented semantics. Cancellation must propagate to in-flight operations and release resources.

## Authorization
Protocol authentication/authorization is separate from application authorization. Validate identity, issuer, audience/resource and scopes according to the applicable authorization specification. Tool descriptions and model decisions never authorize access.

## Compatibility
Maintain a matrix of MCP spec version, FastMCP version, transport, client implementation and feature availability. Test the minimum and target supported combinations where practical. Never claim interoperability from a single happy-path client test.

## Extensions / deprecations
Treat extensions such as Tasks as explicitly versioned opt-in features. Do not silently depend on draft behavior. Avoid deprecated Roots, Sampling or Logging for new architecture unless compatibility requires them and document the reason.

## Testing
Use protocol-level tests for lifecycle/discovery, capability negotiation, valid/invalid messages, notifications, tool/resource/prompt discovery and invocation, error mapping, cancellation, disconnect/reconnect, transport behavior and authorization. Prefer official SDK/client test facilities. Add interoperability tests for supported client combinations where practical.

## Rejection criteria
Reject if protocol version is implicit, capabilities are over-advertised, lifecycle assumptions contradict the target version, custom transport code duplicates native functionality, protocol/application errors are conflated, unsupported features are silently accepted, deprecated/draft behavior is hidden, or tests cover only application internals without protocol interoperability checks.

## Deliverables
Protocol version/feature matrix, lifecycle state model, transport decision, capability contract, primitive contracts, error mapping, authorization boundary, compatibility plan, protocol test matrix, implementation and verification report.