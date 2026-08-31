# Opencode Plugin Deep Verification Plan — fastmcp-engineering

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Скептическая, evidence-first верификация плагина `fastmcp-engineering.ts` для opencode — фиксировать PASS/FAIL/WARN без жёлтых очков, найти все дефекты и исправить.

**Architecture:** Один файл-плагин `~/.config/opencode/plugin/fastmcp-engineering.ts` + запись в `~/.config/opencode/opencode.json` (references, skills.paths, plugin). Плагин обязан резолвить `ENGINEERING_DIR`, регистрировать reference и skills-путь в хуке `config`, инжектить подсказку в `tool.execute.before` только для релевантных `task` вызовов. Верификация идёт снизу вверх: файлы → конфиг → типы → рантайм-загрузка.

**Tech Stack:** opencode config schema (`https://opencode.ai/config.json`), TypeScript Plugin API (`@opencode-ai/plugin`), Node.js `path`/`fs`, `opencode --help` / `opencode mcp` / `opencode skill list` если доступно, `python3 -m json.tool`, `rg`, `tsc --noEmit` если есть.

## Global Constraints

- Не ломать существующий `~/.config/opencode/opencode.json` — валидный JSON с `$schema`.
- Плагин живёт в `~/.config/opencode/plugin/fastmcp-engineering.ts` (глобальный scope, автодискавери).
- `ENGINEERING_DIR` должен указывать на существующий checkout `/Users/laptop/dev/fastmcp-engineering`.
- Любой FAIL = баг, любой WARN = риск — фиксируется в отчёте, не скрывается.
- Исправление только после фиксации дефекта, с повторным прогоном проверки.

---

### Task 1: Инвентаризация исходного состояния

**Files:**
- Read: `~/.config/opencode/opencode.json`
- Read: `~/.config/opencode/plugin/fastmcp-engineering.ts`
- Read: `/Users/laptop/dev/fastmcp-engineering/.codex-plugin/plugin.json`
- Read: `/Users/laptop/dev/fastmcp-engineering/skills` (listing)
- Read: `/Users/laptop/.config/opencode/package.json` (если есть — версия opencode)

**Interfaces:**
- Consumes: файловая система, git checkout
- Produces: таблица фактов (пути, размеры, git HEAD, opencode версия) для всех последующих задач

- [ ] **Step 1: Зафиксировать файлы и размеры**

```bash
ls -la ~/.config/opencode/opencode.json ~/.config/opencode/plugin/fastmcp-engineering.ts
wc -l ~/.config/opencode/plugin/fastmcp-engineering.ts
ls -la /Users/laptop/dev/fastmcp-engineering/skills | head -n 50
cat /Users/laptop/dev/fastmcp-engineering/.codex-plugin/plugin.json
```

- [ ] **Step 2: Зафиксировать git HEAD и версии**

```bash
git -C /Users/laptop/dev/fastmcp-engineering rev-parse HEAD
git -C /Users/laptop/dev/fastmcp-engineering status --short
cat /Users/laptop/.config/opencode/package.json 2>/dev/null || cat ~/.config/opencode/package.json 2>/dev/null || echo "no package.json"
opencode --version 2>&1 || npx opencode --version 2>&1 || echo "opencode version unknown"
```

- [ ] **Step 3: Вывести таблицу фактов в отчёт**

Собрать: пути, размеры, HEAD, dirty-файлы, версия opencode, node, plugin.json версия.

---

### Task 2: Валидация opencode.json против схемы

**Files:**
- Read: `~/.config/opencode/opencode.json`
- Fetch: `https://opencode.ai/config.json` (схема)

**Interfaces:**
- Consumes: Task 1 — путь к конфигу
- Produces: PASS/FAIL по каждому полю (`references`, `skills.paths`, `plugin`)

- [ ] **Step 1: JSON-парсинг**

```bash
python3 -m json.tool ~/.config/opencode/opencode.json > /dev/null && echo "JSON PASS" || echo "JSON FAIL"
```

- [ ] **Step 2: Проверка $schema**

```bash
python3 -c "import json; d=json.load(open('/Users/laptop/.config/opencode/opencode.json')); assert d.get('\$schema')=='https://opencode.ai/config.json', d.get('\$schema'); print('schema PASS')"
```

- [ ] **Step 3: Проверка references.fastmcp-eng**

