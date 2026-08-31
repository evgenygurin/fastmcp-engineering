---
description: Dispatch a fastmcp-engineering workflow task to the matching fm-* subagent
---
Route the following fastmcp-engineering task to the right fm-* subagent using
the task tool.

Routing (first word of the arguments):
- research → subagent_type `fm-research`
- implementation / implement → `fm-implementation`
- audit → `fm-audit`
- review → `fm-review`
- governor / architecture → `fm-governor`
- unknown or missing → `fm-research`

Pass everything after the routing word as the task prompt, verbatim. Wait for
the subagent's result and relay its report. If the subagent reports missing
evidence or a blocked gate, relay that verbatim — do not soften it.

Arguments: $ARGUMENTS
