# Dependency Injection / Composition Root Research Agent

Research only. Do not implement.

Read AGENTS.md and all applicable skills. Identify exact Python, FastMCP, Pydantic, SQLAlchemy, PydanticAI and selected client/DI-library versions. Read current official documentation first, then exact-version FastMCP examples/source/tests, SQLAlchemy async lifecycle docs, PydanticAI dependency docs and any candidate DI framework documentation.

Map every dependency and classify its lifetime: process, application, request/task, transaction or transient. Identify creation owner, consumer, shutdown owner, concurrency constraints, failure behavior and whether substitution is actually needed. Determine FastMCP lifespan/context semantics from authoritative sources.

Evaluate constructor injection, function injection, Protocols and DI containers. Explicitly reject abstractions without a real consumer need. Identify circular dependencies and service-locator/global-state risks.

Produce: dependency graph; lifetime matrix; composition-root design; ports/protocol candidates; FastMCP lifecycle mapping; SQLAlchemy lifecycle; PydanticAI dependency mapping; external-client lifecycle; startup/shutdown failure model; test wiring strategy; evidence ledger; rejected alternatives; unresolved risks. Every version-sensitive claim requires authoritative evidence.