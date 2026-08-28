# Context / DI Agent Context Contract

Every fresh implementation session must receive or construct this package before coding.

```yaml
skill_context:
  skill: fastmcp-context-di
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
  boundaries:
    mcp_runtime_context: []
    application_ports: []
    domain_dependencies: []
    infrastructure: []
  dependencies:
    graph: []
    scopes: []
    factories: []
    overrides: []
  lifecycle:
    owner:
    startup:
    shutdown:
    cleanup:
  runtime:
    concurrency_model:
    mutable_state: []
  security:
    identity_source:
    authorization_owner:
    trust_boundary:
  verification:
    acceptance_criteria: []
    required_checks: []
```

Missing version, research, scope, lifecycle, security, or concurrency semantics are blocking when implementation depends on them.