# Components Version Gate

FastMCP component APIs are version-sensitive. Before implementation, the agent must record the exact target version and verify the relevant API against current first-party documentation/source.

## Required checks

- [ ] Target FastMCP version recorded.
- [ ] Stable/prerelease status recorded.
- [ ] Tool API verified.
- [ ] Resource API verified.
- [ ] Prompt API verified.
- [ ] Schema/validation behavior verified.
- [ ] Result/error behavior verified.
- [ ] Context/DI behavior verified if used.
- [ ] Client/testing behavior verified if relevant.
- [ ] Relevant migration notes checked.

## Rule

Examples from another major version are evidence of historical design, not authorization to copy an API. If an example conflicts with the target version's documentation/source/tests, the target version wins and the conflict must be recorded.
