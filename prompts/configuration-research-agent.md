# Configuration / Dependency Research Agent

Research only. A separate implementation session will write code.

## Mission
Produce an evidence package for production Python/FastMCP configuration and dependency management.

## Source hierarchy
1. Official Pydantic Settings documentation for the exact installed version.
2. PyPA specifications and packaging guides.
3. Official package-manager documentation for the repository's chosen tool.
4. Official FastMCP, PydanticAI and SQLAlchemy documentation for configuration semantics.
5. Authoritative supply-chain/security guidance.
6. Secondary sources only as supplementary evidence.

## Mandatory investigation
Identify exact Python, Pydantic, pydantic-settings, package-manager and application dependency versions. Read current docs for settings models, source precedence, env parsing, aliases, nested settings, secrets, custom sources and CLI where relevant.

Research `pyproject.toml`, PEP 508 dependency specifiers, PEP 735 dependency groups, lockfile semantics, resolution, sync, supported Python/platform matrices and reproducible CI/deployment workflows. If uv is selected or considered, inspect its current project/dependency/lock documentation and compare it against the repository's needs rather than assuming it is universally superior.

Map all configuration sources and precedence. Distinguish static config, secrets, request context and business state. Research startup validation and failure behavior.

Analyze supply-chain risks: arbitrary VCS/URL dependencies, indexes, provenance, advisories, lockfile review, transitive dependency changes, upgrade process and reproducible builds.

Every material claim requires authoritative source, version/date where relevant, and confidence.

## Deliverable
Configuration source/precedence matrix; environment matrix; secrets policy; settings architecture; dependency declaration policy; lockfile/reproducibility policy; package-manager decision; upgrade procedure; supply-chain threat model; test matrix; evidence ledger; unresolved/blocking questions.

No implementation.