# Installing FastMCP Engineering for Codex

## Prerequisites
- Codex installed

## Installation
Install fastmcp-engineering from the Codex plugin marketplace or git URL.

Open the Codex plugin interface (run `/plugins`) and install the
fastmcp-engineering plugin from your configured marketplace, or install it
directly from this repository's git URL. The plugin is declared by
`.codex-plugin/plugin.json`, which registers `./skills/` and declares an empty
`hooks` object to suppress `hooks/hooks.json` auto-discovery (Codex surfaces
skills natively and runs no session-start hook).

## Verify
Start a fresh Codex session. Codex surfaces the installed skills natively via
skill discovery — the `using-fastmcp-engineering` skill's description should
prompt the model to load it. Ask the model to list its available skills; the
bundled fastmcp-engineering skills should appear. Tool mapping lives in
`skills/using-fastmcp-engineering/references/codex-tools.md`.

## Updating
Reinstall or refresh the plugin from the Codex plugin marketplace or the git
URL to pull the latest version.
