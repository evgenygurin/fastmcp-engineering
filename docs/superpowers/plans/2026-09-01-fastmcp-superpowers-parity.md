# FastMCP Engineering × Superpowers Parity Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Reproduce the `obra/superpowers` three-component architecture (harness-agnostic skills / per-harness tool mapping / session-start bootstrap) so fastmcp-engineering's domain skills auto-trigger in every major coding agent (Claude Code, Cursor, Copilot CLI, Codex, Kimi, OpenCode, pi, Gemini).

**Architecture:** One canonical `skills/using-fastmcp-engineering/SKILL.md` bootstrap injected at session start in every harness (wrapped in `<EXTREMELY_IMPORTANT>` + per-harness tool mapping). Skills stay harness-agnostic (they already name actions, not tools — verified 0 tool mentions). Per-harness wiring ships via each harness's own install mechanism: Shape A shell-hook (Claude Code, Cursor, Copilot CLI), Shape B in-process plugin (OpenCode, pi), Shape C instructions-file (Gemini), native skill discovery (Codex, Kimi).

**Tech Stack:** opencode 1.17.x plugin API (`experimental.chat.messages.transform`, `config`), pi `ExtensionAPI`, Claude Code/Cursor hook JSON, bash/polyglot `run-hook.cmd`, Python pytest contract tests, ruff, shellcheck.

**Spec:** `docs/superpowers/specs/2026-09-01-fastmcp-superpowers-parity-design.md`

## Global Constraints

