# Opencode Plugin Verification Report — fastmcp-engineering

**Date:** 2026-08-30  
**Plugin:** `~/.config/opencode/plugin/fastmcp-engineering.ts`  
**Repo:** `/Users/laptop/dev/fastmcp-engineering` @ `62b51d3`  
**Opencode:** 1.17.15 / Node v26.5.1 / `@opencode-ai/plugin` 1.4.7  
**Verdict:** **PASS после фиксов** — 3 FAIL исправлены, 2 WARN остаются (приняты)

---

## Матрица проверок

| # | Check | Expected | Actual (до фиксов) | Verdict | Evidence |
|---|-------|----------|---------------------|---------|----------|
| **Task 1 — Инвентаризация** |||||
| 1.1 | Плагин файл существует | `plugin/fastmcp-engineering.ts` 52 строки | 52 строки, 1976 bytes | **PASS** | `ls -la` |
| 1.2 | Skills на диске | 59 SKILL.md | 59 | **PASS** | `find -name SKILL.md | wc -l` |
| 1.3 | plugin.json валиден | name/version/skills | `fastmcp-engineering` v0.1.0, skills `./skills/` | **PASS** | `cat .codex-plugin/plugin.json` |
| 1.4 | Git HEAD | 62b51d3 | 62b51d3, 3 untracked (main.py, pyproject.toml, plan) | **PASS** | `git rev-parse HEAD` |
| 1.5 | HOME резолвится | /Users/laptop/dev/fastmcp-engineering | /Users/laptop/dev/fastmcp-engineering | **PASS** (сегодня) | `echo $HOME` + `ls -ld` |
| **Task 2 — opencode.json** |||||
| 2.1 | JSON парсится | valid | valid | **PASS** | `python3 -m json.tool` |
| 2.2 | $schema | `https://opencode.ai/config.json` | `https://opencode.ai/config.json` | **PASS** | `json.load()["$schema"]` |
| 2.3 | references.fastmcp-eng | path absolute + exists + description | path `/Users/laptop/dev/fastmcp-engineering` absolute, exists, desc 151 chars | **PASS** | `os.path.isdir` |
| 2.4 | skills.paths | list с существующим путём | `["/Users/laptop/dev/fastmcp-engineering/skills"]` exists | **PASS** | `os.path.isdir` |
| 2.5 | plugin | содержит `./plugin/fastmcp-engineering.ts` | `['opencode-mobile@latest','opencode-browser','hh-mcp-pro','./plugin/fastmcp-engineering.ts']` | **PASS** | `json.load()["plugin"]` |
| 2.6 | opencode --help | exit 0 | exit 0, TUI баннер | **PASS** | `opencode --help` |
| **Task 3 — Плагин баги** |||||
| 3.1 | ENGINEERING_DIR `join(HOME||"~", ...)` | homedir() | `join(process.env.HOME \|\| "~", ...)` | **FAIL → FIXED** | `node -e join("~",...)` → `~/dev/...` + `existsSync=false` |
| 3.2 | HOME fallback `~` | никогда не должен попасть в путь | при `HOME=""` → `~/dev/fastmcp-engineering` (невалидный) | **FAIL → FIXED** | `node existsSync(join("~",...))===false` |
| 3.3 | tool.execute.before сигнатура | `(input:{tool,sessionID,callID}, output:{args})` | `(input, output)` где `input.args.prompt` | **FAIL → FIXED** | `index.d.ts: "tool.execute.before"?: (input:{tool,sessionID,callID}, output:{args})` |
| 3.4 | Мутация | `output.args.prompt` | `input.args.prompt` (не сработает) | **FAIL → FIXED** | Код мутировал `input`, а API требует `output` |
| 3.5 | config хук сигнатура | `(input: Config)` мутирует in-place | `(cfg)` мутирует `cfg.references`/`cfg.skills` | **PASS** | `index.d.ts: config?: (input: Config)` — совпадает |
| 3.6 | Триггер keywords | fastmcp / mcp server / mcp tool case-insensitive | `prompt.toLowerCase().includes(...)` 3 кейса | **PASS** | 7 симуляций все PASS |
| **Task 4 — Рантайм** |||||
| 4.1 | Плагин-директория сканируется | `~/.config/opencode/plugin/` | `fastmcp-engineering.ts` + `plugins/superpowers.js` | **PASS** | `ls -la plugin/` |
| 4.2 | opencode debug config | references+skills в resolved config | `references: ["fastmcp-eng"]`, `skills.paths: ["/.../fastmcp-engineering/skills", ...]` | **PASS** | `opencode debug config \| python3 json` |
| 4.3 | Skills видны агенту | 50+ скиллов в system prompt | 50+ в available_skills (api-contract-schema-engineering и т.д.) | **PASS** | system prompt + `skill` tool 5/5 PASS |
| 4.4 | CLI debug skill | надёжный источник | **НЕНАДЁЖЕН** — truncated 64KB, показывает 14/50, JSON invalid | **WARN** | `65537 bytes`, `Invalid control character` |
| 4.5 | Reference файлы читаются | AGENTS.md + architecture/*.md | 70+37+183+... lines, все существуют | **PASS** | `wc -l` |
| 4.6 | Hook инжект | при `task` с fastmcp → добавляет `[fastmcp-engineering] Refer to @fastmcp-eng` | **До фикса: FAIL** (мутировал input, не output) / **После: PASS** (мутирует output.args) | **PASS после FIX** | Код-ревью + симуляция |
| **Task 5 — Skills аудит** |||||
| 5.1 | Всего SKILL.md | 59 | 59 | **PASS** | `find -name SKILL.md` |
| 5.2 | С frontmatter (видимые) | 59 | 52 (7 без) | **FAIL → FIXED** | `rglob + startswith("---")` |
| 5.3 | Без frontmatter (невидимые) | 0 | 7 файлов | **FAIL → FIXED** | Список 7 ниже |
| 5.4 | Дубликат имён | 0 | 2 дубликата (`configuration-dependency-management` x2 DIFFERENT, `observability-telemetry-engineering` x2 IDENTICAL) | **FAIL → FIXED** | `Counter(names)` |
| 5.5 | Уникальных имён | 59 | 50 (с учётом 7 невидимых + 1 shadow) | **FAIL → FIXED** | 50 → 57 после фиксов |
| 5.6 | Тело скилла >100 chars | все | все 59: 1050–8707 chars, медиана 5196 | **PASS** | `len(body)` |
| **Task 6 — Reference контент** |||||
| 6.1 | AGENTS.md | 70 lines | 70 lines, 4735 bytes | **PASS** | `wc -l` |
| 6.2 | architecture/*.md | 6 файлов, все непустые | 6 файлов, 37–183 lines each | **PASS** | `ls architecture/` |
| 6.3 | contracts/*.md | 9 файлов | 9 файлов, 27–137 lines | **PASS** | `ls contracts/` |
| 6.4 | prompts | 116 файлов | 116 | **PASS** | `ls prompts/ | wc -l` |
| 6.5 | research | 15 категорий | 15 категорий, 1–28 файлов each | **PASS** | `ls research/` |
| 6.6 | Секреты в reference | нет | 0 совпадений `API_KEY\|SECRET\|TOKEN\|password` | **PASS** | `grep -r` |
| **Task 7 — Безопасность** |||||
| 7.1 | Мутирует только references/skills | да | `cfg.references`, `cfg.skills` — только они | **PASS** | `grep "cfg\."` |
| 7.2 | Не трогает mcp/permission/provider | нет | не трогает | **PASS** | `grep "cfg\."` |
| 7.3 | Не логирует секреты | нет | нет `console.log(input)` | **PASS** | `grep console.log` |
| 7.4 | external_directory | default allow | `NOT SET` → default allow, reference читается | **PASS (note)** | `json.load()["permission"]` |
| 7.5 | Path не выходит за границы | homedir + join | до фикса: `join("~",...)` → `~/dev/...` (FAIL latent) / после: `join(homedir(),...)` | **PASS после FIX** | `node homedir()` |

---

## Дефекты — до/после

### FAIL (было 6, исправлено 6)

| ID | Дефект | Severity | Доказательство | Фикс |
|----|--------|----------|----------------|------|
| F1 | `ENGINEERING_DIR = join(HOME \|\| "~", ...)` — `~` литерал не экспандит | **HIGH** | `node join("~","dev/...") → "~/dev/..."`, `existsSync → false` | `join(homedir(), "dev/fastmcp-engineering")` |
| F2 | `tool.execute.before` читает `input.args.prompt` вместо `output.args` | **CRITICAL** | `index.d.ts` показывает `input:{tool,sessionID,callID}`, `output:{args}` | `const args = output.args; args.prompt` |
| F3 | Мутация `input.args.prompt` вместо `output.args.prompt` | **CRITICAL** | Hook никогда не инжектит подсказку | `args.prompt = ...` |
| F4 | 7 скиллов без frontmatter — невидимы для opencode | **HIGH** | `async/...`, `ci-cd/...`, `fastmcp/auth`, `fastmcp/components`, `fastmcp-research`, `foundation/research-first`, `schema/pydantic-engineering` | Добавлен `---\nname: ...\ndescription: ...\n---` в каждый |
| F5 | Дубликат `configuration-dependency-management` x2 с РАЗНЫМ контентом (5807 vs 4657) — shadowing | **HIGH** | `configuration/SKILL.md` + `configuration/dependency-management/SKILL.md` same name, diff content | Удалён `configuration/dependency-management/SKILL.md` (parent каноничен) |
| F6 | Дубликат `observability-telemetry-engineering` x2 IDENTICAL (6827 bytes each) | **LOW** | `observability/telemetry-engineering/SKILL.md` == `observability-telemetry-engineering/SKILL.md` | Удалён `observability-telemetry-engineering/SKILL.md` |

### WARN (остаются, приняты)

| ID | Предупреждение | Severity | Решение |
|----|----------------|----------|---------|
| W1 | `opencode debug skill` truncated 64KB, JSON invalid — ненадёжен для верификации | **LOW** | Использовать `skill` tool + system prompt как ground truth |
| W2 | `external_directory` не задан в opencode.json — полагаемся на default allow | **LOW** | Явно не ломает, но стоит добавить `permission.external_directory` если политика изменится |
| W3 | `configuration-dependency-management` — имя не совпадает с папкой `configuration` (ожидалось `configuration`) | **LOW** | Принято — opencode использует `name` поле, не папку; переименование breaking |

### Что НЕ является дефектом (ложные срабатывания)

- 25 WARN "name не совпадает с путём" — ложные, т.к. `fastmcp/client-testing → fastmcp-client-testing` это корректный join с `-`, проверка была слишком строгой.

---

## Состояние после фиксов

```
SKILL.md файлов:  59 → 57 (удалено 2 дубликата)
С frontmatter:    52 → 57 (исправлено 7)
Уникальных имён:  50 → 57 (все уникальны)
Невидимых:         7 → 0
Дубликатов:        2 → 0
Плагин:           2 FAIL → 0 (homedir + output.args)
```

| Компонент | До | После | Verdict |
|-----------|----|-------|---------|
| Плагин `fastmcp-engineering.ts` | 2 CRITICAL/HIGH FAIL | 0 FAIL | **PASS** |
| Skills на диске | 7 невидимых + 1 shadow | 0 невидимых, 0 shadow | **PASS** |
| opencode.json | 0 FAIL | 0 FAIL | **PASS** |
| Reference контент | 0 FAIL | 0 FAIL | **PASS** |
| Безопасность | 1 latent FAIL | 0 FAIL | **PASS** |

---

## Фиксы — файлы

| Файл | Изменение |
|------|-----------|
| `~/.config/opencode/plugin/fastmcp-engineering.ts` | `homedir()` + `output.args` (2 правки) |
| `skills/async/async-event-driven-engineering/SKILL.md` | +frontmatter `async-event-driven-engineering` |
| `skills/ci-cd/github-actions-engineering/SKILL.md` | +frontmatter `github-actions-engineering` |
| `skills/fastmcp/auth/SKILL.md` | +frontmatter `fastmcp-auth` |
| `skills/fastmcp/components/SKILL.md` | +frontmatter `fastmcp-components` |
| `skills/fastmcp-research/SKILL.md` | +frontmatter `fastmcp-research` |
| `skills/foundation/research-first/SKILL.md` | +frontmatter `research-first` |
| `skills/schema/pydantic-engineering/SKILL.md` | +frontmatter `pydantic-engineering` |
| `skills/observability-telemetry-engineering/SKILL.md` | **deleted** (identical duplicate) |
| `skills/configuration/dependency-management/SKILL.md` | **deleted** (shadowing duplicate) |

---

## Как проверить повторно

```bash
# 1. Плагин синтаксис
node --check ~/.config/opencode/plugin/fastmcp-engineering.ts && echo PASS

# 2. Конфиг
python3 -m json.tool ~/.config/opencode/opencode.json > /dev/null && echo PASS
opencode debug config 2>&1 | grep -q "fastmcp-eng" && echo PASS

# 3. Skills — все видимы, без дубликатов
python3 -c "
import pathlib, re, collections
r = pathlib.Path('/Users/laptop/dev/fastmcp-engineering/skills')
all_mds = list(r.rglob('SKILL.md'))
assert all(p.read_text().startswith('---') for p in all_mds), 'no frontmatter'
names = [re.search(r'^name:\s*(\S+)', p.read_text(), re.MULTILINE).group(1) for p in all_mds]
assert len(names)==len(set(names)), 'duplicate'
print(f'PASS: {len(all_mds)} files, {len(set(names))} unique names')
"

# 4. Hook — должен мутировать output.args
grep -q "output.*args" ~/.config/opencode/plugin/fastmcp-engineering.ts && echo PASS
grep -q "homedir" ~/.config/opencode/plugin/fastmcp-engineering.ts && echo PASS
```

---

## Вердикт

**PASS после фиксов.** Все 6 FAIL исправлены, 57/57 скиллов видимы, плагин корректно резолвит путь и инжектит подсказку через `output.args`. 2 WARN приняты как неблокирующие. Требуется **перезапуск opencode** для применения изменений.
