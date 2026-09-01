---
name: configuration-environment-engineering
description: Evidence-first typed configuration and environment engineering for production FastMCP systems.
---

# Configuration / Environment Engineering

## Mission
Make configuration explicit, typed, validated, environment-aware and safe. Configuration errors must fail early rather than becoming runtime business failures.

## Trigger / Когда применять

**Scope / When to use:** typed configuration and environment engineering for production FastMCP systems.
**Trigger:** designing or changing configuration models, environment separation, secrets handling, startup validation, operational limits, or feature flags.
**Upstream / Prerequisite:** identified exact versions of Python, FastMCP, Pydantic and pydantic-settings plus deployment/runtime dependencies; evidence recorded.
**Mission / Goal:** make configuration explicit, typed, validated, environment-aware and safe; configuration errors must fail early rather than becoming runtime business failures.
**Research / Evidence:** identify exact versions; read current official documentation for Pydantic Settings and relevant FastMCP configuration/lifespan/CLI/server deployment APIs, then exact-version examples/source/tests; record evidence and re-check version-sensitive behavior before completion.
**Decision / Selection rules:** keep a configuration boundary separate from secrets, runtime state and domain data; use typed Pydantic Settings at the application boundary with documented and tested precedence; treat secrets as not ordinary configuration; validate configuration before accepting MCP traffic; treat resolved configuration as immutable; use native FastMCP configuration mechanisms; centralize operational limits; give feature flags a lifecycle.
**Version / Compatibility:** identify exact versions of Python, FastMCP, Pydantic and pydantic-settings; the exact precedence behavior must come from the installed library version, never from memory.

## Deliverables

**Deliverables / Artifacts:** configuration schema/catalog; source-precedence matrix; environment matrix; secret boundary; startup validation rules; operational limits catalog; feature-flag policy; deployment mapping; test matrix; evidence ledger; rejected alternatives; verification report.
**Verification / Testing:** test required settings, defaults, precedence, malformed values, cross-field constraints, secret loading/redaction, environment isolation, production safety checks and feature-flag behavior; test configuration startup failure before MCP traffic is served; verify configuration snapshots contain no secrets.
**Failure / Stop conditions:** reject scattered environment reads, untyped config dictionaries, secret leakage, undocumented precedence, insecure production defaults, mutable global settings, configuration-dependent domain logic, and runtime acceptance of invalid configuration.
**Positive scenario:** configuration is validated before MCP traffic and a missing or invalid production secret fails fast at startup.
**Negative scenario:** scattered environment reads and untyped configuration allow invalid configuration to be accepted at runtime.

## Mandatory research
Identify exact versions of Python, FastMCP, Pydantic and pydantic-settings plus deployment/runtime dependencies. Read current official documentation for Pydantic Settings and relevant FastMCP configuration/lifespan/CLI/server deployment APIs, then exact-version examples/source/tests. Record evidence and re-check version-sensitive behavior before completion.

## Configuration boundary
Separate configuration from secrets, runtime state and domain data. Define one typed configuration model per coherent concern and a clear composition root. Do not read `os.environ` throughout application code. Do not make domain services environment-aware.

## Pydantic Settings
Use typed Pydantic Settings at the application boundary. Define required vs optional values explicitly, defaults intentionally, validation constraints, nested settings where justified, and source precedence. Unknown configuration should be rejected where safe to detect deployment mistakes. Avoid dynamic `Any` configuration bags.

## Precedence
Document and test the actual precedence chain for every environment. Typical sources may include constructor/runtime values, environment variables, dotenv files, secrets files and CLI configuration, but the exact behavior must come from the installed library version. Never assume precedence from memory.

## Secrets
Secrets are not ordinary configuration. Keep secret material out of logs, traces, error messages, generated config dumps and source control. Prefer a dedicated secret provider/runtime injection mechanism. If Pydantic Settings loads secrets, document the exact source and permissions. Do not silently provide insecure production defaults.

## Environment separation
Define development/test/staging/production behavior explicitly. Avoid branching business logic on arbitrary environment strings. Prefer injected policies/capabilities where behavior genuinely differs. Test production-like configuration independently from developer conveniences.

## Startup validation
Validate configuration before accepting MCP traffic. Fail fast on invalid URLs, credentials, mutually exclusive options, impossible timeouts, insecure production combinations and missing required dependencies. Cross-field validation belongs in configuration/application validation, not scattered handlers.

## Runtime immutability
Treat resolved configuration as immutable during normal runtime. Configuration reload/hot reload is an explicit feature requiring concurrency, lifecycle and consistency analysis; never introduce it accidentally through mutable globals.

## FastMCP integration
Use native FastMCP configuration, CLI, lifespan, middleware or deployment mechanisms when appropriate and verified for the installed version. Keep server construction/composition in the composition root. Do not couple domain code to FastMCP settings objects.

## Timeouts / limits
Centralize operational limits: request deadlines, HTTP timeouts, DB pool limits, queue sizes, payload sizes, pagination limits, concurrency and rate limits. Use typed units and bounded values. Avoid magic numbers scattered through handlers.

## Feature flags
Feature flags are configuration with lifecycle. Define owner, default, rollout scope, expiration/removal criteria and safe fallback. Do not accumulate permanent flags. Security-sensitive flags must fail closed.

## Configuration drift
Document canonical configuration and deployment mapping. Detect missing/unknown/changed configuration where practical. Do not allow local `.env` behavior to become an undocumented production dependency. Keep example configuration non-secret and complete enough for validation.

## Testing
Test required settings, defaults, precedence, malformed values, cross-field constraints, secret loading/redaction, environment isolation, production safety checks and feature-flag behavior. Test configuration startup failure before MCP traffic is served. Verify configuration snapshots contain no secrets.

## Architecture
Composition root → typed settings → application dependencies → use cases → domain/infrastructure. Configuration should flow inward through dependency injection; services should not reach outward to process environment state.

