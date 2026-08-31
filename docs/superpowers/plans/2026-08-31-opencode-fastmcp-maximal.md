# Opencode × fastmcp-engineering Maximal Integration Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Экспонировать все возможности fastmcp-engineering (116 prompts через 5 fm-ролей, canonical layout в репо, глобальные симлинки) в любой opencode-проект + закрыть риски dirty-клона.

**Architecture:** Каноничные `opencode/agents/` + `opencode/commands/` в репо (версионированы, PR-reviewed); глобальная видимость — файловые симлинки в `~/.config/opencode/{agents,commands}/`; fm-агенты в runtime читают `prompts/<domain>-<role>-agent.md` из PRIMARY-клона с fallback на reference-клон (авто-синк, ноль дублирования).

**Tech Stack:** opencode 1.17.x (agents/commands markdown frontmatter, permission keys, `opencode debug config`), git/gh, bash-симлинки. Спека: `docs/superpowers/specs/2026-08-31-opencode-fastmcp-maximal-design.md`.

## Global Constraints

- Репо: `/Users/laptop/dev/fastmcp-engineering`, ветка `feat/opencode-agents-wiring` (уже содержит спек-коммиты `e630e62`, `d72a628`); base `6cefef3` (main)
- Conventional Commits; workflow репо: одна ветка → один PR → merge → delete branch → verify main
- НЕ менять: `~/.config/opencode/opencode.json` (skills.paths/references/plugin остаются), верифицированный плагин `~/.config/opencode/plugin/fastmcp-engineering.ts` (PASS 2026-08-30), глобальный `~/.config/opencode/AGENTS.md`
- Markdown-агенты: frontmatter `description` (обязателен, ≤1024 chars), `mode: subagent`; permission-ключи строго из доков: `edit`, `bash` (glob-паттерны, `*` wildcard ПЕРВЫМ — last match wins), `webfetch`, `websearch`, `skill`, `external_directory`
- PRIMARY prompts: `/Users/laptop/dev/fastmcp-engineering/prompts/`; FALLBACK: `~/.local/share/opencode/repos/github.com/evgenygurin/fastmcp-engineering@main/prompts/`
- Роли: `fm-research`, `fm-implementation`, `fm-audit`, `fm-review`, `fm-governor`; generic-фолбэки: `research-agent.md`, `implementation-agent.md`, `review-agent.md`, `architecture-governor-agent.md`; **fm-audit → `review-agent.md`** (generic audit отсутствует)
- Junk `main.py`, `pyproject.toml` (untracked, артефакты `uv init`) — удалить с диска, git-коммита не требуют и не допускают
- `mcp.telegram.enabled: false` в `.opencode/opencode.json` остаётся (локальный dev-выбор)
- Имена файлов/агентов соответствуют `^[a-z0-9]+(-[a-z0-9]+)*$`

---

### Task 1: Repo hygiene — закоммитить load-bearing WIP, удалить uv-init junk

**Files:**
- Modify (уже в working tree): `skills/async/async-event-driven-engineering/SKILL.md`, `skills/ci-cd/github-actions-engineering/SKILL.md`, `skills/fastmcp-research/SKILL.md`, `skills/fastmcp/auth/SKILL.md`, `skills/fastmcp/components/SKILL.md`, `skills/foundation/research-first/SKILL.md`, `skills/schema/pydantic-engineering/SKILL.md`, `AGENTS.md`
- Delete (уже в working tree): `skills/configuration/dependency-management/SKILL.md`, `skills/observability-telemetry-engineering/SKILL.md`
- Add (untracked): `docs/superpowers/plans/2026-08-30-opencode-plugin-deep-verification.md`, `docs/superpowers/plans/2026-08-30-opencode-plugin-verification-report.md`
- Remove from disk (untracked junk, БЕЗ git-операций): `main.py`, `pyproject.toml`

**Interfaces:**
- Consumes: none
- Produces: clean working tree кроме `.opencode/opencode.json` (сфера Task 2); skills с frontmatter стабильны для глобальной загрузки

