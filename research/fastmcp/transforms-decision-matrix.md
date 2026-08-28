# FastMCP Transforms Decision Matrix

## Core question

A Transform is appropriate only when the problem concerns systematic MCP component transformation or composition. The name of an abstraction is never sufficient justification.

| Problem | Prefer |
|---|---|
| Execute a capability | Tool |
| Serve addressable contextual data | Resource |
| Supply reusable prompt content | Prompt |
| Discover/source MCP components | Provider |
| Alter/combine/filter/wrap exposed components systematically | Transform |
| Apply request-wide cross-cutting behavior | Middleware |
| Construct/manage application dependencies | Composition root / DI |
| Apply domain/application behavior | Domain/Application layer |
| Map application data to a public contract | Explicit mapper/assembler where needed |

Exact semantics must be checked against the target FastMCP release.

## Transform design questions

Before implementation answer:

1. What source components enter the transformation?
2. What observable component properties change?
3. Which properties must be preserved?
4. Does the transform change identity, name, URI, schema, metadata, annotations, description, visibility, or behavior?
5. Is the transformation stateless or stateful?
6. Can it be safely composed with another transform?
7. Does order matter?
8. Is it idempotent?
9. What happens on transformation failure?
10. Who owns authorization decisions?
11. Who owns lifecycle and external resources?
12. What is the simplest non-Transform alternative?

## Pattern restraint

Do not add Adapter, Decorator, Strategy, Registry, Factory, Pipeline, or Mapper abstractions unless Pattern Selection identifies a concrete problem that requires them. FastMCP's native composition mechanisms take precedence over project-specific replicas.

## Security

A transform that filters or modifies component exposure can change the effective attack surface. Explicitly evaluate authorization, information disclosure, tool-description manipulation, schema weakening, and accidental exposure of components that were not intended for the caller.

## Verification matrix

| Concern | Verify when applicable |
|---|---|
| Discovery | transformed component is actually exposed/discoverable |
| Identity | names/URIs/IDs behave as designed |
| Schema | input/output contract remains valid |
| Metadata | descriptions/annotations are preserved or deliberately changed |
| Composition | ordering and interaction are correct |
| Visibility | filtering is correct |
| Security | authorization is not bypassed |
| Failure | errors propagate/translate correctly |
| Lifecycle | resources are not leaked |
| Concurrency | state is safe under concurrent use |
