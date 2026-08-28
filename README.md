# FastMCP Engineering

Engineering methodology, research artifacts, skills, prompts, contracts, and quality gates for building production-grade MCP servers with FastMCP.

## Core principles

- Research official documentation and official examples before making framework decisions.
- Separate domain, application, infrastructure, and MCP delivery responsibilities.
- Prefer the simplest architecture that satisfies real requirements.
- Use SOLID, KISS, DRY, and YAGNI as decision criteria, not as reasons to add abstractions.
- Prefer native FastMCP capabilities before custom infrastructure.
- Keep Pydantic, SQLAlchemy, PydanticAI, Supabase, and other technologies behind appropriate boundaries.
- Verify behavior with tests, protocol checks, security review, and architecture review.

## Engineering workflow

Requirement → Discovery → Documentation Research → Example Research → Architecture → Design Gate → Contracts → TDD → Implementation → Static Analysis → Tests → Security Review → Architecture Review → Final Verification.

## Version policy

FastMCP version-specific claims must identify their version and stability level. Stable and prerelease APIs must never be silently mixed.

## Status

Foundation bootstrap. The repository is being built incrementally with separate research, architecture, implementation, and review stages.
