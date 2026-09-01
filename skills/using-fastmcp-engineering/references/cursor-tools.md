# Cursor Tool Mapping

Skills speak in actions. On Cursor these resolve to Cursor Agent's tools (Claude Code-compatible tool surface).

| Action skills request | Cursor equivalent |
|---|---|
| Invoke a skill | the `Skill` tool (Cursor Agent) |
| Read a file | `Read` |
| Create/edit/delete a file | `Write` / `Edit` |
| Run a shell command | `Bash` / terminal |
| Search file contents | `Grep` |
| Find files by name | `Glob` |
| Fetch a URL | `WebFetch` |
| Search the web | `WebSearch` |
| Dispatch a subagent | `Task` with the role name |
| Create/update todos | `TodoWrite` / Cursor todo list |

## Notes

- Cursor loads the bootstrap through its SessionStart hook (`hooks/hooks-cursor.json`) which injects `additional_context`.
- The `fm-*` role agents are available via `Task` with `subagent_type` set to the role name.