```bash
python3 -c "
import json, os
d=json.load(open('/Users/laptop/.config/opencode/opencode.json'))
r=d.get('references',{}).get('fastmcp-eng')
assert r, 'missing references.fastmcp-eng'
assert 'path' in r and 'description' in r, r
assert os.path.isdir(os.path.expanduser(r['path'])), r['path']
print('references PASS', r)
"
```

Скепсис: проверить что `path` — абсолютный, существует, не указывает на `~` литерал без expand, `description` не пустой.

- [ ] **Step 4: Проверка skills.paths**

```bash
python3 -c "
import json, os
d=json.load(open('/Users/laptop/.config/opencode/opencode.json'))
paths=d.get('skills',{}).get('paths',[])
assert isinstance(paths, list) and len(paths)>0, paths
for p in paths:
    assert os.path.isdir(p), p
print('skills.paths PASS', paths)
# Проверить что не массив-строк с опечаткой, не объект
"
```

- [ ] **Step 5: Проверка plugin массива**

```bash
python3 -c "
import json
d=json.load(open('/Users/laptop/.config/opencode/opencode.json'))
pl=d.get('plugin',[])
assert isinstance(pl, list), pl
assert './plugin/fastmcp-engineering.ts' in pl, pl
print('plugin PASS', pl)
"
```

- [ ] **Step 6: Попытка запустить opencode с текущим конфигом (dry-run)**

```bash
opencode --help 2>&1 | head -n 20
echo "exit: $?"
# Если падает — копировать ошибку целиком, FAIL
```

Ожидаем PASS на всех шагах. Любой assert = FAIL с логом.

---

### Task 3: Анализ плагина — корректность пути и баг с HOME

**Files:**
- Read: `~/.config/opencode/plugin/fastmcp-engineering.ts`

**Interfaces:**
- Consumes: Task 1 — содержимое плагина
- Produces: PASS/FAIL/WARN по каждому дефекту, список фиксов

- [ ] **Step 1: Прочитать файл и зафиксировать текущую строку ENGINEERING_DIR**

```bash
grep -n "ENGINEERING_DIR" ~/.config/opencode/plugin/fastmcp-engineering.ts
```

Ожидаем найти строку:
```ts
const ENGINEERING_DIR = join(process.env.HOME || "~", "dev/fastmcp-engineering")
```

- [ ] **Step 2: Доказать баг: `join("~", "dev/...")` не экспандит `~`**

```bash
node -e "import {join} from 'path'; console.log(join('~','dev/fastmcp-engineering'))"
# Ожидаем: ~/dev/fastmcp-engineering — это НЕвалидный путь, existsSync вернёт false
node -e "import {existsSync} from 'fs'; import {join} from 'path'; console.log(existsSync(join('~','dev/fastmcp-engineering')))"
```

Это FAIL-критичный: когда `HOME` не установлен, `hasSkills=false`, `skills.paths` не добавится, reference укажет на несуществующий путь. Фиксируем как FAIL.

- [ ] **Step 3: Проверить второй баг — хардкод `dev/fastmcp-engineering` без учёта реального HOME**

```bash
node -e "console.log(process.env.HOME)"
ls -la /Users/laptop/dev/fastmcp-engineering/skills | head -n 5
# Если HOME != /Users/laptop, путь сломается
```

- [ ] **Step 4: Проверить обработку `config` хука — мутабельность, идемпотентность**

Прочитать код:
```ts
if (!cfg.references) cfg.references = {}
cfg.references["fastmcp-eng"] = { path: ENGINEERING_DIR, description: "..." }
if (!cfg.skills) cfg.skills = {}
if (!cfg.skills.paths) cfg.skills.paths = []
if (!cfg.skills.paths.includes(skillsDir)) cfg.skills.paths.push(skillsDir)
```

Проверить: перезапись существующего `fastmcp-eng` без WARN? Дубликат `skills.paths` защищён `includes` — PASS, но проверить что `skillsDir` === `ENGINEERING_DIR + "/skills"` консистентен.

- [ ] **Step 5: Проверить `tool.execute.before` — сигнатура, мутация, кейсы**

