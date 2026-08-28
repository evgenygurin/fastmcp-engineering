# FastMCP Engineering — Agent Contract

## Mission

Build production-grade MCP servers through evidence-driven research, explicit architecture, TDD, security review, and verification.

## Non-negotiable rules

1. Research official FastMCP documentation before designing or implementing a FastMCP feature.
2. Inspect relevant official FastMCP examples before selecting an implementation mechanism.
3. Verify the MCP protocol semantics relevant to the feature.
4. Identify the supported FastMCP version before using an API; never silently mix version-specific APIs.
5. Prefer native FastMCP mechanisms (Providers, Transforms, Middleware, Context, Lifespans, tasks, auth, client, etc.) when they fit; justify custom infrastructure.
6. Keep domain logic independent of FastMCP, SQLAlchemy, Pydantic, Supabase, HTTP clients, and LLM SDKs unless a deliberate boundary requires otherwise.
7. Keep MCP handlers thin: validate/translate input, invoke an application use case, translate the result.
8. Apply SOLID, KISS, DRY, and YAGNI as constraints, not slogans. Every non-trivial abstraction needs a reason.
9. Use TDD for behavior changes and verify at the appropriate unit, integration, MCP-contract, transport, security, and conformance levels.
10. Never claim completion without running the prescribed verification.

## Required workflow

Requirement → discovery → official research → example/pattern analysis → version check → architecture → architecture gate → contracts → tests → implementation → static analysis → integration/MCP tests → security review → architecture review → final verification.

## Quality principle

A minimal correct design is preferred over a sophisticated design. Framework correctness is not sufficient: responsibility boundaries, failure modes, security, testability, operability, and maintainability must also be correct.
