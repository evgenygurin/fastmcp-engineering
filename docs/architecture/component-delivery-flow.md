# Component Delivery Flow

This is the default implementation flow for FastMCP Tools, Resources, and Prompts.

```text
Requirement
    |
    v
Research Package
    |
    v
Component Classification
    |
    +---- Provider / Transform / Middleware / Context alternatives
    |
    v
Public MCP Contract
    |
    v
Architecture Gate
    |
    v
Application Boundary
    |
    v
TDD
    |
    v
Thin MCP Adapter
    |
    v
MCP Client / Integration Verification
    |
    v
Architecture Re-check
    |
    v
Final Verification
```

A component must not bypass research or architecture review merely because its implementation appears small. Small protocol adapters can still introduce public contract, authorization, compatibility, and data-exposure defects.