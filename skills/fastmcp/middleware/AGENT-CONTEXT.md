# Middleware Agent Context Contract

Every fresh implementation session must receive or construct this package before coding.

```yaml
skill_context:
  skill: fastmcp-middleware
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
    concern:
    layer:
    downstream_boundary:
    alternatives_checked: []
  chain:
    position:
    order:
    short_circuit:
    error_flow:
    cancellation_flow:
  security:
    identity_source:
    policy_owner:
    trust_boundary:
    failure_behavior:
  runtime:
    stateful: false
    concurrency_model:
    streaming:
    tasks:
  verification:
    acceptance_criteria: []
    required_checks: []
```

Missing version, research, architecture, security, or runtime semantics are blocking when the implementation depends on them.