# Lifespan Agent Context Contract

Every fresh implementation session must receive or construct this package before coding.

```yaml
skill_context:
  skill: fastmcp-lifespan
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
  resources:
    - name:
      owner:
      scope:
      created_by:
      consumers: []
      prerequisites: []
      startup:
      shutdown:
      cleanup:
      shareable:
      concurrency:
  lifecycle:
    startup_order: []
    shutdown_order: []
    partial_failure:
    cancellation:
    composition:
    http_mounting:
  context_di:
    exposure:
    application_boundary:
  background_work:
    tasks: []
    cancellation:
    drain:
  verification:
    acceptance_criteria: []
    required_checks: []
```

Missing version, resource ownership, lifecycle ordering, cleanup, scope, concurrency, or security semantics are blocking when implementation depends on them.