Сигнатура в opencode Plugin API: `(input, output) => Promise<void>`, где `input.tool`, `input.args`. Проверить:
- `input.tool === "task"` — верно ли имя тула? (в opencode тул называется `task` для саб-агентов). Скепсис: проверить список тулов `opencode --help` или доку.
- `input.args.prompt` — точно ли поле называется `prompt`? (может быть `description`/`query`).
- Мутирует `input.args.prompt` напрямую — допустимо ли? Или нужно мутировать `output`?
- Триггер `fastmcp`/`mcp server`/`mcp tool` — покрывает ли `mcp-server`, `MCP Server`, `FastMCP`? (кейс-инсенситив PASS, но дефисы/подчёркивания WARN).
- Нет ли ложных срабатываний на `mcp tool` внутри `mcp toolkit`? WARN.

- [ ] **Step 6: Зафиксировать все FAIL/WARN в таблицу и предложить фиксы**

| Дефект | Severity | Доказательство |
|--------|----------|----------------|
| `join("~", ...)` не экспандит | FAIL | node existsSync false |
| Хардкод `dev/fastmcp-engineering` | WARN | зависит от HOME |
| Неверное имя тула `task` | WARN | проверить доку |
| Мутация `input` вместо `output` | WARN | проверить Plugin API |

---

### Task 4: Проверка загрузки плагина в рантайме opencode

**Files:**
- Read: `~/.config/opencode/plugin/fastmcp-engineering.ts`
- Run: `opencode` CLI

**Interfaces:**
- Consumes: Task 2, Task 3
- Produces: PASS/FAIL — плагин загружается без ошибок

- [ ] **Step 1: Проверить что плагин-директория сканируется**

```bash
ls -la ~/.config/opencode/plugin/
# Также проверить ~/.config/opencode/plugins/ (альтернативный путь)
ls -la ~/.config/opencode/plugins/ 2>&1 || echo "no plugins/ dir"
```

- [ ] **Step 2: Запустить opencode и проверить логи загрузки плагина**

```bash
opencode --help 2>&1 | head -n 50
# Искать ошибки типа "Failed to load plugin" / "Cannot find module"
# Если opencode пишет debug-лог: OPENCODE_LOG=debug opencode --help 2>&1 | grep -i plugin
```

- [ ] **Step 3: Проверить что skills из skills.paths реально подхватились**

```bash
# Попытка: opencode skill list / opencode skills / справка
opencode --help 2>&1 | grep -i skill
# Или проверить через MCP: список скиллов в системном промпте
# Скепсис: skills.paths может быть проигнорирован если плагин не сработал
```

- [ ] **Step 4: Проверить reference резолвится**

```bash
# В opencode references доступны как @fastmcp-eng — проверить что путь резолвится
python3 -c "
import json, os
d=json.load(open('/Users/laptop/.config/opencode/opencode.json'))
# Эмулировать резолв плагина: ENGINEERING_DIR должен существовать
import pathlib
p=pathlib.Path('/Users/laptop/dev/fastmcp-engineering')
print('exists', p.exists())
print('is_dir', p.is_dir())
print('AGENTS.md exists', (p / 'AGENTS.md').exists())
"
```

- [ ] **Step 5: Интеграционный тест — вызвать subagent с fastmcp промптом и проверить инжект**

```bash
# Если есть task tool — проверить что hook инжектит "[fastmcp-engineering] Refer to @fastmcp-eng"
# Эмулировать: создать тестовый task с prompt содержащим "fastmcp" и проверить что хук сработал
# Если нельзя эмулировать — зафиксировать как MANUAL CHECK
```

---

### Task 5: Аудит skills — полнота, схема, дубликаты

**Files:**
- Read: `/Users/laptop/dev/fastmcp-engineering/skills/**/SKILL.md` (59 файлов)
- Read: `https://opencode.ai/config.json` (skill схема — name, description, etc.)

**Interfaces:**
- Consumes: Task 1 — список файлов
- Produces: PASS/FAIL/WARN по каждому скиллу, таблица дефектов

- [ ] **Step 1: Перечислить все SKILL.md и их frontmatter**

```bash
find /Users/laptop/dev/fastmcp-engineering/skills -name "SKILL.md" | sort
for f in $(find /Users/laptop/dev/fastmcp-engineering/skills -name "SKILL.md"); do
  echo "=== $f ==="
  head -n 10 "$f"
done
```

- [ ] **Step 2: Валидация frontmatter — name, description обязательны**

