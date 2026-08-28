---
name: fastmcp-transports-deployment
description: Engineer FastMCP transport and production deployment boundaries with version-specific evidence, explicit session/state semantics, ASGI integration, security, graceful shutdown, scaling, and observability.
---

# FastMCP Transports / Deployment

## Mission

Design the MCP transport and deployment topology as an explicit infrastructure boundary. Never infer transport semantics from a local development setup.

## Mandatory research gate

Before implementation:

1. Read `AGENTS.md` and all engineering contracts.
2. Identify exact FastMCP, Python, ASGI server, and relevant framework versions.
3. Read official FastMCP transport/deployment documentation and llms material.
4. Inspect all relevant official PrefectHQ/fastmcp examples.
5. Inspect FastMCP source/tests for ambiguous transport/session behavior.
6. Check MCP specification/SEP material for protocol semantics.
7. Check first-party ASGI/server dependency documentation.
8. Record evidence before changing code.

Never rely on remembered transport names, endpoints, headers, session behavior, or deployment assumptions.

## Transport decision matrix

Explicitly evaluate the target's supported transports and compatibility behavior, including stdio, Streamable HTTP, and any legacy/compatibility transport documented for the exact version.

For each chosen transport document:

- protocol semantics;
- endpoint/path;
- initialization/session behavior;
- statefulness/statelessness;
- connection lifetime;
- streaming behavior;
- request correlation;
- authentication boundary;
- proxy/load-balancer requirements;
- timeout/cancellation behavior;
- observability;
- failure behavior.

## ASGI integration

When embedding FastMCP in an ASGI application, verify the exact mounting/lifespan integration for the target version. Treat path prefixes, routing, middleware ordering, forwarded headers, and startup/shutdown ownership as correctness concerns.

Do not independently invent MCP HTTP routes when the framework provides a native verified integration.

## Stateful vs stateless deployment

Make state explicit:

```text
             MCP client
                 |
          load balancer/proxy
                 |
       +---------+---------+
       |                   |
    worker A            worker B
       |                   |
       +------ shared -----+
              state?
```

If sessions or task state are process-local, analyze whether sticky routing or external state is required. Never assume multiple workers can safely share an in-memory session store.

## Production topology

Evaluate:

- TLS termination;
- reverse proxy behavior;
- idle/read/write timeouts;
- request body/response limits;
- streaming/proxy buffering;
- connection limits;
- worker model;
- horizontal scaling;
- health/readiness checks;
- graceful shutdown;
- rolling deploy behavior;
- externalized state;
- secret management;
- structured logs, metrics and tracing.

Every production assumption must be backed by target-version documentation or a documented infrastructure contract.

## Security

Separate:

- transport security (TLS/network boundary);
- authentication;
- authorization;
- proxy trust / forwarded headers;
- origin/host validation where applicable;
- secret/token handling;
- tenant isolation.

Never treat a reverse proxy's identity headers as trustworthy without an explicit trusted-proxy boundary.

## Graceful shutdown

Map the complete shutdown path:

```text
SIGTERM
  ↓
ASGI/server shutdown
  ↓
FastMCP lifecycle
  ↓
middleware/tasks/sessions
  ↓
external resources
```

Determine what happens to in-flight requests, streams, background tasks, sessions and resource cleanup. Verify rather than assume.

## Testing

Verify at multiple levels:

- in-process protocol behavior;
- stdio where applicable;
- real Streamable HTTP endpoint;
- ASGI mounting/path prefix;
- authentication;
- proxy headers where applicable;
- session/state behavior;
- cancellation/timeouts;
- streaming;
- multi-worker/scaling assumptions;
- graceful shutdown;
- health/readiness;
- failure injection.

## Rejection criteria

Reject if transport behavior is implemented from memory, if state ownership is undefined, if proxy trust is implicit, if ASGI lifespan ownership is ambiguous, if scaling assumptions rely on process-local mutable state without justification, or if production timeout/shutdown behavior is unspecified.

## Deliverables

- version-specific transport research package;
- transport decision matrix;
- deployment topology;
- state/session ownership map;
- security boundary map;
- shutdown sequence;
- implementation;
- integration/production tests;
- reproducible verification evidence;
- architecture re-check.
