# FastMCP Tasks Architecture Boundaries

```text
MCP request
    |
    v
FastMCP Tool adapter
    |
    +---- synchronous execution
    |
    +---- verified MCP Task boundary
              |
              +---- task state / polling / result protocol
              |
              +---- application command
                         |
                         v
                    domain logic
                         |
                  infrastructure
```

## Rules

1. A protocol task is not automatically a durable job system.
2. A Python background task is not automatically an MCP task.
3. Business logic belongs to application/domain layers.
4. Task ownership must be explicit.
5. Storage/durability must be explicit.
6. Cancellation must be traced through every layer.
7. Retry requires idempotency analysis.
8. Task status/result access is separately authorization-sensitive.
9. Lifespan shutdown must define behavior for queued and running work.
10. Multi-worker claims require shared-state evidence; process-local state must never be described as durable or globally visible.
