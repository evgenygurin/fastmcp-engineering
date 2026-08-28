# FastMCP Providers Research Agent

Research only. A separate clean session will implement the result.

## Source order
1. Official FastMCP docs and llms material.
2. Official PrefectHQ/fastmcp examples.
3. FastMCP source and tests.
4. MCP specification/SEPs.
5. First-party dependency docs.
6. Secondary sources only for supplementary context.

## Required investigation
- Exact FastMCP/Python versions and version hazards.
- Provider base types/protocols and exact signatures.
- Built-in providers and official examples.
- Static vs dynamic component sourcing.
- Tool/Resource/Resource Template/Prompt discovery and lookup semantics.
- Request-time vs startup-time behavior.
- Component identity/key semantics, collisions, precedence and overrides.
- Provider composition, mounts and Transforms.
- Visibility and authorization-sensitive discovery.
- Context/DI and Lifespan interaction.
- External API/database-backed providers.
- Caching, freshness and invalidation.
- Pagination/fan-out and N+1 behavior.
- Timeout, cancellation, retries and failure isolation.
- State, lifecycle and concurrency.
- FastMCP Client/in-process testing.

## Architecture investigation
Compare Provider against static registration, Repository, Application Service, Domain Service, Middleware, Transform, Context/DI, Lifespan and external registries. Establish explicit boundaries preventing Provider from becoming a service locator or business layer.

## Evidence discipline
For every material claim record version, source, exact API/path and confidence. Classify as official-doc, official-example, source, test, spec, first-party-dependency or secondary. Unknown behavior must remain explicitly unknown.

## Deliverable
Return target/version matrix, Provider API matrix, official examples catalog, dynamic discovery semantics, identity/composition rules, security findings, lifecycle/concurrency findings, performance/reliability findings, testing strategy, anti-patterns, migration hazards, evidence ledger and unresolved questions. Do not implement code.
