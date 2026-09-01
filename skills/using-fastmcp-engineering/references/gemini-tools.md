# Gemini CLI Tool Mapping

Skills speak in actions. On Gemini CLI these resolve to Gemini's tools.

| Action skills request | Gemini CLI equivalent |
|---|---|
| Invoke a skill | `activate_skill` |
| Read a file | `read_file` |
| Read multiple files | `read_many_files` |
| Create a file | `write_file` |
| Edit a file | `replace` |
| Run a shell command | `run_shell_command` |
| Search file contents | `grep_search` |
| Find files by name | `glob` |
| List files | `list_directory` |
| Fetch a URL | `web_fetch` |
| Search the web | `google_web_search` |
| Dispatch a subagent | `invoke_agent` with `agent_name: "generalist"` |
| Create/update todos | `write_todos` |

## Notes

- Gemini loads the bootstrap through the extension's declared context file (`FME.md`), which `@`-includes this mapping.
- Instructions file for the extension: `FME.md`.
- Skills live in the installed extension's `skills/` directory.
