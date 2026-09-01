# FastMCP v4 Methodology Server — Design

- Date: 2026-09-01
- Status: approved (brainstorming, all design sections user-approved)
- Target: `fastmcp>=4.0.0,<4.1` · Python >=3.10 · stdio (local, unauthenticated)
- Branch: `feat/server-v4` (single PR per `contracts/github-workflow-contract.md`)

## 1. Problem / Goal

fastmcp-engineering ships its methodology — 58 skills, 9 contracts, 116 role
prompts, research artifacts — as repository content consumable only through
per-harness plugins. The goal is to expose these capabilities as a FastMCP v4
MCP server: the "methodology brain" that any coding agent (opencode, Claude
Code, Codex, Cursor) connects to over stdio and uses during work.

Non-goals (v1): HTTP deployment, authentication, `fastmcp-tasks`, research
artifacts as served content, modifying existing repository content.

## 2. Evidence base (official sources only)

- gofastmcp.com: `getting-started/whats-new.md`,
  `getting-started/upgrading/from-fastmcp-3.md`, `servers/providers/skills.md`,
  `servers/providers/filesystem.md`, `servers/completions.md`,
  `servers/sessions.md`, `servers/extensions.md`,
  `servers/storage-backends.md`, `deployment/server-configuration.md`,
  `servers/testing.md`, `llms.txt` index.
- PrefectHQ/fastmcp @ `v4.0.0` (stable since 2026-08-31): release notes,
  repository tree (`fastmcp_slim/`, `fastmcp_tasks/`, `examples/`, `tests/`),
  upstream `CLAUDE.md`.
- Local facts: `skills/` — 58 `SKILL.md` files with `name`/`description`
  frontmatter plus sibling `ACCEPTANCE.md`; `contracts/` — 9 markdown
  contracts; `prompts/` — 116 markdown role prompts.
- Claims not covered by the docs above are marked **unverified** and carry a
  verification step (Section 12).

## 3. Architecture

Everything lives inside fastmcp-engineering; the server is a new deliverable,
not a modification of existing content.

```
fastmcp-engineering/
├── server/
│   ├── server.py        # FastMCP("fastmcp-engineering"): provider composition
│   │                    # + @mcp.completion + add_extension + SessionProvider
│   ├── components/      # scanned by FileSystemProvider:
│   │   ├── find_skills.py   # @tool find_skills + @tool clarify_find
│   │   ├── contracts.py     # @resource("contract://{name}")
│   │   └── prompts.py       # @resource("fme-prompt://{name}") + 5 @prompt defs
│   ├── extension.py     # MethodologyExtension (ServerExtension)
│   └── indexing.py      # startup index over skills/, contracts/, prompts/
├── fastmcp.json         # strict JSON, $schema v1
└── tests/server/        # in-memory Client tests (pytest + pytest-asyncio)
```

Responsibility boundaries: providers are content sources; `components/` are
thin adapters; `indexing.py` owns search; `server.py` owns composition only.

## 4. Component surface

| Surface | Mechanism | Contract |
| --- | --- | --- |
| 58 skills | `SkillsDirectoryProvider(roots=[<repo>/skills])` | `skill://<name>/SKILL.md`, `skill://<name>/ACCEPTANCE.md`, `skill://<name>/_manifest` (SHA256), supporting files; traversal/null-byte/symlink protection built in |
| 9 contracts | resource template `contract://{name}` | lazy disk read per request; content always current |
| 116 prompts | resource template `fme-prompt://{name}` | lazy disk read; not MCP prompts (client list hygiene) |
| Search | `@tool find_skills(task, domain=None, limit=5, session_id=None)` | ranked matches `[{name, description, uri, domain, score}]` |
| Clarify | `@tool clarify_find(task)` | interactive: `InputRequiredResult` domain question → re-run with `ctx.input_responses` |
| MCP prompts (5) | `dispatch(task)`, `skill_context(skill)`, `domain_guide(domain, task)`, `role_prompt(role)`, `contract_check(contract, artifact)` | parameterized; completions on all name args |
| Completions | single `@mcp.completion` handler in `server.py` | prompt + resource-template references, both protocol eras |
| Extension | `MethodologyExtension` (`dev.fastmcp-eng/methodology`) | `settings()` metadata, additive `methodology/stats` method, tool-call interceptor counters |

## 5. v4 primitives (full showcase, per approved revision)

| Primitive | Decision | Detail |
| --- | --- | --- |
| Argument completion | use | every name argument of the 5 prompts + both resource templates; prefix filter via `argument.value`; use `context.arguments` where applicable |
| Resource templates | use | `contract://{name}`, `fme-prompt://{name}` |
| Dual-era negotiation | use (free) | any v4 server serves both protocol eras per connection |
| Session state | use, verify | `SessionProvider()` + `SessionId` on `find_skills`; search history boosts recently used domains (×1.5). **Unverified:** `SessionId`/`create_session` behavior without auth on stdio — decided by test; fallback is a plain string argument with an in-memory history map |
| Server extension | use | `ServerExtension` subclass, reverse-DNS identifier; `settings()` → skill/domain counts + repo version under `capabilities.extensions`; `MethodBinding(method="methodology/stats")` returning index summary; tool-call interceptor counting tool usage |
| Interactive tools | use | `clarify_find` returns `InputRequiredResult` when top score is below threshold; stdio is single-process so `RequestStateSecurity` uses the automatic process-local key (no config); non-interactive `find_skills` remains the fallback path |
| Storage | in-memory default | stdio single-process norm; `FileTreeStore`/Redis documented in docs as future HTTP options |

