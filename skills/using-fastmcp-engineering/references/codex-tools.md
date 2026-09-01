# Codex Tool Mapping

Skills speak in actions. On Codex these resolve to Codex CLI/App tools. Codex surfaces skills natively from `.codex-plugin/plugin.json` `skills` field.

| Action skills request | Codex equivalent |
|---|---|
| Invoke a skill | Codex's native skill tool |
| Read a file | `read` |
| Create/edit/delete a file | `write` / `edit` |
| Run a shell command | `shell` |
| Search file contents | `grep` |
| Find files by name | `glob` |
| Fetch a URL | `web_fetch` |
| Search the web | `web_search` |
| Dispatch a subagent | `spawn_agent` / `wait_agent` / `close_agent` — requires `multi_agent = true` in `~/.codex/config.toml` |
| Create/update todos | a todo/task tool if available, otherwise a plan file |

## Notes

- Multi-agent features must be enabled: `[features] multi_agent = true` in the Codex config.
- fastmcp-engineering skills are discovered natively; the bootstrap is triggered by the surfaced `using-fastmcp-engineering` description.
