# FastMCP Engineering × Superpowers Parity — Design Spec

> **Дата:** 2026-09-01
> **Ветка:** `feat/superpowers-parity`
> **Статус:** согласовано с пользователем (5 секций дизайна одобрены)

## Goal

Достичь паритета с архитектурой плагина `obra/superpowers` для всех харнесов:
воспроизвести трёхкомпонентную модель (skills / tool mapping / bootstrap),
обеспечив auto-trigger доменных fastmcp-engineering скиллов в любом кодовом
агенте (Claude Code, Cursor, Copilot CLI, Codex, Kimi, OpenCode, pi, Gemini).

**Бутстрап — это вся интеграция.** Без инъекции `using-fastmcp-engineering`
в начале каждого сеанса скиллы инертны — присутствуют на диске, но никогда
не вызываются.

## Non-negotiable rules (из superpowers `docs/porting-to-a-new-harness.md`)

1. **Скиллы называют действия, а не инструменты.** Тела доменных скиллов не
   редактируются под конкретный харнес. Адаптация — только в tool mapping
   (`references/<harness>-tools.md`) и бутстрапе.
2. **Всё доставляется через собственный install-механизм харнеса.** Плагин,
   extension, marketplace entry, context file, объявленный манифестом. НИКОГДА
   не правим файлы пользователя (`~/.gemini/config/AGENTS.md`, `settings.json`,
   `~/.bashrc`, глобальные `opencode.json` и т.д.).
3. **Автоматическая инъекция на старте сеанса — обязательна**, без per-session
   opt-in пользователя. Если харнес не умеет — он не поддерживается.
4. **Zero-dependency плагин.** Никаких сторонних runtime-зависимостей.
   Исключение (как в superpowers) — только новый харнес и только type-only
   импорты.