```bash
python3 << 'PY'
import pathlib, re
for p in sorted(pathlib.Path("/Users/laptop/dev/fastmcp-engineering/skills").rglob("SKILL.md")):
    text = p.read_text()
    m = re.match(r'^---\n(.*?)\n---', text, re.DOTALL)
    if not m:
        print(f"FAIL {p}: no frontmatter")
        continue
    fm = m.group(1)
    if 'name:' not in fm: print(f"FAIL {p}: missing name")
    if 'description:' not in fm: print(f"FAIL {p}: missing description")
    # Проверить name matches folder, lowercase hyphen, <=64
    name = re.search(r'name:\s*(\S+)', fm)
    if name and len(name.group(1)) > 64: print(f"WARN {p}: name too long")
PY
```

Скепсис: opencode фильтрует скиллы без `description` — фиксируем сколько отфильтруется.

- [ ] **Step 3: Проверка дубликатов name**

```bash
python3 << 'PY'
import pathlib, re, collections
names = collections.Counter()
for p in pathlib.Path("/Users/laptop/dev/fastmcp-engineering/skills").rglob("SKILL.md"):
    text = p.read_text()
    m = re.search(r'^name:\s*(\S+)', text)
    if m: names[m.group(1)] += 1
for n,c in names.items():
    if c>1: print(f"FAIL duplicate name {n}: {c} files")
PY
```

- [ ] **Step 4: Проверка что skills.paths резолвит все скиллы**

```bash
ls /Users/laptop/dev/fastmcp-engineering/skills/ | wc -l
find /Users/laptop/dev/fastmcp-engineering/skills -name "SKILL.md" | wc -l
# Скепсис: skills.paths — рекурсивный **/SKILL.md или только топ-уровень?
```

- [ ] **Step 5: Выборочная проверка контента 3 скиллов на битые ссылки**

Открыть 3 случайных SKILL.md, проверить что `SKILL.md` ссылки на `scripts/`/`reference/` существуют если указаны.

---

### Task 6: Аудит reference-контента — AGENTS.md, architecture, contracts, prompts

**Files:**
- Read: `/Users/laptop/dev/fastmcp-engineering/AGENTS.md`
- Read: `/Users/laptop/dev/fastmcp-engineering/architecture/*`
- Read: `/Users/laptop/dev/fastmcp-engineering/contracts/*`
- Read: `/Users/laptop/dev/fastmcp-engineering/prompts/*`

- [ ] **Step 1: Проверить AGENTS.md — не пустой, содержит workflow**

```bash
wc -l /Users/laptop/dev/fastmcp-engineering/AGENTS.md
head -n 30 /Users/laptop/dev/fastmcp-engineering/AGENTS.md
```

- [ ] **Step 2: Проверить architecture и contracts — каждый .md не пустой, валидный markdown**

```bash
for f in /Users/laptop/dev/fastmcp-engineering/architecture/* /Users/laptop/dev/fastmcp-engineering/contracts/*; do
  echo "=== $f ==="; wc -l "$f"; head -n 5 "$f"
done
```

- [ ] **Step 3: Проверить prompts — 116 файлов, каждый не пустой**

```bash
ls /Users/laptop/dev/fastmcp-engineering/prompts/ | wc -l
for f in /Users/laptop/dev/fastmcp-engineering/prompts/*.md | head -n 5; do echo "=== $f ==="; wc -l "$f"; done
```

- [ ] **Step 4: Проверить что reference path не содержит секретов**

```bash
grep -r "API_KEY\|SECRET\|TOKEN\|password" /Users/laptop/dev/fastmcp-engineering/AGENTS.md /Users/laptop/dev/fastmcp-engineering/architecture/ 2>&1 | head -n 20
# WARN если найдено
```

---

### Task 7: Безопасность и изоляция

**Files:**
- Read: `~/.config/opencode/plugin/fastmcp-engineering.ts`
- Read: `~/.config/opencode/opencode.json` (mcp, permissions)

- [ ] **Step 1: Проверить что плагин не мутирует permissions, mcp, provider**

Код должен трогать только `references` и `skills.paths`. Если мутирует `mcp`/`permission` — FAIL.

- [ ] **Step 2: Проверить что ENGINEERING_DIR не выходит за границы**

`path.join(HOME, "dev/fastmcp-engineering")` — не должен резолвить в `/` или `~` литерал. Проверить `path.resolve`.