- Репо: `/Users/laptop/dev/fastmcp-engineering`, ветка `feat/superpowers-parity` (создана, base `f8bd101` main)
- Conventional Commits; workflow репо: одна ветка → один PR → merge → delete branch → verify main
- НЕ менять: глобальный `~/.config/opencode/opencode.json`, глобальный `~/.config/opencode/plugin/fastmcp-engineering.ts` (верифицирован PASS), глобальный `~/.config/opencode/AGENTS.md`, `.codex-plugin/plugin.json` version 0.1.0 (до Task 8)
- НЕ редактировать файлы пользователя ни в одном харнесе (правило 2 superpowers); всё — через install-механизм харнеса
- Скиллы называют действия, а не инструменты: тела 57 доменных SKILL.md не редактируются кроме добавления секций Trigger/Deliverables (Task 2); фикс — только в tool mapping и бутстрапе
- Zero-dependency: никаких новых runtime-зависимостей (кроме type-only импортов для pi-расширения)
- Инъекция бутстрапа — user-сообщение, не system-сообщение (token bloat, поломка Qwen #894)
- Dedup guard (маркер `EXTREMELY_IMPORTANT`) + кэш контента бутстрапа (не читать диск на каждый шаг)
- Hook-скрипты без расширения (`session-start`, не `.sh`); `.gitattributes` — LF для shell/`.cmd`/json/md/js/mjs/ts
- `EXPECTED_SKILL_COUNT`: 57 → 58 (добавляется `using-fastmcp-engineering`)
- Секция-шаблон для доменных скиллов содержит ВСЕ 10 семантических токенов контракта как явные английские лейблы: mission, scope, trigger, upstream, research, decision, verification, failure, deliverables, version
- Scenario-тесты требуют маркеры: positive scenario, negative scenario, evidence/verification (в SKILL.md или ACCEPTANCE.md); stop-condition-тест требует в ACCEPTANCE.md маркеры stop/reject/escalate/deny/must not/invalid
- Репозиторий superpowers-эталон: `~/.config/opencode/superpowers/` (локальный клон, version 6.2.0). Его файлы — образцы для портирования, НЕ копируются целиком с упоминанием чужих доменов
- Имена файлов/агентов/скиллов: `^[a-z0-9]+(-[a-z0-9]+)*$`

---

### Task 1: Бутстрап-скилл `using-fastmcp-engineering` + 8 tool-mapping references

**Files:**
- Create: `skills/using-fastmcp-engineering/SKILL.md`
- Create: `skills/using-fastmcp-engineering/ACCEPTANCE.md`
- Create: `skills/using-fastmcp-engineering/references/claude-code-tools.md`, `cursor-tools.md`, `codex-tools.md`, `copilot-tools.md`, `gemini-tools.md`, `kimi-tools.md`, `opencode-tools.md`, `pi-tools.md`
- Modify: `tests/test_skill_contract.py:9` (`EXPECTED_SKILL_COUNT = 57` → `58`)

**Interfaces:**
- Consumes: none
- Produces: `using-fastmcp-engineering` — скилл, чьё тело читают все инъекторы (Task 3-6); его `references/*-tools.md` — tool mapping для 8 харнесов; `EXPECTED_SKILL_COUNT = 58`

- [ ] **Step 1: Write the bootstrap skill `skills/using-fastmcp-engineering/SKILL.md`**

Дословно (тело содержит ВСЕ 10 контрактных токенов: mission, scope, trigger, upstream, research, decision, verification, failure, deliverables, version):

````markdown
---
name: using-fastmcp-engineering
description: Use when starting any FastMCP/MCP engineering work - establishes how to find and use fastmcp-engineering skills, requiring skill invocation before ANY response including clarifying questions
---

<SUBAGENT-STOP>
If you were dispatched as a subagent to execute a specific task, ignore this skill.
</SUBAGENT-STOP>

<EXTREMELY-IMPORTANT>
If you think there is even a 1% chance a fastmcp-engineering skill might apply to what you are doing, you ABSOLUTELY MUST invoke the skill.

IF A SKILL APPLIES TO YOUR TASK, YOU DO NOT HAVE A CHOICE. YOU MUST USE IT.

This is not negotiable. You cannot rationalize your way out of this.
</EXTREMELY-IMPORTANT>

## The Rule

**Invoke relevant or requested fastmcp-engineering skills BEFORE any response or action** — including clarifying questions, exploring the codebase, or checking files. If it turns out wrong for the situation, you don't have to use it.

**Before entering plan mode:** if you haven't already brainstormed, invoke the brainstorming skill first.

Then announce "Using [skill] to [purpose]" and follow the skill exactly. If it has a checklist, create a todo per item.

## Skill Priority

When multiple skills apply, process skills come first — they set the approach, then implementation skills carry it out. Research-first and engineering-governance are the most common process skills, but the rule holds for any of them.

- "Let's build X" → research-first, then brainstorming/domain skills.
- "Fix this bug" → systematic-debugging first, then domain skills.

## Mission

Make every FastMCP/MCP engineering task evidence-first and architecture-governed: research official documentation before design, gate architecture, define contracts, use TDD, verify before claiming completion. The goal of this skill is to trigger the correct domain skill at the correct moment.

## Scope

This skill applies when the task touches FastMCP servers, MCP protocol semantics, Python/Pydantic contracts, databases, security, observability, deployment, or agent workflows built on these. It does not apply to pure frontend or non-engineering prose work with no framework-sensitive component.

## Trigger

Use when starting any conversation or task that may involve FastMCP/MCP engineering — before any response, exploration, or implementation. Apply before entering plan mode and before writing any code.

## Upstream

Prerequisite context: the task description and the current repository state (branch, contracts, AGENTS.md). Required input is whatever the dispatcher supplied; never substitute memory for current evidence.

## Research

Official documentation is mandatory evidence. Consult current FastMCP docs, the MCP specification, official examples, and primary dependency sources before any design or implementation decision. Never rely on memory-only claims.

## Decision

Selection rules: choose the smallest native FastMCP mechanism that fits; justify custom infrastructure; apply SOLID/KISS/DRY/YAGNI as constraints. When skills conflict, process skills win.

## Verification

Testing is mandatory. Run the repository's configured tests, lint, type checks, and protocol/contract checks before reporting completion. Never claim completion without fresh verification evidence.

## Failure

Stop conditions: if required evidence is unobtainable, the target version is unclear, or behavior cannot be established from official sources — stop and report what is missing. Escalate instead of guessing.

## Deliverables

The artifact required by the invoked domain skill (research record, contract, implementation with tests, verification evidence). Every deliverable cites file:line evidence where applicable.

## Version

FastMCP and MCP APIs are version-sensitive. Identify the exact supported version before using an API; never silently mix version-specific APIs or compatibility across releases.

## Domain skills index

Invoke the matching domain skill when its trigger matches (full inventory lives in the repository `skills/`):

- Research gate: `research-first`, `documentation-evidence-governance`, `fastmcp-research`
- Architecture: `architecture-governor`, `application-domain`, `application-architecture-usecases`, `pattern-selection`
- Components/API: `fastmcp-components`, `api-tool-engineering`, `mcp-primitives-engineering`, `api-contract-schema-engineering`, `api-lifecycle-versioning`, `pydantic-schema-engineering`
- Protocol: `mcp-protocol-engineering`, `fastmcp-protocol-compliance`, `fastmcp-server-architecture`
- FastMCP internals: `fastmcp-auth`, `fastmcp-context-di`, `fastmcp-lifespan`, `fastmcp-middleware`, `fastmcp-providers`, `fastmcp-tasks`, `fastmcp-transforms`, `fastmcp-transports-deployment`, `fastmcp-client-testing`
- Data: `sqlalchemy-engineering`, `sqlalchemy-postgresql-engineering`, `sqlalchemy-persistence-architecture`, `database-persistence-sqlalchemy`, `data-persistence-engineering`, `pydantic-engineering`
- Security: `security-engineering`, `security-threat-modeling`, `security-privacy-governance`, `dependency-supply-chain-security`
- Reliability/performance: `reliability-resilience-engineering`, `resilience-engineering`, `performance-capacity-engineering`, `performance-resource-engineering`, `async-event-driven-engineering`
- Observability: `observability-diagnostics`, `observability-opentelemetry`, `observability-operations`
- Testing/QA: `testing-tdd-engineering`, `testing-verification-engineering`, `testing-quality-engineering`, `final-review`
- Ops: `deployment-operations-engineering`, `packaging-build-deployment`, `ci-cd-github-actions-engineering`, `configuration-environment-engineering`, `dependency-injection-composition-root`

## Platform Adaptation

Per-harness tool mapping (how this skill's actions resolve to real tools) lives in `references/`:

- Claude Code → `references/claude-code-tools.md`
- Cursor → `references/cursor-tools.md`
- Codex → `references/codex-tools.md`
- Copilot CLI → `references/copilot-tools.md`
- Gemini CLI → `references/gemini-tools.md`
- Kimi Code → `references/kimi-tools.md`
- OpenCode → `references/opencode-tools.md`
- pi → `references/pi-tools.md`
````

- [ ] **Step 2: Run contract tests — expect semantic/inventory shift**

Run: `uv run --with pytest python -m pytest tests/ -q`
Expected: `test_skill_inventory_matches_current_baseline` FAILS (57 found, 58 expected); new skill may fail semantic/scenario/acceptance tests until Steps 3-4 complete.

- [ ] **Step 3: Write `skills/using-fastmcp-engineering/ACCEPTANCE.md`**

Дословно (содержит stop-маркер и scenario-маркеры):

```markdown
# Acceptance — Using FastMCP Engineering

- [ ] At session start, the agent recognizes fastmcp-engineering skills exist and invokes the matching domain skill before any implementation action.
- [ ] Positive scenario: a FastMCP/MCP task triggers research-first before code is written.
- [ ] Negative scenario: a non-engineering task does not trigger any fastmcp-engineering skill.
- [ ] Evidence: the session transcript shows a skill announcement ("Using X to Y") before any design or implementation.
- [ ] Stop condition: when no official evidence is obtainable, the agent stops and reports what is missing instead of guessing.
```

- [ ] **Step 4: Write the 8 tool-mapping references**

Каждый файл — таблица «Action skills request → harness equivalent», покрывающая: read file, create/edit/delete file, run shell, grep/glob, fetch URL/web search, dispatch subagent (с указанием как передать тип агента), todos, invoke skill. Ниже — готовые содержимое. Копировать дословно каждый.

**`references/opencode-tools.md`:**

```markdown
# OpenCode Tool Mapping

Skills speak in actions ("invoke a skill", "dispatch a subagent", "create a todo"). On OpenCode these resolve to OpenCode's native tools.

| Action skills request | OpenCode equivalent |
|---|---|
| Invoke a skill | OpenCode's native `skill` tool |
| Create/update todos | `todowrite` |
| Dispatch a subagent | `task` with `subagent_type` (`general`, `explore`, or a fastmcp-engineering `fm-*` role) |
| Read a file | `read` |
| Create/edit/delete a file | `write` / `edit` / `bash rm` |
| Run a shell command | `bash` |
| Search file contents | `grep` |
| Find files by name | `glob` |
| Fetch a URL | `webfetch` |
| Search the web | `websearch` or Exa web-search tools |

## fm-* role agents

fastmcp-engineering ships `fm-research`, `fm-implementation`, `fm-audit`, `fm-review`, `fm-governor` role agents. Dispatch them via the `task` tool with `subagent_type` set to the role name, or use the `/fm` command.

## Notes

- Skills must be invoked through the native `skill` tool; do not bypass it by reading `SKILL.md` with `read` unless the skill itself documents that path.
- The `fm-*` agents load `prompts/<token>-<role>-agent.md` at runtime (PRIMARY local clone, FALLBACK reference clone).
```

**`references/pi-tools.md`:**

```markdown
# Pi Tool Mapping

Skills speak in actions. On Pi these resolve to Pi's native tools (lowercase) and optional extensions.

| Action skills request | Pi equivalent |
|---|---|
| Invoke a skill | Pi's native skill system: load the relevant `SKILL.md` with `read`, or a human invokes `/skill:name` |
| Read a file | `read` |
| Create/edit/delete a file | `write` / `edit` |
| Run a shell command | `bash` |
| Search file contents | `grep` |
| Find files by name | `find` / `ls` |
| Fetch a URL | Pi's web fetch tool if available |
| Search the web | Pi's web search tool if available |
| Dispatch a subagent | An installed subagent tool (e.g. `pi-subagents`) if available; otherwise do the work inline |
| Task tracking | An installed todo tool if available; otherwise a plan file or repo-local `TODO.md` |

## Notes

- Pi has no native `Skill` tool: reading the relevant `SKILL.md` with `read` IS the sanctioned invocation mechanism for fastmcp-engineering skills.
- Never invent `task` calls; if no subagent tool exists, execute sequentially or explain the missing capability.
```

**`references/claude-code-tools.md`:**

```markdown
# Claude Code Tool Mapping

Skills speak in actions. On Claude Code these resolve to Claude Code's native tools.

| Action skills request | Claude Code equivalent |
|---|---|
| Invoke a skill | the `Skill` tool |
| Read a file | `Read` |
| Create/edit/delete a file | `Write` / `Edit` / `Bash rm` |
| Run a shell command | `Bash` |
| Search file contents | `Grep` |
| Find files by name | `Glob` |
| Fetch a URL | `WebFetch` |
| Search the web | `WebSearch` |
| Dispatch a subagent | `Task` with a fastmcp-engineering `fm-*` role or `general-purpose` |
| Create/update todos | `TodoWrite` |

## Notes

- Claude Code discovers `skills/` and the SessionStart hook by convention from `.claude-plugin/plugin.json`.
- The `fm-*` role agents are available via the `Task` tool with `subagent_type` set to the role name.
```

**`references/cursor-tools.md`:**

```markdown
# Cursor Tool Mapping

Skills speak in actions. On Cursor these resolve to Cursor Agent's tools (Claude Code-compatible tool surface).

| Action skills request | Cursor equivalent |
|---|---|
| Invoke a skill | the `Skill` tool (Cursor Agent) |
| Read a file | `Read` |
| Create/edit/delete a file | `Write` / `Edit` |
| Run a shell command | `Bash` / terminal |
| Search file contents | `Grep` |
| Find files by name | `Glob` |
| Fetch a URL | `WebFetch` |
| Search the web | `WebSearch` |
| Dispatch a subagent | `Task` with the role name |
| Create/update todos | `TodoWrite` / Cursor todo list |

## Notes

- Cursor loads the bootstrap through its SessionStart hook (`hooks/hooks-cursor.json`) which injects `additional_context`.
- The `fm-*` role agents are available via `Task` with `subagent_type` set to the role name.
```

**`references/copilot-tools.md`:**

```markdown
# GitHub Copilot CLI Tool Mapping

Skills speak in actions. On Copilot CLI these resolve to Copilot CLI's tools (Claude Code-compatible tool surface, SDK standard).

| Action skills request | Copilot CLI equivalent |
|---|---|
| Invoke a skill | the `Skill` tool |
| Read a file | `Read` |
| Create/edit/delete a file | `Write` / `Edit` |
| Run a shell command | `Bash` |
| Search file contents | `Grep` |
| Find files by name | `Glob` |
| Fetch a URL | `WebFetch` |
| Search the web | `WebSearch` |
| Dispatch a subagent | `Task` with the role name |
| Create/update todos | `TodoWrite` |

## Notes

- Copilot CLI shares the Claude Code session-start hook path; `hooks/session-start` detects it via `COPILOT_CLI=1` and emits the SDK-standard `additionalContext` shape.
- The `fm-*` role agents are available via `Task` with `subagent_type` set to the role name.
```

**`references/codex-tools.md`:**

```markdown
# Codex Tool Mapping

Skills speak in actions. On Codex these resolve to Codex CLI/App tools. Codex surfaces skills natively from `.codex-plugin/plugin.json` `skills` field.

| Action skills request | Codex equivalent |
|---|---|
| Invoke a skill | Codex's native skill tool |
| Read a file | `read` |
| Create/edit/delete a file | `write` / `edit` |
| Run a shell command | `shell` |
| Search file contents | `grep` |
| Find files by name | `glob` |
| Fetch a URL | `web_fetch` |
| Search the web | `web_search` |
| Dispatch a subagent | `spawn_agent` / `wait_agent` / `close_agent` — requires `multi_agent = true` in `~/.codex/config.toml` |
| Create/update todos | a todo/task tool if available, otherwise a plan file |

## Notes

- Multi-agent features must be enabled: `[features] multi_agent = true` in the Codex config.
- fastmcp-engineering skills are discovered natively; the bootstrap is triggered by the surfaced `using-fastmcp-engineering` description.
```

**`references/kimi-tools.md`:**

```markdown
# Kimi Code Tool Mapping

Skills speak in actions. On Kimi Code these resolve to Kimi Code's tools.

| Action skills request | Kimi Code equivalent |
|---|---|
| Invoke a skill | the `Skill` tool |
| Read a file | `Read` |
| Create/edit/delete a file | `Write` / `Edit` |
| Run a shell command | `Bash` |
| Search file contents | `Grep` |
| Find files by name | `Glob` |
| Fetch a URL | `FetchURL` |
| Search the web | `WebSearch` |
| Dispatch a subagent | `Agent` tool with a Kimi subagent type (e.g. `coder`, `explore`, `plan`) |
| Create/update todos | `TodoList` |

## Notes

- Kimi loads the bootstrap via `sessionStart.skill: "using-fastmcp-engineering"` in `.kimi-plugin/plugin.json`.
- Do not pass `general-purpose` as `subagent_type`; use Kimi's own subagent types.
```

**`references/gemini-tools.md`:**

```markdown
# Gemini CLI Tool Mapping

Skills speak in actions. On Gemini CLI these resolve to Gemini's tools.

| Action skills request | Gemini CLI equivalent |
|---|---|
| Invoke a skill | `activate_skill` |
| Read a file | `read_file` |
| Read multiple files | `read_many_files` |
| Create a file | `write_file` |
| Edit a file | `replace` |
| Run a shell command | `run_shell_command` |
| Search file contents | `grep_search` |
| Find files by name | `glob` |
| List files | `list_directory` |
| Fetch a URL | `web_fetch` |
| Search the web | `google_web_search` |
| Dispatch a subagent | `invoke_agent` with `agent_name: "generalist"` |
| Create/update todos | `write_todos` |

## Notes

- Gemini loads the bootstrap through the extension's declared context file (`FME.md`), which `@`-includes this mapping.
- Instructions file for the extension: `FME.md`.
- Skills live in the installed extension's `skills/` directory.
```

- [ ] **Step 5: Update `EXPECTED_SKILL_COUNT`**

Edit `tests/test_skill_contract.py:9`:

```python
EXPECTED_SKILL_COUNT = 58
```

- [ ] **Step 6: Run full test suite**

Run: `uv run --with pytest python -m pytest tests/ -q`
Expected: `test_skill_inventory_matches_current_baseline` PASSES; bootstrap skill passes semantic/scenario/acceptance tests; the 3 pre-existing failures remain (fixed in Task 2).

- [ ] **Step 7: Commit**

```bash
git add skills/using-fastmcp-engineering/ tests/test_skill_contract.py
git commit -m "feat(skills): add using-fastmcp-engineering bootstrap skill and tool mappings"
```

---

### Task 2: Trigger/Deliverables секции для 57 доменных скиллов + ACCEPTANCE stop-conditions + контракт-тесты

**Files:**
- Modify: все `skills/*/SKILL.md` (57 файлов) — добавить блок `## Trigger / Когда применять` + `## Deliverables`
- Modify: `skills/*/ACCEPTANCE.md` (файлы без stop-маркера, ~46) — добавить строку stop condition
- Test: `tests/test_skill_contract.py`, `tests/test_skill_scenarios.py`

**Interfaces:**
- Consumes: Task 1 (контрактные токены; `EXPECTED_SKILL_COUNT = 58`)
- Produces: все скиллы проходят `test_every_skill_has_required_semantic_contract`, `test_every_skill_has_explicit_positive_and_negative_scenarios`, `test_scenario_contract_requires_a_stop_condition`

**Шаблон секции для каждого SKILL.md** (вставляется после заголовка `## Mission` / `## Purpose` / `## Overview` — первого H2 после `# Title`; если скилл уже имеет `## Deliverable`/`## Deliverables`, переименовать в единый блок). Шаблон содержит ВСЕ 10 контрактных токенов как явные английские лейблы:

```markdown
## Trigger / Когда применять

**Scope / When to use:** <вывести из существующего Purpose/Mission/Invocation — случаи применения>
**Trigger:** <вывести из существующего тела — сигналы задачи, при которых скилл ДОЛЖЕН быть вызван>
**Upstream / Prerequisite:** <вывести из существующего тела — нужный контекст/входные данные до применения>
**Mission / Goal:** <вывести из существующего Purpose/Mission — цель скилла>
**Research / Evidence:** <вывести из существующего тела — требование официальной документации/evidence>
**Decision / Selection rules:** <вывести из существующего тела — правила выбора/решений>
**Version / Compatibility:** <вывести из существующего тела — версии/совместимость, если есть; иначе "Привязан к целевому FastMCP/MCP/Python-релизу.">

## Deliverables

**Deliverables / Artifacts:** <вывести из существующего Deliverable/Outputs/артефактов>
**Verification / Testing:** <вывести из существующего Testing/Verification — как проверить>
**Failure / Stop conditions:** <вывести из существующего Rejection criteria/Stop conditions — когда остановиться/отклонить>
**Positive scenario:** <один happy-path исход>
**Negative scenario:** <один failure-mode исход>
```

**Правило:** контент каждой строки выводится ТОЛЬКО из существующего тела скилла (Purpose, Mission, Invocation, Testing, Rejection criteria, Stop conditions, Deliverable). Не выдумывать новую логику. Строка `**Version / Compatibility:**` допускает дефолт «Привязан к целевому FastMCP/MCP/Python-релизу.» только если в теле нет версионных упоминаний.

- [ ] **Step 1: Полный список скиллов, проходящих/не проходящих контракт**

```bash
cd /Users/laptop/dev/fastmcp-engineering
uv run --with pytest python -m pytest tests/test_skill_contract.py::test_every_skill_has_required_semantic_contract tests/test_skill_scenarios.py -q 2>&1 | grep -E '^E         skills/' | sort -u > /tmp/fail_list.txt
wc -l /tmp/fail_list.txt
```
Expected: 56+46 строк (детали); после Task 2 — пусто.

- [ ] **Step 2: Для каждого из 57 скиллов добавить блок Trigger/Deliverables по шаблону**

Для каждого файла `skills/<pkg>/SKILL.md`:
1. Прочитать тело.
2. Найти первый H2 после `# Title`.
3. Вставить блок после него (и, если есть, удалить/слить старый `## Deliverable`/`## Deliverables` и `## Rejection criteria`/`## Stop conditions` в новые секции).
4. Заполнить строки по правилу выше.

Пример готового результата для `skills/foundation/research-first/SKILL.md` (у него нет Mission, есть Purpose; целевой вид):

```markdown
---
name: research-first
description: Enforce research-first workflow before any framework-sensitive change — use to prevent implementation based on stale APIs or assumptions.
---

# Research First

## Purpose

Prevent implementation based on memory, assumptions, stale APIs, or incomplete examples.

## Trigger / Когда применять

**Scope / When to use:** before any task that changes FastMCP behavior, MCP contracts, integrations, security, persistence, transport, lifecycle, or other framework-sensitive behavior.
**Trigger:** any framework-sensitive change; requirement unclear; version not identified; official docs not yet consulted.
**Upstream / Prerequisite:** a clarified requirement; identified target versions; repository contracts and AGENTS.md.
**Mission / Goal:** prevent implementation based on memory, assumptions, stale APIs, or incomplete examples.
**Research / Evidence:** read official FastMCP documentation, official examples and tests, the MCP specification, and primary dependency docs; record evidence and unresolved questions.
**Decision / Selection rules:** compare native FastMCP mechanisms against custom alternatives before choosing; hand the result to architecture review.
**Version / Compatibility:** target FastMCP and MCP versions must be identified before research proceeds.

## Deliverables

**Deliverables / Artifacts:** a research record conforming to `contracts/research-contract.md`.
**Verification / Testing:** evidence ledger complete; unresolved questions recorded; sources and versions cited.
**Failure / Stop conditions:** stop rather than guess when official sources conflict, the target version is unclear, or behavior cannot be established from available evidence.
**Positive scenario:** a feature request is researched against current official docs before design and the research record is approved.
**Negative scenario:** implementation starts from memory; no evidence ledger exists; the target version is never pinned.
```

После вставки удалить старые секции `## Invocation`, `## Required sequence`, `## Deliverable`, `## Stop conditions` из этого скилла (их содержимое слито в новые секции).

- [ ] **Step 3: Добавить stop-condition в ACCEPTANCE.md без stop-маркера**

```bash
cd /Users/laptop/dev/fastmcp-engineering
for acc in $(find skills -name ACCEPTANCE.md); do
  grep -qiE 'stop|reject|escalate|deny|must not|invalid' "$acc" || echo "NO-STOP: $acc"
done
```
Для каждого NO-STOP файла добавить строку в конец (заменяя `<тема>` на тему скилла):

```markdown
- [ ] Stops when <тема> cannot be established from evidence; rejects invented behavior and escalates to the user instead of guessing.
```

- [ ] **Step 4: Прогнать контракт-тесты**

Run: `uv run --with pytest python -m pytest tests/ -q`
Expected: ВСЕ тесты зелёные (включая 3 ранее падавших). Если какой-то скилл всё ещё не проходит — проверить, что шаблон вставлен и все 10 лейблов присутствуют.

- [ ] **Step 5: ruff check**

Run: `uv run ruff check tests/`
Expected: no errors.

- [ ] **Step 6: Commit**

```bash
git add skills/ tests/
git commit -m "feat(skills): add trigger/deliverables contract sections and acceptance stop conditions"
```

---

### Task 3: Shape A — shell-hook бутстрап (Claude Code, Cursor, Copilot CLI)

**Files:**
- Create: `hooks/session-start`
- Create: `hooks/run-hook.cmd`
- Create: `hooks/hooks.json` (Claude Code)
- Create: `hooks/hooks-cursor.json` (Cursor)
- Create: `.claude-plugin/plugin.json`
- Create: `.cursor-plugin/plugin.json`
- Create: `.gitattributes`
- Test: `tests/hooks/test-session-start.sh`
- Test: `tests/hooks/run-tests.sh`

**Interfaces:**
- Consumes: Task 1 (`skills/using-fastmcp-engineering/SKILL.md`, references)
- Produces: `hooks/session-start` — единый скрипт, печатающий JSON ровно одной формы по env-детекции харнеса; манифесты Claude/Cursor; polyglot wrapper; тесты форм

- [ ] **Step 1: Write `hooks/session-start`**

Дословно (по образцу superpowers, адаптировано под fastmcp-engineering):

```bash
#!/usr/bin/env bash
# SessionStart hook for fastmcp-engineering plugin

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PLUGIN_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

using_content=$(cat "${PLUGIN_ROOT}/skills/using-fastmcp-engineering/SKILL.md" 2>&1 || echo "Error reading using-fastmcp-engineering skill")

escape_for_json() {
    local s="$1"
    s="${s//\\/\\\\}"
    s="${s//\"/\\\"}"
    s="${s//$'\n'/\\n}"
    s="${s//$'\r'/\\r}"
    s="${s//$'\t'/\\t}"
    printf '%s' "$s"
}

using_escaped=$(escape_for_json "$using_content")
session_context="<EXTREMELY_IMPORTANT>\nYou have fastmcp-engineering.\n\n**Below is the full content of your 'fastmcp-engineering:using-fastmcp-engineering' skill - your introduction to using fastmcp-engineering skills. For all other skills, use the 'Skill' tool:**\n\n${using_escaped}\n</EXTREMELY_IMPORTANT>"

if [ -n "${CURSOR_PLUGIN_ROOT:-}" ]; then
  printf '{\n  "additional_context": "%s"\n}\n' "$session_context" | cat
elif [ -n "${CLAUDE_PLUGIN_ROOT:-}" ] && [ -z "${COPILOT_CLI:-}" ]; then
  printf '{\n  "hookSpecificOutput": {\n    "hookEventName": "SessionStart",\n    "additionalContext": "%s"\n  }\n}\n' "$session_context" | cat
else
  printf '{\n  "additionalContext": "%s"\n}\n' "$session_context" | cat
fi

exit 0
```

- [ ] **Step 2: Write `hooks/run-hook.cmd`**

Дословно polyglot wrapper (по образцу superpowers):

```bash
: << 'CMDBLOCK'
@echo off
REM Cross-platform polyglot wrapper for hook scripts.
REM On Windows: cmd.exe runs the batch portion, which finds and calls bash.
REM On Unix: the shell interprets this as a script (: is a no-op in bash).

if "%~1"=="" (
    echo run-hook.cmd: missing script name >&2
    exit /b 1
)

set "HOOK_DIR=%~dp0"

if exist "C:\Program Files\Git\bin\bash.exe" (
    "C:\Program Files\Git\bin\bash.exe" "%HOOK_DIR%%~1" %2 %3 %4 %5 %6 %7 %8 %9
    exit /b %ERRORLEVEL%
)
if exist "C:\Program Files (x86)\Git\bin\bash.exe" (
    "C:\Program Files (x86)\Git\bin\bash.exe" "%HOOK_DIR%%~1" %2 %3 %4 %5 %6 %7 %8 %9
    exit /b %ERRORLEVEL%
)

where bash >nul 2>nul
if %ERRORLEVEL% equ 0 (
    bash "%HOOK_DIR%%~1" %2 %3 %4 %5 %6 %7 %8 %9
    exit /b %ERRORLEVEL%
)

exit /b 0
CMDBLOCK

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SCRIPT_NAME="$1"
shift
exec bash "${SCRIPT_DIR}/${SCRIPT_NAME}" "$@"
```

- [ ] **Step 3: Write `hooks/hooks.json` (Claude Code)**

```json
{
  "hooks": {
    "SessionStart": [
      {
        "matcher": "startup|clear|compact",
        "hooks": [
          {
            "type": "command",
            "command": "\"${CLAUDE_PLUGIN_ROOT}/hooks/run-hook.cmd\" session-start",
            "shell": "bash",
            "async": false
          }
        ]
      }
    ]
  }
}
```

- [ ] **Step 4: Write `hooks/hooks-cursor.json` (Cursor)**

```json
{
  "version": 1,
  "hooks": {
    "sessionStart": [
      {
        "command": "./hooks/run-hook.cmd session-start"
      }
    ]
  }
}
```

- [ ] **Step 5: Write `.claude-plugin/plugin.json`**

```json
{
  "name": "fastmcp-engineering",
  "description": "Research-first FastMCP and MCP engineering skills, contracts, and prompts for production MCP servers",
  "version": "0.2.0",
  "author": {
    "name": "evgenygurin",
    "url": "https://github.com/evgenygurin"
  },
  "homepage": "https://github.com/evgenygurin/fastmcp-engineering",
  "repository": "https://github.com/evgenygurin/fastmcp-engineering",
  "license": "MIT",
  "keywords": [
    "fastmcp",
    "mcp",
    "model-context-protocol",
    "python",
    "engineering",
    "research-first"
  ]
}
```

- [ ] **Step 6: Write `.cursor-plugin/plugin.json`**

```json
{
  "name": "fastmcp-engineering",
  "displayName": "FastMCP Engineering",
  "description": "Research-first FastMCP and MCP engineering skills, contracts, and prompts",
  "version": "0.2.0",
  "author": {
    "name": "evgenygurin",
    "url": "https://github.com/evgenygurin"
  },
  "homepage": "https://github.com/evgenygurin/fastmcp-engineering",
  "repository": "https://github.com/evgenygurin/fastmcp-engineering",
  "license": "MIT",
  "keywords": [
    "fastmcp",
    "mcp",
    "python",
    "engineering",
    "research-first"
  ],
  "skills": "./skills/",
  "hooks": "./hooks/hooks-cursor.json"
}
```

- [ ] **Step 7: Write `.gitattributes`**

```gitattributes
*.sh text eol=lf
hooks/session-start text eol=lf
*.cmd text eol=lf
*.md text eol=lf
*.json text eol=lf
*.js text eol=lf
*.mjs text eol=lf
*.ts text eol=lf
*.png binary
*.jpg binary
*.gif binary
```

- [ ] **Step 8: Write `tests/hooks/run-tests.sh`**

```bash
#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
"$SCRIPT_DIR/test-session-start.sh"
```

- [ ] **Step 9: Write `tests/hooks/test-session-start.sh`**

Проверяет: для каждого харнеса (CURSOR_PLUGIN_ROOT / CLAUDE_PLUGIN_ROOT / COPILOT_CLI=1 / none) `hooks/session-start` печатает ровно ожидаемую JSON-форму, содержит `<EXTREMELY_IMPORTANT>` и `fastmcp-engineering`, и НЕ содержит поле другой формы (нет двойной инъекции).

```bash
#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
HOOK="$REPO_ROOT/hooks/session-start"
FAILURES=0
TEST_ROOT="$(mktemp -d)"
trap 'rm -rf "$TEST_ROOT"' EXIT

pass() { echo "  [PASS] $1"; }
fail() { echo "  [FAIL] $1"; FAILURES=$((FAILURES + 1)); }

assert_shape() {
    local name="$1" expected_shape="$2" home="$3"
    shift 3
    local output
    output="$(env -i PATH="${PATH:-}" HOME="$home" "$@" 2>&1)"
    local json
    json="$(printf '%s' "$output" | node -e 'let s="";process.stdin.on("data",d=>s+=d).on("end",()=>{const j=JSON.parse(s);console.log(JSON.stringify(j));})')"
    local shape
    shape="$(printf '%s' "$json" | node -e 'let s="";process.stdin.on("data",d=>s+=d).on("end",()=>{const j=JSON.parse(s);console.log(Object.keys(j).join(","));})')"
    if [ "$shape" != "$expected_shape" ]; then
        fail "$name: expected shape '$expected_shape', got '$shape'"
        return
    fi
    if ! printf '%s' "$json" | grep -q 'EXTREMELY_IMPORTANT'; then
        fail "$name: bootstrap marker missing"
        return
    fi
    if ! printf '%s' "$json" | grep -q 'fastmcp-engineering'; then
        fail "$name: fastmcp-engineering text missing"
        return
    fi
    pass "$name"
}

HOME_C="$TEST_ROOT/home-cursor"; mkdir -p "$HOME_C"
HOME_CC="$TEST_ROOT/home-cc"; mkdir -p "$HOME_CC"
HOME_CP="$TEST_ROOT/home-copilot"; mkdir -p "$HOME_CP"
HOME_N="$TEST_ROOT/home-none"; mkdir -p "$HOME_N"

assert_shape "cursor" "additional_context" "$HOME_C" env CURSOR_PLUGIN_ROOT=/x "$HOOK"
assert_shape "claude" "hookSpecificOutput" "$HOME_CC" env CLAUDE_PLUGIN_ROOT=/x "$HOOK"
assert_shape "copilot" "additionalContext" "$HOME_CP" env CLAUDE_PLUGIN_ROOT=/x COPILOT_CLI=1 "$HOOK"
assert_shape "none" "additionalContext" "$HOME_N" "$HOOK"

# No double injection: claude output must not contain additional_context top-level
OUT_CC="$(env -i PATH="${PATH:-}" HOME="$HOME_CC" CLAUDE_PLUGIN_ROOT=/x "$HOOK" 2>&1)"
if printf '%s' "$OUT_CC" | grep -q '"additional_context"'; then
    fail "claude: must not emit additional_context (double injection risk)"
else
    pass "claude: no additional_context field"
fi

echo
if [ "$FAILURES" -eq 0 ]; then
    echo "All hook tests passed."
    exit 0
else
    echo "$FAILURES hook test(s) failed."
    exit 1
fi
```

- [ ] **Step 10: Run hook tests**

Run: `bash tests/hooks/run-tests.sh`
Expected: 4× PASS + no-double-injection PASS; exit 0.

- [ ] **Step 11: shellcheck**

Run: `shellcheck hooks/session-start tests/hooks/test-session-start.sh tests/hooks/run-tests.sh`
Expected: no errors (или зафиксировать, что shellcheck недоступен — записать в evidence).

- [ ] **Step 12: Commit**

```bash
git add hooks/ .claude-plugin/ .cursor-plugin/ .gitattributes tests/hooks/
git commit -m "feat(hooks): add session-start bootstrap injection for Claude Code, Cursor, Copilot CLI"
```

---

### Task 4: Shape B — OpenCode plugin (config hook + messages.transform)

**Files:**
- Create: `.opencode/plugins/fastmcp-engineering.js`
- Modify: `.opencode/opencode.json` (plugin array → добавить `./plugins/fastmcp-engineering.js`; оставить `./plugin/fastmcp-local.ts`)
- Test: `tests/opencode/run-tests.sh`
- Test: `tests/opencode/test-bootstrap-caching.mjs`
- Test: `tests/opencode/test-plugin-loading.sh`

**Interfaces:**
- Consumes: Task 1 (SKILL.md content, `references/opencode-tools.md`)
- Produces: `FastMcpEngineeringPlugin` — opencode-плагин, регистрирующий `skills/` dir через `config` hook и инъецирующий бутстрап через `experimental.chat.messages.transform`

- [ ] **Step 1: Write `.opencode/plugins/fastmcp-engineering.js`**

Дословно (по образцу superpowers `.opencode/plugins/superpowers.js`, адаптировано):

```js
/**
 * FastMCP Engineering plugin for OpenCode.ai
 *
 * Injects fastmcp-engineering bootstrap context via message transform.
 * Auto-registers skills directory via config hook (no symlinks needed).
 */

import path from 'path';
import fs from 'fs';
import os from 'os';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));

// Simple frontmatter extraction (avoid dependency on skills-core for bootstrap)
const extractAndStripFrontmatter = (content) => {
  const match = content.match(/^---\n([\s\S]*?)\n---\n([\s\S]*)$/);
  if (!match) return { frontmatter: {}, content };

  const frontmatterStr = match[1];
  const body = match[2];
  const frontmatter = {};

  for (const line of frontmatterStr.split('\n')) {
    const colonIdx = line.indexOf(':');
    if (colonIdx > 0) {
      const key = line.slice(0, colonIdx).trim();
      const value = line.slice(colonIdx + 1).trim().replace(/^["']|["']$/g, '');
      frontmatter[key] = value;
    }
  }

  return { frontmatter, content: body };
};

// Normalize a path: trim whitespace, expand ~, resolve to absolute
const normalizePath = (p, homeDir) => {
  if (!p || typeof p !== 'string') return null;
  let normalized = p.trim();
  if (!normalized) return null;
  if (normalized.startsWith('~/')) {
    normalized = path.join(homeDir, normalized.slice(2));
  } else if (normalized === '~') {
    normalized = homeDir;
  }
  return path.resolve(normalized);
};

// Module-level cache for bootstrap content.
let _bootstrapCache = undefined; // undefined = not yet loaded, null = file missing

export const FastMcpEngineeringPlugin = async ({ client, directory }) => {
  const homeDir = os.homedir();
  const engineeringSkillsDir = path.resolve(__dirname, '../../skills');
  const envConfigDir = normalizePath(process.env.OPENCODE_CONFIG_DIR, homeDir);
  const configDir = envConfigDir || path.join(homeDir, '.config/opencode');

  const getBootstrapContent = () => {
    if (_bootstrapCache !== undefined) return _bootstrapCache;

    const skillPath = path.join(engineeringSkillsDir, 'using-fastmcp-engineering', 'SKILL.md');
    if (!fs.existsSync(skillPath)) {
      _bootstrapCache = null;
      return null;
    }

    const fullContent = fs.readFileSync(skillPath, 'utf8');
    const { content } = extractAndStripFrontmatter(fullContent);

    const toolMapping = `**Tool Mapping for OpenCode:**
When skills request actions, substitute OpenCode equivalents:
- Create or update todos → \`todowrite\`
- \`Subagent (general-purpose):\` → \`task\` with \`subagent_type: "general"\`
- Invoke a skill → OpenCode's native \`skill\` tool
- Read files → \`read\`
- Create, edit, or delete files → \`apply_patch\`
- Run shell commands → \`bash\`
- Search files → \`grep\`, \`glob\`
- Fetch a URL → \`webfetch\`

Use OpenCode's native \`skill\` tool to list and load skills.`;

    _bootstrapCache = `<EXTREMELY_IMPORTANT>
You have fastmcp-engineering.

**IMPORTANT: The using-fastmcp-engineering skill content is included below. It is ALREADY LOADED - you are currently following it. Do NOT use the skill tool to load "using-fastmcp-engineering" again - that would be redundant.**

${content}

${toolMapping}
</EXTREMELY_IMPORTANT>`;

    return _bootstrapCache;
  };

  return {
    config: async (config) => {
      config.skills = config.skills || {};
      config.skills.paths = config.skills.paths || [];
      if (!config.skills.paths.includes(engineeringSkillsDir)) {
        config.skills.paths.push(engineeringSkillsDir);
      }
    },

    'experimental.chat.messages.transform': async (_input, output) => {
      const bootstrap = getBootstrapContent();
      if (!bootstrap || !output.messages.length) return;
      const firstUser = output.messages.find(m => m.info.role === 'user');
      if (!firstUser || !firstUser.parts.length) return;

      if (firstUser.parts.some(p => p.type === 'text' && p.text.includes('EXTREMELY_IMPORTANT'))) return;

      const ref = firstUser.parts[0];
      firstUser.parts.unshift({ ...ref, type: 'text', text: bootstrap });
    }
  };
};
```

- [ ] **Step 2: Modify `.opencode/opencode.json`**

Добавить плагин в массив:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "references": {
    "fastmcp-eng": {
      "repository": "evgenygurin/fastmcp-engineering",
      "branch": "main",
      "description": "FastMCP engineering methodology: architecture principles, contracts, skills, prompts, and research artifacts for building production-grade MCP servers. Use for research-first architecture decisions, engineering gates, verification procedures, and FastMCP best practices."
    }
  },
  "skills": {
    "paths": ["../skills"]
  },
  "instructions": ["../AGENTS.md"],
  "plugin": ["./plugin/fastmcp-local.ts", "./plugins/fastmcp-engineering.js"],
  "mcp": {
    "telegram": {
      "enabled": false
    }
  }
}
```

