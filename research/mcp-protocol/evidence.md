# MCP Protocol Research Evidence Ledger

Research target: MCP specification `2026-07-28` (current stable specification as of 2026-08-29) and current FastMCP 3.x documentation. Version-sensitive implementation choices must be re-checked against the exact project dependency versions before code changes.

| Topic | Required source | Version/date | Finding | Confidence | Consequence |
|---|---|---|---|---|---|
| Lifecycle | Official MCP specification / release notes | 2026-07-28 | Core protocol is stateless: no initialize handshake/session is required; modern requests are self-describing and discovery is optional. | High | Do not impose legacy initialize/session assumptions on modern implementations. |
| Version negotiation | Official MCP specification / SDK version docs | 2026-07-28 | Modern protocol uses the stateless lifecycle; older handshake versions remain compatibility targets. | High | Maintain explicit supported-version matrix; never silently mix lifecycle eras. |
| Capabilities | Official MCP specification | 2026-07-28 | Discovery/capability information is explicit and requests can be routed without deep JSON inspection. | High | Advertise only implemented capabilities and test discovery/compatibility. |
| Transports | Official MCP specification / FastMCP docs | 2026-07-28 / current | Streamable HTTP remains the remote transport; modern protocol adds routing headers and removes dependence on long-lived bidirectional sessions. | High | Transport design must account for ordinary HTTP load balancing and header consistency. |
| Sessions | Official MCP specification | 2026-07-28 | Stateless protocol core removes protocol-level handshake/session requirements; applications may still maintain state. | High | Keep application state explicit and independently scoped; do not confuse application state with protocol sessions. |
| Cancellation | Official MCP specification + FastMCP Context docs | Current | Cancellation must propagate to in-flight work and release resources. | High | Test cancellation, timeouts and cleanup at protocol and application boundaries. |
| Tools | Official MCP specification + FastMCP docs | 2026-07-28 / current | Tools are executable capabilities; current spec supports full JSON Schema 2020-12 input/output schemas. | High | Define explicit schemas and test invalid input/output contracts. |
| Resources | Official MCP specification + FastMCP docs | 2026-07-28 / current | Resources expose read-oriented data; templates parameterize resource URIs; list/read results have cache hints. | High | Define URI ownership/authorization and deterministic resource behavior; respect cache scope/TTL. |
| Prompts | Official MCP specification + FastMCP docs | 2026-07-28 / current | Prompts are distinct reusable message templates and remain a first-class MCP primitive. | High | Keep prompt contracts separate from tools/resources and validate arguments. |
| Errors | Official MCP specification | 2026-07-28 | Protocol errors and application/tool errors remain distinct; resource-not-found mapping changed to standard Invalid Params in this revision. | High | Preserve protocol error semantics and avoid leaking internal details. |
| Authorization | Official MCP authorization specification / release notes | 2026-07-28 | Authorization hardening includes RFC 9207 issuer validation and movement away from DCR toward client metadata documents. | High | Treat authorization as a protocol boundary and validate issuer/resource/audience as applicable. |
| Tasks | Official Tasks extension | Current draft | Tasks are an extension for durable async tool execution with `tasks/get`, `tasks/update`, `tasks/cancel`; task creation must be durable before its handle is returned. | High | Treat Tasks as optional extension, not core protocol, and model task state/recovery explicitly. |
| Deprecations | Official MCP specification/release notes | 2026-07-28 | Roots, Sampling and Logging are deprecated but remain supported during the deprecation window. | High | Do not build new architecture around deprecated features without an explicit compatibility reason. |
| FastMCP components | Official FastMCP docs | Current 3.x docs | FastMCP exposes tools, resources, prompts and provider abstractions; providers can source components from local/remote/database-backed sources. | High | Prefer native FastMCP primitives/providers over custom protocol plumbing. |
| FastMCP Context | Official FastMCP docs | Current 3.x docs | Context provides request information and access to MCP capabilities such as progress, resources, prompts and sampling. | High | Use framework context/lifecycle facilities instead of global mutable state. |

## Authoritative web evidence

- MCP 2026-07-28 release: https://blog.modelcontextprotocol.io/posts/2026-07-28/
- MCP 2026-07-28 release candidate / migration details: https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/
- MCP Tasks extension: https://tasks.extensions.modelcontextprotocol.io/specification/draft/tasks
- FastMCP resources: https://gofastmcp.com/servers/resources
- FastMCP context: https://gofastmcp.com/servers/context
- FastMCP providers: https://gofastmcp.com/servers/providers/overview
- FastMCP client CLI: https://gofastmcp.com/cli/client

## Rule
No `TBD` may remain for a feature used by an implementation. Claims must be tied to authoritative evidence; secondary articles cannot override the protocol specification. Before implementation, re-check the exact installed MCP/FastMCP dependency versions and replace any broader current-version claim with exact-version evidence where behavior differs.
