# Installing FastMCP Engineering for pi

## Prerequisites
- pi installed

## Installation
Install the package via pi's package mechanism (the `package.json` `pi`
fields).

The repository's `package.json` declares a `pi` field with `extensions`
(`./.pi/extensions/fastmcp-engineering.ts`) and `skills` (`./skills`), plus the
`pi-package` keyword. Install the package through pi's own package install
command for this repository. The extension registers the skills directory via
`resources_discover` → `skillPaths` and injects the bootstrap as a user message
on the `context` event (lifecycle-flag + compaction-aware).

## Verify
Start a fresh pi session and ask the model to describe its fastmcp-engineering
skills. If the extension injected the bootstrap, it knows it has them. A
FastMCP/MCP task should auto-trigger a domain skill before any code is written.
Because pi has no native `Skill` tool, reading a skill's `SKILL.md` with the
file-read tool is the sanctioned loading mechanism — see
`references/pi-tools.md`.

## Updating
Reinstall or update the package through pi's package mechanism to pull the
latest version.
