# Installing FastMCP Engineering for Copilot CLI

## Prerequisites
- GitHub Copilot CLI installed

## Installation
Install the fastmcp-engineering plugin from this repository via your Copilot
CLI plugin install.

Copilot CLI shares the Claude Code hook path (the `session-start` script
detects Copilot via the `COPILOT_CLI` environment variable and emits the
standard `additionalContext` JSON shape). Install the plugin through Copilot
CLI's own plugin install mechanism using this repository's git URL.

## Verify
Start a fresh Copilot CLI session and ask the model to describe its
fastmcp-engineering skills. If the session-start hook injected the bootstrap,
it knows it has them. The `skills/using-fastmcp-engineering/SKILL.md` bootstrap
is injected at session start, so a FastMCP/MCP task should auto-trigger a
domain skill before any code is written.

## Updating
Reinstall or refresh the plugin through your Copilot CLI plugin install to pull
the latest version.
