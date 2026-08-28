# Component Boundaries

FastMCP-facing components are adapters at the delivery boundary. They are not automatically the application layer.

```text
MCP Client / Model
        |
        v
Tool / Resource / Prompt
        |
        v
Application Use Case / Port
        |
        +---- Domain
        |
        +---- Infrastructure implementations
```

Provider, Transform, and Middleware are separate mechanisms with separate responsibilities and must not be used as arbitrary service containers.

The component layer may handle protocol concerns such as schema validation, MCP Context access, component metadata, protocol-specific result/error translation, and delegation. Business invariants and persistence policy belong behind the application boundary unless an Architecture Governor decision explicitly documents otherwise.

For every component, document the public contract, authorization, side effects, failure semantics, and test seam.