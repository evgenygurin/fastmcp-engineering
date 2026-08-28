# FastMCP Native Mechanisms — Research Record

Status: current research snapshot

## Evidence basis

Primary sources:

- FastMCP server documentation: https://gofastmcp.com/servers/server
- FastMCP middleware documentation: https://gofastmcp.com/servers/middleware
- FastMCP providers documentation: https://gofastmcp.com/servers/providers/overview
- FastMCP transforms documentation: https://gofastmcp.com/servers/transforms/transforms
- FastMCP client documentation: https://gofastmcp.com/clients/client
- FastMCP repository examples: https://github.com/PrefectHQ/fastmcp/tree/main/examples

## Findings

### Components

Tools, Resources, and Prompts are distinct MCP-facing component types. Tool handlers should remain delivery adapters and delegate application behavior.

### Providers

Providers are the native mechanism for sourcing MCP components dynamically. Use them when the component catalog itself is dynamic or originates from another source. Do not confuse a Provider with a domain Repository.

### Transforms

Transforms operate on the component presentation/composition pipeline. They are preferred for MCP-facing namespace, discovery, filtering, renaming, and related transformations rather than introducing application services for presentation concerns.

### Middleware

Middleware is a FastMCP-specific cross-cutting pipeline. It is appropriate for authentication/authorization checks, logging, rate limiting, timing, caching, centralized error handling, and request/response processing. Business rules do not belong there.

Middleware order is semantically significant. Error handling that should cover downstream middleware must be registered early; logging/timing placement must reflect the desired observation boundary.

### Lifespan

Lifespan owns startup/shutdown resource management. Database engines, HTTP clients, pools, and other long-lived resources should be initialized and disposed according to an explicit lifecycle policy rather than per-tool ad hoc construction.

### Context and dependency injection

Context and dependency injection are runtime/delivery mechanisms. They may supply request-scoped capabilities to a use case boundary, but should not be used to smuggle framework objects into domain code.

### Client

FastMCP Client is a first-class testing and integration mechanism. Prefer protocol-level tests through Client over testing only the Python function behind a decorated tool.

### Composition

Mounting, proxying, Providers, and Transforms can compose MCP servers dynamically. Before writing a custom aggregation layer, evaluate these native composition mechanisms.

## Decision rule

The existence of a native mechanism is not sufficient justification to use it. The agent must still verify responsibility, lifecycle, security, testability, and complexity. However, a custom mechanism must explain why the native mechanism is insufficient.

## Production warning

Official examples are intentionally small. They demonstrate API mechanics and are not complete production architectures. Production adaptation must explicitly address configuration, dependency wiring, persistence boundaries, security, observability, failure handling, testing, and deployment topology.

## Version note

Version-sensitive APIs must be checked against the repository's version policy before implementation. FastMCP 4 migration material must not be silently applied to a FastMCP 3.x target.