- [ ] **Step 3: Write `tests/opencode/test-bootstrap-caching.mjs`**

Дословно (адаптированный superpowers-тест: `FastMcpEngineeringPlugin`, путь `using-fastmcp-engineering/SKILL.md`):

```js
import fs from 'fs';
import { pathToFileURL } from 'url';

const [, , pluginPath, scenario] = process.argv;

if (!pluginPath || !['present', 'missing'].includes(scenario)) {
  console.error('Usage: node test-bootstrap-caching.mjs PLUGIN_PATH present|missing');
  process.exit(2);
}

let existsCount = 0;
let readCount = 0;

const originalExistsSync = fs.existsSync;
const originalReadFileSync = fs.readFileSync;

fs.existsSync = function (...args) {
  if (isBootstrapSkillPath(args[0])) {
    existsCount += 1;
  }
  return originalExistsSync.apply(this, args);
};

fs.readFileSync = function (...args) {
  if (isBootstrapSkillPath(args[0])) {
    readCount += 1;
  }
  return originalReadFileSync.apply(this, args);
};

const mod = await import(pathToFileURL(pluginPath).href);
const plugin = await mod.FastMcpEngineeringPlugin({ client: {}, directory: '.' });
const transform = plugin['experimental.chat.messages.transform'];

const firstOutput = makeOutput(`${scenario} bootstrap first step`);
await transform({}, firstOutput);
const afterFirst = { existsCount, readCount };

const secondOutput = makeOutput(`${scenario} bootstrap second step`);
await transform({}, secondOutput);
const afterSecond = { existsCount, readCount };

const result = {
  scenario,
  firstBootstrapParts: countBootstrapParts(firstOutput),
  secondBootstrapParts: countBootstrapParts(secondOutput),
  mapsSubagentToTask: bootstrapText(firstOutput).includes('`task` with `subagent_type: "general"`'),
  mapsMutationToApplyPatch: bootstrapText(firstOutput).includes('`apply_patch`'),
  firstReadCount: afterFirst.readCount,
  secondReadCount: afterSecond.readCount,
  firstExistsCount: afterFirst.existsCount,
  secondExistsCount: afterSecond.existsCount,
};

const failures = scenario === 'present'
  ? assertPresentBootstrap(result)
  : assertMissingBootstrap(result);

if (failures.length > 0) {
  console.error(JSON.stringify(result, null, 2));
  for (const failure of failures) {
    console.error(`FAIL: ${failure}`);
  }
  process.exit(1);
}

console.log(JSON.stringify(result, null, 2));

function isBootstrapSkillPath(filePath) {
  return String(filePath).replaceAll('\\', '/').includes('using-fastmcp-engineering/SKILL.md');
}

function makeOutput(text) {
  return {
    messages: [{
      info: { role: 'user' },
      parts: [{ type: 'text', text }],
    }],
  };
}

function bootstrapText(output) {
  const parts = output.messages[0].parts;
  return parts.filter(p => p.type === 'text').map(p => p.text).join('\n');
}

function countBootstrapParts(output) {
  return bootstrapText(output).split('<EXTREMELY_IMPORTANT>').length - 1;
}

function assertPresentBootstrap(r) {
  const failures = [];
  if (r.firstBootstrapParts !== 1) failures.push(`expected 1 bootstrap in first output, got ${r.firstBootstrapParts}`);
  if (r.secondBootstrapParts !== 0) failures.push(`expected 0 bootstrap in second output (dedup), got ${r.secondBootstrapParts}`);
  if (r.firstReadCount !== 1) failures.push(`expected 1 read of SKILL.md (cached), got ${r.firstReadCount}`);
  if (r.secondReadCount !== 1) failures.push(`expected no re-read after cache, got ${r.secondReadCount}`);
  if (!r.mapsSubagentToTask) failures.push('bootstrap missing subagent→task mapping');
  if (!r.mapsMutationToApplyPatch) failures.push('bootstrap missing edit→apply_patch mapping');
  return failures;
}

function assertMissingBootstrap(r) {
  const failures = [];
  if (r.firstBootstrapParts !== 0) failures.push(`expected 0 bootstrap when file missing, got ${r.firstBootstrapParts}`);
  if (r.secondBootstrapParts !== 0) failures.push(`expected 0 bootstrap when file missing, got ${r.secondBootstrapParts}`);
  return failures;
}
```

