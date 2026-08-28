# Transform Skill Context Contract

A fresh implementation session must receive a self-contained context package. At minimum it must contain:

```yaml
skill_context:
  skill: fastmcp-transforms
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
    source_boundary:
    output_boundary:
    responsibilities: []
    non_responsibilities: []
    alternatives_checked: []
  transformation:
    changed_properties: []
    preserved_properties: []
    identity:
    schema:
    metadata:
    visibility:
    ordering:
    idempotency:
    state:
    lifecycle:
    concurrency:
  security:
    authorization_owner:
    exposure_risks: []
  verification:
    acceptance_criteria: []
    required_checks: []
```

The implementation agent must validate the package against current official FastMCP evidence. Missing or stale information is a hard stop, not permission to infer.
