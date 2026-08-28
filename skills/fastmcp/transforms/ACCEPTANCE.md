# Transforms Skill Acceptance Criteria

## Research

- [ ] Exact FastMCP version identified.
- [ ] Official Transform documentation read.
- [ ] Relevant official examples inspected.
- [ ] Source/tests inspected for ambiguous semantics.
- [ ] MCP specification checked where required.
- [ ] Evidence ledger completed.

## Architecture

- [ ] Transform is genuinely an MCP component transformation/composition concern.
- [ ] Provider/Middleware/Component/application alternatives were considered.
- [ ] Source and output boundaries are explicit.
- [ ] Domain/application logic remains outside Transform.
- [ ] Authorization ownership is explicit.
- [ ] Identity/schema/metadata/visibility semantics are explicit where relevant.
- [ ] Ordering/composition semantics are explicit where relevant.

## Implementation

- [ ] Target-version FastMCP APIs are used.
- [ ] No unnecessary custom registry/pipeline framework was introduced.
- [ ] Lifecycle/concurrency behavior is safe where relevant.
- [ ] Failure behavior is explicit.

## Verification

- [ ] Focused tests pass.
- [ ] MCP/client integration behavior is tested where relevant.
- [ ] Composition/ordering is tested where relevant.
- [ ] Visibility/security behavior is tested where relevant.
- [ ] Static quality checks pass.
- [ ] Architecture re-check passes.
- [ ] Evidence is reproducible.