- [ ] **Step 4: Write `tests/opencode/test-plugin-loading.sh`**

```bash
#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
PLUGIN="$REPO_ROOT/.opencode/plugins/fastmcp-engineering.js"
FAILURES=0

# Scenario: skill present (real repo)
if ! node "$SCRIPT_DIR/test-bootstrap-caching.mjs" "$PLUGIN" present >/tmp/oc-present.json 2>&1; then
  echo "  [FAIL] present scenario"
  cat /tmp/oc-present.json
  FAILURES=$((FAILURES + 1))
else
  echo "  [PASS] present scenario (bootstrap injects once, cached)"
fi

# Scenario: skill missing (fake repo root) — point plugin at a dir without the skill
TMP_MISSING="$(mktemp -d)"
if ! (cd "$TMP_MISSING" && node "$SCRIPT_DIR/test-bootstrap-caching.mjs" "$PLUGIN" missing >/tmp/oc-missing.json 2>&1); then
  echo "  [FAIL] missing scenario"
  cat /tmp/oc-missing.json
  FAILURES=$((FAILURES + 1))
else
  echo "  [PASS] missing scenario (no bootstrap, no crash)"
fi
rm -rf "$TMP_MISSING"

# Config hook registers skills dir
if node -e '
const mod = await import("file://" + process.argv[1]);
const plugin = await mod.FastMcpEngineeringPlugin({ client: {}, directory: "." });
const cfg = {};
await plugin.config(cfg);
if (!cfg.skills || !cfg.skills.paths || !cfg.skills.paths.some(p => p.includes("skills"))) {
  console.error("config hook did not register skills path");
  process.exit(1);
}
console.log("config hook registered skills path");
' "$PLUGIN" >/tmp/oc-config.json 2>&1; then
  echo "  [PASS] config hook registers skills path"
else
  echo "  [FAIL] config hook"
  cat /tmp/oc-config.json
  FAILURES=$((FAILURES + 1))
fi

echo
if [ "$FAILURES" -eq 0 ]; then
  echo "All opencode plugin tests passed."
  exit 0
else
  echo "$FAILURES opencode plugin test(s) failed."
  exit 1
fi
```

