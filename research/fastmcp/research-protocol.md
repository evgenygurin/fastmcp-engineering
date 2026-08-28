# FastMCP Research Protocol

This protocol is the execution contract for research performed before FastMCP implementation.

## Research graph

```text
Requirement
  -> FastMCP capability map
  -> official docs
  -> official source/tests
  -> official examples
  -> MCP specification
  -> dependency documentation
  -> pattern synthesis
  -> architecture decision
```

## Source ledger

Every research task maintains a source ledger:

| Source | Type | Version | What it proves | Status |
|---|---|---|---|---|
| canonical URL/path | official-docs/source/tests/example/spec | version | claim | verified/unverified |

## Evidence rules

- Documentation establishes the public contract.
- Source establishes implementation behavior, not necessarily a stable contract.
- Tests establish observed/intended behavior and edge cases.
- Examples establish usage patterns and API mechanics.
- MCP specifications establish protocol semantics.
- Secondary sources may explain operational experience but cannot override first-party evidence.

## Example analysis record

```yaml
example:
  path: examples/...
  mechanism: provider|transform|middleware|tool|resource|prompt|auth|client|other
  version: 3.x|4.x|unknown
  demonstrates: []
  assumptions: []
  omitted_production_concerns: []
  reusable_patterns: []
  anti_patterns_if_copied: []
  evidence: []
```

## Capability decision record

```yaml
capability: <name>
target_version: <version>
native_options:
  - mechanism: <FastMCP mechanism>
    responsibility: <owner>
    evidence: []
selected:
  mechanism: <choice>
  reason: <reason>
rejected:
  - option: <option>
    reason: <reason>
custom_solution_required: false
custom_solution_justification: null
```

## Research completeness gate

Before implementation, confirm:

- [ ] target version established;
- [ ] official docs mapped;
- [ ] relevant examples searched;
- [ ] source/tests inspected where semantics are non-trivial;
- [ ] protocol boundary identified;
- [ ] dependencies researched from first-party sources;
- [ ] alternatives compared;
- [ ] production omissions identified;
- [ ] security implications identified;
- [ ] test strategy identified;
- [ ] unresolved questions escalated.

## Freshness

Research artifacts are snapshots. Time-sensitive facts such as latest stable version, prereleases, deprecations, and current API availability MUST be revalidated when the skill executes.