## 6. Data flows

1. **Startup**: `SkillsDirectoryProvider` scans `skills/`; `indexing.py`
   parses each `SKILL.md` fully into an in-memory index
   `{name, description, domain, path, tokens}` with term weights
   `name ×3, description ×2, body ×1`. Contracts and prompts are indexed by
   name only and read from disk lazily per request.
2. **find_skills**: deterministic token-overlap scoring over the index;
   optional domain filter (domains = skill subdirectories, derived from the
   index at startup, never hardcoded); session history boost for recently
   used domains; returns top-N with scores.
3. **skill_context(skill)**: validate against index → read `SKILL.md` →
   return an execution prompt embedding the skill content.
4. **dispatch(task)**: routing prompt = top `find_skills` matches + domain
   index. **domain_guide(domain, task)**: domain-specific routing.
   **role_prompt(role)**: returns the named prompt file content.
   **contract_check(contract, artifact)**: returns a verification prompt
   embedding the contract.
5. **Completions**: filter candidate names by typed prefix per reference.
6. **clarify_find**: low top-score → `InputRequiredResult` with a domain
   question; next round reads `ctx.input_responses` and re-runs the search.

## 7. Error handling

- Unknown `skill`/`contract`/`role` name → clear MCP error listing nearest
  valid names; never a silent empty read.
- `find_skills` with no matches → empty result plus a hint (not an error).
- Content file missing on disk between requests → error naming the path.
- Completion handler returns `None` for unrecognized references (protocol-
  correct empty answer).
- Interactive flow declined or unanswered → correct non-interactive result.
- No tracebacks leak to clients; MCP error codes only.

## 8. Security

- Skills content protection (traversal, null bytes, symlinks) is provided by
  the official Skills Provider.
- `contract://` and `fme-prompt://` read only from the fixed `contracts/`
  and `prompts/` directories, resolved by name; no user-supplied paths.
- stdio is a deliberate local trust boundary: no auth, no secrets involved.
- Session ids are owned: foreign or unknown ids raise loudly (official
  behavior).

## 9. Testing

Official pattern: in-memory `Client(mcp)` fixtures, `pytest-asyncio`
(`asyncio_mode = auto`), `inline-snapshot` for structural assertions.

- Resources: 58 skills expose `SKILL.md` + `_manifest` (+ `ACCEPTANCE.md`);
  9 contracts; 116 prompts readable.
- `find_skills`: parametrized ranking cases; deterministic scores.
- Completions: both reference kinds, prefix filtering, `context.arguments`.
- Session: `create_session` → `find_skills(session_id=…)` → history boost.
  This test also **decides the unverified SessionId-without-auth question**;
  failure triggers the documented fallback.
- Extension: `settings()` advertised; `methodology/stats` responds;
  interceptor counts calls.
- Interactive: `InputRequiredResult` round-trip via the official Client
  elicitation handler; declined path returns the plain result.
- Repository invariants untouched: 58 `SKILL.md` files remain; `pytest` and
  `ruff check .` green across the whole repository.

## 10. Distribution

- `fastmcp.json` at repo root (strict JSON, no comments):
  `source` → `server/server.py`, entrypoint `mcp`;
  `environment` → uv, `fastmcp>=4.0.0,<4.1`;
  `deployment` → `transport: stdio`, `log_level: INFO`.
- Harnesses connect via `fastmcp run fastmcp.json`; per-harness config
  snippets (opencode, Claude Code, Codex, Cursor) documented in `docs/`.
- Documentation sync in the same PR: README (server as a deliverable), a
  docs page for the server, AGENTS.md note per content-invariant rules.

## 11. Success criteria

An external coding agent over stdio can: find the right skill for a task →
read it → obtain its execution-context prompt → check an artifact against a
contract; completions work in supporting clients; all repository checks
(`pytest`, `ruff check .`) pass.

## 12. Verification points / open questions

1. **SessionId without auth on stdio** — decided by test at implementation
   time; fallback documented in Section 5.
2. Completion and elicitation support varies across coding clients; the
   server degrades gracefully (`None` completions, non-interactive path).
3. Domain values are derived from `skills/` subdirectories at startup.
4. **Nested skill layout** — repository skills live at
   `skills/<domain>/<skill>/SKILL.md` (two levels below the root). Whether
   `SkillsDirectoryProvider` discovers nested skill folders or only direct
   children is not stated explicitly in the official docs; verify against
   source/tests at implementation time. Fallback: pass every
   `skills/<domain>/` directory in the `roots` list (name collisions across
   domains are impossible — skill names are unique repo-wide).

## 13. Out of scope (documented future options)

HTTP deployment with token verification and `UserSession`; `fastmcp-tasks`
background search; embedding-based search; `research/` artifacts as
resources; persistent/distributed storage backends.