- [ ] **Step 1: Verify WIP state matches expectation**

```bash
cd /Users/laptop/dev/fastmcp-engineering && git status -sb
# Expected: M .opencode/opencode.json, M AGENTS.md, 7 M skills/*.md, 2 D skills/*,
# ?? docs/superpowers/plans/2026-08-30-*.md (2 файла), ?? main.py, ?? pyproject.toml
```

- [ ] **Step 2: Validate every modified SKILL.md has required frontmatter**

```bash
for f in skills/async/async-event-driven-engineering/SKILL.md skills/ci-cd/github-actions-engineering/SKILL.md skills/fastmcp-research/SKILL.md skills/fastmcp/auth/SKILL.md skills/fastmcp/components/SKILL.md skills/foundation/research-first/SKILL.md skills/schema/pydantic-engineering/SKILL.md; do
  head -1 "$f" | grep -q '^---$' && grep -m1 '^name:' "$f" && grep -m1 '^description:' "$f" || echo "FAIL: $f"
done
# Expected: каждый файл печатает name: и description:, ни одного FAIL
```

- [ ] **Step 3: Validate the 2 deleted files were duplicates (name collision with remaining skills)**

```bash
git show HEAD:skills/configuration/dependency-management/SKILL.md | grep -m1 '^name:'
# Expected: name: configuration-dependency-management
ls skills/ | grep -c '^configuration'
# Expected: >=1 (остаётся skills/configuration/ + configuration-environment-engineering)
git show HEAD:skills/observability-telemetry-engineering/SKILL.md | grep -m1 '^name:'
# Expected: name: observability-telemetry-engineering
ls skills/observability/
# Expected: diagnostics/ opentelemetry/ operations/ (3 суб-скилла остаются)
```

- [ ] **Step 4: Commit WIP + verification docs (НЕ добавлять .opencode/opencode.json, main.py, pyproject.toml)**

```bash
git add AGENTS.md skills/ docs/superpowers/plans/2026-08-30-opencode-plugin-deep-verification.md docs/superpowers/plans/2026-08-30-opencode-plugin-verification-report.md
git commit -m "chore: commit load-bearing skills frontmatter, dedup, gitnexus block, plugin verification docs"
```

- [ ] **Step 5: Remove uv-init junk from disk (untracked — no git action)**

```bash
rm main.py pyproject.toml
git status -sb
# Expected: только " M .opencode/opencode.json" (сфера Task 2)
```

---

### Task 2: Верифицировать и починить skills-путь в .opencode/opencode.json

**Files:**
- Modify: `.opencode/opencode.json` (поле `skills.paths`)

**Interfaces:**
- Consumes: Task 1 (clean tree кроме этого файла)
- Produces: верифицированная форма `skills.paths`, работающая при запуске opencode внутри репо

- [ ] **Step 1: Check available opencode CLI introspection commands**

```bash
opencode --help 2>&1 | grep -iE 'skill|debug|config'
# Записать вывод: есть ли `opencode skill list` / `opencode debug config`
```

- [ ] **Step 2: Empirically test current form ["skills"]**

Если Step 1 нашёл команду листинга скиллов (например `opencode skill list`):
```bash
opencode skill list 2>&1 | grep -c .
# Expected: >0 скиллов; проверить, что fastmcp-auth или другой из репо присутствует
```
Если команды нет — использовать `opencode debug config`:
```bash
opencode debug config 2>&1 | grep -A5 '"skills"'
# Записать, как резолвится путь
```

- [ ] **Step 3: If skills NOT loading — test alternative form ["../skills"]**

```bash
# изменить "paths": ["skills"] → "paths": ["../skills"] в .opencode/opencode.json
# повторить проверку из Step 2; записать, какая форма грузит скиллы
```

- [ ] **Step 4: Decision rule if both forms inconclusive**

Оставить `"../skills"]` — соответствует документированной конвенции opencode «paths relative to the config file directory» (поведение `{file:}`, config docs) и форме, смерженной в PR #98. Записать evidence gap в тело коммита.

- [ ] **Step 5: Commit**

