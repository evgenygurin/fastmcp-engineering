# Transport / Deployment Agent Context Contract

Every fresh implementation session must construct this context before coding.

```yaml
skill_context:
  skill: fastmcp-transports-deployment
  target:
    fastmcp_version:
    python_version:
    asgi_server:
    framework:
  requirement:
  non_goals: []
  research:
    official_docs: []
    official_examples: []
    source_tests: []
    mcp_spec: []
    dependency_docs: []
  transport:
    selected:
    endpoint:
    session_model:
    streaming:
    cancellation:
    timeouts:
  deployment:
    topology: []
    workers:
    replicas:
    load_balancer:
    proxy:
    state_store:
  security:
    tls_boundary:
    authentication_boundary:
    trusted_proxy:
    forwarded_headers:
  lifecycle:
    startup:
    shutdown:
    inflight_requests:
    streams:
    tasks:
  verification:
    acceptance_criteria: []
    required_checks: []
```

Missing version, protocol semantics, state ownership, proxy trust, lifecycle, or scaling assumptions are blocking when implementation depends on them.