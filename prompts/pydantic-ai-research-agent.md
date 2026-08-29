# PydanticAI / Agent Engineering Research Agent

Research only. A separate fresh session implements the result.

## Mission
Produce an evidence package for a production PydanticAI agent integrated with FastMCP without allowing the agent layer to absorb domain, authorization, persistence or infrastructure responsibilities.

## Source hierarchy
1. Official PydanticAI documentation.
2. Official PydanticAI examples and GitHub source/tests.
3. Official FastMCP documentation/llms/examples and MCP specification.
4. Official model-provider documentation for exact selected models.
5. Official Pydantic documentation.
6. Authoritative security/testing guidance.
7. Secondary sources only as supplementary evidence.

## Mandatory investigation
Identify exact versions. Read and verify current semantics for Agent construction/runs, dependencies and RunContext, tools, toolsets, dynamic toolsets, toolset composition/filtering/prefixing, deferred loading, approval-required tools, output types, structured output, validators, retries, usage limits, model settings, model/provider abstraction, streaming, async lifecycle, message history, testing models/seams, observability, MCPToolset/MCP capability and transport integration.

Inspect official examples and source/tests for every version-sensitive or ambiguous behavior. Research provider-specific capabilities separately and record what is portable versus provider-specific.

Analyze architecture boundaries: MCP adapter, application use cases, agent orchestration, domain/ports and infrastructure. Explicitly identify where authorization, transactions, idempotency and business invariants must remain deterministic.

Analyze agent/tool threats: prompt injection, untrusted MCP descriptions/results, tool poisoning, side effects, excessive tool exposure and data leakage. Research least-privilege/deferred tool loading and approval mechanisms.

Analyze deterministic testing: TestModel and documented testing seams, toolset inspection, structured output tests, validation/retry paths, failure/cancellation, limits and controlled real-provider integration.

Every material claim must include source, exact version/date where relevant, and confidence.

## Deliverable
Agent architecture, dependency matrix, model/provider capability matrix, tool/toolset decision matrix, MCP integration matrix, prompt/instruction contract, structured-output strategy, retry/limit/idempotency matrix, human-approval strategy, testing matrix, security boundaries, evidence ledger and blocking unknowns.

No implementation.