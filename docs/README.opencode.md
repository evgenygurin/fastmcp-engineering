# Installing FastMCP Engineering for OpenCode

## Prerequisites
- OpenCode installed

## Installation
Add the fastmcp-engineering plugin to your `opencode.json` `plugin` array:

```json
{
  "plugin": [
    "fastmcp-engineering@git+https://github.com/evgenygurin/fastmcp-engineering.git"
  ]
}
```

The plugin (`.opencode/plugins/fastmcp-engineering.js`) registers the `skills/`
directory via its `config` hook and injects the bootstrap as a user message via
`experimental.chat.messages.transform` at session start.

## Verify
Run a one-shot log-grep check:

```bash
opencode run --print-logs "hello" 2>&1 | grep -i fastmcp
```

If the plugin injected the bootstrap, the fastmcp-engineering context appears
in the logs (`2>&1` matters because logs go to stderr). You can also ask the
model to describe its fastmcp-engineering skills in a fresh session.

## Updating
Update the git URL / plugin version in your `opencode.json` `plugin` array, or
reinstall the plugin, to pull the latest version.