```bash
git add .opencode/opencode.json
git commit -m "fix(opencode): verified skills path resolution in project config"
git status -sb
# Expected: clean
```

---

### Task 3: fm-агенты + команды + README (core deliverable)

**Files:**
- Create: `opencode/agents/fm-research.md`, `opencode/agents/fm-implementation.md`, `opencode/agents/fm-audit.md`, `opencode/agents/fm-review.md`, `opencode/agents/fm-governor.md`
- Create: `opencode/commands/fm.md`, `opencode/commands/fm-prompts.md`
- Modify: `README.md` (новая секция «opencode integration»)

**Interfaces:**
- Consumes: PRIMARY/FALLBACK prompts-пути (Global Constraints)
- Produces: 7 каноничных файлов, на которые Task 4 навешивает симлинки; роли `fm-*` с точными permissions

- [ ] **Step 1: Write `opencode/agents/fm-research.md` (полный контент ниже, дословно)**

````markdown
---
description: fastmcp-engineering evidence-first research agent for a task domain (official docs via context7/exa/gitnexus) — dispatch before design or implementation of any FastMCP/MCP feature
mode: subagent
permission:
  edit: deny
  bash:
    "*": ask
    "git log*": allow
    "git diff*": allow
    "git show*": allow
    "ls *": allow
  webfetch: allow
  websearch: allow
  skill: allow
  external_directory: allow
---

You are the fastmcp-engineering RESEARCH agent — a role-runner for the canonical
prompts of the fastmcp-engineering methodology.

## Procedure (mandatory)

1. Read the dispatched task. Identify its engineering domain token. Known tokens
   (non-exhaustive, they are exact file prefixes in `prompts/`): api-contract,
   api-lifecycle, api-tool, application-architecture, application-domain,
   architecture, async-event-driven, ci-cd, config-dependency, configuration,
   data-persistence, database, dependency-injection, dependency-supply-chain,
   deployment-operations, documentation, engineering-governance, fastmcp-auth,
   fastmcp-client-testing, fastmcp-components, fastmcp-context-di,
   fastmcp-lifespan, fastmcp-middleware, fastmcp-protocol-compliance,
   fastmcp-providers, fastmcp-tasks, fastmcp-transforms,
   fastmcp-transports-deployment, github-lifecycle, mcp-primitives,
   mcp-protocol, mcp-server, observability, packaging-build-deployment,
   pattern-selection, performance-capacity, pydantic, pydantic-ai,
   pydantic-schema, reliability-resilience, security, sqlalchemy, testing.
2. Load your role prompt, in this order:
   - PRIMARY: `/Users/laptop/dev/fastmcp-engineering/prompts/<token>-research-agent.md`
   - FALLBACK: `~/.local/share/opencode/repos/github.com/evgenygurin/fastmcp-engineering@main/prompts/<token>-research-agent.md`
   - No domain match → generic `research-agent.md` (same two locations).
   - Unsure of the token → run `ls /Users/laptop/dev/fastmcp-engineering/prompts/`
     and pick the closest prefix.
3. Follow the loaded prompt verbatim — including its mandatory evidence-first
   research gate (official documentation via context7, web search via exa,
   code graph via gitnexus; never memory-only claims) and its output format.
4. Deliver exactly the artifact the prompt requires (research package with
   evidence links, version pins, gaps). If required evidence is unobtainable,
   stop and report what is missing — never guess.

## Boundaries

- Read-only: you produce research artifacts, not code changes.
- You run as a subagent: report back to the dispatcher with the complete
  artifact; do not ask the end user questions unless the loaded prompt
  mandates it.
- Never substitute memory for current official evidence.
````

- [ ] **Step 2: Write `opencode/agents/fm-implementation.md`**

````markdown
---
description: fastmcp-engineering implementation agent — TDD execution of a researched task following the domain implementation prompt
mode: subagent
permission:
  edit: allow
  bash: allow
  skill: allow
  external_directory: allow
---

You are the fastmcp-engineering IMPLEMENTATION agent — a role-runner for the
canonical prompts of the fastmcp-engineering methodology.

