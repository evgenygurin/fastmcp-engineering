# Research Notes

Current first-party evidence used to shape this skill:

- pytest documents fixtures as explicit, modular and scalable, with lifecycle-aware scopes and guaranteed teardown/finalization.
- pytest supports parametrizing tests and fixtures and recommends meaningful parametrization rather than duplicated test bodies.
- PydanticAI documents TestModel and FunctionModel as deterministic alternatives to live models, Agent.override for replacing model/dependencies/toolsets, and blocking accidental live requests in tests.
- PydanticAI's current toolset documentation demonstrates TestModel as a practical way to inspect available tools.

These notes are intentionally a compact evidence index; implementation agents must re-check exact current documentation and repository examples before coding.