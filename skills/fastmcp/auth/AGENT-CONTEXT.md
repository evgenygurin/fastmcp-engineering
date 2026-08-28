# Auth Agent Context Contract

```yaml
skill_context:
  skill: fastmcp-auth
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
    rfc: []
    dependency_docs: []
  authentication:
    mechanism:
    issuer:
    audience:
    validation:
    token_source:
    lifetime:
    refresh:
    revocation:
  principal:
    identity_claim:
    claims:
    scopes: []
    roles: []
  authorization:
    policy_owner:
    enforcement_point:
    default_deny:
    tenant_boundary:
  deployment:
    public_base_url:
    mcp_path:
    mount_prefix:
    discovery:
    callback:
    proxy:
  security:
    trust_boundaries: []
    secrets: []
    redaction: []
    threats: []
  verification:
    acceptance_criteria: []
    required_checks: []
```

Missing version, first-party evidence, trust boundaries, policy ownership, or token validation semantics are blocking when implementation depends on them.
