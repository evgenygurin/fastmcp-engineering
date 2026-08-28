---
name: pattern-selection
description: Select the smallest justified architectural pattern for a concrete problem without cargo-culting design patterns.
---

# Pattern Selection

## Mission

Choose an abstraction only when the requirement demonstrates a real boundary, variability, lifecycle concern, or dependency inversion need.

## Required sequence

1. State the concrete problem.
2. Implement mentally the simplest direct solution.
3. Identify the reason that solution becomes insufficient.
4. List at least one viable simpler alternative.
5. Select a pattern only if its benefit exceeds its complexity cost.
6. Record the decision in the architecture decision contract.

## Pattern heuristics

| Pattern | Justify when | Reject when |
|---|---|---|
| Repository | persistence is an explicit application boundary | it only wraps one trivial ORM call without a boundary need |
| Adapter | an external API/model must be isolated | the wrapper merely renames methods |
| Strategy | algorithms are genuinely interchangeable | there is only one algorithm and no real variability |
| Factory | creation has meaningful selection/lifecycle rules | construction is a one-line constructor call |
| Facade | a subsystem is genuinely complex for callers | it hides one simple dependency |
| Observer/Event bus | asynchronous decoupled subscribers are required | it replaces a direct function call without a concrete need |
| CQRS | read/write models or scaling/consistency needs justify separation | CRUD complexity is low |

## FastMCP-specific rule

Before introducing a custom pattern, check whether FastMCP already provides the relevant mechanism through Providers, Transforms, Middleware, Context, lifespan, tasks, authentication, authorization, pagination, versioning, proxy/composition, or Client testing.

## Output

Return:

- selected approach;
- problem;
- simpler alternative;
- reason alternative is insufficient;
- complexity cost;
- testing impact;
- YAGNI decision;
- rejected patterns and why.
