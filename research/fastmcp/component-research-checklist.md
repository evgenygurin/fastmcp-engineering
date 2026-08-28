# Component Research Checklist

Use this checklist before implementing or materially changing a Tool, Resource, or Prompt.

## Version

- [ ] Exact FastMCP version identified.
- [ ] Stable/prerelease status checked from official documentation.
- [ ] Example and API versions match the target version.

## Official FastMCP evidence

- [ ] Component documentation read.
- [ ] Relevant official examples inspected.
- [ ] Relevant source inspected when semantics are unclear.
- [ ] Relevant tests inspected when behavior is subtle/version-sensitive.
- [ ] Client/testing guidance checked.

## Protocol

- [ ] MCP specification/SEP checked when semantics depend on protocol behavior.
- [ ] Public input/output contract defined.
- [ ] Error semantics defined.

## Architecture

- [ ] Tool/Resource/Prompt classification justified.
- [ ] Provider/Transform/Middleware alternatives checked.
- [ ] Context/DI and lifecycle requirements checked.
- [ ] Application boundary identified.
- [ ] Domain/business rules remain outside the adapter.
- [ ] Persistence and external SDK dependencies remain outside the adapter.

## Quality

- [ ] Positive path tested.
- [ ] Validation/failure paths tested.
- [ ] Authorization tested where relevant.
- [ ] MCP-level behavior tested where relevant.
- [ ] Static quality checks run.
- [ ] Architecture re-check completed.

## Evidence

Record source URLs/paths, version, relevant API/example names, conclusions, and unresolved questions in the feature's research artifact.