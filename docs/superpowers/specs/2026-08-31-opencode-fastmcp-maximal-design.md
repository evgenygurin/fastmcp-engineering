# Opencode × fastmcp-engineering — Maximal Integration Design

Date: 2026-08-31
Status: Approved (brainstorming → user "да")
Repos: `evgenygurin/fastmcp-engineering` (canonical), `~/.config/opencode/` (global exposure)
Related: `docs/superpowers/plans/2026-08-30-opencode-plugin-verification-report.md` (plugin PASS), opencode docs (config/agents/commands/plugins/skills, verified 2026-08-31)

## 1. Goal / Non-Goals

**Goal:** Все возможности fastmcp-engineering (44 skills, 116 prompts, contracts, architecture, research, plugin-hint, reference) доступны из ЛЮБОГО opencode-проекта через глобальный конфиг, с репо как single source of truth.

**Non-Goals:** MCP-обёртка над репо; 116 команд; мутация `cfg.command` в плагине; per-project конфиги; изменения codex-плагина; изменения верифицированного plugin-hint.

## 2. Current state audit (2026-08-31)

Работает глобально: `skills.paths` → 44 skills; reference `@fastmcp-eng`; plugin-hint (PASS, отчёт 2026-08-30); Agent Contract в глобальном `AGENTS.md`.

Не подключено: **116 prompts** (`prompts/*.md` — research/implementation/audit role-агенты по ~20 доменам) нигде не экспонированы.

Риски в dev-клоне `/Users/laptop/dev/fastmcp-engineering` (branch main, dirty):

| Артефакт | Статус | Действие |
|---|---|---|
| Frontmatter в 7 `SKILL.md` | M, **load-bearing** (opencode требует `name`+`description` — без этого skills не грузятся) | закоммитить |
| Дедупликация: `skills/configuration/dependency-management`, `skills/observability-telemetry-engineering` | D (дубли) | закоммитить |
| GitNexus-блок в `AGENTS.md` | M (auto-generated `gitnexus:start/end`) | закоммитить |
| Verification-доки 2026-08-30 (plan + report) | untracked, легитимные | закоммитить |
| `main.py`, `pyproject.toml` (root) | untracked, мусор `uv init` | удалить |
| `.opencode/opencode.json`: `skills` path `["skills"]` vs `["../skills"]`; telegram disable | M, резолюция не верифицирована | верифицировать `opencode debug config`, оставить рабочую форму; telegram-disable оставить |

## 3. Design

### 3.1 Каноничный layout в репо

Новый top-level `opencode/` (в стиле существующих `skills/`, `prompts/`, `contracts/`):

```
opencode/
├── agents/
│   ├── fm-research.md
│   ├── fm-implementation.md
│   ├── fm-audit.md
│   ├── fm-review.md
│   └── fm-governor.md
└── commands/
    ├── fm.md
    └── fm-prompts.md
```

Версонируется, PR-reviewed, шарится (README описывает setup для других машин).

### 3.2 Глобальная экспозиция — симлинки

`~/.config/opencode/agents/fm-*.md` → симлинки на файлы репо; `~/.config/opencode/commands/{fm,fm-prompts}.md` → аналогично. Ноль копий, авто-синк, канон в git. (Discovery сканирует директории; файловые симлинки резолвятся при чтении.)

### 3.3 Контракт fm-агента

`mode: subagent` (виден в `@`-автокомплите + task tool), `model`: inherit. Системный промпт — процедура:

1. Прочитать задачу, определить engineering-домен (security / observability / database / transports / …)
2. Прочитать `prompts/{domain}-{role}-agent.md` из PRIMARY-клона `/Users/laptop/dev/fastmcp-engineering/prompts/`; fallback: `~/.local/share/opencode/repos/github.com/evgenygurin/fastmcp-engineering@main/prompts/`
3. Нет доменного промпта → generic: `research-agent.md`, `implementation-agent.md`, `review-agent.md`, `architecture-governor-agent.md` (fm-audit fallback → `review-agent.md` — generic audit отсутствует)
4. Следовать загруженному промпту дословно, включая mandatory research gate (context7/exa/gitnexus evidence)
5. Отчёт по output-формату промпта

Permissions per-role (`external_directory: allow` обязателен — промпты вне worktree):

| Агент | edit | bash | прочее |
|---|---|---|---|
| `fm-research` | deny | `git log*`/`git diff*`/`git show*`/`ls *`: allow, `*`: ask | webfetch, websearch, skill, external_directory: allow |
| `fm-implementation` | allow | allow | skill, external_directory: allow |
| `fm-audit` / `fm-review` / `fm-governor` | deny | `git log*`/`git diff*`/`git show*`/`ls *`: allow, `*`: ask | webfetch, skill, external_directory: allow |

### 3.4 Команды

- `/fm` — dispatcher: template роутит role-слово ($1: research/implementation/audit/review/governor) на соответствующий fm-субагента (task tool), остаток — задача; неизвестное/пропущенное role-слово → `fm-research`; без `subtask:` (роутит основной агент)
- `/fm-prompts` — инвентаризация: `!`ls`` prompts-директории + маппинг role→домены

### 3.5 Чистка dev-клона (та же ветка `feat/opencode-agents-wiring`, отдельные коммиты)

1. `docs:` — этот спек
2. `chore: commit load-bearing skills frontmatter WIP + verification docs` — SKILL.md frontmatter, дедупликация, gitnexus-блок, 2 дока 2026-08-30
3. `chore: remove uv init artifacts` — `main.py`, `pyproject.toml`
4. `fix(opencode): verify skills path via opencode debug config` — `.opencode/opencode.json` (рабочая форма пути; telegram-disable остаётся)
5. `feat(opencode): fm role agents + commands` — `opencode/agents/*`, `opencode/commands/*`, README-секция «opencode integration» (setup симлинков)
6. Машина-локально (не в репо): создать симлинки в `~/.config/opencode/{agents,commands}/`

### 3.6 Edge cases

- PRIMARY-клон отсутствует → fallback reference-путь (оба пути зашиты в промпт агента)
- Домен-промпт отсутствует → generic role-промпт
- Битый симлинк → файл не грузится (детект: `opencode debug config` + `/fm-prompts` smoke)
- Drift исключён: агенты читают промпты в runtime

## 4. Verification

1. `opencode debug config` внутри репо — resolved skills path + agents/commands видны
2. Новая opencode-сессия в произвольном проекте: `@fm-*` в автокомплите; `/fm-prompts` листит 116; smoke-dispatch `@fm-research` (мини-задача); skills по-прежнему грузятся (44 + 19 workflow)
3. Repo workflow: одна ветка → один PR → merge → delete branch → verify main

## 5. YAGNI (явные исключения)

MCP-server обёртка; генерация 116 команд; plugin `cfg.command` мутация; per-project `.opencode` в других репо; codex-plugin правки.

## Self-Review

- Placeholders: нет TBD
- Consistency: symlink-схема ↔ repo-layout ↔ cleanup-коммиты согласованы; permissions соответствуют ролям
- Scope: один план имплементации (5 коммитов + машинно-локальные симлинки)
- Ambiguity: resolved — fm-audit fallback = review-agent.md; telegram-disable = оставить; junk = удалить
