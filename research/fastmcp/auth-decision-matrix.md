# FastMCP Authentication / Authorization Decision Matrix

## Core separation

Authentication answers **who/what is calling?** Authorization answers **what may that principal do?**

| Concern | Preferred boundary |
|---|---|
| Credential parsing/validation | FastMCP auth/infrastructure |
| OAuth protocol flow | FastMCP/provider/client boundary |
| Verified principal | Security/application adapter |
| Authorization policy | Application authorization port/policy |
| Domain invariant | Domain |
| Cross-cutting request enforcement | Middleware when appropriate |
| Runtime request/session capability | Context |
| Startup/shutdown auth resources | Lifespan |

## Mandatory questions

1. What authenticates the caller?
2. What makes the resulting identity trustworthy?
3. Which issuer/audience/signature rules apply?
4. What is the principal identifier?
5. Which claims/scopes/roles are trusted?
6. Who owns authorization policy?
7. Is the policy default-deny?
8. What is the tenant boundary?
9. How does the intended client acquire/refresh credentials?
10. What are token lifetime and revocation semantics?
11. What secrets exist and where are they stored?
12. What is the exact public URL/mount/discovery/callback topology?

## Hard anti-patterns

- Treating an unverified JWT claim as identity.
- `if role == ...` scattered across tools.
- Authorization based solely on a client-supplied header.
- Logging Authorization headers or bearer tokens.
- Storing OAuth secrets in source control.
- Assuming an OAuth provider implements MCP discovery/DCR correctly.
- Hardcoding callback URLs that do not match mounted topology.
- Fail-open authorization.
- Making domain code depend on FastMCP `AccessToken` or provider classes.
- Implementing custom auth when a verified native provider already satisfies the requirement.

## Threat matrix

| Threat | Required control |
|---|---|
| Forged token | signature/issuer/audience validation |
| Stolen token | short lifetime, secure transport/storage, refresh/revocation strategy |
| Privilege escalation | explicit policy/default deny |
| Tenant breakout | principal-to-tenant authorization |
| Confused deputy | explicit actor/resource authorization |
| Token leakage | redaction/no credential logging |
| OAuth redirect attack | exact registered callback validation |
| Discovery mismatch | verify metadata against actual deployment |
| Fail-open | negative authorization tests |
