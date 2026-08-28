# FastMCP Pattern Catalog

This catalog records official FastMCP mechanisms as architectural patterns. It is intentionally prescriptive about boundaries, not about one universal application architecture.

## Provider

**Problem:** MCP components originate dynamically from another source or server.

**Use:** dynamic tools/resources/prompts, remote or composed component sources, runtime discovery.

**Do not use:** as a generic application repository or business service.

**Evidence:** FastMCP documents Providers as sources that can supply components dynamically and be queried at request time.

## Transform

**Problem:** the set or presentation of MCP components must change between provider and client.

**Use:** namespace/presentation changes, filtering, discovery/search, tool adaptation, composition.

**Do not use:** domain rules or persistence orchestration.

## Middleware

**Problem:** behavior applies across many MCP operations.

**Use:** authentication/authorization gates, logging, rate limiting, error handling, timing, telemetry, request/response cross-cutting concerns.

**Do not use:** business workflows.

FastMCP middleware forms a request/response pipeline and supports method-specific hooks. citeturn0search1

## Context / state

**Problem:** a tool/resource/prompt needs request/session-scoped FastMCP runtime information.

**Use:** runtime context, progress/reporting, state, sampling/elicitation where supported.

**Do not use:** as a replacement for domain state or persistence.

## Lifespan

**Problem:** startup/shutdown resources need explicit lifecycle ownership.

**Use:** database engines, clients, caches, external resources, controlled initialization/cleanup.

**Do not use:** for per-request business operations.

## Client

**Problem:** deterministic MCP integration and contract testing.

**Use:** in-memory and transport-level MCP tests, authentication flows, protocol interaction.

**Do not use:** as the application service abstraction.

## Auth / authorization

**Problem:** remote MCP access needs identity and access control.

**Use:** FastMCP authentication providers and explicit authorization mechanisms where supported.

**Do not use:** hard-coded credentials or ad-hoc auth checks scattered across tools.

## Pagination

**Problem:** component/data catalogs can exceed safe response sizes.

**Use:** native pagination before inventing custom page protocols.

## Versioning

**Problem:** component evolution without ambiguous identity.

**Use:** FastMCP component/version semantics where applicable.

## Composition / mount / proxy

**Problem:** multiple MCP capabilities need controlled composition.

**Use:** mount, providers, proxying, and transforms according to the ownership boundary.

## Pattern-selection rule

Always choose the smallest native mechanism that satisfies the requirement. A custom wrapper around a native FastMCP capability requires a documented reason such as policy enforcement, application boundary isolation, or a stable project-owned contract.
