# FastMCP Engineering

Engineering methodology, research artifacts, skills, prompts, contracts, and quality gates for building production-grade MCP servers with FastMCP.

## Core principles

- Research official documentation and official examples before making framework decisions.
- Separate domain, application, infrastructure, and MCP delivery responsibilities.
- Prefer the simplest architecture that satisfies real requirements.
- Use SOLID, KISS, DRY, and YAGNI as decision criteria, not as reasons to add abstractions.
- Prefer native FastMCP capabilities before custom infrastructure.
- Keep Pydantic, SQLAlchemy, PydanticAI, Supabase, and other technologies behind appropriate boundaries.
- Verify behavior with tests, protocol checks, security review, and architecture review.
- Treat documentation and repository hygiene as part of correctness.

## Engineering workflow

Preflight → Requirement → Discovery → Documentation Research → Example Research → Architecture → Design Gate → Contracts → TDD → Implementation → Documentation Sync → Static Analysis → Tests → Security Review → Architecture Review → PR Review → Merge → Delete Source Branch → Verify `main` → Branch Audit.

## GitHub workflow

`main` is the only persistent branch. Work is performed on one short-lived intent-named branch with exactly one PR:

```text
main → feat/fix/refactor/docs/chore branch → PR → review → merge → delete branch → verify main
```

A branch without a PR is orphan work. A merged PR whose source branch survives is incomplete work. If branch deletion is unavailable through the current tooling, completion must be reported as blocked.

## Verification without CI

GitHub Actions are optional and are not a prerequisite for development or merge. When CI is unavailable, run the strongest applicable local checks: tests, lint, type checks, builds, static analysis, protocol/conformance checks, and security checks. Never invent CI results and never lower the verification standard because CI is unavailable.

## Documentation synchronization

Changes to externally relevant behavior, architecture, API, configuration, operations, testing procedures, or agent workflow must update the relevant documentation in the same PR. Intentional documentation non-changes must be explained in the review evidence.

## Version policy

FastMCP version-specific claims must identify their version and stability level. Stable and prerelease APIs must never be silently mixed.

## Status

Consolidated engineering foundation. The repository contains canonical skills, prompts, contracts, architecture guidance, research artifacts, and verification rules. New implementation work follows the branch/PR lifecycle above.

## Installation (all agents)

FastMCP Engineering auto-triggers its skills in every major coding agent. Install
through each harness's own mechanism (never by hand-copying files):

| Harness | Install | Details |
|---|---|---|
| Claude Code | `/plugin install ...` | `docs/README.claude-code.md` |
| Cursor | `/add-plugin ...` | `docs/README.cursor.md` |
| Codex | `/plugins` | `docs/README.codex.md` |
| Copilot CLI | plugin install | `docs/README.copilot.md` |
| Kimi Code | `/plugins install` | `docs/README.kimi.md` |
| OpenCode | `plugin` array in opencode.json | `docs/README.opencode.md` |
| pi | package install | `docs/README.pi.md` |
| Gemini | `gemini extensions install` | `docs/README.gemini.md` |

How it works: at session start, `skills/using-fastmcp-engineering/SKILL.md` is
injected into the model context (wrapped in `<EXTREMELY_IMPORTANT>` + per-harness
tool mapping), which makes the domain skills auto-trigger. Design:
`docs/superpowers/specs/2026-09-01-fastmcp-superpowers-parity-design.md`.

## Methodology Server (FastMCP v4, stdio)

This repository includes a FastMCP v4 server (`fastmcp.json` + `server/server.py`) that exposes the methodology as MCP resources, tools, and prompts over stdio.

### Running the server

```bash
uv run fastmcp run fastmcp.json
```

The server uses stdio transport and requires Python 3.12+ with `fastmcp>=4.0.0,<4.1` (managed via uv).

### What the server exposes

| Category | Items | Description |
|----------|-------|-------------|
| **Tools** | `find_skills`, `clarify_find` | Search 58 skills by task description with weighted ranking and session-aware domain boosting |
| **Resources** | `skill://{name}/SKILL.md`, `skill://{name}/ACCEPTANCE.md`, `skill://{name}/_manifest` | 58 skills as versioned resources with content hashes |
| **Resources** | `contract://{name}` | All contracts (e.g. `skill-contract`, `github-workflow-contract`) |
| **Resources** | `fme-prompt://{name}` | All prompt templates from `prompts/` |
| **Prompts** | `dispatch`, `skill_context`, `domain_guide`, `role_prompt`, `contract_check` | Reusable prompt templates for agent workflows |
| **Completion** | Skills, contracts, prompts, domains | Tab-completion for prompt arguments and resource templates |
| **Extension** | `methodology/stats` | Skill count, domains, and tool-call interceptor stats |
| **Sessions** | `create_session`, `end_session` | Session lifecycle with `recent_domains` storage for history boost |

