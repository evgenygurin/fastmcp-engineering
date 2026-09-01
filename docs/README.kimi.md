# Installing FastMCP Engineering for Kimi Code

## Prerequisites
- Kimi Code installed

## Installation
Run `/plugins install` and add the fastmcp-engineering git URL.

In Kimi Code, open the plugin interface and run `/plugins install`, then add
this repository's git URL
(`https://github.com/evgenygurin/fastmcp-engineering.git`). The plugin is
declared by `.kimi-plugin/plugin.json`, which registers `./skills/` and a
`sessionStart.skill` of `using-fastmcp-engineering` plus inline
`skillInstructions` tool mapping.

## Verify
Start a fresh Kimi Code session. The manifest's `sessionStart.skill` loads
`using-fastmcp-engineering` at session start, so the model knows it has
fastmcp-engineering skills. Ask it to describe them, or start a FastMCP/MCP
task and confirm a domain skill auto-triggers before any code is written.

## Updating
Reinstall or refresh the plugin via `/plugins install` with the same git URL to
pull the latest version.
