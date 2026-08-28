# FastMCP Client / Testing Agent Context Contract

Every fresh implementation session must construct or receive this package before coding.

```yaml
skill_context:
  skill: fastmcp-client-testing
  target:
    fastmcp_version:
    python_version:
  requirement:
  risk_level:
  research:
    official_docs: []
    official_examples: []
    source_tests: []
    mcp_spec: []
    dependency_docs: []
  verification:
    lowest_sufficient_layer:
    required_higher_layers: []
    protocol_contracts: []
    transports: []
  fixtures:
    ownership:
    isolation:
    cleanup:
    synchronization:
  security:
    authentication:
    authorization:
    tenant_isolation:
  runtime:
    lifecycle:
    cancellation:
    concurrency:
    tasks:
    streaming:
```

Missing version, protocol evidence, transport assumptions, fixture ownership, or security semantics are blocking when the implementation depends on them.