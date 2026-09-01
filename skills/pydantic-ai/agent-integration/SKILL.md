---
name: pydantic-ai-agent-integration
description: Engineer PydanticAI agents behind explicit application boundaries and integrate them with FastMCP without leaking agent state, prompts, model concerns, or provider details into domain logic.
---

# PydanticAI / Agent Integration

## Mission

Treat an LLM agent as an application/infrastructure capability, not as the domain model and not as the MCP server itself. Keep protocol, orchestration, domain, persistence and model-provider concerns independently testable.

## Trigger / Когда применять

**Scope / When to use:** PydanticAI agents behind explicit application boundaries integrated with FastMCP without leaking agent state, prompts, model concerns, or provider details into domain logic.
**Trigger:** integrating a PydanticAI agent with FastMCP, designing agent tools, structured output, model/provider boundaries, or agent reliability.
**Upstream / Prerequisite:** `AGENTS.md` and repository engineering contracts read; identified exact versions; evidence recorded before coding.
**Mission / Goal:** treat an LLM agent as an application/infrastructure capability, not the domain model and not the MCP server itself; keep protocol, orchestration, domain, persistence and model-provider concerns independently testable.
**Research / Evidence:** read official PydanticAI documentation for the requested features; read official FastMCP documentation and llms material relevant to MCP integration; inspect all relevant official examples from PydanticAI and FastMCP; inspect source/tests for ambiguous agent/tool/MCP behavior; check MCP specification semantics for protocol-facing behavior.
**Decision / Selection rules:** do not make the Agent object a global service locator, repository, domain service, or MCP protocol adapter; prefer typed dependency injection over globals; do not conflate an MCP tool with an internal application service; validate model output before it reaches domain/application logic; keep tool authorization deterministic and independent of model intent; isolate provider/model configuration and make model selection explicit; define timeout, retry, fallback, usage, idempotency, cancellation, concurrency and recovery policy with retries safe for the complete operation.
**Version / Compatibility:** identify exact Python, PydanticAI, Pydantic, FastMCP, model/provider SDK and relevant dependency versions.

## Deliverables

**Deliverables / Artifacts:** research package, agent/application boundary, dependency map, tool security matrix, model/provider strategy, reliability policy, implementation, deterministic tests, MCP integration tests, observability checks, architecture re-check and evidence ledger.
**Verification / Testing:** use deterministic/fake model seams for unit tests; test dependency injection, output validation, tool authorization, malformed outputs, tool failures, retries, usage limits, cancellation, prompt-injection fixtures, and end-to-end FastMCP protocol behavior; do not make normal CI depend on a live paid model.
**Failure / Stop conditions:** reject if the agent owns business logic that belongs to domain/application layers, global mutable agent state leaks across requests, tool authorization depends on model output, provider SDK types leak through public layers, structured output is unvalidated, or live LLM calls are required for deterministic unit tests.
**Positive scenario:** a PydanticAI agent is integrated behind an application boundary and passes deterministic tests without a live model.
**Negative scenario:** an agent owns business logic that belongs to domain/application layers or tool authorization depends on model output.

## Mandatory research gate

Before implementation:
1. Read AGENTS.md and repository engineering contracts.
2. Identify exact Python, PydanticAI, Pydantic, FastMCP, model/provider SDK and relevant dependency versions.
3. Read official PydanticAI documentation for the requested features.
4. Read official FastMCP documentation and llms material relevant to MCP integration.
5. Inspect all relevant official examples from PydanticAI and FastMCP.
6. Inspect source/tests for ambiguous agent/tool/MCP behavior.
7. Check MCP specification semantics for protocol-facing behavior.
8. Record evidence before coding.

## Architecture

```text
FastMCP
   ↓
MCP adapter / Tool boundary
   ↓
Application use case
   ↓
Agent orchestration port
   ↓
PydanticAI Agent
   ├── typed dependencies
   ├── model/provider
   ├── tools
   ├── output schema
   ├── validators
   ├── usage limits
   └── retries
   ↓
Domain/application services
   ↓
Infrastructure
```

Do not make the Agent object a global service locator, repository, domain service, or MCP protocol adapter.

## PydanticAI

Verify exact-version semantics for:
- Agent;
- typed dependencies and RunContext;
- output/result types;
- output validators;
- tools and tool dependencies;
- model/provider configuration;
- model settings;
- retries;
- usage limits;
- messages/history;
- streaming;
- deferred tools / approvals where applicable;
- durable execution where applicable;
- instrumentation/evals where applicable.

Prefer typed dependency injection over globals. Keep dependency objects explicit, minimal and scoped to a run/use case.

## MCP integration

Determine whether MCP is used as:
- the server-facing protocol boundary;
- a source of agent tools/resources;
- an outbound client integration;
- or multiple roles.

Do not conflate an MCP tool with an internal application service. Adapt external MCP tools into an explicit application capability boundary.

## Structured output

Use a typed result contract. Validate model output before it reaches domain/application logic. Distinguish output validation from authorization and business invariants. Domain invariants must still be enforced by domain/application code.

## Tool safety

Treat tool descriptions, tool results and external MCP content as untrusted input. Design against prompt injection and indirect instruction attacks. Tool authorization must be deterministic and independent of model intent. Never let the model choose credentials, tenant identity, authorization policy, or unrestricted resource access.

## Model/provider boundary

Do not couple application code to one provider's SDK. Isolate provider/model configuration and make model selection explicit. Secrets belong in infrastructure configuration, never prompts, schemas or source code.

## Reliability

Define:
- timeout;
- retry policy;
- model/provider fallback if applicable;
- usage/token limits;
- idempotency;
- cancellation;
- concurrency limits;
- partial/failed tool execution;
- deterministic recovery behavior.

Retries must be safe for the complete operation, including side-effecting tools.

## Observability

Instrument runs without logging secrets or sensitive prompt/tool data. Correlate MCP request, application use case and agent run. Capture latency, outcome, token/usage information and tool-call failures where supported and appropriate.

## Testing

Use deterministic/fake model seams for unit tests. Test dependency injection, output validation, tool authorization, malformed outputs, tool failures, retries, usage limits, cancellation, prompt-injection fixtures, and end-to-end FastMCP protocol behavior. Do not make normal CI depend on a live paid model.
