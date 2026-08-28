# System Architecture

## Purpose

FastMCP Engineering is a development methodology and skill system. It is not itself an MCP server and does not prescribe one universal application architecture.

## Default application boundary model

```text
Domain
  ↑
Application
  ↑
Infrastructure adapters
  ↑
Composition root
  ↑
MCP delivery adapters
```

Dependencies point inward toward stable policy. Concrete frameworks remain at the outer boundaries unless a documented decision explicitly places them elsewhere.

## Responsibilities

### Domain

Business rules, entities, value objects, domain services, domain policies, and domain errors. The domain does not know FastMCP, SQLAlchemy, PydanticAI, Supabase, HTTP clients, or LLM SDKs.

### Application

Use cases, application services, ports, commands/queries, and application-level result models. Application code orchestrates domain behavior and infrastructure through abstractions.

### Infrastructure

Concrete persistence and integration adapters: SQLAlchemy, Supabase, HTTP clients, queues, caches, filesystem, external APIs, and AI providers where applicable.

### MCP delivery

Tools, resources, prompts, serializers, providers, transforms, middleware, authentication integration, and protocol-facing translation. MCP handlers remain thin and delegate behavior to application use cases.

### Composition root

Configuration, dependency wiring, concrete implementation selection, lifecycle assembly, and FastMCP server construction.

## FastMCP mapping

- Components represent the MCP-facing contract.
- Providers source components.
- Transforms adapt component collections between provider and client.
- Middleware handles cross-cutting request/response concerns.
- Context exposes request/runtime capabilities to delivery/application boundaries where appropriate.
- Lifespans own application startup/shutdown resources.
- Client is used for deterministic MCP integration testing and MCP-to-MCP interaction.

Do not create custom equivalents when the native FastMCP mechanism already satisfies the requirement.

## Model boundaries

Keep these concepts distinct by default:

`Domain Model != Application DTO != MCP Schema != SQLAlchemy Model != External API Model`.

They may share an implementation only when the coupling is intentional, documented, and harmless to the affected boundary.