- [ ] **Step 5: Write `tests/opencode/run-tests.sh`**

```bash
#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
"$SCRIPT_DIR/test-plugin-loading.sh"
```

- [ ] **Step 6: Run opencode tests**

Run: `bash tests/opencode/run-tests.sh`
Expected: present PASS, missing PASS, config hook PASS; exit 0.

- [ ] **Step 7: Live smoke — opencode debug config**

```bash
cd /tmp && opencode debug config 2>&1 | grep -i 'using-fastmcp-engineering' | head -3
```
Expected: скилл виден в resolved config (skills.paths → репо).

- [ ] **Step 8: Commit**

```bash
git add .opencode/plugins/fastmcp-engineering.js .opencode/opencode.json tests/opencode/
git commit -m "feat(opencode): add fastmcp-engineering bootstrap plugin (config hook + messages.transform)"
```

---

### Task 5: Shape B — pi extension

**Files:**
- Create: `.pi/extensions/fastmcp-engineering.ts`
- Create: root `package.json` (name/version/main/pi fields — для pi-дистрибуции)
- Test: `tests/pi/test-pi-extension.mjs`
- Test: `tests/pi/run-tests.sh`

**Interfaces:**
- Consumes: Task 1 (SKILL.md, `references/pi-tools.md`)
- Produces: pi-extension, регистрирующий `skills/` через `resources_discover` и инъецирующий бутстрап через `context` event (lifecycle-флаг + compaction-aware)

- [ ] **Step 1: Write `.pi/extensions/fastmcp-engineering.ts`**

Дословно (по образцу superpowers `.pi/extensions/superpowers.ts`, адаптировано):

```ts
import { readFileSync } from "node:fs";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import type { ExtensionAPI } from "@earendil-works/pi-coding-agent";

const EXTREMELY_IMPORTANT_MARKER = "<EXTREMELY_IMPORTANT>";
const BOOTSTRAP_MARKER = "fastmcp-engineering:using-fastmcp-engineering bootstrap for pi";

const extensionDir = dirname(fileURLToPath(import.meta.url));
const packageRoot = resolve(extensionDir, "../..");
const skillsDir = resolve(packageRoot, "skills");
const bootstrapSkillPath = resolve(skillsDir, "using-fastmcp-engineering", "SKILL.md");

let cachedBootstrap: string | null | undefined;

export default function fastmcpEngineeringPiExtension(pi: ExtensionAPI) {
	let injectBootstrap = true;

	pi.on("resources_discover", async () => ({
		skillPaths: [skillsDir],
	}));

	pi.on("session_start", async () => {
		injectBootstrap = true;
	});

	pi.on("session_compact", async () => {
		injectBootstrap = true;
	});

	pi.on("agent_end", async () => {
		injectBootstrap = false;
	});

	pi.on("context", async (event) => {
		if (!injectBootstrap) return;
		if (event.messages.some(messageContainsBootstrap)) return;

		const bootstrap = getBootstrapContent();
		if (!bootstrap) return;

		const bootstrapMessage = {
			role: "user" as const,
			content: [{ type: "text" as const, text: bootstrap }],
			timestamp: Date.now(),
		};

		const insertAt = firstNonCompactionSummaryIndex(event.messages);
		return {
			messages: [
				...event.messages.slice(0, insertAt),
				bootstrapMessage,
				...event.messages.slice(insertAt),
			],
		};
	});
}

function getBootstrapContent(): string | null {
	if (cachedBootstrap !== undefined) return cachedBootstrap;

	try {
		const skillContent = readFileSync(bootstrapSkillPath, "utf8");
		const body = stripFrontmatter(skillContent);
		cachedBootstrap = `${EXTREMELY_IMPORTANT_MARKER}
${BOOTSTRAP_MARKER}

