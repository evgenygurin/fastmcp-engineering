# FastMCP Official Examples Catalog

This catalog is a research index, not a copy of examples. Before implementing a feature, inspect the relevant official example and record what it demonstrates and what it intentionally leaves out.

## Required classification

For every relevant example record:

- path;
- FastMCP mechanism;
- problem demonstrated;
- API surface used;
- architectural lesson;
- production gaps;
- security considerations;
- tests demonstrated or missing;
- version/protocol era;
- whether the example is safe to copy directly.

## Example families to inspect

### Server fundamentals

- quickstart and basic tool/resource/prompt examples;
- complex inputs and serialization;
- configuration and CLI behavior;
- lifecycle/lifespan.

### Composition

- mounted servers;
- proxy servers;
- providers;
- transforms;
- namespace/search/discovery patterns.

### Security

- OAuth providers;
- bearer/JWT authentication;
- mounted multi-provider authentication;
- authorization and role/scope behavior.

The official mounted authentication example demonstrates multiple OAuth-protected MCP servers under one application and path-aware discovery. citeturn0search4

### Runtime capabilities

- middleware;
- context/state;
- background tasks;
- progress reporting;
- elicitation;
- sampling;
- pagination;
- telemetry/diagnostics.

### Client and testing

- in-memory clients;
- HTTP clients;
- authenticated clients;
- integration/conformance examples.

### Advanced integrations

- OpenAPI;
- filesystem/provider integrations;
- MCP Apps;
- code mode;
- custom serializers;
- external service integrations.

## Production adaptation rule

An example is evidence of API usage, not an application architecture prescription. Minimal examples often omit configuration isolation, dependency injection, persistence boundaries, observability, security hardening, failure handling, and tests. A production skill must explicitly add the missing concerns rather than blindly copying example structure.

## Current evidence

FastMCP's server API documents Providers as dynamic component sources, Transforms as server-level component transformations, Middleware as cross-cutting request/response processing, and lifespan as startup/shutdown lifecycle management. citeturn0search0

The official HTTP deployment documentation recommends authentication for remote servers and calls out explicit CORS configuration for browser-facing deployments. citeturn0search2
