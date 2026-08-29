---
name: pydantic-ai-agent-engineering
description: Evidence-first engineering of production PydanticAI agents integrated with FastMCP, layered application architecture, deterministic tools, structured outputs, MCP toolsets, dependencies, model providers, retries, limits, streaming and human approval.
---

# PydanticAI / Agent Engineering

## Mission

Treat the LLM as a probabilistic component behind explicit application boundaries. Agent orchestration must not become the domain, authorization, persistence, or infrastructure layer.

## Mandatory research gate

Before implementation:
1. Read AGENTS.md and repository architecture/security/testing contracts.
2. Identify exact Python, PydanticAI, Pydantic, FastMCP/MCP and model-provider versions.
3. Read official PydanticAI documentation for Agent, run context/dependencies, tools/toolsets, output types, model/provider abstraction, retries, usage limits, streaming, message history, testing and MCP integration.
4. Read official PydanticAI examples and source/tests for version-sensitive semantics.
5. Read official FastMCP/MCP documentation and examples for the server/client boundary.
6. Read provider documentation for the selected model features and constraints.
7. Inspect repository architecture before deciding where agent code belongs.
8. Record an evidence ledger and unresolved questions.

Do not rely on memory for current PydanticAI APIs or provider semantics.

## Layered architecture

```text
MCP Adapter / API
       ↓
Application Use Case
       ↓
Agent Orchestrator ────── Model Provider
       │
       ├── typed dependencies
       ├── deterministic application tools
       ├── MCP toolsets
       └── structured output
       ↓
Domain / Ports
       ↓
Infrastructure
```

Agent code may orchestrate probabilistic reasoning, tool selection and structured output. Domain invariants, authorization, transaction ownership and security policy remain deterministic application/domain responsibilities.

## Dependencies

Use typed `deps_type` / run context for services and request-scoped state. Dependencies must be explicit and testable. Do not use global mutable state or turn run context into a service locator/god object.

## Tools and toolsets

Choose the smallest appropriate abstraction. Use function tools for local deterministic capabilities; toolsets for reusable/composable collections; MCP toolsets for MCP servers. Verify tool definitions, argument schemas, return schemas, lifecycle and error semantics. Use filtering, prefixing, metadata, deferred loading or approval mechanisms only when their current documented semantics justify them.

Security-sensitive authorization is never delegated to the model. Validate arguments structurally and enforce authorization in deterministic application/policy layers.

## MCP integration

Treat MCP tool descriptions and tool results as untrusted external content. Verify the exact PydanticAI MCP integration API and transport behavior against current official documentation. Avoid coupling domain logic to MCP-specific classes.

For large toolsets, evaluate documented deferred-loading/discovery mechanisms rather than automatically exposing every tool to every run. Tool availability should follow least-privilege policy.

## Instructions / prompts

Separate stable agent instructions from dynamic request context and toolset-specific instructions. Keep prompts versioned and reviewable. Do not encode business authorization solely in natural language. Avoid duplicating policy across system instructions and application code.

## Structured output

Use explicit Pydantic output models when a downstream application contract exists. Validate output before application use. Define retry behavior for validation failures and distinguish model failure from business rejection. Keep schema evolution backward-compatible where required.

## Model/provider abstraction

Do not leak provider-specific model types through domain/application interfaces unless provider-specific behavior is intentionally part of the boundary. Verify model capabilities, structured-output support, tool calling, streaming, usage accounting and retry behavior for the exact provider/model.

## Retries and limits

Bound retries, model calls, tool calls, tokens and execution time. Distinguish retryable infrastructure/model failures from deterministic validation/business failures. Ensure retries do not duplicate side effects; require idempotency or approval for non-idempotent operations.

## Human-in-the-loop

Use explicit approval/deferred-tool mechanisms for consequential operations when required. Approval is a policy boundary, not a prompt instruction. Persist enough state to resume safely and prevent replay/duplicate side effects.

## Streaming / async

Use streaming only where it provides a real product or infrastructure benefit. Define cancellation and cleanup semantics. Preserve request-scoped dependencies and avoid sharing mutable agent/run state across concurrent tasks unless documented safe.

## Context and history

Treat message history as data with lifecycle, size and privacy controls. Define what is persisted, summarized, redacted and discarded. Never place secrets or unrestricted authorization state in model-visible history.

## Observability

Instrument agent runs, model calls and tool calls with correlation IDs, latency, usage and outcome metadata while redacting prompts, credentials, PII and sensitive tool payloads according to the observability/security contracts.

## Testing

Use deterministic PydanticAI test models or documented test seams for normal CI. Test tool selection, arguments, structured outputs, validation retries, limits, failures, dependencies, MCP toolset composition and approval flows without requiring live providers. Use separate controlled integration tests for real providers.

## Rejection criteria

Reject if an agent owns domain invariants/authorization/transactions, dependencies are hidden globals, live LLMs are required for deterministic CI, model output is trusted without validation, retries can duplicate side effects, unbounded tools are exposed, provider-specific details leak across stable boundaries without justification, or version-sensitive behavior was not checked against official sources.

## Deliverables

Agent architecture, dependency contract, model/provider matrix, tool/toolset policy, MCP integration design, prompt/instruction contract, output schemas, retry/limit policy, approval strategy, testing strategy, implementation, verification report and residual-risk register.