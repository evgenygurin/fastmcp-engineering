# Skill Dependency Graph

Skills are independent execution units connected by explicit artifacts, not by conversation history.

## Core pipeline

```text
Research Foundation
       ↓
Architecture Governor
       ↓
Pattern Selection
       ↓
Skill Context Package
       ↓
Specialized Skill
       ↓
Verification
       ↓
Downstream Context Package
```

## Dependency rules

1. A downstream skill may depend only on declared upstream artifacts.
2. A skill must not require an upstream agent session to remain available.
3. Circular skill dependencies are forbidden.
4. A dependency must identify an artifact path, schema/version, and freshness rule.
5. A skill may consume research artifacts but must revalidate them when the target library/version changes.
6. Specialized skills must not redefine foundation contracts.
7. If two skills require the same knowledge, extract a shared research artifact or contract rather than duplicating authoritative rules.

## Context package lifecycle

```text
CREATE
  ↓
VALIDATE
  ↓
EXECUTE
  ↓
VERIFY
  ↓
PUBLISH
  ↓
CONSUME
```

## Failure behavior

If a required artifact is absent, stale, incompatible, or internally contradictory, the skill must stop and report the dependency failure. It must not infer missing architecture from memory.

## Parallelism

Independent research streams may run in parallel when they do not mutate shared artifacts. Architecture decisions remain a synchronization point. Implementation may start only after its declared gates pass.

## FastMCP-specific dependency note

FastMCP evolves rapidly. Current official documentation describes components, providers, transforms, middleware, authentication, composition, and lifecycle as server-level capabilities; these capabilities must be considered by specialized skills before custom abstractions are proposed. citeturn0search1turn0search6

## Skill package identity

Each skill must have a stable identifier and schema version. A package update that changes behavior, acceptance criteria, or required evidence must increment its package version and trigger downstream compatibility checks.
