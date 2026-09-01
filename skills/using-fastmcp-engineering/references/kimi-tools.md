# Kimi Code Tool Mapping

Skills speak in actions. On Kimi Code these resolve to Kimi Code's tools.

| Action skills request | Kimi Code equivalent |
|---|---|
| Invoke a skill | the `Skill` tool |
| Read a file | `Read` |
| Create/edit/delete a file | `Write` / `Edit` |
| Run a shell command | `Bash` |
| Search file contents | `Grep` |
| Find files by name | `Glob` |
| Fetch a URL | `FetchURL` |
| Search the web | `WebSearch` |
| Dispatch a subagent | `Agent` tool with a Kimi subagent type (e.g. `coder`, `explore`, `plan`) |
| Create/update todos | `TodoList` |

## Notes

- Kimi loads the bootstrap via `sessionStart.skill: "using-fastmcp-engineering"` in `.kimi-plugin/plugin.json`.
- Do not pass `general-purpose` as `subagent_type`; use Kimi's own subagent types.