You have fastmcp-engineering.

The using-fastmcp-engineering skill content is included below and is already loaded for this Pi session. Follow it now. Do not try to load using-fastmcp-engineering again.

${body}

${piToolMapping()}
</EXTREMELY_IMPORTANT>`;
		return cachedBootstrap;
	} catch {
		cachedBootstrap = null;
		return null;
	}
}

function stripFrontmatter(content: string): string {
	const match = content.match(/^---\n[\s\S]*?\n---\n([\s\S]*)$/);
	return (match ? match[1] : content).trim();
}

function piToolMapping(): string {
	return `## Pi tool mapping

Pi has native skills but does not expose a Skill tool. When a fastmcp-engineering instruction says to invoke a skill, use Pi's native skill system instead: load the relevant \`SKILL.md\` with \`read\` when the skill applies, or let a human invoke \`/skill:name\` explicitly.

Pi's built-in coding tools are lowercase: \`read\`, \`write\`, \`edit\`, \`bash\`, plus optional \`grep\`, \`find\`, and \`ls\`. Use those for the corresponding actions: read a file, create or edit files, run shell commands, search file contents, find files by name, and list directories.

Pi does not ship a standard subagent tool. If a subagent tool such as \`subagent\` from \`pi-subagents\` is available, use it for subagent workflows. If no subagent tool is available, do the work in this session or explain the missing capability instead of inventing \`Task\` calls.

Pi does not ship a standard task-list tool. If an installed todo/task tool is available, use it. Otherwise track work in plan files or a repo-local \`TODO.md\` when task tracking is needed.`;
}

function messageContainsBootstrap(message: unknown): boolean {
	const content = (message as { content?: unknown }).content;
	if (typeof content === "string") return content.includes(BOOTSTRAP_MARKER);
	if (!Array.isArray(content)) return false;
	return content.some((part) => {
		return (
			part &&
			typeof part === "object" &&
			(part as { type?: unknown }).type === "text" &&
			typeof (part as { text?: unknown }).text === "string" &&
			(part as { text: string }).text.includes(BOOTSTRAP_MARKER)
		);
	});
}

function firstNonCompactionSummaryIndex(messages: unknown[]): number {
	let index = 0;
	while ((messages[index] as { role?: unknown } | undefined)?.role === "compactionSummary") {
		index += 1;
	}
	return index;
}
```

- [ ] **Step 2: Write root `package.json`**

```json
{
  "name": "fastmcp-engineering",
  "version": "0.2.0",
  "description": "Research-first FastMCP and MCP engineering skills and bootstrap for coding agents",
  "type": "module",
  "keywords": [
    "pi-package",
    "skills",
    "fastmcp",
    "mcp",
    "engineering",
    "research-first"
  ],
  "pi": {
    "extensions": [
      "./.pi/extensions/fastmcp-engineering.ts"
    ],
    "skills": [
      "./skills"
    ]
  }
}
```

- [ ] **Step 3: Write `tests/pi/test-pi-extension.mjs`**

Fake-API тест по образцу superpowers: проверяет, что lifecycle-обработчики регистрируются, бутстрап инъецируется один раз, dedup работает, compaction re-inject работает.

```js
import { pathToFileURL } from 'url';
import { mkdtempSync, rmSync, mkdirSync, writeFileSync } from 'fs';
import { tmpdir } from 'os';
import { join } from 'path';

const extensionPath = process.argv[2];
if (!extensionPath) {
  console.error('Usage: node test-pi-extension.mjs EXTENSION_PATH');
  process.exit(2);
}

const tmp = mkdtempSync(join(tmpdir(), 'pi-test-'));
const skillsDir = join(tmp, 'skills');
mkdirSync(join(skillsDir, 'using-fastmcp-engineering'), { recursive: true });
writeFileSync(
  join(skillsDir, 'using-fastmcp-engineering', 'SKILL.md'),
  '---\nname: using-fastmcp-engineering\ndescription: test\n---\n\n# Bootstrap body\n',
  'utf8'
);

const handlers = {};
const api = {
  on(name, fn) { handlers[name] = fn; },
};

const mod = await import(pathToFileURL(extensionPath).href);
const ext = mod.default(api);

// resources_discover registers skills
const discovered = await handlers.resources_discover();
if (!discovered.skillPaths || !discovered.skillPaths.some(p => p.includes('skills'))) {
  console.error('FAIL: resources_discover did not register skills path');
  process.exit(1);
}
console.log('PASS: resources_discover registers skills path');

// context event injects bootstrap once
const makeMessages = (n = 1) => Array.from({ length: n }, (_, i) => ({
  role: 'user',
  content: [{ type: 'text', text: `message ${i}` }],
}));

let messages = makeMessages();
let result = await handlers.context({ messages });
if (!result || !result.messages.some(m => JSON.stringify(m).includes('fastmcp-engineering'))) {
  console.error('FAIL: bootstrap not injected');
  process.exit(1);
}
const injected = result.messages.filter(m => JSON.stringify(m).includes('fastmcp-engineering')).length;
if (injected !== 1) {
  console.error(`FAIL: expected 1 bootstrap message, got ${injected}`);
  process.exit(1);
}
console.log('PASS: bootstrap injected once');

// dedup: after injection, context event must not re-inject
messages = result.messages;
result = await handlers.context({ messages });
if (result && result.messages.some(m => JSON.stringify(m).includes('fastmcp-engineering'))) {
  // dedup via marker: no new injection
  const count = result.messages.filter(m => JSON.stringify(m).includes('fastmcp-engineering')).length;
  if (count > 1) {
    console.error(`FAIL: dedup failed, ${count} bootstrap messages`);
    process.exit(1);
  }
}
console.log('PASS: dedup guard works');

// compaction: agent_end clears flag, session_start re-arms
handlers.agent_end();
let result2 = await handlers.context({ messages: makeMessages() });
if (result2 && result2.messages.some(m => JSON.stringify(m).includes('fastmcp-engineering'))) {
  console.error('FAIL: bootstrap injected after agent_end');
  process.exit(1);
}
handlers.session_start();
result2 = await handlers.context({ messages: makeMessages() });
if (!result2 || !result2.messages.some(m => JSON.stringify(m).includes('fastmcp-engineering'))) {
  console.error('FAIL: bootstrap not re-injected after session_start');
  process.exit(1);
}
console.log('PASS: compaction/lifecycle re-injection works');

rmSync(tmp, { recursive: true, force: true });
console.log('\nAll pi extension tests passed.');
```

- [ ] **Step 4: Write `tests/pi/run-tests.sh`**

```bash
#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
node "$SCRIPT_DIR/test-pi-extension.mjs" "$REPO_ROOT/.pi/extensions/fastmcp-engineering.ts"
```

- [ ] **Step 5: Run pi tests**

Run: `bash tests/pi/run-tests.sh`
Expected: 4× PASS; exit 0. (Примечание: тест переписывает путь к `skills/` через mkdtemp — расширение резолвит `packageRoot` от своего расположения; если тест не проходит из-за пути, поправить `skillsDir` в тесте на `join(packageRoot, 'skills')` с реальным repo root.)

- [ ] **Step 6: Commit**

```bash
git add .pi/ package.json tests/pi/
git commit -m "feat(pi): add fastmcp-engineering extension with session bootstrap injection"
```

---

### Task 6: Shape C — Gemini extension

**Files:**
- Create: `gemini-extension.json`
- Create: `FME.md`
- Test: `tests/gemini/run-tests.sh`
- Test: `tests/gemini/test-extension-manifest.sh`

**Interfaces:**
- Consumes: Task 1 (SKILL.md, `references/gemini-tools.md`)
- Produces: Gemini extension с `contextFileName: "FME.md"`, `@`-инклюдами бутстрапа и tool mapping

- [ ] **Step 1: Write `gemini-extension.json`**

```json
{
  "name": "fastmcp-engineering",
  "description": "Research-first FastMCP and MCP engineering skills, contracts, and prompts",
  "version": "0.2.0",
  "contextFileName": "FME.md"
}
```

- [ ] **Step 2: Write `FME.md`**

```markdown
@./skills/using-fastmcp-engineering/SKILL.md
@./skills/using-fastmcp-engineering/references/gemini-tools.md
```

- [ ] **Step 3: Write `tests/gemini/test-extension-manifest.sh`**

```bash
#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
FAILURES=0

MANIFEST="$REPO_ROOT/gemini-extension.json"
CTX="$REPO_ROOT/FME.md"

if ! node -e '
const fs = require("fs");
const m = JSON.parse(fs.readFileSync(process.argv[1], "utf8"));
if (m.contextFileName !== "FME.md") throw new Error("contextFileName mismatch");
if (!m.name || !m.version) throw new Error("missing name/version");
console.log("manifest OK");
' "$MANIFEST" >/dev/null 2>&1; then
  echo "  [FAIL] manifest invalid"
  FAILURES=$((FAILURES + 1))
else
  echo "  [PASS] manifest valid"
fi

for line in \
  "./skills/using-fastmcp-engineering/SKILL.md" \
  "./skills/using-fastmcp-engineering/references/gemini-tools.md"; do
  if grep -qF "@${line}" "$CTX"; then
    target="$REPO_ROOT/${line#./}"
    if [ -f "$target" ]; then
      echo "  [PASS] @-include resolves: $line"
    else
      echo "  [FAIL] @-include target missing: $line"
      FAILURES=$((FAILURES + 1))
    fi
  else
    echo "  [FAIL] @-include not found in FME.md: $line"
    FAILURES=$((FAILURES + 1))
  fi
done

echo
if [ "$FAILURES" -eq 0 ]; then
  echo "All gemini extension tests passed."
  exit 0
else
  echo "$FAILURES gemini extension test(s) failed."
  exit 1