## Procedure (mandatory)

1. Read the dispatched task. Identify its engineering domain token (exact file
   prefix in `prompts/`; see the non-exhaustive list in the repository's
   `prompts/` directory listing).
2. Load your role prompt, in this order:
   - PRIMARY: `/Users/laptop/dev/fastmcp-engineering/prompts/<token>-implementation-agent.md`
   - FALLBACK: `~/.local/share/opencode/repos/github.com/evgenygurin/fastmcp-engineering@main/prompts/<token>-implementation-agent.md`
   - No domain match → generic `implementation-agent.md` (same two locations).
   - Unsure of the token → run `ls /Users/laptop/dev/fastmcp-engineering/prompts/`
     and pick the closest prefix.
3. Follow the loaded prompt verbatim — including its research gate, TDD cycle
   (failing test → minimal implementation → green → refactor), static analysis,
   and verification requirements.
4. If required evidence (docs, examples, version semantics) is unobtainable,
   stop and report what is missing — never guess an API.

## Boundaries

- Write access is for implementing the dispatched task only; do not
  restructure code outside the task scope.
- Run the repository's verification suite before reporting done; report
  commands and outputs as evidence.
- You run as a subagent: report back to the dispatcher.
````

- [ ] **Step 3: Write `opencode/agents/fm-audit.md`**

````markdown
---
description: fastmcp-engineering adversarial audit agent for an area (architecture, data, security, observability, performance, protocol) against repository contracts
mode: subagent
permission:
  edit: deny
  bash:
    "*": ask
    "git log*": allow
    "git diff*": allow
    "git show*": allow
    "ls *": allow
  webfetch: allow
  skill: allow
  external_directory: allow
---

You are the fastmcp-engineering AUDIT agent — a role-runner for the canonical
audit prompts of the fastmcp-engineering methodology.

## Procedure (mandatory)

1. Read the dispatched task. Identify its engineering domain token (exact file
   prefix in `prompts/`; audit prompts exist for: application-architecture,
   data-persistence, database-persistence, dependency-supply-chain,
   deployment-operations, engineering-governance, mcp-protocol, observability,
   performance-capacity, pydantic-ai-agent, reliability-resilience,
   security-privacy — run `ls /Users/laptop/dev/fastmcp-engineering/prompts/`
   to confirm current inventory).
2. Load your role prompt, in this order:
   - PRIMARY: `/Users/laptop/dev/fastmcp-engineering/prompts/<token>-audit-agent.md`
   - FALLBACK: `~/.local/share/opencode/repos/github.com/evgenygurin/fastmcp-engineering@main/prompts/<token>-audit-agent.md`
   - No domain match → generic fallback `review-agent.md` (same two locations)
     — there is no generic audit prompt.
3. Follow the loaded prompt verbatim — including its evidence-first procedure
   (repository contracts, official docs, version pins) and its verdict/output
   format.
4. An audit reports findings and verdicts; it never edits code. If required
   evidence is unobtainable, stop and report what is missing.

## Boundaries

- Read-only: findings, evidence references (file:line), verdicts.
- You run as a subagent: report back to the dispatcher.
````

- [ ] **Step 4: Write `opencode/agents/fm-review.md`**

````markdown
---
description: fastmcp-engineering evidence-based review agent (code/PR/design) per the review-agent prompt — findings with file:line, no edits
mode: subagent
permission:
  edit: deny
  bash:
    "*": ask
    "git log*": allow
    "git diff*": allow
    "git show*": allow
    "ls *": allow
  webfetch: allow
  skill: allow
  external_directory: allow
---

You are the fastmcp-engineering REVIEW agent — a role-runner for the canonical
review prompt of the fastmcp-engineering methodology.

## Procedure (mandatory)

