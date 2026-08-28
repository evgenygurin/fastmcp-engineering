# Providers Skill Acceptance Criteria

## Research

- [ ] Exact FastMCP version identified.
- [ ] Official Provider documentation read.
- [ ] Relevant official examples inspected.
- [ ] Relevant source/tests inspected where semantics are ambiguous.
- [ ] MCP specification checked where protocol semantics matter.
- [ ] Evidence ledger completed.

## Architecture

- [ ] Provider responsibility is component sourcing/discovery/composition.
- [ ] Repository and application-service responsibilities remain separate.
- [ ] Provider is not used as a generic service locator or DI container.
- [ ] Native FastMCP alternatives were considered.
- [ ] Dynamic visibility and authorization are explicitly designed.
- [ ] Lifecycle and concurrency semantics are explicit where relevant.

## Implementation

- [ ] Version-correct FastMCP APIs are used.
- [ ] Business logic remains behind application/domain boundaries.
- [ ] External infrastructure is accessed through approved boundaries.
- [ ] Error and cleanup behavior is explicit.

## Verification

- [ ] Provider behavior has focused tests.
- [ ] MCP/in-process integration behavior is tested where relevant.
- [ ] Failure paths are covered.
- [ ] Security/authorization behavior is covered where relevant.
- [ ] Static quality checks pass.
- [ ] Architecture re-check passes.
- [ ] Verification evidence is reproducible.