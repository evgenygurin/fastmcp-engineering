# FastMCP Tasks Agent Context Contract

Every fresh implementation session must construct or receive this package before coding.

```yaml
skill_context:
  skill: fastmcp-tasks
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
  semantics:
    protocol_task:
    framework_task:
    state_machine: []
    polling:
    result_retrieval:
    cancellation:
    timeout:
    ttl:
  execution:
    owner:
    worker_boundary:
    storage:
    durability:
    restart_recovery:
    concurrency:
  reliability:
    retry_policy:
    idempotency_strategy:
    failure_model:
  security:
    creation_policy:
    status_policy:
    result_policy:
    tenant_binding:
  lifecycle:
    startup:
    shutdown:
    abandoned_work:
  verification:
    acceptance_criteria: []
    required_checks: []
```

Missing version, protocol semantics, ownership, durability, cancellation, security, or recovery semantics are blocking when the implementation depends on them.