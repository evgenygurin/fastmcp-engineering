# Provider Skill Context Contract

A fresh Provider implementation session must read:

1. `AGENTS.md`;
2. `contracts/skill-contract.md`;
3. `contracts/skill-context.md`;
4. `contracts/verification-gate.md`;
5. `architecture/architecture-governor.md`;
6. `architecture/pattern-selection.md`;
7. `research/fastmcp/research-protocol.md`;
8. `skills/fastmcp/providers/SKILL.md`;
9. `research/fastmcp/providers-decision-matrix.md`;
10. the feature-specific research/evidence package.

Minimum feature context:

```yaml
skill_context:
  skill: fastmcp-providers
  target:
    fastmcp_version:
    python_version:
  requirement:
  non_goals: []
  research:
    official_docs: []
    official_examples: []
    source_tests: []
    mcp_spec: []
    dependency_docs: []
  architecture:
    responsibilities: []
    non_responsibilities: []
    application_boundary:
    native_alternatives_checked: []
  provider:
    source_of_truth:
    discovery_trigger:
    lookup:
    listing:
    filtering:
    identity:
    precedence:
    visibility:
    authorization:
    lifecycle:
    caching:
    freshness:
    invalidation:
    timeout:
    cancellation:
    concurrency:
  verification:
    acceptance_criteria: []
    required_checks: []
```

Missing or stale context is a hard stop until resolved by research.