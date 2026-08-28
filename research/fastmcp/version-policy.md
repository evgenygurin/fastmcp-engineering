# FastMCP Version Policy

## Production baseline

Skills must target the latest stable FastMCP 3.x release unless a project explicitly specifies another version.

## Research channels

For every version-sensitive recommendation, consult:

1. official FastMCP documentation;
2. official FastMCP source when behavior is ambiguous;
3. official `examples/`;
4. official migration/upgrade notes;
5. MCP specification and relevant SEP material.

## Evidence labels

Use one of:

- `V3-STABLE` — supported by the stable 3.x documentation/API.
- `V4-BETA` — prerelease or development material; never present as stable 3.x guidance.
- `PROTOCOL-STANDARD` — behavior defined by MCP rather than FastMCP.
- `VERSION-INDEPENDENT` — architectural guidance not tied to a framework API.
- `PROJECT-DECISION` — local recommendation chosen for this repository.

## No silent API mixing

A skill must not copy an API from FastMCP 4 development material into a FastMCP 3.x implementation without an explicit compatibility note and project target change.

## Protocol-era awareness

FastMCP 4 research must be tracked separately because the project documents a newer protocol/session model and additional runtime capabilities. The architecture system must preserve stable 3.x guidance while keeping a migration/compatibility stream.

## Upgrade workflow

When a project upgrades FastMCP:

```text
Current lockfile
  -> release notes
  -> migration guide
  -> affected API search
  -> official examples
  -> tests
  -> architecture review
  -> dependency lock update
```

No framework upgrade is complete based solely on a successful import or startup.