fi
```

- [ ] **Step 4: Write `tests/gemini/run-tests.sh`**

```bash
#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
"$SCRIPT_DIR/test-extension-manifest.sh"
```

- [ ] **Step 5: Run gemini tests**

Run: `bash tests/gemini/run-tests.sh`
Expected: manifest PASS + 2× @-include PASS; exit 0.

- [ ] **Step 6: Commit**

```bash
git add gemini-extension.json FME.md tests/gemini/
git commit -m "feat(gemini): add fastmcp-engineering extension with context-file bootstrap"
```

---

### Task 7: Native skills — Codex (расширить) и Kimi

**Files:**
- Modify: `.codex-plugin/plugin.json` (добавить `references`-поле не нужно; `hooks: {}` подавить авто-дискавери; оставить version 0.1.0 до Task 8)
- Create: `.kimi-plugin/plugin.json`
- Test: `tests/codex/run-tests.sh`
- Test: `tests/codex/test-plugin-manifest.sh`
- Test: `tests/kimi/run-tests.sh`
- Test: `tests/kimi/test-plugin-manifest.sh`

**Interfaces:**
- Consumes: Task 1 (references/codex-tools.md, references/kimi-tools.md)
- Produces: Codex-манифест с подавленным авто-хуком; Kimi-манифест с `sessionStart.skill` и `skillInstructions`

- [ ] **Step 1: Modify `.codex-plugin/plugin.json`**

Добавить `"hooks": {}` (подавить авто-дискавери `hooks/hooks.json`, иначе Codex попытается запустить Claude-хук) — остальное без изменений:

```json
{
  "name": "fastmcp-engineering",
  "version": "0.1.0",
  "description": "Research-first engineering skills for designing, implementing, testing, securing, and operating FastMCP and MCP systems.",
  "author": {
    "name": "evgenygurin",
    "url": "https://github.com/evgenygurin"
  },
  "homepage": "https://github.com/evgenygurin/fastmcp-engineering",
  "repository": "https://github.com/evgenygurin/fastmcp-engineering",
  "license": "MIT",
  "keywords": [
    "fastmcp",
    "mcp",
    "model-context-protocol",
    "python",
    "engineering",
    "testing",
    "architecture",
    "security"
  ],
  "skills": "./skills/",
  "hooks": {},
  "interface": {
    "displayName": "FastMCP Engineering",
    "shortDescription": "Research-first FastMCP and MCP engineering workflows",
    "longDescription": "A governed engineering skill system for FastMCP and MCP work. It combines research-first decision making, architecture gates, implementation guidance, testing and verification, security, observability, reliability, persistence, deployment, and evidence-based acceptance contracts.",
    "developerName": "evgenygurin",
    "category": "Developer Tools",
    "capabilities": [
      "FastMCP engineering",
      "MCP protocol engineering",
      "Research-first architecture",
      "Testing and verification",
      "Security and reliability",
      "Database and persistence engineering",
      "Deployment and observability"
    ],
    "websiteURL": "https://github.com/evgenygurin/fastmcp-engineering",
    "defaultPrompt": [
      "Design a FastMCP server using research-first architecture gates",
      "Review this MCP implementation for protocol and security risks",
      "Plan tests and verification for this FastMCP feature"
    ]
  }
}
```

- [ ] **Step 2: Write `.kimi-plugin/plugin.json`**

```json
{
  "name": "fastmcp-engineering",
  "version": "0.2.0",
  "description": "Research-first FastMCP and MCP engineering skills, contracts, and prompts.",
  "author": {
    "name": "evgenygurin",
    "url": "https://github.com/evgenygurin"
  },
  "homepage": "https://github.com/evgenygurin/fastmcp-engineering",
  "repository": "https://github.com/evgenygurin/fastmcp-engineering",
  "license": "MIT",
  "keywords": [
    "fastmcp",
    "mcp",
    "model-context-protocol",
    "python",
    "engineering",
    "research-first"
  ],
  "skills": "./skills/",
  "sessionStart": {
    "skill": "using-fastmcp-engineering"
  },
  "skillInstructions": "Kimi Code tool mapping for fastmcp-engineering skills:\n\n- When a fastmcp-engineering skill refers to the `Skill` tool, use Kimi Code's native `Skill` tool.\n- When a skill says to ask the user, ask clarifying questions one at a time, presenting multiple-choice options where possible; use Kimi Code's `AskUserQuestion` tool for structured questions.\n- When a skill refers to `TodoWrite`, use Kimi Code's `TodoList` tool.\n- When a skill says `Subagent (general-purpose):` or asks to dispatch an implementer/reviewer subagent, use Kimi Code's `Agent` tool with a Kimi subagent type (`coder` for implementation/review, `explore` for read-only exploration, `plan` for design). Do not pass `general-purpose` as `subagent_type`.\n- For the fastmcp-engineering `fm-*` role agents, dispatch `Agent` with `subagent_type: \"coder\"` (or `explore`/`plan` per the role) and paste the fully filled prompt into `prompt`.\n- Use Kimi Code's `Read`, `Write`, `Edit`, `Bash`, `Grep`, `Glob`, `FetchURL`, `WebSearch`, and MCP tools by their actual exposed names.\n- When a skill asks to search file contents, use `Grep`; to find files by path or pattern, use `Glob`; to fetch a URL, use `FetchURL`; to search the web, use `WebSearch`.",
  "interface": {
    "displayName": "FastMCP Engineering",
    "shortDescription": "Research-first FastMCP and MCP engineering workflows",
    "longDescription": "A governed engineering skill system for FastMCP and MCP work. It combines research-first decision making, architecture gates, implementation guidance, testing and verification, security, observability, reliability, persistence, deployment, and evidence-based acceptance contracts.",
    "developerName": "evgenygurin",
    "capabilities": [
      "FastMCP engineering",
      "MCP protocol engineering",
      "Research-first architecture",
      "Testing and verification",
      "Security and reliability",
      "Database and persistence engineering",
      "Deployment and observability"
    ],
    "websiteURL": "https://github.com/evgenygurin/fastmcp-engineering"
  }
}
```

- [ ] **Step 3: Write `tests/codex/test-plugin-manifest.sh`**

```bash
#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
FAILURES=0
MANIFEST="$REPO_ROOT/.codex-plugin/plugin.json"

if ! node -e '
const fs = require("fs");
const m = JSON.parse(fs.readFileSync(process.argv[1], "utf8"));
if (m.name !== "fastmcp-engineering") throw new Error("name mismatch");
if (m.skills !== "./skills/") throw new Error("skills path mismatch");
if (!m.hooks || Object.keys(m.hooks).length !== 0) throw new Error("hooks must be empty to suppress auto-discovery");
console.log("codex manifest OK");
' "$MANIFEST" >/dev/null 2>&1; then
  echo "  [FAIL] codex manifest invalid"
  FAILURES=$((FAILURES + 1))
else
  echo "  [PASS] codex manifest valid"
fi

if [ -f "$REPO_ROOT/skills/using-fastmcp-engineering/references/codex-tools.md" ]; then
  echo "  [PASS] codex-tools reference present"
else
  echo "  [FAIL] codex-tools reference missing"
  FAILURES=$((FAILURES + 1))
fi

echo
if [ "$FAILURES" -eq 0 ]; then
  echo "All codex tests passed."
  exit 0
else
  echo "$FAILURES codex test(s) failed."
  exit 1
fi
```

- [ ] **Step 4: Write `tests/codex/run-tests.sh`**

```bash
#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
"$SCRIPT_DIR/test-plugin-manifest.sh"
```

- [ ] **Step 5: Write `tests/kimi/test-plugin-manifest.sh`**

```bash
#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
FAILURES=0
MANIFEST="$REPO_ROOT/.kimi-plugin/plugin.json"

if ! node -e '
const fs = require("fs");
const m = JSON.parse(fs.readFileSync(process.argv[1], "utf8"));
if (m.name !== "fastmcp-engineering") throw new Error("name mismatch");
if (m.skills !== "./skills/") throw new Error("skills path mismatch");
if (!m.sessionStart || m.sessionStart.skill !== "using-fastmcp-engineering") throw new Error("sessionStart.skill mismatch");
if (!m.skillInstructions) throw new Error("skillInstructions missing");
console.log("kimi manifest OK");
' "$MANIFEST" >/dev/null 2>&1; then
  echo "  [FAIL] kimi manifest invalid"
  FAILURES=$((FAILURES + 1))
else
  echo "  [PASS] kimi manifest valid"
fi

if [ -f "$REPO_ROOT/skills/using-fastmcp-engineering/references/kimi-tools.md" ]; then
  echo "  [PASS] kimi-tools reference present"
else
  echo "  [FAIL] kimi-tools reference missing"
  FAILURES=$((FAILURES + 1))
fi

echo
if [ "$FAILURES" -eq 0 ]; then
  echo "All kimi tests passed."
  exit 0
else
  echo "$FAILURES kimi test(s) failed."
  exit 1
fi
```

- [ ] **Step 6: Write `tests/kimi/run-tests.sh`**

```bash
#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
"$SCRIPT_DIR/test-plugin-manifest.sh"
```

- [ ] **Step 7: Run codex + kimi tests + python contract tests**

Run: `bash tests/codex/run-tests.sh && bash tests/kimi/run-tests.sh`
Expected: 2× PASS each; exit 0.
Also run: `uv run --with pytest python -m pytest tests/test_plugin_manifest.py -q`
Expected: PASS (манифест codex всё ещё валиден).

- [ ] **Step 8: Commit**

```bash
git add .codex-plugin/plugin.json .kimi-plugin/plugin.json tests/codex/ tests/kimi/
git commit -m "feat(plugins): codex hooks suppression and kimi native skill bootstrap"
```

---

### Task 8: Версионирование — `.version-bump.json` + `scripts/bump-version.sh`

**Files:**
- Create: `.version-bump.json`
- Create: `scripts/bump-version.sh`
- Modify: `tests/test_plugin_manifest.py` (version 0.1.0 → 0.2.0)
- Modify: `.codex-plugin/plugin.json` (version 0.1.0 → 0.2.0)

**Interfaces:**
- Consumes: Task 3-7 (манифесты)
- Produces: локстейп версий всех манифестов; скрипт бампа

- [ ] **Step 1: Write `.version-bump.json`**

```json
{
  "files": [
    { "path": "package.json", "field": "version" },
    { "path": ".claude-plugin/plugin.json", "field": "version" },
    { "path": ".cursor-plugin/plugin.json", "field": "version" },
    { "path": ".codex-plugin/plugin.json", "field": "version" },
    { "path": ".kimi-plugin/plugin.json", "field": "version" },
    { "path": "gemini-extension.json", "field": "version" }
  ],
  "audit": {
    "exclude": [
      "CHANGELOG.md",
      "RELEASE-NOTES.md",
      "node_modules",
      ".git",
      ".version-bump.json",
      "scripts/bump-version.sh"
    ]
  }
}
```

- [ ] **Step 2: Write `scripts/bump-version.sh`**

```bash
#!/usr/bin/env bash
# Bump version across all fastmcp-engineering manifests.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
CONFIG="$REPO_ROOT/.version-bump.json"

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <new-version>" >&2
    exit 1
fi
NEW_VERSION="$1"

if ! command -v node >/dev/null 2>&1; then
    echo "node required" >&2
    exit 1
fi

node - "$CONFIG" "$NEW_VERSION" <<'EOF'
const [configPath, newVersion] = process.argv.slice(2);
const fs = require("fs");
const config = JSON.parse(fs.readFileSync(configPath, "utf8"));
let changed = 0;
for (const entry of config.files) {
    const full = require("path").resolve(configPath, "..", entry.path);
    if (!fs.existsSync(full)) {
        console.warn(`skip (missing): ${entry.path}`);
        continue;
    }
    const raw = fs.readFileSync(full, "utf8");
    const json = JSON.parse(raw);
    const parts = entry.field.split(".");
    let cursor = json;
    for (let i = 0; i < parts.length - 1; i++) cursor = cursor[parts[i]];
    cursor[parts[parts.length - 1]] = newVersion;
    fs.writeFileSync(full, JSON.stringify(json, null, 2) + "\n");
    console.log(`updated ${entry.path} -> ${newVersion}`);
    changed++;
}
if (changed === 0) {
    console.error("no manifests updated");
    process.exit(1);
}
EOF
```

- [ ] **Step 3: Update `.codex-plugin/plugin.json` version → 0.2.0 и `tests/test_plugin_manifest.py`**

`tests/test_plugin_manifest.py:9`:

```python
    assert manifest["version"] == "0.2.0"
