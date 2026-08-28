# Component Skill Context Package

A new implementation session for the components skill must receive or construct this minimum context package before code changes.

```yaml
skill_context:
  skill: fastmcp-components
  target:
    fastmcp_version: <exact version/range>
    python_version: <version>
  requirement: <feature requirement>
  non_goals: []
  research:
    official_docs: []
    official_examples: []
    source_tests: []
    mcp_spec: []
    dependency_docs: []
  architecture:
    layer_map: []
    application_boundary: <use case/port>
    native_mechanisms_checked: []
  contract:
    component_type: <tool/resource/prompt>
    input: <schema>
    output: <schema>
    errors: []
    auth: <requirements>
    side_effects: []
  verification:
    required_checks: []
    acceptance_criteria: []
```

The implementation agent must validate this package against current official evidence. A stale or incomplete package is not sufficient authorization to implement.