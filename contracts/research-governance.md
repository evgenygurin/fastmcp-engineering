# Research Governance

Research is a prerequisite for framework decisions. An agent MUST NOT invent FastMCP APIs, infer behavior from memory, or treat a minimal example as a production prescription.

## Evidence order

1. Current official FastMCP documentation for the target version.
2. Official FastMCP source and tests when documentation is ambiguous.
3. Official FastMCP examples relevant to the mechanism.
4. MCP specification / SEP material relevant to the behavior.
5. First-party documentation of integrated libraries.
6. High-quality secondary material only for supplementary context.

## Version discipline

Every framework claim MUST carry a version/stability label. Stable 3.x and 4.x prerelease material MUST remain explicitly separated.

## Research record

A research artifact MUST record:

- question / requirement;
- target versions;
- sources consulted;
- relevant examples;
- observed API and semantics;
- rejected alternatives;
- production implications;
- unresolved uncertainty;
- verification performed.

## Example interpretation

Examples are evidence of a mechanism, not blanket architecture templates. The agent MUST identify what an example demonstrates, what it intentionally omits, production risks, and how it should or should not be adapted.

## Completion gate

Research is complete only when another engineer can reproduce the decision from the recorded evidence without relying on the researcher's memory.