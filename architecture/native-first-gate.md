# FastMCP Native-First Decision Gate

Before introducing custom infrastructure around MCP behavior, the agent MUST inspect the native FastMCP mechanisms relevant to the requirement.

## Mandatory candidates

- Tools, Resources, Prompts
- Providers
- Transforms
- Middleware
- Context and dependency injection
- Lifespan
- Tasks / background execution
- Authentication and authorization
- Composition / mount / proxy
- Pagination
- Versioning
- Telemetry / observability
- FastMCP Client
- serialization / schema customization

## Decision rule

If a native mechanism satisfies the requirement, use it unless there is documented evidence that it is unsuitable. A custom abstraction requires an Architecture Decision Record explaining the gap, alternatives considered, and long-term cost.

## Responsibility rule

Native FastMCP mechanisms are delivery/runtime concerns. They MUST NOT become a reason to move domain rules, persistence logic, or application orchestration into MCP adapters.

## Example rule

Before selecting a mechanism, inspect at least one official example or source/test case that exercises the same mechanism. Record what is demonstrated and what is deliberately simplified.