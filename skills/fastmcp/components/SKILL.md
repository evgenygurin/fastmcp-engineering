---
name: fastmcp-components
description: Design and implement FastMCP Tools, Resources, and Prompts as thin MCP delivery adapters after evidence-first research, architecture review, and public-contract design.
---

# FastMCP Components

## Mission

Design MCP-facing Tools, Resources, and Prompts without leaking business logic, persistence, or external integration concerns into the protocol adapter.

## Mandatory prerequisites

Before implementation:

1. Read `AGENTS.md`.
2. Read the applicable skill and verification contracts.
3. Read the Architecture Governor and Pattern Selection artifacts.
4. Build a Skill Context Package for the target feature.
5. Identify the exact FastMCP version.
6. Read the relevant official FastMCP documentation.
7. Inspect relevant official examples.
8. Inspect source/tests when API semantics are ambiguous or version-sensitive.
9. Check MCP specification/SEP material when protocol semantics are involved.

Do not proceed on remembered FastMCP APIs.

## Procedure

### 1. Classify the capability

Determine whether the requirement is primarily:

- an executable operation → Tool;
- addressable/read-oriented contextual data → Resource;
- reusable prompt/instruction content → Prompt;
- cross-cutting behavior → Middleware;
- component discovery/composition → Provider;
- systematic component transformation → Transform.

Do not choose Tool by default.

### 2. Define the public contract

Specify inputs, outputs, errors, authorization semantics, side effects, idempotency, pagination/freshness where relevant, and observable behavior.

Treat MCP schema as an external contract. Do not expose persistence or domain models merely because their schemas are convenient.

### 3. Locate application boundary

Map the component to an application use case or explicitly justified boundary. Keep business rules outside the MCP adapter.

### 4. Implement the thinnest adapter

The component should primarily:

```text
MCP input
   ↓
MCP adapter
   ↓
Application boundary
   ↓
MCP result/error mapping
```

Use FastMCP-native Context/DI, auth, middleware, providers, transforms, and lifecycle mechanisms when appropriate instead of inventing equivalent infrastructure.

### 5. Verify

At minimum, verify:

- registration/discovery;
- input/output schema;
- success behavior;
- validation failures;
- authorization behavior;
- application failure mapping;
- relevant integration behavior through the documented FastMCP Client/testing seam;
- architecture boundaries;
- static quality.

Add regression coverage for defects.

## Rejection criteria

Reject the implementation if:

- the component contains business invariants;
- the component queries persistence directly without an approved architectural exception;
- the component constructs concrete external SDK clients;
- a Resource is being used as generic RPC;
- a Prompt is being used to enforce authorization;
- public MCP contracts accidentally expose internal ORM/domain objects;
- a native FastMCP mechanism would solve the problem more appropriately and no justification exists for a custom mechanism;
- required official research has not been performed.

## Deliverables

- component decision record;
- MCP contract;
- implementation;
- focused tests;
- integration/MCP tests where applicable;
- verification evidence;
- architecture decision updates if boundaries changed.
