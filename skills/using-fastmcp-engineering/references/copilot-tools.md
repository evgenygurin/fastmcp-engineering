# GitHub Copilot CLI Tool Mapping

Skills speak in actions. On Copilot CLI these resolve to Copilot CLI's tools (Claude Code-compatible tool surface, SDK standard).

| Action skills request | Copilot CLI equivalent |
|---|---|
| Invoke a skill | the `Skill` tool |
| Read a file | `Read` |
| Create/edit/delete a file | `Write` / `Edit` |
| Run a shell command | `Bash` |
| Search file contents | `Grep` |
| Find files by name | `Glob` |
| Fetch a URL | `WebFetch` |
| Search the web | `WebSearch` |
| Dispatch a subagent | `Task` with the role name |
| Create/update todos | `TodoWrite` |

## Notes

- Copilot CLI shares the Claude Code session-start hook path; `hooks/session-start` detects it via `COPILOT_CLI=1` and emits the SDK-standard `additionalContext` shape.
- The `fm-*` role agents are available via `Task` with `subagent_type` set to the role name.
