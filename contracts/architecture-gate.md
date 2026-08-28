# Architecture Gate

Implementation must not begin until this gate has a written answer.

## Required checks

- [ ] Responsibilities are identified.
- [ ] Domain/application/infrastructure/MCP boundaries are explicit.
- [ ] Dependency direction is valid.
- [ ] Public MCP contracts are separated from persistence models unless reuse is deliberately justified.
- [ ] MCP handlers are thin and delegate behavior.
- [ ] Providers, Transforms, Middleware, Context, Lifespans, tasks, auth, and Client were considered where relevant.
- [ ] Every custom abstraction has a documented reason.
- [ ] No unnecessary pattern or framework coupling was introduced.
- [ ] Failure modes and transactional boundaries are identified.
- [ ] Security boundaries are explicit.
- [ ] Test seams are explicit.

## Required output

```yaml
architecture_gate:
  status: approved|rejected|needs_revision
  layers: []
  dependencies: []
  responsibilities: []
  native_fastmcp_mechanisms_considered: []
  abstractions_justified: []
  rejected_abstractions: []
  risks: []
  tests_required: []
```
