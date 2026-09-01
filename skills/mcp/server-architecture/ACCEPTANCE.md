# MCP / FastMCP Server Architecture Acceptance Criteria

## Research
- [ ] Exact FastMCP/MCP/Python versions identified.
- [ ] Relevant official `llms.txt` material read.
- [ ] Relevant official FastMCP server/tools/resources/resource-template/prompts docs read.
- [ ] Context/dependencies/lifespan/middleware docs read.
- [ ] Transport docs read.
- [ ] Auth/composition/mount/proxy docs read where applicable.
- [ ] Exact-version upgrade/migration docs checked.
- [ ] Relevant official examples inspected comprehensively.
- [ ] Relevant source/tests inspected for ambiguity.
- [ ] MCP specification checked.
- [ ] Evidence ledger completed.

## Architecture
- [ ] FastMCP is isolated at the protocol/application adapter boundary.
- [ ] Domain does not depend on FastMCP/MCP/transport types.
- [ ] Tool handlers are thin.
- [ ] Tool/resource/prompt contracts are explicit.
- [ ] Context is not leaked into domain state.
- [ ] Request/application lifetimes are explicit.
- [ ] Lifespan ownership and cleanup are explicit.
- [ ] Middleware ordering is verified.
- [ ] Transport is not embedded in business logic.
- [ ] Authn/authz boundaries are explicit.
- [ ] Mount/proxy composition has explicit ownership and security boundaries.

## Verification
- [ ] Unit/component tests pass.
- [ ] MCP protocol/client tests pass.
- [ ] Transport tests pass where transport semantics matter.
- [ ] Discovery/schema tests pass.
- [ ] Lifecycle/cancellation tests pass where applicable.
- [ ] Middleware ordering tests pass where applicable.
- [ ] Auth boundary tests pass where applicable.
- [ ] Security/observability/database regressions pass where affected.
- [ ] Architecture re-check passes.
- [ ] Stops when server architecture behavior cannot be established from evidence; rejects invented behavior and escalates to the user instead of guessing.
