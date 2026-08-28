# FastMCP Components

Design Tools, Resources, Resource Templates, and Prompts as thin MCP adapters over explicit application capabilities. Exact APIs are version-sensitive: research the target release first.

## Mandatory research gate
1. Read `AGENTS.md` and engineering contracts.
2. Identify exact FastMCP/Python versions.
3. Read official docs for every component type involved.
4. Inspect relevant official PrefectHQ/fastmcp examples.
5. Inspect source/tests for ambiguous identity, registration, schema, execution, and error semantics.
6. Check MCP specification/SEP material for protocol claims.
7. Check first-party dependency docs for Pydantic and directly involved libraries.
8. Record evidence before coding.

FastMCP currently documents Tools as executable capabilities, Resources as readable data, and Prompts as reusable message templates. Official docs must be rechecked for the target release.

## Component decision
- Tool: invoke an operation or cause an action.
- Resource: read addressable data.
- Resource Template: read data parameterized by a URI template.
- Prompt: provide reusable message/instruction templates.

Do not force a requirement into a component when its semantics do not fit.

## Architecture

```text
MCP client / LLM
      ↓
FastMCP component adapter
      ↓
Application port / use case
      ↓
Domain
      ↓
Infrastructure adapter
```

The adapter owns MCP-facing naming, descriptions, schemas, result shaping, Context access where required, and protocol error translation. Application/domain layers must not depend on FastMCP decorators or runtime Context merely because an MCP component invokes them.

## Tools

Define a stable semantic name, model-facing description, typed input/output contract, authorization boundary, side effects/idempotency, and error semantics. Do not expose internal CRUD methods one-to-one unless that is genuinely the desired agent capability. Avoid giant tools containing unrelated workflows.

## Resources

Resources are readable data capabilities, not disguised actions. Define stable URIs and explicit template semantics. Hidden mutations are prohibited unless deliberately justified. Verify binary content, MIME types, structured content, cache hints, and resource-template APIs for the target version.

## Prompts

Prompts are reusable message templates. Keep business operations and data access outside them unless explicitly part of the verified contract. Arguments require clear descriptions and deterministic serialization.

## Schema / Pydantic

FastMCP derives schemas from Python signatures and validates boundary inputs/outputs. Use Pydantic for complex/reusable boundary contracts and ordinary annotations for simple contracts. Treat required fields, defaults, enums, output shapes and descriptions as compatibility-sensitive API changes. Never expose ORM entities, DB sessions, secrets, or infrastructure structures accidentally.

## Identity / registration

Determine canonical component identity for the target version. When composing Providers, Transforms, mounts, or programmatic registration, verify collision, deduplication, precedence, and visibility semantics from first-party evidence. FastMCP repository guidance identifies `FastMCPComponent.key` as the canonical identity surface; verify exact target-version behavior before relying on it.

## Errors

Distinguish invalid input, authentication/authorization failure, expected application/domain rejection, transient infrastructure failure, and unexpected programmer failure. Do not swallow exceptions merely to return friendly strings or leak internal details.

## Context / DI

Use FastMCP Context only for verified MCP runtime capabilities. Dependencies belong in explicit DI/application boundaries. Never use Context as a service locator.

## Security

For every component document who may discover/read/invoke it, tenant/user scope, returned data, side effects, and capability disclosure through names/descriptions/schemas. Authorization must be enforced at the security/application boundary, not delegated to the LLM.

## Composition

When components come from Providers, Transforms, mounts, or programmatic registration, verify ordering, identity, deduplication, visibility, and override behavior. Choose decorator or imperative registration based on the target architecture and verified version semantics.

## Testing

Use `fastmcp.Client` / in-process testing where appropriate. Test discovery, schemas, success/error paths, authorization, malformed input, URI/template behavior, prompt rendering, identity/collision behavior, and cancellation/timeouts where applicable.

## Reject

Reject thin database dumps, domain logic coupled to decorators, public schemas exposing persistence models, LLM-only authorization, guessed identity semantics, and implementations not verified against the target FastMCP version.

## Deliverables

Research package, component decision record, public MCP contract, application boundary map, implementation, Client/in-process tests, security/error verification, architecture re-check, evidence ledger.