```

- [ ] **Step 4: Run bump script (dry)**

```bash
cd /Users/laptop/dev/fastmcp-engineering
bash scripts/bump-version.sh 0.2.0
git diff --stat
```
Expected: все манифесты (package.json, .claude-plugin, .cursor-plugin, .codex-plugin, .kimi-plugin, gemini-extension.json) показывают 0.2.0.

- [ ] **Step 5: Run python tests**

Run: `uv run --with pytest python -m pytest tests/ -q`
Expected: все зелёные (включая test_plugin_manifest).

- [ ] **Step 6: Commit**

```bash
git add .version-bump.json scripts/bump-version.sh .codex-plugin/plugin.json tests/test_plugin_manifest.py
git commit -m "chore(versioning): add manifest version lockstep and bump script"
```

---

### Task 9: Документация — porting guide, README.<harness>, README.md, AGENTS.md sync

**Files:**
- Create: `docs/porting-to-a-new-harness.md`
- Create: `docs/README.opencode.md`, `docs/README.claude-code.md`, `docs/README.cursor.md`, `docs/README.copilot.md`, `docs/README.codex.md`, `docs/README.kimi.md`, `docs/README.gemini.md`, `docs/README.pi.md`
- Modify: `README.md` (секция установки для всех харнесов)
- Modify: `AGENTS.md` (синхронизация: упомянуть бутстрап-скилл и правило «используй fastmcp-engineering скиллы до действия»)

**Interfaces:**
- Consumes: Tasks 1-8 (все файлы)
- Produces: документация установки по каждому харнесу; porting guide для будущих харнесов

- [ ] **Step 1: Write `docs/porting-to-a-new-harness.md`**

Адаптировать структуру superpowers `docs/porting-to-a-new-harness.md` под fastmcp-engineering: Part 1 (3 компонента), Part 2 (может ли харнес поддержать — hard requirement: auto session-start injection), Part 3 (definition of done: bootstrap loads, tool mapping, skills invokable, acceptance test), Part 4 (3 shapes + routing table), Part 5 (процедура: reference implementation, manifest, bootstrap wiring, tool mapping, no-skill-tool case), Part 6 (distribution), Part 7 (Windows polyglot), Part 8 (PR), Appendix A (reference integrations table с нашими 8), Appendix B (gotchas). Заменить все упоминания `superpowers`/`using-superpowers` на `fastmcp-engineering`/`using-fastmcp-engineering`. Acceptance prompt: «Let's make a FastMCP server».

- [ ] **Step 2: Write `docs/README.<harness>.md` — по одному на каждый из 8 харнесов**

Формат каждого (заполнить `<harness>` и install-команду):

```markdown
# Installing FastMCP Engineering for <Harness>

## Prerequisites
- <Harness> installed

## Installation
<Команда установки через собственный install-механизм харнеса>

## Verify
<как проверить, что бутстрап загружен — вопрос модели или log-grep>

## Updating
<как обновить>
```

Конкретные install-команды:
- Claude Code: `/plugin install fastmcp-engineering@<marketplace>` (или marketplace entry, задокументировать)
- Cursor: `/add-plugin` / marketplace (задокументировать; исходник — `.cursor-plugin/`)
- Codex: `/plugins` → install from fork/git URL
- Copilot CLI: plugin install через git URL
- Kimi: `/plugins install` + git URL
- OpenCode: `"plugin": ["fastmcp-engineering@git+https://github.com/evgenygurin/fastmcp-engineering.git"]` в opencode.json + `opencode run --print-logs "hello" 2>&1 | grep -i fastmcp`
- pi: package install через `package.json` `pi`-поля
- Gemini: `gemini extensions install` + git URL

- [ ] **Step 3: Modify `README.md` — добавить секцию установки**

Добавить секцию `## Installation (all agents)` после `## Status`, со списком харнесов, install-командами и ссылками на `docs/README.<harness>.md`. Образец:

```markdown
## Installation (all agents)

FastMCP Engineering auto-triggers its skills in every major coding agent. Install
through each harness's own mechanism (never by hand-copying files):

| Harness | Install | Details |
|---|---|---|
| Claude Code | `/plugin install ...` | `docs/README.claude-code.md` |
| Cursor | `/add-plugin ...` | `docs/README.cursor.md` |
| Codex | `/plugins` | `docs/README.codex.md` |
| Copilot CLI | plugin install | `docs/README.copilot.md` |
| Kimi Code | `/plugins install` | `docs/README.kimi.md` |
| OpenCode | `plugin` array in opencode.json | `docs/README.opencode.md` |
| pi | package install | `docs/README.pi.md` |
| Gemini | `gemini extensions install` | `docs/README.gemini.md` |

How it works: at session start, `skills/using-fastmcp-engineering/SKILL.md` is
injected into the model context (wrapped in `<EXTREMELY_IMPORTANT>` + per-harness
tool mapping), which makes the domain skills auto-trigger. Design:
`docs/superpowers/specs/2026-09-01-fastmcp-superpowers-parity-design.md`.
```

- [ ] **Step 4: Modify `AGENTS.md` — синхронизация**

Добавить пункт в Non-negotiable rules (после правила 11) или в отдельную секцию «Agent bootstrap»:

```markdown
## Agent bootstrap

When working in any harness that loads fastmcp-engineering skills, the
`using-fastmcp-engineering` bootstrap skill is injected at session start. It
teaches the agent to invoke a matching fastmcp-engineering skill BEFORE any
response or action. Do not bypass the bootstrap; follow the invoked skill's
procedure, including its research gate, architecture gate, TDD cycle, and
verification requirements.
```

- [ ] **Step 5: Verify docs link targets exist**

```bash
cd /Users/laptop/dev/fastmcp-engineering
for f in docs/README.*.md; do echo "$f"; done | wc -l
# Expected: 8
grep -c 'docs/README' README.md
# Expected: >=8
```

- [ ] **Step 6: Commit**

```bash
git add docs/ README.md AGENTS.md
git commit -m "docs: add harness installation guides, porting guide, and agent bootstrap sync"
```

---

### Task 10: Итоговая верификация + branch inventory + PR

**Files:** none (проверки и git-операции)

**Interfaces:**
- Consumes: Tasks 1-9

- [ ] **Step 1: Полная локальная верификация**

```bash
cd /Users/laptop/dev/fastmcp-engineering
uv run --with pytest python -m pytest tests/ -q
uv run ruff check tests/
bash tests/hooks/run-tests.sh
bash tests/opencode/run-tests.sh
bash tests/pi/run-tests.sh
bash tests/gemini/run-tests.sh
bash tests/codex/run-tests.sh
bash tests/kimi/run-tests.sh
if command -v shellcheck >/dev/null; then shellcheck hooks/session-start hooks/run-hook.cmd scripts/bump-version.sh tests/*/*.sh; else echo "shellcheck unavailable — skipped (recorded)"; fi
```
Expected: всё зелёное; любые недоступные проверки записать в evidence.

- [ ] **Step 2: Smoke — opencode debug config видит скилл**

```bash
cd /tmp && opencode debug config 2>&1 | grep -i 'using-fastmcp-engineering' | head -3
```
Expected: скилл в resolved config.

- [ ] **Step 3: gitnexus detect_changes**

Run: `gitnexus detect_changes` (или `node .gitnexus/run.cjs` эквивалент)
Expected: изменения только в ожидаемых файлах (новые плагины/манифесты/скиллы/тесты/доки), без непредвиденных исполняемых цепочек.

- [ ] **Step 4: Финальный обзор диффа**

```bash
git log --oneline main..HEAD
git diff --stat main..HEAD
git status -sb
```
Expected: чистое дерево; коммиты по задачам.

- [ ] **Step 5: Branch inventory + PR**

```bash
git branch -a | grep -i superpowers
# Expected: только feat/superpowers-parity
git push -u origin feat/superpowers-parity
gh pr create --base main --head feat/superpowers-parity \
  --title "feat: superpowers-parity — multi-harness bootstrap for fastmcp-engineering skills" \
  --body "Implements docs/superpowers/specs/2026-09-01-fastmcp-superpowers-parity-design.md.

## What
- using-fastmcp-engineering bootstrap skill + 8 tool mappings
- Trigger/Deliverables contract sections for all 57 domain skills (contract tests green)
- Shape A: session-start hook for Claude Code / Cursor / Copilot CLI
- Shape B: OpenCode plugin (config + messages.transform) and pi extension
- Shape C: Gemini context-file extension
- Native: Codex (hooks suppression) + Kimi (sessionStart.skill)
- .version-bump.json + bump script; harness install docs; porting guide
## Evidence
- pytest tests/: all green
- hook/opencode/pi/gemini/codex/kimi test suites: all green
- opencode debug config: using-fastmcp-engineering present
## Notes
- Merge → delete branch → verify main (repo workflow)."
# Вернуть PR URL. Merge/delete — по решению владельца.
```

- [ ] **Step 6: Дождаться решения владельца по merge; после merge — verify main + branch inventory**

```bash
# (после merge)
git checkout main && git pull
git log --oneline -5
git branch -a | grep -i superpowers || echo "branch deleted"
```

---

## Self-Review

**1. Spec coverage:**
- §Component 1 (Skills) → Task 1 (bootstrap) + Task 2 (Trigger/Deliverables)
- §Component 2 (Tool mapping) → Task 1 Step 4 (8 references)
- §Component 3 (Bootstrap) → Task 3 (Shape A), Task 4-5 (Shape B), Task 6 (Shape C), Task 7 (native)
- §Versioning → Task 8
- §Testing → каждый Task + Task 10
- §Documentation → Task 9
- §Working process → порядок задач, Task 10 PR
- Constraints «НЕ трогать глобальные файлы» → соблюдены (только репо-файлы)

**2. Placeholder scan:** все файлы даны дословно (кроме per-skill контента Task 2, где правило вывода из тела + 1 полный пример + шаблон); install-команды харнесов в Task 9 Step 2 требуют уточнения реальных команд в момент выполнения (задокументированы как конкретные, но marketplace-команды Claude/Cursor уточняются при наличии доступа).

**3. Type consistency:** `FastMcpEngineeringPlugin` (Task 4) ↔ тест Task 4 Step 3-4; `fastmcpEngineeringPiExtension` (Task 5) ↔ тест Task 5 Step 3; имена скиллов/манифестов совпадают между задачами; `EXPECTED_SKILL_COUNT = 58` во всех местах; версия 0.2.0 консистентна (Task 3-8).