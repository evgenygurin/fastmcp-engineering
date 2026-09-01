# OpenCode Tool Mapping

Skills speak in actions ("invoke a skill", "dispatch a subagent", "create a todo"). On OpenCode these resolve to OpenCode's native tools.

| Action skills request | OpenCode equivalent |
|---|---|
| Invoke a skill | OpenCode's native `skill` tool |
| Create/update todos | `todowrite` |
| Dispatch a subagent | `task` with `subagent_type` (`general`, `explore`, or a fastmcp-engineering `fm-*` role) |
| Read a file | `read` |
| Create/edit/delete a file | `write` / `edit` / `bash rm` |
| Run a shell command | `bash` |
| Search file contents | `grep` |
| Find files by name | `glob` |
| Fetch a URL | `webfetch` |
| Search the web | `websearch` or Exa web-search tools |

## fm-* role agents

fastmcp-engineering ships `fm-research`, `fm-implementation`, `fm-audit`, `fm-review`, `fm-governor` role agents. Dispatch them via the `task` tool with `subagent_type` set to the role name, or use the `/fm` command.

## Notes

- Skills must be invoked through the native `skill` tool; do not bypass it by reading `SKILL.md` with `read` unless the skill itself documents that path.
- The `fm-*` agents load `prompts/<token>-<role>-agent.md` at runtime (PRIMARY local clone, FALLBACK reference clone).
