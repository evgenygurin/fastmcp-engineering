# FastMCP Engineering — Plugin Experience Brief

## Product

FastMCP Engineering is a skills-only Codex Plugin for engineers who build and review production-grade MCP servers with FastMCP.

## Primary recurring job

Turn an MCP requirement into an implementation that has explicit architecture, contracts, tests, protocol conformance, security review, and verification evidence.

## Public boundary

The public surface is the repository's engineering Skills. Repository governance, internal orchestration, branch bookkeeping, and implementation-only artifacts are supporting material rather than user-facing capabilities.

The Plugin is intentionally **skills-only**. It does not declare an MCP server or external app dependency.

## Capability groups

- FastMCP and MCP protocol engineering
- API contracts and schema design
- Architecture and dependency boundaries
- Python implementation patterns
- Configuration and environment engineering
- Database and persistence engineering
- Testing, conformance, and verification
- Security and dependency/supply-chain review
- CI/CD and operational engineering

## Host-workspace profile

| Capability | Disposition | Boundary |
|---|---|---|
| read | preferred | Inspect known repository files and evidence. |
| list | preferred | Establish repository/package shape before edits. |
| search | preferred | Discover relevant Skills, contracts, tests, and examples. |
| grep | preferred | Locate exact symbols, paths, and configuration fields. |
| write | mutation | Create files only when the requested workflow authorizes it. |
| patch | mutation | Prefer focused edits to existing files. |
| shell | mutation | Use for repository tests, packaging, and other commands when available. |
| python | optional | Deterministic parsing, validation, hashing, and package inspection. |

## Mutation boundary

Discovery is read-only by default. Writes, patches, and mutating shell commands require explicit task authorization. Verification must produce execution evidence; Skills must never claim a command ran when it did not.

## Dependencies

No external app or MCP server is required for the core Plugin surface. Host-native workspace capabilities are used when the current Codex host exposes them.

## Starter prompts

1. Design a production-grade FastMCP server for this requirement.
2. Review this MCP architecture and identify risks and missing contracts.
3. Build a verification plan for this FastMCP implementation.

## Discovery test brief

### Direct

- Build a production FastMCP server from this requirement.
- Review this MCP architecture for protocol and security risks.
- Create a TDD and verification plan for this MCP server.

### Indirect

- I need to turn this Python service into a production MCP server.
- Check whether this MCP design has the right boundaries and contracts.
- Help me prove this FastMCP implementation is production-ready.

### Negative

- General-purpose Python tutoring with no MCP or engineering context.
- Generic UI design or marketing copy unrelated to MCP engineering.
- Deploy an arbitrary non-MCP application with no FastMCP relevance.

## Invocation policy

Low-risk research, architecture, testing, and review Skills may be discovered implicitly. Mutation-oriented workflows must preserve an explicit authorization boundary and should not imply that repository changes were made unless the host executed them.

## Listing risks

- Public publisher/legal metadata is not yet fully verified; privacy and terms URLs are intentionally omitted until verified.
- Full package validation, deterministic ZIP comparison, clean extraction validation, and repository-native test execution remain execution-dependent gates.
- The current branch must not be treated as released or submitted until those gates pass.
