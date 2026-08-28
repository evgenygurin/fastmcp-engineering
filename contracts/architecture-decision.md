# Architecture Decision Contract

Every non-trivial architectural decision must be explicit and reviewable.

```yaml
id: <stable-id>
context: <problem and constraints>
requirement: <concrete requirement>
options:
  - name: <option>
    benefits: []
    costs: []
    risks: []
decision: <selected option>
responsibility: <owning layer/module>
dependencies: []
patterns: []
fastmcp_mechanisms: []
principles:
  solid: []
  kiss: <assessment>
  dry: <assessment>
  yagni: <assessment>
tradeoffs: []
verification: []
```

## Review questions

- Does the decision solve a demonstrated problem?
- Is the owning responsibility unambiguous?
- Are dependencies pointing in the intended direction?
- Could a simpler design satisfy the requirement?
- Is a framework-native FastMCP mechanism sufficient?
- Does the decision introduce an abstraction before it is needed?
- Does it create unnecessary coupling?
- Can the behavior be tested at the appropriate boundary?
