# Claude Code Tool Mapping

Skills speak in actions. On Claude Code these resolve to Claude Code's native tools.

| Action skills request | Claude Code equivalent |
|---|---|
| Invoke a skill | the `Skill` tool |
| Read a file | `Read` |
| Create/edit/delete a file | `Write` / `Edit` / `Bash rm` |
| Run a shell command | `Bash` |
| Search file contents | `Grep` |
| Find files by name | `Glob` |
| Fetch a URL | `WebFetch` |
| Search the web | `WebSearch` |
| Dispatch a subagent | `Task` with a fastmcp-engineering `fm-*` role or `general-purpose` |
| Create/update todos | `TodoWrite` |

## Notes

- Claude Code discovers `skills/` and the SessionStart hook by convention from `.claude-plugin/plugin.json`.
- The `fm-*` role agents are available via the `Task` tool with `subagent_type` set to the role name.
