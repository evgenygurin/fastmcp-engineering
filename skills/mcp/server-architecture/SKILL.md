---
name: mcp-server-architecture
description: Evidence-first FastMCP v3+ server architecture covering MCP boundaries, tools, resources, prompts, middleware, context, lifespan, transports, composition, proxying, auth integration and lifecycle.
---

# MCP / FastMCP Server Architecture

## Mission

Keep the MCP boundary thin, explicit and protocol-correct. FastMCP owns MCP protocol machinery; application/domain code owns business behavior. Architecture must prevent MCP decorators, context objects and transport concerns from leaking into the domain.

## Mandatory research gate

Before implementation:
1. Read AGENTS.md and repository architecture contracts.
2. Read the target FastMCP version's complete official `llms.txt` material relevant to the feature; when the feature crosses several subsystems, read the relevant `llms-full.txt` sections.
3. Read official FastMCP server, tools, resources, resource templates, prompts, context, middleware, lifespan, transports, composition/mounting/proxy, auth and deployment documentation.
4. Read the exact version's official upgrade/migration notes when moving from another major version.
5. Inspect all relevant official examples and their tests/source, not just one happy-path example.
6. Read the MCP specification for protocol semantics that FastMCP exposes.
7. Verify version-sensitive behavior against source/tests when documentation is ambiguous.
8. Record evidence and unresolved questions before coding.

## Layering

Use a strict dependency direction:

```text
MCP / FastMCP adapter
        ↓
Application / use cases
        ↓
Domain
        ↓
Ports / interfaces
        ↓
Infrastructure adapters
```

The domain must not import FastMCP, MCP SDK types, transport objects, HTTP request objects or database sessions. Application services may depend on domain ports, not on protocol details.

## Server composition

Treat `FastMCP` as the composition root/container for MCP-facing components. Keep server construction separate from business implementation. Prefer explicit assembly modules over a giant `server.py` containing configuration, tools, persistence and business logic.

Use subservers/mounting/composition/proxying only when they create a real ownership or deployment boundary. Do not split a small coherent server merely to look modular.

## Tools

Tools represent invocable operations. Tool handlers should be thin adapters:
1. validate protocol input through declared schemas;
2. obtain request-scoped dependencies/context;
3. invoke an application use case;
4. map application/domain result to an MCP-safe result;
5. translate expected errors at the boundary.

Do not put transaction orchestration, authorization policy, complex business rules or HTTP/database implementation inside the tool handler.

Tool descriptions and schemas are part of the public contract. Make names, descriptions, argument constraints and return semantics precise. Do not expose internal implementation details or unnecessary capabilities.

## Resources

Resources represent readable/passive data, distinct from action-oriented tools. Resource URIs/templates are public contracts. Keep resource resolution separate from domain retrieval. Validate resource identifiers and enforce authorization before retrieving sensitive data.

Do not turn every read operation into a tool or every action into a resource merely for convenience; choose the MCP primitive based on semantics.

## Prompts

Prompts are reusable interaction templates, not authorization mechanisms and not a place to encode hidden business logic. Keep prompt generation deterministic and versioned as a public contract. Treat prompt arguments and external data as untrusted.

## Context

Use FastMCP/MCP context only at the adapter/application boundary for request-scoped concerns such as logging correlation, progress, cancellation, request metadata and approved dependencies. Do not pass `Context` through the domain model or persist it.

Never make global mutable state the source of request identity, user authorization or tenant context.

## Dependencies

Use FastMCP's documented dependency/context mechanisms for request-scoped infrastructure only after verifying the exact version's semantics. Application dependencies should be explicit and testable. Avoid hidden service locators and implicit global singletons.

## Lifespan

Use lifespan for application-wide startup/shutdown resources such as connection pools, HTTP clients, model clients or caches when the exact lifecycle semantics justify it. Define ownership, initialization failure behavior, shutdown ordering and cleanup. Do not create per-request resources in global startup or leak application resources into tests.

## Middleware

Middleware belongs at cross-cutting protocol/application boundaries: telemetry, auth enforcement, rate limiting, error normalization, request policy and similar concerns. Middleware must have a single responsibility, deterministic ordering and documented scope. Do not use middleware as a hidden business-service registry.

Verify exact FastMCP middleware ordering and short-circuit semantics before relying on them.

## Transport

Separate protocol/application logic from transport selection. STDIO, Streamable HTTP and any legacy transport have different lifecycle/security/deployment properties. Use the transport supported by the target MCP client and FastMCP version. Treat SSE as legacy/deprecated when the target version documents it as such; do not select it for a new system without explicit compatibility justification.

Do not write transport-specific business code into tools.

## Authentication / authorization

Authentication is a server-boundary concern; authorization is an application/domain policy. FastMCP auth providers and middleware must be used according to exact target-version semantics. Propagate an immutable authenticated principal/context into application authorization without exposing protocol objects to domain code.

Never let model-generated text decide authorization.

## Error boundary

Classify errors at the appropriate layer. Domain errors remain domain concepts; application errors express use-case failures; MCP adapter maps them to protocol-safe responses according to verified FastMCP/MCP behavior. Preserve root-cause telemetry without leaking sensitive internals to clients.

## Composition / proxying

For mounted servers, subservers and proxies, explicitly document ownership, namespace/path behavior, auth boundaries, lifecycle, middleware scope, capability exposure and failure propagation. Inspect official mounted/proxy examples and tests before implementation. Never assume mounted auth/discovery paths or middleware ordering.

## Testing architecture

Every MCP component needs two levels where appropriate:
- unit/component tests for handler/application behavior;
- protocol-level tests through `fastmcp.Client` or the exact MCP transport for schemas, discovery, lifecycle and wire behavior.

In-memory clients are appropriate for deterministic MCP integration tests when they faithfully exercise the relevant protocol boundary. Real HTTP/STDIO tests are required when transport behavior itself is the invariant.

## Rejection criteria

Reject if FastMCP types leak into the domain, tool handlers contain substantial business logic, transport assumptions are embedded in application code, request/global state is conflated, middleware ordering is assumed rather than verified, resources are used as actions or tools as arbitrary data endpoints without semantic justification, or architecture depends on undocumented FastMCP behavior.

## Deliverables

Versioned FastMCP research package, MCP component inventory, layer/dependency diagram, server composition plan, tool/resource/prompt contracts, context/dependency policy, lifespan/middleware policy, transport matrix, auth boundary, error mapping, protocol test plan, implementation and architecture re-check.