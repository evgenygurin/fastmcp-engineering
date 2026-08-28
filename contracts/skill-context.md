# Skill Context Package Contract

A Skill Context Package (SCP) is the portable, versioned context given to a new agent session before it develops or executes a skill. It exists so a skill can be developed independently without relying on conversation history or hidden memory.

## Required properties

A context package MUST be:

- self-contained;
- version-aware;
- evidence-linked;
- explicit about upstream dependencies;
- explicit about expected artifacts;
- explicit about non-goals;
- reproducible from repository state.

## Package structure

```yaml
skill_context:
  schema_version: "1"
  skill: <name>
  purpose: <one sentence>
  status: design|implementation|review|maintenance
  target:
    fastmcp_version: <version or range>
    python_version: <version or range>
    protocol_version: <if relevant>
  requirements: []
  non_goals: []
  upstream_skills: []
  required_artifacts: []
  required_research:
    official_docs: []
    official_examples: []
    source_or_tests: []
    mcp_spec: []
    first_party_dependencies: []
  architecture_constraints: []
  pattern_constraints: []
  security_constraints: []
  testing_constraints: []
  expected_outputs: []
  verification_commands: []
  acceptance_criteria: []
  open_questions: []
  known_risks: []
```

## Upstream dependency rule

A skill may consume another skill's output only through a named artifact or contract. Conversation history is never an implicit dependency.

Every upstream dependency must specify:

- artifact path or contract;
- minimum schema/version;
- what information is consumed;
- what happens when it is missing or stale.

## Research freshness

Every research artifact must identify the target library/version and evidence source. If an artifact targets a different version, the agent must revalidate it against official documentation before use.

For FastMCP, the agent must verify current version behavior rather than assuming that v3 and v4 APIs are interchangeable. For example, the official migration documentation records v4 removals such as `FastMCP.as_proxy`, `add_tool_transformation`, and the v3 decorator-object escape hatch. citeturn0search2

## Execution rule

At session start the agent MUST:

1. read this contract;
2. load its complete Skill Context Package;
3. inspect all referenced artifacts;
4. validate freshness and version compatibility;
5. identify missing evidence;
6. stop if a mandatory dependency is missing or incompatible;
7. only then begin research/design/implementation.

## Context minimization

Do not copy the entire repository into every package. Reference stable artifacts by path and schema/version. Include only decision-critical facts inline.

## Handoff

A completed skill MUST publish a context package for downstream skills containing:

- what it established;
- artifacts it created;
- decisions it made;
- constraints it introduced;
- verification evidence;
- unresolved questions;
- compatibility information.
