# Pattern Selection System

Design patterns are tools, not architectural goals. This system prevents pattern-driven design and speculative abstraction.

## Selection algorithm

For each proposed abstraction:

1. State the concrete problem in one sentence.
2. Identify the knowledge, behavior, variability, or boundary that changes.
3. Identify the current owner of that responsibility.
4. List the simplest implementation that satisfies the current requirement.
5. List the candidate pattern(s).
6. Compare implementation and maintenance cost.
7. Check FastMCP-native alternatives when the concern is MCP-related.
8. Check whether the abstraction is required by a real external boundary, security boundary, testing seam, or demonstrated variability.
9. Reject hypothetical future requirements.
10. Record the decision.

## Pattern classes

### Adapter

Use when an external interface must conform to an internal port without leaking the external model or protocol inward.

Do not use an Adapter merely to wrap a class with an identical interface.

### Repository

Use when persistence is a meaningful application boundary. Keep persistence models and query mechanics in infrastructure. Do not add one solely because CRUD exists.

### Strategy

Use when multiple algorithms are genuinely interchangeable under a stable contract and the choice varies at runtime or by policy.

Do not create Strategy for a single algorithm with no demonstrated variability.

### Factory

Use when object construction contains meaningful selection or lifecycle rules that should not be owned by the caller.

Do not create factories that merely forward constructor arguments.

### Facade

Use when a subsystem has a stable simplified boundary and the facade hides meaningful coordination complexity.

Do not create a facade that merely renames methods.

### Specification / Policy

Use when a business rule is independently named, composed, tested, or reused. Do not turn every boolean condition into a class.

### Unit of Work

Use only when a business transaction spans multiple repository operations and atomicity is an explicit requirement not already owned by the persistence/application transaction boundary.

### CQRS

Use only when command/query separation produces measurable benefits such as materially different models, scaling, authorization, consistency, or read/write workloads. Do not introduce CQRS for ordinary CRUD.

### Event-driven patterns

Use only when asynchronous decoupling, integration boundaries, durable event semantics, or independently managed consumers are actual requirements. Do not introduce an event bus as a generic substitute for direct method calls.

## FastMCP-specific decision order

For MCP concerns, evaluate in this order unless the requirement clearly rules one out:

```text
Component
  → Provider
  → Transform
  → Middleware
  → Context / dependency injection
  → Lifespan
  → native task/background mechanism
  → composition/proxy
  → custom abstraction
```

This is a decision heuristic, not a requirement to force every problem through these mechanisms. Providers supply components dynamically; Transforms alter component presentation/behavior; Middleware provides cross-cutting request/response processing. Prefer these native mechanisms before inventing application-layer equivalents.

## Rejection triggers

Reject the proposed pattern when:

- its only justification is "SOLID";
- it is present because it is fashionable;
- it protects hypothetical future variability;
- it duplicates an existing FastMCP capability;
- it increases indirection without improving a real boundary;
- it makes testing harder without a compensating benefit;
- it causes domain/application code to depend on infrastructure;
- it makes a simple requirement materially harder to understand.

## Adversarial review questions

- Would this still be necessary if there were only one implementation?
- What code becomes simpler because of this abstraction?
- What code becomes harder?
- Is the abstraction protecting a real boundary or only organizing files?
- Does FastMCP already solve this problem?
- Could a plain function, module, dataclass, or composition root solve it?
- Is duplicated code actually duplicated knowledge?
- Are we designing for an explicit requirement or an imagined future?

## Decision record

```yaml
pattern_decision:
  pattern: <name or none>
  problem: <concrete problem>
  boundary_or_variability: <what changes>
  simplest_solution: <description>
  candidates: []
  native_fastmcp_alternatives: []
  selected: <solution>
  why_not_simpler: <reason>
  why_not_overengineering: <reason>
  complexity_cost: low|medium|high
  verification: []
```
