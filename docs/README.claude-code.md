# Installing FastMCP Engineering for Claude Code

## Prerequisites
- Claude Code installed

## Installation
Install fastmcp-engineering via your Claude Code plugin marketplace.

In Claude Code run `/plugin install fastmcp-engineering@<marketplace>`, or find
the fastmcp-engineering entry in your configured plugin marketplace and install
it from there. The marketplace entry points at the plugin's
`.claude-plugin/plugin.json`, which auto-discovers `skills/` and
`hooks/hooks.json` by convention.

## Verify
Start a fresh Claude Code session and ask the model to describe its
fastmcp-engineering skills. If the session-start hook injected the bootstrap,
it knows it has them. The `skills/using-fastmcp-engineering/SKILL.md` bootstrap
is injected at session start (wrapped in `<EXTREMELY_IMPORTANT>`), so a
FastMCP/MCP task should auto-trigger a domain skill before any code is written.

## Updating
Reinstall or refresh the plugin through your Claude Code plugin marketplace to
pull the latest version.