5. **Инъекция — user-сообщение, а не system-сообщение** (token bloat #750,
   поломка моделей при множественных system-сообщениях #894).
6. **Dedup guard + кэш контента бутстрапа.** Колбэки могут срабатывать на
   каждый шаг (opencode) или каждый ход (pi); не читаем диск повторно (#1202),
   не инъецируем дважды.
7. **Re-injection после compaction.** pi: lifecycle-флаг
   (`session_start`/`session_compact` → true, `agent_end` → false) и вставка
   после compaction-summary сообщений. opencode: per-step re-injection +
   dedup guard.
8. **Сообщение-объект per-harness** — не копировать литерал из чужого
   харнеса; формы `pi` и `opencode` несовместимы.
9. **`.sh` на Windows → polyglot `run-hook.cmd`**, hook-скрипты без расширения
   (`session-start`, не `session-start.sh`).
10. **Версии манифестов — в локстейпе** через `.version-bump.json`.

## Architecture

Три компонента (по образцу superpowers):

```
fastmcp-engineering/
├── skills/
│   ├── using-fastmcp-engineering/          # НОВЫЙ бутстрап-скилл (ядро)
│   │   └── references/                     # per-harness tool mapping (8 файлов)
│   │       ├── claude-code-tools.md
│   │       ├── cursor-tools.md
│   │       ├── codex-tools.md
│   │       ├── copilot-tools.md
│   │       ├── gemini-tools.md
│   │       ├── kimi-tools.md
│   │       ├── opencode-tools.md
│   │       └── pi-tools.md
│   ├── ...                                 # 57 доменных скиллов (тела без изменений,
│   │                                          добавляем секции Trigger/Deliverables)
├── hooks/
│   ├── session-start                       # единый shell-hook, 3 формы JSON (Shape A)
│   └── run-hook.cmd                        # polyglot Windows/Unix обёртка
├── .claude-plugin/plugin.json              # Claude Code (Shape A)
├── .cursor-plugin/plugin.json
│   └── hooks/hooks-cursor.json             # Cursor (Shape A)
├── .codex-plugin/plugin.json               # Codex (расширить; нативные скиллы)
├── .kimi-plugin/plugin.json                # Kimi (manifest sessionStart.skill)
├── .opencode/plugins/fastmcp-engineering.js  # OpenCode (Shape B, расширить)
├── .pi/extensions/fastmcp-engineering.ts     # pi (Shape B)
├── gemini-extension.json + FME.md          # Gemini (Shape C)
├── .version-bump.json                      # версии манифестов в локстейпе
├── scripts/bump-version.sh                 # синхронизация версий (zero-dep)
├── docs/
│   ├── porting-to-a-new-harness.md         # адаптированный гайд superpowers
│   └── README.<harness>.md                 # установка по каждому харнесу
└── tests/
    ├── hooks/   ├── opencode/   ├── pi/
    ├── codex/   ├── kimi/       ├── gemini/
    ├── test_skill_contract.py  (обновить: trigger/deliverables, инвентарь 58)
    └── test_skill_scenarios.py (обновить)
```

## Component 1 — Skills

- **Доменные скиллы (57):** тела tool-нейтральны (проверено: 0 упоминаний
  инструментов). К каждому добавляются две секции, консистентно после
  `## Mission/Purpose`:

  ```markdown
  ## Trigger / Когда применять
  <сценарии, при которых скилл ДОЛЖЕН быть вызван; признаки задачи;
  случаи, когда применять НЕ нужно>

  ## Deliverables
  <что агент обязан произвести: артефакт, формат, evidence, критерии приёмки>
  ```

  Контент выводится из существующего тела скилла, без новой логики.

- **Бутстрап-скилл `using-fastmcp-engineering/SKILL.md`:** фронтматтер
  `name` + `description` (≤1024 chars); секции: SUBAGENT-STOP,
  `<EXTREMELY-IMPORTANT>` (правило «проверь скилл до любого действия»),
  The Rule, Skill Priority, «How FastMCP/MCP work is different» (research-first,
  версионирование протокола/API, архитектурный гейт, контракты, TDD,
  верификация), Domain skills index, Platform Adaptation (ссылки на 8
  references-файлов).

## Component 2 — Tool mapping

8 файлов `skills/using-fastmcp-engineering/references/<harness>-tools.md`.
Покрывают действия: read/create/edit/delete file, shell, grep/glob, web
fetch/search, dispatch subagent (с указанием как передать тип агента),
create/update todos, invoke skill (native Skill tool ИЛИ чтение `SKILL.md` —
для харнесов без skill tool это санкционированный путь, прописываем явно).

## Component 3 — Bootstrap injection

Формы инъекции по харнесу:

- **Shape A (shell-hook):** `hooks/session-start` читает
  `skills/using-fastmcp-engineering/SKILL.md`, оборачивает в
  `<EXTREMELY_IMPORTANT>` + preamble «You have fastmcp-engineering...», и
  печатает JSON ровно одной формы в зависимости от env:
  - Cursor (`CURSOR_PLUGIN_ROOT`): `{ "additional_context": "…" }`
  - Claude Code (`CLAUDE_PLUGIN_ROOT`, `!COPILOT_CLI`):
    `{ "hookSpecificOutput": { "hookEventName": "SessionStart", "additionalContext": "…" } }`
  - Copilot CLI / SDK (else): `{ "additionalContext": "…" }`
  Манифесты: `.claude-plugin/plugin.json` + `hooks/hooks.json`
  (matcher `startup|clear|compact`, `${CLAUDE_PLUGIN_ROOT}/hooks/run-hook.cmd session-start`);
  `.cursor-plugin/plugin.json` + `hooks/hooks-cursor.json`
  (version 1, lowercase `sessionStart`, relative `./hooks/run-hook.cmd session-start`).

- **Shape B (in-process):**
  - OpenCode `.opencode/plugins/fastmcp-engineering.js`: `config` hook
    регистрирует `skills/` dir; `experimental.chat.messages.transform`
    инъецирует бутстрап в первое user-сообщение; dedup по маркеру
    `EXTREMELY_IMPORTANT`; кэш контента. Tool mapping inline + reference.
  - pi `.pi/extensions/fastmcp-engineering.ts`: `resources_discover` →
    `skillPaths`; `context` event инъецирует user-сообщение; lifecycle-флаг +
    compaction-aware. Tool mapping inline + reference.

- **Shape C (instructions-file):**
  - Gemini `gemini-extension.json` (`contextFileName: "FME.md"`) + `FME.md` с
    двумя `@-includes`: бутстрап-скилл + `references/gemini-tools.md`.

- **Native skills без session-hook:**
  - Codex `.codex-plugin/plugin.json` (расширить): `"skills": "./skills/"`,
    пустой `hooks` (подавить авто-дискавери `hooks.json`); tool mapping →
    `references/codex-tools.md`; бутстрап — surfaced description скилла.
  - Kimi `.kimi-plugin/plugin.json`: `"skills": "./skills/"`,
    `sessionStart.skill: "using-fastmcp-engineering"`,
    `skillInstructions` (inline mapping).

## Versioning

`.version-bump.json` — все 7 версионируемых манифестов:
`package.json` (если появится), `.claude-plugin/plugin.json`,
`.cursor-plugin/plugin.json`, `.codex-plugin/plugin.json`,
`.kimi-plugin/plugin.json`, `gemini-extension.json`,
`.claude-plugin/marketplace.json` (plugins.0.version).
`scripts/bump-version.sh` — бамп во всех разом (zero-dep, порт из superpowers).

## Testing

- `tests/hooks/test-session-start.sh` — Shape A: точная JSON-форма каждого
  харнеса + присутствие бутстрапа (как `tests/hooks/test-session-start.sh`).
- `tests/opencode/` — faked plugin API: handler'ы регистрируются, бутстрап
  инъецируется ровно раз, dedup работает, кэш при отсутствии файла.
- `tests/pi/` — lifecycle-флаг, compaction re-inject, dedup.
- `tests/codex/` — манифест валиден, `skills` path существует, references.
- `tests/kimi/`, `tests/gemini/` — манифесты + `@-includes` разрешаются.
- `tests/test_skill_contract.py` — `SEMANTIC_REQUIREMENTS` пополняется
  токенами `trigger` и `deliverables`; инвентарь 57 → 58
  (`EXPECTED_SKILL_COUNT`). 3 текущих падающих теста станут зелёными.
- `tests/test_skill_scenarios.py` — обновление под новые секции.

## Documentation

- `docs/porting-to-a-new-harness.md` — адаптированный гайд: инварианты,
  3 shape, правила, Appendix A (референс-интеграции), Appendix B (gotchas).
- `docs/README.<harness>.md` — установка по каждому харнесу через его
  собственный install-механизм (никогда не правим файлы пользователя).
- `README.md` — секция установки для всех харнесов.
- `AGENTS.md` / `CLAUDE.md` — синхронизация, если меняется агентский воркфлоу
  (бутстрап-скилл и его инъекция — часть агентского воркфлоу).

## Working process

Одна ветка `feat/superpowers-parity`, один PR. Порядок (TDD):

1. Бутстрап-скилл + 8 references
2. Trigger/Deliverables 57 скиллам + контракт-тесты (инвентарь 58)
3. Shape A: hooks + .claude-plugin + .cursor-plugin + Copilot-ветка + тесты
4. Shape B: .opencode + .pi + тесты
5. Shape C: gemini + тесты
6. Native: .codex-plugin (расширить) + .kimi-plugin + тесты
7. .version-bump.json + scripts/bump-version.sh
8. Доки
9. Итоговая верификация: pytest зелёный, ruff, shellcheck, smoke (opencode
   debug config / вопрос модели), branch inventory, PR

## Verification evidence

- `uv run --with pytest python -m pytest tests/ -q` — все зелёные
- `ruff check tests/`
- shellcheck для `hooks/session-start`, `scripts/bump-version.sh`
- Smoke: `opencode debug config` показывает `using-fastmcp-engineering`;
  при доступной модели — «какие у тебя fastmcp-engineering скиллы?»

## Constraints / Not touched

- НЕ меняем: `~/.config/opencode/opencode.json` (глобальный), глобальный
  `~/.config/opencode/plugin/fastmcp-engineering.ts` (верифицирован),
  глобальный `~/.config/opencode/AGENTS.md`.
- Расширяем (не ломаем): `.codex-plugin/plugin.json`, `.opencode/opencode.json`
  (проектный), `opencode/agents/` (fm-* роли остаются), `README.md`, `AGENTS.md`.
- Не удаляем существующие fm-агенты и команды.
- Существующие 3 падающих теста — pre-existing долг; фиксируются в рамках
  Task 2 (trigger/deliverables).

## Self-review

- Placeholders: нет.
- Внутренняя согласованность: architecture ↔ components ↔ tasks соответствуют.
- Scope: одна ветка, один PR, декомпозиция на 9 задач с TDD.
- Однозначность: каждая секция дизайна явная; формы JSON зафиксированы.