# FastMCP Engineering Methodology Server

## Purpose

The Methodology Server exposes the FastMCP Engineering repository's skills, contracts, prompts, and research artifacts as a production-grade MCP server using FastMCP v4 over stdio transport. It enables coding agents (Claude Code, Cursor, Codex, OpenCode, Gemini, etc.) to discover and consume methodology guidance programmatically via the MCP protocol.

## fastmcp.json Reference

```json
{
  "$schema": "https://gofastmcp.com/public/schemas/fastmcp.json/v1.json",
  "source": {
    "type": "filesystem",
    "path": "server/server.py",
    "entrypoint": "mcp"
  },
  "environment": {
    "type": "uv",
    "python": ">=3.12",
    "dependencies": ["fastmcp>=4.0.0,<4.1"]
  },
  "deployment": {
    "transport": "stdio",
    "log_level": "INFO"
  }
}
```

| Field | Description |
|-------|-------------|
| `source.path` | Entry point module (`server/server.py`) |
| `source.entrypoint` | Variable name of the `FastMCP` instance (`mcp`) |
| `environment.type` | Package manager (`uv`) |
| `environment.python` | Minimum Python version (3.12) |
| `environment.dependencies` | Pinned FastMCP v4 range |
| `deployment.transport` | `stdio` for stdio transport |
| `deployment.log_level` | Logging level for the server process |

## Stdio Wiring

The server runs as a stdio subprocess launched by the MCP client (harness). The harness is responsible for:

1. Spawning `uv run --directory /repo/root fastmcp run fastmcp.json`
2. Communicating over stdin/stdout using JSON-RPC 2.0
3. Managing process lifecycle (start, graceful shutdown on disconnect)

The `uv run --directory` prefix ensures the working directory is the repository root so that relative paths (`skills/`, `contracts/`, `prompts/`) resolve correctly.

### Required Environment

- Python 3.12+
- `uv` package manager
- FastMCP 4.0.x (pinned in `fastmcp.json`)

No additional environment variables are required. The server has no external service dependencies (no database, no API keys).

## Exposed Capabilities

### Tools

| Tool | Parameters | Description |
|------|------------|-------------|
| `find_skills` | `task: str`, `domain?: str`, `limit?: int`, `session_id?: SessionId` | Weighted search across 58 skills; returns ranked list with URIs |
| `clarify_find` | `task: str`, `ctx: Context` | Interactive elicitation for ambiguous tasks; asks for domain clarification |

### Resources

| URI Pattern | Description |
|-------------|-------------|
| `skill://{name}/SKILL.md` | Full skill markdown (frontmatter + body) |
| `skill://{name}/ACCEPTANCE.md` | Acceptance criteria for the skill |
| `skill://{name}/_manifest` | JSON manifest with file hashes for integrity verification |
| `contract://{name}` | Contract documents (e.g., `skill-contract`, `github-workflow-contract`) |
| `fme-prompt://{name}` | Prompt templates from `prompts/` directory |

All skill resources are provided by `SkillsDirectoryProvider` with recursive discovery. Contract and prompt resources are registered via `FileSystemProvider` and explicit `@resource` decorators.

### Prompts

| Prompt | Arguments | Purpose |
|--------|-----------|---------|
| `dispatch` | `task: str` | Routes a task to top-5 relevant skills with URIs |
| `skill_context` | `skill: str` | Returns full skill text wrapped in execution context |
| `domain_guide` | `domain: str`, `task: str` | Domain-filtered skill recommendations |
| `role_prompt` | `role: str` | Loads role prompt from `prompts/{role}.md` |
| `contract_check` | `contract: str`, `artifact: str` | Validates an artifact against a contract |

Prompt arguments support tab-completion via `@mcp.completion` handlers (skills, contracts, roles, domains).

### Completion

The server implements `completion` for:
- Prompt arguments: `skill_context.skill`, `role_prompt.role`, `contract_check.contract`, `domain_guide.domain`
- Resource templates: `contract://{name}`, `fme-prompt://{name}`

Completions are sourced from the live skill index, contracts directory, and prompts directory.

### Extension: `dev.fastmcp-eng/methodology`

The `MethodologyExtension` (identifier: `dev.fastmcp-eng/methodology`) provides:

1. **Settings** (`settings()`): Advertised at initialize — `{skillsCount, domains[], version}`
2. **Method** (`methodology/stats`): Returns `{skillsCount, domains[], callCounts{}}`
3. **Tool-call interceptor**: Increments per-tool call counts for observability

Clients can call `methodology/stats` to get runtime statistics and verify the extension is active.

### Sessions

`SessionProvider` enables:
- `create_session` / `end_session` tools for explicit lifecycle
- `SessionId` resolution in tool parameters
- Per-session `recent_domains` storage used by `find_skills` for history boosting

Session data is in-memory; it does not persist across server restarts.

## Running the Server

```bash
# From repository root
uv run fastmcp run fastmcp.json
```

### Verification

```bash
# Run server test suite
uv run pytest tests/server/ -v

# Run full repo test suite
uv run pytest -q

# Lint
ruff check .
```

## Session Note

The server is stateless between runs except for in-memory session data. All skills, contracts, and prompts are read from the filesystem at request time (skills are indexed on each `find_skills` call via `build_index()`). This ensures the server always reflects the current repository state without requiring restarts.

The `MethodologyExtension` call counts reset on each server start.

## Storage Future Options

Current implementation uses filesystem reads with in-memory indexing. Future enhancements could include:

| Option | Trade-off |
|--------|-----------|
| **Persistent index** (SQLite/LMDB) | Faster startup for large skill sets; requires invalidation on file changes |
| **Vector embeddings** (pgvector, Chroma) | Semantic search beyond token matching; adds dependency and maintenance |
| **GitNexus-backed index** | Leverages existing code graph; requires GitNexus server running |
| **Hot-reload watcher** | Near-instant index updates; adds complexity (fsnotify, debouncing) |

For the current 58-skill corpus, the on-demand filesystem index is fast enough (<50ms). Persistent indexing becomes worthwhile at ~500+ skills or when semantic search is required.

## Troubleshooting

| Issue | Resolution |
|-------|------------|
| "Module not found" errors | Ensure `uv run --directory /repo/root` is used; the server must run from repo root |
| Skills not found | Verify `skills/` directory exists and contains `SKILL.md` files with frontmatter `name` |
| Completion not working | Check that the client supports MCP completions and the server's `@mcp.completion` handlers are registered |
| Extension not advertised | Verify `mcp.add_extension(MethodologyExtension())` is called before any providers |
| Session tools missing | Verify `mcp.add_provider(SessionProvider())` is called |