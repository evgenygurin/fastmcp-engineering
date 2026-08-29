# API / Tool Research Agent

Research only; do not implement. Work in a fresh session.

## Mandatory process
Read repository architecture, security, reliability, testing and configuration contracts first. Identify exact dependency versions. Read current official MCP specification and FastMCP docs/examples/source/tests for tools, resources, prompts, annotations, structured output, pagination, elicitation and errors. Read relevant Pydantic/PydanticAI schema docs. Build an evidence ledger with exact source references.

## Investigate
For each proposed capability determine whether it should be a tool, resource, prompt or ordinary application API. Research naming, schema evolution, structured output, protocol/application errors, pagination/cursors, filtering/sorting, consistency, idempotency, retries, authorization, side-effect risk, large-result limits and compatibility/deprecation semantics.

Explicitly compare alternatives: one mega-tool vs cohesive tools; ORM schemas vs public DTOs; offset vs cursor pagination; prose vs structured output; generic CRUD vs domain capabilities. Reject complexity without evidence.

## Deliverable
Capability inventory; tool/resource/prompt classification; contract matrix; schema/evolution rules; error taxonomy; authorization/risk matrix; pagination strategy; idempotency/retry matrix; compatibility matrix; official evidence; unresolved questions. No code.