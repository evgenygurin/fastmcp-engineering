# FastMCP Research Index

This index defines the research surface that the research agent must revisit when producing or refreshing FastMCP guidance.

## Core framework

- Installation and version policy
- Server
- Tools
- Resources
- Resource templates
- Prompts
- Context
- Dependency injection
- Lifespan
- Middleware
- Providers
- Transforms
- Composition and mounting
- Proxying
- Serialization
- Versioning
- Pagination
- Background tasks
- FastMCP Client
- CLI

## Protocol and interaction

- MCP protocol lifecycle
- transports
- Streamable HTTP
- stdio
- legacy SSE
- elicitation
- sampling
- progress reporting
- logging
- roots
- notifications
- capability negotiation

## Security

- authentication
- authorization
- OAuth providers
- OAuth proxy
- token verification
- scopes
- roles
- dynamic client registration
- path-aware discovery
- security middleware
- secrets/configuration

## Advanced FastMCP

- MCP Apps
- tool UI
- OpenAPI provider
- filesystem provider
- remote/provider composition
- transforms
- tool search
- code mode
- custom serializers
- custom providers
- custom middleware
- custom extensions

## Testing and quality

- in-memory Client tests
- HTTP integration tests
- stdio tests
- protocol/conformance tests
- middleware tests
- auth tests
- lifecycle tests
- task/background tests
- schema tests
- agent/evaluation tests

## Deployment and operations

- HTTP deployment
- ASGI integration
- Starlette integration
- Uvicorn
- reverse proxies
- horizontal scaling
- state/storage
- telemetry
- logging
- health/readiness
- failure handling

## Version research

Always check:

1. current stable release;
2. prerelease line;
3. v3 -> v4 migration guide;
4. deprecated/removed APIs;
5. version badges on relevant documentation;
6. source/test changes for version-sensitive behavior.

## Research strategy

This is a coverage index, not a requirement to read unrelated pages for every task. The agent must select all entries materially related to the task and record why unrelated areas were excluded when the boundary is not obvious.