1. Read the dispatched task (a diff, a PR, a design, or an area).
2. Load your role prompt, in this order:
   - Domain-specific: `/Users/laptop/dev/fastmcp-engineering/prompts/<token>-review-agent.md` (if it exists for the task's domain token)
   - Generic: `/Users/laptop/dev/fastmcp-engineering/prompts/review-agent.md`
   - FALLBACK for both: `~/.local/share/opencode/repos/github.com/evgenygurin/fastmcp-engineering@main/prompts/review-agent.md`
   - Unsure of the token → run `ls /Users/laptop/dev/fastmcp-engineering/prompts/`.
3. Follow the loaded prompt verbatim — including its evidence-first procedure
   and its findings format (every finding cites file:line; severity levels;
   no invented behavior).
4. Reviews never edit code. If required evidence is unobtainable, stop and
   report what is missing.

## Boundaries

- Read-only: findings with file:line references, strengths, severity-ranked
  issues, verdict.
- You run as a subagent: report back to the dispatcher.
````

- [ ] **Step 5: Write `opencode/agents/fm-governor.md`**

````markdown
---
description: fastmcp-engineering Architecture Governor — adversarial design review, responsibility boundaries, and gate verdict before implementation
mode: subagent
permission:
  edit: deny
  bash:
    "*": ask
    "git log*": allow
    "git diff*": allow
    "git show*": allow
    "ls *": allow
  webfetch: allow
  skill: allow
  external_directory: allow
---

You are the fastmcp-engineering ARCHITECTURE GOVERNOR — a role-runner for the
canonical `architecture-governor-agent.md` prompt.

## Procedure (mandatory)

1. Read the dispatched task (a design, a plan, or an intended change).
2. Load the governor prompt, in this order:
   - PRIMARY: `/Users/laptop/dev/fastmcp-engineering/prompts/architecture-governor-agent.md`
   - FALLBACK: `~/.local/share/opencode/repos/github.com/evgenygurin/fastmcp-engineering@main/prompts/architecture-governor-agent.md`
3. Follow it verbatim — including its mandatory evidence-first procedure
   (read AGENTS.md and repository contracts; identify target FastMCP version
   and stability; read official docs/examples/source; check MCP spec when
   protocol semantics matter; never silently substitute memory for evidence)
   and its gate-verdict output format.
4. You do not start by writing code. You inspect evidence, establish
   boundaries, and issue a gate verdict. If required evidence is unobtainable,
   stop and report the missing evidence instead of guessing.

## Boundaries

- Read-only: gate verdict, boundary assignments, rejection criteria.
- You run as a subagent: report back to the dispatcher.
````

- [ ] **Step 6: Write `opencode/commands/fm.md`**

````markdown
---
description: Dispatch a fastmcp-engineering workflow task to the matching fm-* subagent
---
Route the following fastmcp-engineering task to the right fm-* subagent using
the task tool.

Routing (first word of the arguments):
- research → subagent_type `fm-research`
- implementation / implement → `fm-implementation`
- audit → `fm-audit`
- review → `fm-review`
- governor / architecture → `fm-governor`
- unknown or missing → `fm-research`

Pass everything after the routing word as the task prompt, verbatim. Wait for
the subagent's result and relay its report. If the subagent reports missing
evidence or a blocked gate, relay that verbatim — do not soften it.

Arguments: $ARGUMENTS
````

- [ ] **Step 7: Write `opencode/commands/fm-prompts.md`**

````markdown
---
description: Inventory of fastmcp-engineering role prompts and the fm-* agent mapping
---
fastmcp-engineering prompts available to the fm-* agents:

!`ls /Users/laptop/dev/fastmcp-engineering/prompts/ 2>/dev/null || ls ~/.local/share/opencode/repos/github.com/evgenygurin/fastmcp-engineering@main/prompts/`

Mapping (loaded at runtime by the fm-* subagents):
- `fm-research` loads `<token>-research-agent.md` (generic: `research-agent.md`)
- `fm-implementation` loads `<token>-implementation-agent.md` (generic: `implementation-agent.md`)
- `fm-audit` loads `<token>-audit-agent.md` (generic fallback: `review-agent.md`)
- `fm-review` loads `<token>-review-agent.md` (generic: `review-agent.md`)
- `fm-governor` loads `architecture-governor-agent.md`

Domain tokens are file prefixes (`security`, `observability`, `database`,
`fastmcp-auth`, `mcp-protocol`, `sqlalchemy`, `testing`, `ci-cd`, ...).
Dispatch via `/fm <role> <task>` or `@fm-<role>`.
````

- [ ] **Step 8: Add README section «opencode integration» (после секции Status)**

````markdown
## opencode integration

Global exposure of this repository's capabilities in opencode:

- **Skills**: global `skills.paths` → this clone (frontmatter `name`+`description` required)
- **Reference**: `references.fastmcp-eng` — whole repo readable in any project
- **Plugin hint**: `~/.config/opencode/plugin/fastmcp-engineering.ts` (verified PASS 2026-08-30)
- **fm-* role agents**: `opencode/agents/` — research/implementation/audit/review/governor subagents; they load `prompts/<token>-<role>-agent.md` at runtime (auto-sync, no duplication)
- **Commands**: `opencode/commands/` — `/fm` dispatcher, `/fm-prompts` inventory

Setup on a new machine (symlinks into global config, run from repo root):

    ln -s "$PWD/opencode/agents/fm-research.md" ~/.config/opencode/agents/fm-research.md
    ln -s "$PWD/opencode/agents/fm-implementation.md" ~/.config/opencode/agents/fm-implementation.md
    ln -s "$PWD/opencode/agents/fm-audit.md" ~/.config/opencode/agents/fm-audit.md
    ln -s "$PWD/opencode/agents/fm-review.md" ~/.config/opencode/agents/fm-review.md
    ln -s "$PWD/opencode/agents/fm-governor.md" ~/.config/opencode/agents/fm-governor.md
    ln -s "$PWD/opencode/commands/fm.md" ~/.config/opencode/commands/fm.md
    ln -s "$PWD/opencode/commands/fm-prompts.md" ~/.config/opencode/commands/fm-prompts.md

Design: `docs/superpowers/specs/2026-08-31-opencode-fastmcp-maximal-design.md`
````

- [ ] **Step 9: Structural validation**

```bash
cd /Users/laptop/dev/fastmcp-engineering
for f in opencode/agents/*.md; do
  head -1 "$f" | grep -q '^---$' && grep -m1 '^description:' "$f" >/dev/null && grep -m1 '^mode: subagent' "$f" >/dev/null && grep -m1 '^permission:' "$f" >/dev/null && echo "OK: $f" || echo "FAIL: $f"
done
# Expected: 5× OK, 0× FAIL
for f in opencode/commands/*.md; do
  head -1 "$f" | grep -q '^---$' && grep -m1 '^description:' "$f" >/dev/null && echo "OK: $f" || echo "FAIL: $f"
done
# Expected: 2× OK, 0× FAIL
grep -c 'fm-' README.md
# Expected: >=6
```

- [ ] **Step 10: Commit**

```bash
git add opencode/ README.md
git commit -m "feat(opencode): fm role agents, commands, README integration section"
```

---

### Task 4: Глобальные симлинки + верификация (machine-local, без коммита в репо)

**Files:**
- Create (symrefs): `~/.config/opencode/agents/fm-{research,implementation,audit,review,governor}.md`, `~/.config/opencode/commands/{fm,fm-prompts}.md`

**Interfaces:**
- Consumes: Task 3 files
- Produces: глобально видимые fm-агенты и команды во всех проектах

- [ ] **Step 1: Create 7 symlinks**

```bash
mkdir -p ~/.config/opencode/agents ~/.config/opencode/commands
cd /Users/laptop/dev/fastmcp-engineering
for a in fm-research fm-implementation fm-audit fm-review fm-governor; do
  ln -sf "$PWD/opencode/agents/$a.md" ~/.config/opencode/agents/$a.md
done
ln -sf "$PWD/opencode/commands/fm.md" ~/.config/opencode/commands/fm.md
ln -sf "$PWD/opencode/commands/fm-prompts.md" ~/.config/opencode/commands/fm-prompts.md
```

- [ ] **Step 2: Verify symlinks resolve**

```bash
ls -la ~/.config/opencode/agents/ ~/.config/opencode/commands/ | grep '\->'
# Expected: 7 симлинков на /Users/laptop/dev/fastmcp-engineering/opencode/...
for f in ~/.config/opencode/agents/fm-*.md ~/.config/opencode/commands/fm*.md; do
  test -r "$f" && echo "OK: $f" || echo "BROKEN: $f"
done
# Expected: 7× OK
```

- [ ] **Step 3: Verify opencode loads them (new process)**

```bash
cd /tmp && opencode debug config 2>&1 | grep -iE 'fm-(research|implementation|audit|review|governor)|"fm"|"fm-prompts"'
# Expected: fm-агенты и/или fm-команды видны в resolved config
# Если debug config их не показывает — проверить наличие иной команды листинга
# из Task 2 Step 1; если и её нет, финальный smoke: opencode run "/fm-prompts"
# из /tmp (новый процесс) — ожидание: инвентаризация промптов в ответе
```

- [ ] **Step 4: Skills regression check (глобальная загрузка не сломана)**

```bash
# командой листинга скиллов из Task 2 Step 1 (если есть):
opencode skill list 2>&1 | grep -c .
# Expected: счётчик скиллов >= 44 (глобальные из fastmcp-engineering) — записать число
# иначе: opencode debug config | grep -A3 skills — пути на месте
```

- [ ] **Step 5: Записать verification evidence (выводы Step 3-4) — без коммита**

---

### Task 5: Push + PR (repo workflow)

**Files:** none (git operations)

**Interfaces:**
- Consumes: Tasks 1-4 (commits `e630e62`, `d72a628`, + 3 новых)

- [ ] **Step 1: Final state check**

```bash
cd /Users/laptop/dev/fastmcp-engineering
git status -sb && git log --oneline main..HEAD
# Expected: clean tree; 5 коммитов поверх 6cefef3
```

- [ ] **Step 2: Push + PR**

```bash
git push -u origin feat/opencode-agents-wiring
gh pr create --base main --head feat/opencode-agents-wiring \
  --title "feat(opencode): fm role agents + commands, maximal integration" \
  --body "Implements docs/superpowers/specs/2026-08-31-opencode-fastmcp-maximal-design.md.

## What
- 5 fm-* role subagents (opencode/agents/) loading prompts/<token>-<role>-agent.md at runtime (PRIMARY dev clone, FALLBACK reference clone; generic fallbacks; fm-audit → review-agent.md)
- Commands /fm (dispatcher) + /fm-prompts (inventory of 116 prompts)
- README «opencode integration» section (symlink setup for other machines)
- Repo hygiene: load-bearing SKILL.md frontmatter committed, 2 duplicate skills removed, gitnexus AGENTS.md block, plugin verification docs 2026-08-30, uv-init junk removed
- .opencode/opencode.json skills path empirically verified

## Permissions (per role)
- fm-research / fm-audit / fm-review / fm-governor: edit deny, read-only git bash allows, webfetch/skill/external_directory allow
- fm-implementation: edit+bash allow, skill/external_directory allow

## Evidence
- Symlinks: 7/7 resolve
- opencode load check: <вставить вывод Task 4 Step 3>
- Skills regression: <вставить вывод Task 4 Step 4>

Merge → delete branch → verify main (repo workflow)."
# Вернуть PR URL. Merge/delete branch — по решению владельца.
```

## Self-Review

- Spec coverage: §3.1 layout → Task 3; §3.2 symlinks → Task 4; §3.3 контракт+permissions → Task 3 Steps 1-5; §3.4 команды → Task 3 Steps 6-7; §3.5 коммиты → Tasks 1,2,3,5 (junk-«коммит» из спеки скорректирован: untracked-файлы удаляются с диска без git-операции); §3.6 edge cases → зашиты в контент агентов (fallback-пути, generic); §4 verification → Tasks 2,4
- Placeholders: нет — все 7 файлов даны дословно
- Type consistency: роли/имена файлов совпадают между Task 3, Task 4, README, командами
