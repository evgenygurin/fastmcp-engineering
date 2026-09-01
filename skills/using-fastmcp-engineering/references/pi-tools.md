# Pi Tool Mapping

Skills speak in actions. On Pi these resolve to Pi's native tools (lowercase) and optional extensions.

| Action skills request | Pi equivalent |
|---|---|
| Invoke a skill | Pi's native skill system: load the relevant `SKILL.md` with `read`, or a human invokes `/skill:name` |
| Read a file | `read` |
| Create/edit/delete a file | `write` / `edit` |
| Run a shell command | `bash` |
| Search file contents | `grep` |
| Find files by name | `find` / `ls` |
| Fetch a URL | Pi's web fetch tool if available |
| Search the web | Pi's web search tool if available |
| Dispatch a subagent | An installed subagent tool (e.g. `pi-subagents`) if available; otherwise do the work inline |
| Task tracking | An installed todo tool if available; otherwise a plan file or repo-local `TODO.md` |

## Notes

- Pi has no native `Skill` tool: reading the relevant `SKILL.md` with `read` IS the sanctioned invocation mechanism for fastmcp-engineering skills.
- Never invent `task` calls; if no subagent tool exists, execute sequentially or explain the missing capability.