### Per-harness install (stdio)

The server runs over stdio — configure each harness to launch it via `fastmcp run fastmcp.json`.

**Claude Code** (`~/.claude/mcp_servers.json`):
```json
{
  "mcpServers": {
    "fastmcp-engineering": {
      "command": "uv",
      "args": ["run", "--directory", "/absolute/path/to/fastmcp-engineering", "fastmcp", "run", "fastmcp.json"],
      "transport": "stdio"
    }
  }
}
```

**Cursor** (`.cursor/mcp.json`):
```json
{
  "mcpServers": {
    "fastmcp-engineering": {
      "command": "uv",
      "args": ["run", "--directory", "/absolute/path/to/fastmcp-engineering", "fastmcp", "run", "fastmcp.json"],
      "transport": "stdio"
    }
  }
}
```

**Codex** (`~/.codex/config.toml`):
```toml
[mcp_servers.fastmcp-engineering]
command = "uv"
args = ["run", "--directory", "/absolute/path/to/fastmcp-engineering", "fastmcp", "run", "fastmcp.json"]
transport = "stdio"
```

**OpenCode** (`.opencode/mcp.json`):
```json
{
  "mcpServers": {
    "fastmcp-engineering": {
      "command": "uv",
      "args": ["run", "--directory", "/absolute/path/to/fastmcp-engineering", "fastmcp", "run", "fastmcp.json"],
      "transport": "stdio"
    }
  }
}
```

**Gemini** (`~/.gemini/settings.json`):
```json
{
  "mcpServers": {
    "fastmcp-engineering": {
      "command": "uv",
      "args": ["run", "--directory", "/absolute/path/to/fastmcp-engineering", "fastmcp", "run", "fastmcp.json"],
      "transport": "stdio"
    }
  }
}
```

Replace `/absolute/path/to/fastmcp-engineering` with the actual clone path. The `uv run --directory` ensures the server runs from the repo root so `skills/`, `contracts/`, and `prompts/` resolve correctly.

### Example agent flow

```python
from fastmcp import Client

async with Client("fastmcp-engineering") as client:
    # 1. Find relevant skills for a task
    skills = await client.call_tool("find_skills", {"task": "add OAuth to my FastMCP server"})
    top_skill = skills[0]["name"]  # e.g. "fastmcp-auth"

    # 2. Read the full skill
    skill = await client.read_resource(f"skill://{top_skill}/SKILL.md")

    # 3. Get execution context prompt
    context = await client.get_prompt("skill_context", {"skill": top_skill})

    # 4. Validate an artifact against a contract
    check = await client.get_prompt("contract_check", {"contract": "skill-contract", "artifact": "..."})
```

Full integration test: `tests/server/test_integration.py`.

---

## opencode integration

Global exposure of this repository's capabilities in opencode:

- **Skills**: global `skills.paths` → this clone (frontmatter `name`+`description` required)
- **Reference**: `references.fastmcp-eng` — whole repo readable in any project
- **Plugin hint**: `~/.config/opencode/plugin/fastmcp-engineering.ts` (verified PASS 2026-08-30)
- **fm-* role agents**: `opencode/agents/` — research/implementation/audit/review/governor subagents; they load `prompts/<token>-<role>-agent.md` at runtime (auto-sync, no duplication)
- **Commands**: `opencode/commands/` — `/fm` dispatcher, `/fm-prompts` inventory

Setup on a new machine (symlinks into global config, run from repo root):

    ln -s "$PWD/opencode/agents/fm-research.md" ~/.config/opencode/agents/fm-research.md
    ln -s "$PWD/opencode/agents/fm-implementation.md" ~/.config/opencode/agents/fm-implementation.md
    ln -s "$PWD/opencode/agents/fm-audit.md" ~/.config/opencode/agents/fm-audit.md
    ln -s "$PWD/opencode/agents/fm-review.md" ~/.config/opencode/agents/fm-review.md
    ln -s "$PWD/opencode/agents/fm-governor.md" ~/.config/opencode/agents/fm-governor.md
    ln -s "$PWD/opencode/commands/fm.md" ~/.config/opencode/commands/fm.md
    ln -s "$PWD/opencode/commands/fm-prompts.md" ~/.config/opencode/commands/fm-prompts.md

Design: `docs/superpowers/specs/2026-08-31-opencode-fastmcp-maximal-design.md`
