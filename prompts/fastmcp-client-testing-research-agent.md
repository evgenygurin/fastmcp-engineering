# FastMCP Client / Testing Research Agent

Research only. A separate session implements the result.

## Source hierarchy

1. Official FastMCP documentation / llms material.
2. Official PrefectHQ/fastmcp examples.
3. FastMCP source and tests.
4. MCP specification/SEP material.
5. First-party dependency documentation.
6. Secondary sources only as supplementary evidence.

## Required investigation

- Identify exact FastMCP/Python versions.
- Exhaustively inspect official Client documentation and examples.
- Determine exact Client APIs, session lifecycle, initialization, context manager semantics, transport selection, and error behavior.
- Investigate in-process, stdio, Streamable HTTP and deployed HTTP testing semantics.
- Determine how Tools, Resources, Prompts, templates, structured output, metadata, pagination, progress, cancellation, tasks, subscriptions and streaming are tested.
- Investigate authentication and authorization through the MCP boundary.
- Inspect source/tests for lifecycle, concurrency, cleanup and session behavior.
- Determine fixture and dependency-override patterns.
- Identify deterministic testing strategies and anti-flake practices.
- Compare unit, component, MCP integration, transport integration, security and E2E tests.
- Identify which guarantees cannot be proven by in-process tests.

## Evidence discipline

For every material claim record source, version, API/path and confidence. Distinguish official docs, examples, source, tests, specification, first-party dependency and secondary evidence.

## Deliverable

Produce:

- version matrix;
- Client API matrix;
- transport matrix;
- official examples catalog;
- MCP contract test matrix;
- auth/security test matrix;
- lifecycle/concurrency test matrix;
- fixture/isolation strategy;
- flaky-test hazards;
- property/fuzz candidates;
- anti-patterns;
- evidence ledger;
- unresolved questions.

Do not implement application code.