- [ ] **Step 3: Проверить что hook не логирует секреты**

`input.args.prompt` может содержать секреты — hook не должен логировать. Проверить отсутствие `console.log(input)`.

- [ ] **Step 4: Проверить external_directory permissions**

Если reference указывает на `~/dev/fastmcp-engineering`, opencode должен разрешить чтение. Проверить `permission.external_directory` в конфиге.

---

### Task 8: Фиксы дефектов (только после фиксации всех FAIL/WARN)

**Files:**
- Modify: `~/.config/opencode/plugin/fastmcp-engineering.ts`
- Modify: `~/.config/opencode/opencode.json` (если нужно)
- Modify: `/Users/laptop/dev/fastmcp-engineering/skills/**/SKILL.md` (если дубликаты/frontmatter)

**Interfaces:**
- Consumes: таблицы FAIL/WARN из Task 3, 5
- Produces: патчи + повторный прогон Task 2-4

- [ ] **Step 1: Пофиксить ENGINEERING_DIR — использовать `os.homedir()` или `process.env.HOME` с fallback на `resolve`**

```ts
import { homedir } from "os"
import { join, resolve } from "path"
const ENGINEERING_DIR = resolve(homedir(), "dev/fastmcp-engineering")
// Или: process.env.HOME ? join(process.env.HOME, "dev/fastmcp-engineering") : resolve(homedir(), "dev/fastmcp-engineering")
```

- [ ] **Step 2: Пофиксить дубликат name если найден**

Переименовать один из файлов, обновить frontmatter `name` чтобы совпадал с папкой.

- [ ] **Step 3: Добавить frontmatter в скиллы без него если найдены**

- [ ] **Step 4: Уточнить tool.execute.before — проверить реальную сигнатуру Plugin API, исправить мутацию если нужно**

Сверить с `~/.config/opencode/node_modules/@opencode-ai/plugin/dist/index.d.ts` — точная сигнатура хука.

- [ ] **Step 5: Повторный прогон Task 2-4 после фиксов**

```bash
python3 -m json.tool ~/.config/opencode/opencode.json > /dev/null && echo "JSON PASS"
node -e "import {existsSync} from 'fs'; import {homedir} from 'os'; import {join} from 'path'; console.log(existsSync(join(homedir(),'dev/fastmcp-engineering/skills')))"
opencode --help 2>&1 | head -n 20
```

---

### Task 9: Итоговый отчёт — PASS/FAIL/WARN матрица

**Files:**
- Create: `docs/superpowers/plans/2026-08-30-opencode-plugin-verification-report.md` (или секция в этом файле)

**Interfaces:**
- Consumes: все предыдущие задачи
- Produces: таблица со всеми проверками, evidence, вердиктом

- [ ] **Step 1: Собрать матрицу**

| # | Check | Expected | Actual | Verdict | Evidence |
|---|-------|----------|--------|---------|----------|
| 1 | JSON валиден | PASS | ... | PASS/FAIL | `python3 -m json.tool` output |
| 2 | $schema | `https://opencode.ai/config.json` | ... | ... | ... |
| ... | ... | ... | ... | ... | ... |

Каждая строка — одна проверка из Task 2-7. Никаких "в целом ок" — только по-штучно.

- [ ] **Step 2: Выдать вердикт**

`VERDICT: PASS` только если 0 FAIL. Если есть FAIL — `VERDICT: FAIL` с списком блокеров. WARN не блокируют но фиксируются.

- [ ] **Step 3: Сохранить отчёт и вывести в консоль**

---

## Self-Review

**1. Spec coverage:**
- [ ] Каждый пункт ТЗ пользователя ("проверять как удачи, так ошибки и предупреждение") покрыт задачей с PASS/FAIL/WARN матрицей (Task 9).
- [ ] Скепсис и профессионализм — Task 3 (баги пути), Task 4 (рантайм), Task 7 (безопасность) явно ищут дефекты.
- [ ] "Абсолютно всё фиксирует" — Task 1 (инвентаризация), Task 9 (матрица) фиксируют каждый чек.

**2. Placeholder scan:** Нет TBD/TODO — все шаги содержат конкретные команды и ожидаемые выводы.

**3. Type consistency:** `ENGINEERING_DIR: string`, `skillsDir: string`, `cfg: Config` — консистентны между Task 3 и Task 8.
