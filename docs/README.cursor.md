# Installing FastMCP Engineering for Cursor

## Prerequisites
- Cursor installed

## Installation
Add fastmcp-engineering via Cursor's plugin marketplace.

In Cursor run `/add-plugin fastmcp-engineering@<marketplace>`, or add the
fastmcp-engineering plugin entry from your configured plugin marketplace. The
source plugin lives in `.cursor-plugin/plugin.json`, which points Cursor at
`./skills/` and `./hooks/hooks-cursor.json`.

## Verify
Start a fresh Cursor session and ask the model to describe its
fastmcp-engineering skills. If the session-start hook injected the bootstrap,
it knows it has them. The `skills/using-fastmcp-engineering/SKILL.md` bootstrap
is injected at session start, so a FastMCP/MCP task should auto-trigger a
domain skill before any code is written.

## Updating
Reinstall or refresh the plugin through Cursor's plugin marketplace to pull the
latest version.
