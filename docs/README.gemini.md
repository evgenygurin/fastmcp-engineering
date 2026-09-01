# Installing FastMCP Engineering for Gemini

## Prerequisites
- Gemini CLI installed

## Installation
Install the fastmcp-engineering extension via git URL:

```bash
gemini extensions install https://github.com/evgenygurin/fastmcp-engineering.git
```

The extension is declared by `gemini-extension.json`, whose `contextFileName`
points at the extension's own `FME.md` — a context file that `@`-includes the
`using-fastmcp-engineering` bootstrap skill and the
`references/gemini-tools.md` tool mapping. Because the file ships inside the
installed extension and is declared by the manifest, Gemini loads it every
session.

## Verify
Start a fresh Gemini session and ask the model to describe its
fastmcp-engineering skills. If the extension's context file loaded, it knows it
has them. A FastMCP/MCP task should auto-trigger a domain skill before any code
is written.

## Updating
Reinstall the extension via `gemini extensions install` with the same git URL
to pull the latest version.
