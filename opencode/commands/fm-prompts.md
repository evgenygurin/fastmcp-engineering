---
description: Inventory of fastmcp-engineering role prompts and the fm-* agent mapping
---
fastmcp-engineering prompts available to the fm-* agents:

!`ls /Users/laptop/dev/fastmcp-engineering/prompts/ 2>/dev/null || ls ~/.local/share/opencode/repos/github.com/evgenygurin/fastmcp-engineering@main/prompts/`

Mapping (loaded at runtime by the fm-* subagents):
- `fm-research` loads `<token>-research-agent.md` (generic: `research-agent.md`)
- `fm-implementation` loads `<token>-implementation-agent.md` (generic: `implementation-agent.md`)
- `fm-audit` loads `<token>-audit-agent.md` (generic fallback: `review-agent.md`)
- `fm-review` loads `<token>-review-agent.md` (generic: `review-agent.md`)
- `fm-governor` loads `architecture-governor-agent.md`

Domain tokens are file prefixes (`security`, `observability`, `database`,
`fastmcp-auth`, `mcp-protocol`, `sqlalchemy`, `testing`, `ci-cd`, ...).
Dispatch via `/fm <role> <task>` or `@fm-<role>`.
