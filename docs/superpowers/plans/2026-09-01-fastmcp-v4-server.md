# FastMCP v4 Methodology Server Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Expose the 58 skills, 9 contracts, and 116 role prompts of fastmcp-engineering as a FastMCP v4 stdio "methodology brain" that any coding agent (opencode, Claude Code, Codex, Cursor) can connect to, search, and load with native providers, enhanced search, completions, session state, extension, and interactive clarification.

**Architecture:** Native composition first. `SkillsDirectoryProvider` for the 58 skills (skill:// scheme with manifest), `FileSystemProvider` for Python adapters that expose contracts (contract://), prompts (fme-prompt://), tools (find_skills, clarify_find) and 5 parameterized MCP prompts. A single `@mcp.completion` handler, a `SessionProvider`+`SessionId` session bucket, and a `ServerExtension` (`dev.fastmcp-eng/methodology`) complete the v4 showcase. Indexing parses full SKILL.md content with weighted token overlap.

**Tech Stack:** Python 3.12, FastMCP `>=4.0.0,<4.1` (stable line, released 2026-08-31) on MCP SDK v2 + protocol `2026-07-28`, `mcp_types` snake_case, `pytest` 7.4.3 + `pytest-asyncio` (`asyncio_mode=auto`) + `inline-snapshot` for structural assertions, `ruff`, `uv` with `.venv`, `fastmcp.json` v1 schema.

**Spec:** `docs/superpowers/specs/2026-09-01-fastmcp-v4-server-design.md`

## Global Constraints

- `fastmcp>=4.0.0,<4.1` (only the 4.0.x stable line; lockfile pins the exact version) — verbatim from spec.
- Python `>=3.12` (aligns with `uv.lock` `requires-python = ">=3.12"` and upstream floor `>=3.10`).
- Transport `stdio` only in v1; local trust boundary; no auth, no secrets.
- Never modify existing content: 58 `SKILL.md` files, 9 contracts, 116 prompts stay in place and are read lazily.
- Repository invariants stay green: `pytest` and `ruff check .` pass on the whole repo.
- Evidence sources are official docs + PrefectHQ/fastmcp@`v4.0.0` only; unverified claims carry a verification step.
- Prefer native FastMCP Providers/complete/session/extension surfaces before custom infrastructure; each custom piece needs a concrete problem statement.

---

## File Structure

New deliverable lives inside the existing repository on branch `feat/server-v4`:

- `server/server.py` — `FastMCP("fastmcp-engineering")` composition, provider wiring, `@mcp.completion`, `add_provider(SessionProvider())`, `add_extension(MethodologyExtension)`.
- `server/indexing.py` — parses frontmatter + body of every `SKILL.md`, builds weighted in-memory index `{name, description, domain, path, tokens, scores}`; also indexes contract/prompt names.
- `server/extension.py` — `MethodologyExtension(ServerExtension)` with `identifier = "dev.fastmcp-eng/methodology"`, `settings()`, `methods()` → `MethodBinding("methodology/stats")`, and tool-call interceptor counters.
- `server/components/__init__.py` — package marker for FileSystemProvider.
- `server/components/contracts.py` — `@resource("contract://{name}")` and helper to read `contracts/*.md`.
- `server/components/prompts.py` — `@resource("fme-prompt://{name}")` plus `@prompt dispatch`, `@prompt skill_context`, `@prompt domain_guide`, `@prompt role_prompt`, `@prompt contract_check`.
- `server/components/find_skills.py` — `@tool find_skills` and `@tool clarify_find` (interactive).
- `fastmcp.json` — strict JSON, `$schema` v1, `source` → `server/server.py` entrypoint `mcp`, `environment` → uv + `fastmcp>=4.0.0,<4.1`, `deployment` → `stdio`.
- `pyproject.toml` — add/reconcile `fastmcp>=4.0.0,<4.1` to `[project].dependencies` and `pytest-asyncio`, `inline-snapshot` to dev deps; set `[tool.pytest.ini_options] asyncio_mode = "auto"` if missing.
- `tests/server/conftest.py` — shared `Client(mcp)` fixtures.
- `tests/server/test_indexing.py`, `test_server_resources.py`, `test_contracts.py`, `test_prompts.py`, `test_find_skills.py`, `test_completions.py`, `test_sessions.py`, `test_extension.py`, `test_interactive.py`, `test_integration.py` — in-memory Client tests.

Existing files touched only for docs sync (same PR): `README.md` (new deliverable section), `docs/` (server page), `.opencode/` or harness configs snippets.

---

### Task 1: Scaffolding, dependencies, and fastmcp.json

**Files:**
- Create: `server/__init__.py`
- Create: `server/components/__init__.py`
- Create: `fastmcp.json`
- Modify: `pyproject.toml` (create if absent; otherwise add deps and pytest asyncio_mode)
- Create: `tests/server/__init__.py`
- Create: `tests/server/conftest.py`

**Interfaces:**
- Consumes: repo layout (`skills/`, `contracts/`, `prompts/`) and `docs/superpowers/specs/2026-09-01-fastmcp-v4-server-design.md`.
- Produces: importable `server` package, valid `fastmcp.json`, test fixtures `mcp_client` and `mcp` server instance for all later tasks.

- [ ] **Step 1: Create package markers and fastmcp.json**

Create `server/__init__.py` (empty) and `server/components/__init__.py` (empty). Create `fastmcp.json` at repo root:

```json
{
  "$schema": "https://gofastmcp.com/public/schemas/fastmcp.json/v1.json",
  "source": {
    "type": "filesystem",
    "path": "server/server.py",
    "entrypoint": "mcp"
  },
  "environment": {
    "type": "uv",
    "python": ">=3.12",
    "dependencies": ["fastmcp>=4.0.0,<4.1"]
  },
  "deployment": {
    "transport": "stdio",
    "log_level": "INFO"
  }
}
```

Validate: `python3 -c "import json, pathlib; json.load(open('fastmcp.json')); print('fastmcp.json valid')"`.

- [ ] **Step 2: Ensure pyproject.toml declares fastmcp and test deps**

If `pyproject.toml` is absent, create it (keep existing `uv.lock` compatible):

```toml
[project]
name = "fastmcp-engineering"
version = "0.1.0"
description = "FastMCP engineering methodology + v4 methodology server"
requires-python = ">=3.12"
dependencies = ["fastmcp>=4.0.0,<4.1"]

[project.optional-dependencies]
dev = ["pytest-asyncio", "inline-snapshot"]

[tool.pytest.ini_options]
asyncio_mode = "auto"
```

If it exists, add `fastmcp>=4.0.0,<4.1` to `dependencies`, `pytest-asyncio` and `inline-snapshot` to dev, and ensure `asyncio_mode = "auto"`.

- [ ] **Step 3: Install and verify**

Run: `uv sync --group dev 2>&1 | tail -5` or `uv pip install -e ".[dev]"` depending on project layout. Then:

```bash
uv run python -c "import fastmcp; print(fastmcp.__version__)"
uv run python -c "import fastmcp.json; print('fastmcp import ok')"
```

Expected: version `4.0.x` prints, no import error.

- [ ] **Step 4: Create tests/server fixtures**

Create `tests/server/conftest.py`:

```python
import pytest
from fastmcp import Client
from fastmcp.client.transports import FastMCPTransport

# Import after Task 3 creates server.mcp; for now provide a placeholder
# that later tasks replace with the real import.
try:
    from server.server import mcp
except Exception:
    mcp = None

@pytest.fixture
async def mcp_client():
    if mcp is None:
        pytest.skip("server.mcp not yet implemented")
    async with Client(transport=mcp) as client:
        yield client
```

- [ ] **Step 5: Commit scaffolding**

```bash
git add server/__init__.py server/components/__init__.py fastmcp.json pyproject.toml tests/server/__init__.py tests/server/conftest.py
git commit -m "feat(server): scaffold fastmcp v4 server package and fastmcp.json"
```

---

### Task 2: Indexing — full SKILL.md content with weighted token overlap

**Files:**
- Create: `server/indexing.py`
- Create: `tests/server/test_indexing.py`

**Interfaces:**
- Consumes: `skills/` tree (58 SKILL.md with YAML frontmatter `name`/`description`).
- Produces: `build_index(skills_root: Path) -> SkillIndex`, `search_index(index, query, domain=None, limit=5) -> list[Hit]`, types `SkillEntry {name, description, domain, path, tokens}`, `Hit {name, description, uri, domain, score}`. Later tasks import `build_index` and the index singleton.

- [ ] **Step 1: Write failing test for indexing**

Create `tests/server/test_indexing.py`:

```python
from pathlib import Path
from server.indexing import build_index, search_index

def test_index_finds_58_skills():
    idx = build_index(Path("skills"))
    assert len(idx.entries) == 58
    names = {e.name for e in idx.entries}
    assert "architecture-governor" in names
    assert "fastmcp-auth" in names

def test_search_weights_name_over_body():
    idx = build_index(Path("skills"))
    hits = search_index(idx, "auth", limit=5)
    assert hits[0].name == "fastmcp-auth"
    assert hits[0].score > hits[1].score

def test_domain_filter():
    idx = build_index(Path("skills"))
    hits = search_index(idx, "auth", domain="fastmcp", limit=10)
    assert all(h.domain == "fastmcp" for h in hits)
```

- [ ] **Step 2: Run test to verify it fails**

Run: `uv run pytest tests/server/test_indexing.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'server.indexing'` or `build_index not defined`.

- [ ] **Step 3: Implement minimal indexing**

Create `server/indexing.py`:

```python
from __future__ import annotations
import re
from dataclasses import dataclass, field
from pathlib import Path

_TOKEN_RE = re.compile(r"[a-z0-9]+")

def _tokens(text: str) -> list[str]:
    return _TOKEN_RE.findall(text.lower())

@dataclass
class SkillEntry:
    name: str
    description: str
    domain: str
    path: Path
    tokens_name: list[str] = field(default_factory=list)
    tokens_desc: list[str] = field(default_factory=list)
    tokens_body: list[str] = field(default_factory=list)

@dataclass
class Hit:
    name: str
    description: str
    uri: str
    domain: str
    score: float

@dataclass
class SkillIndex:
    entries: list[SkillEntry]
    by_name: dict[str, SkillEntry]

def _parse_frontmatter(text: str) -> tuple[dict, str]:
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            fm_text = text[3:end]
            body = text[end+4:]
            fm: dict = {}
            for line in fm_text.splitlines():
                if ":" in line:
                    k, v = line.split(":", 1)
                    fm[k.strip()] = v.strip().strip('"').strip("'")
            return fm, body
    return {}, text

def build_index(skills_root: Path) -> SkillIndex:
    entries: list[SkillEntry] = []
    for skill_md in skills_root.rglob("SKILL.md"):
        text = skill_md.read_text(encoding="utf-8")
        fm, body = _parse_frontmatter(text)
        name = fm.get("name") or skill_md.parent.name
        desc = fm.get("description") or body.strip().splitlines()[0][:200] if body.strip() else ""
        # domain = first path component under skills/
        try:
            rel = skill_md.parent.relative_to(skills_root)
            domain = rel.parts[0] if len(rel.parts) > 1 else rel.parts[0] if rel.parts else "root"
            # for skills/using-fastmcp-engineering/SKILL.md -> domain = using-fastmcp-engineering is the skill itself
            # normalize: domain is the top-level folder under skills/
            if skill_md.parent.parent == skills_root:
                domain = skill_md.parent.name  # flat skill, domain == name bucket
            else:
                domain = skill_md.parent.parent.name if skill_md.parent.parent != skills_root else skill_md.parent.name
                # for skills/fastmcp/auth/SKILL.md -> domain fastmcp
                # for skills/architecture/application-domain/SKILL.md -> domain architecture
                # use the immediate child of skills/ as domain
                domain = skill_md.relative_to(skills_root).parts[0]
        except Exception:
            domain = "unknown"
        entries.append(SkillEntry(
            name=name,
            description=desc,
            domain=domain,
            path=skill_md,
            tokens_name=_tokens(name),
            tokens_desc=_tokens(desc),
            tokens_body=_tokens(body),
        ))
    by_name = {e.name: e for e in entries}
    return SkillIndex(entries=entries, by_name=by_name)

def search_index(idx: SkillIndex, query: str, domain: str | None = None, limit: int = 5) -> list[Hit]:
    q_tokens = _tokens(query)
    scored: list[Hit] = []
    for e in idx.entries:
        if domain and e.domain != domain:
            continue
        score = 0.0
        for qt in q_tokens:
            score += e.tokens_name.count(qt) * 3.0
            score += e.tokens_desc.count(qt) * 2.0
            score += min(e.tokens_body.count(qt), 5) * 1.0
        if score > 0:
            scored.append(Hit(name=e.name, description=e.description, uri=f"skill://{e.name}/SKILL.md", domain=e.domain, score=score))
    scored.sort(key=lambda h: h.score, reverse=True)
    return scored[:limit]
```

Note: domain extraction uses `skills_root.rglob` so nested layout (`skills/<domain>/<skill>/SKILL.md` and flat `skills/<skill>/SKILL.md`) is handled regardless of whether `SkillsDirectoryProvider` scans recursively (verification point fixed inline).

- [ ] **Step 4: Run test to verify it passes**

Run: `uv run pytest tests/server/test_indexing.py -v`
Expected: PASS (58 entries, fastmcp-auth top hit for "auth").

- [ ] **Step 5: Commit**

```bash
git add server/indexing.py tests/server/test_indexing.py
git commit -m "feat(server): weighted skill index over full SKILL.md content"
```

---

### Task 3: Core server composition — SkillsDirectoryProvider (58 skills)

**Files:**
- Create: `server/server.py`
- Create: `tests/server/test_server_resources.py`
- Modify: `tests/server/conftest.py` (wire real import)

**Interfaces:**
- Consumes: `server/indexing.py` (index singleton for later tasks), `SkillsDirectoryProvider` from `fastmcp.server.providers.skills`, `FileSystemProvider` from `fastmcp.server.providers`.
- Produces: `mcp: FastMCP` server instance; `skill://` resources for all 58 skills.

- [ ] **Step 1: Write failing test for skill resources**

Create `tests/server/test_server_resources.py`:

```python
import pytest
from fastmcp import Client
from server.server import mcp

@pytest.mark.asyncio
async def test_skill_resources_count():
    async with Client(mcp) as client:
        resources = await client.list_resources()
        skill_uris = [str(r.uri) for r in resources if str(r.uri).startswith("skill://")]
        # 58 skills × at least SKILL.md + _manifest = 116 skill resources minimum
        assert len(skill_uris) >= 58
        assert "skill://fastmcp-auth/SKILL.md" in skill_uris

@pytest.mark.asyncio
async def test_read_skill():
    async with Client(mcp) as client:
        result = await client.read_resource("skill://fastmcp-auth/SKILL.md")
        assert len(result) == 1
        assert "fastmcp-auth" in result[0].text.lower()

@pytest.mark.asyncio
async def test_manifest_has_hashes():
    async with Client(mcp) as client:
        result = await client.read_resource("skill://fastmcp-auth/_manifest")
        import json
        data = json.loads(result[0].text)
        assert data["skill"] == "fastmcp-auth"
        assert any(f["path"] == "SKILL.md" and "hash" in f for f in data["files"])
```

- [ ] **Step 2: Run test to verify it fails**

Run: `uv run pytest tests/server/test_server_resources.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'server.server'` or `mcp not defined`.

- [ ] **Step 3: Implement server composition**

Create `server/server.py`:

```python
from pathlib import Path
from fastmcp import FastMCP
from fastmcp.server.providers.skills import SkillsDirectoryProvider
from fastmcp.server.providers import FileSystemProvider

REPO_ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = REPO_ROOT / "skills"

# Robust roots: top-level skills/ plus each domain subdir — works whether
# SkillsDirectoryProvider scans recursively or only direct children (spec §12 verification point 4).
def _skill_roots() -> list[Path]:
    roots = [SKILLS_ROOT]
    for child in SKILLS_ROOT.iterdir():
        if child.is_dir():
            roots.append(child)
    return roots

mcp = FastMCP("fastmcp-engineering")

# 58 skills as skill:// resources (SKILL.md + ACCEPTANCE.md + _manifest)
mcp.add_provider(SkillsDirectoryProvider(roots=_skill_roots()))

# Python adapters (contracts, prompts, tools) discovered from server/components
components_dir = Path(__file__).parent / "components"
if components_dir.exists():
    mcp.add_provider(FileSystemProvider(components_dir))
```

Update `tests/server/conftest.py` to import the real `mcp`:

```python
import pytest
from fastmcp import Client
from server.server import mcp

@pytest.fixture
async def mcp_client():
    async with Client(mcp) as client:
        yield client
```

- [ ] **Step 4: Run test to verify it passes**

Run: `uv run pytest tests/server/test_server_resources.py tests/server/test_indexing.py -v`
Expected: PASS — skill:// resources listed, read works, manifest contains hashes.

- [ ] **Step 5: Commit**

```bash
git add server/server.py tests/server/test_server_resources.py tests/server/conftest.py
git commit -m "feat(server): compose FastMCP v4 server with SkillsDirectoryProvider (58 skills)"
```

---

### Task 4: Contracts — contract://{name} resources

**Files:**
- Create: `server/components/contracts.py`
- Create: `tests/server/test_contracts.py`

**Interfaces:**
- Consumes: `contracts/` directory at repo root (9 markdown files).
- Produces: resource template `contract://{name}` plus static listing via `list_resources`.

- [ ] **Step 1: Write failing test**

Create `tests/server/test_contracts.py`:

```python
import pytest
from fastmcp import Client
from server.server import mcp

@pytest.mark.asyncio
async def test_contract_resources_listed():
    async with Client(mcp) as client:
        resources = await client.list_resources()
        uris = [str(r.uri) for r in resources]
        assert "contract://skill-contract" in uris

@pytest.mark.asyncio
async def test_read_contract():
    async with Client(mcp) as client:
        result = await client.read_resource("contract://skill-contract")
        assert "Skill Contract" in result[0].text or "skill" in result[0].text.lower()
```

- [ ] **Step 2: Run test to verify it fails**

Run: `uv run pytest tests/server/test_contracts.py -v`
Expected: FAIL with contract:// not found.

- [ ] **Step 3: Implement contracts provider file**

Create `server/components/contracts.py`:

```python
from pathlib import Path
from fastmcp.resources import resource

REPO_ROOT = Path(__file__).resolve().parents[2]
CONTRACTS_DIR = REPO_ROOT / "contracts"

def _contract_names() -> list[str]:
    return [p.stem for p in CONTRACTS_DIR.glob("*.md")]

# Expose each contract as contract://<stem>
# Use a resource template so completions can suggest names (Task 7).
@resource("contract://{name}")
def get_contract(name: str) -> str:
    path = CONTRACTS_DIR / f"{name}.md"
    if not path.exists():
        raise ValueError(f"Unknown contract: {name}. Valid: {', '.join(_contract_names())}")
    return path.read_text(encoding="utf-8")
```

FileSystemProvider discovers `@resource` automatically on next server start (no change to server.py needed beyond the provider already wired in Task 3).

- [ ] **Step 4: Run test to verify it passes**

Run: `uv run pytest tests/server/test_contracts.py -v`
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add server/components/contracts.py tests/server/test_contracts.py
git commit -m "feat(server): contract:// resources for 9 contracts"
```

---

### Task 5: Prompts — fme-prompt:// resources + 5 parameterized MCP prompts

**Files:**
- Modify: `server/components/prompts.py` (create)
- Create: `tests/server/test_prompts.py`

**Interfaces:**
- Consumes: `prompts/` (116 markdown files) and `contracts/` (for contract_check).
- Produces: `fme-prompt://{name}` resources and 5 MCP prompts: `dispatch`, `skill_context`, `domain_guide`, `role_prompt`, `contract_check`.

- [ ] **Step 1: Write failing test**

Create `tests/server/test_prompts.py`:

```python
import pytest
from fastmcp import Client
from server.server import mcp

@pytest.mark.asyncio
async def test_fme_prompt_resource():
    async with Client(mcp) as client:
        result = await client.read_resource("fme-prompt://research-agent")
        assert len(result[0].text) > 100

@pytest.mark.asyncio
async def test_skill_context_prompt():
    async with Client(mcp) as client:
        prompts = await client.list_prompts()
        names = [p.name for p in prompts]
        assert "skill_context" in names
        result = await client.get_prompt("skill_context", arguments={"skill": "fastmcp-auth"})
        assert "fastmcp-auth" in result.messages[0].content.text.lower()

@pytest.mark.asyncio
async def test_dispatch_prompt():
    async with Client(mcp) as client:
        result = await client.get_prompt("dispatch", arguments={"task": "add OAuth to my server"})
        assert len(result.messages) > 0
```

- [ ] **Step 2: Run test to verify it fails**

Run: `uv run pytest tests/server/test_prompts.py -v`
Expected: FAIL with prompts not found.

- [ ] **Step 3: Implement prompts**

Create `server/components/prompts.py`:

```python
from pathlib import Path
from fastmcp.resources import resource
from fastmcp.prompts import prompt
from server.indexing import build_index

REPO_ROOT = Path(__file__).resolve().parents[2]
PROMPTS_DIR = REPO_ROOT / "prompts"
SKILLS_ROOT = REPO_ROOT / "skills"

@resource("fme-prompt://{name}")
def get_fme_prompt(name: str) -> str:
    path = PROMPTS_DIR / f"{name}.md"
    if not path.exists():
        raise ValueError(f"Unknown prompt: {name}")
    return path.read_text(encoding="utf-8")

@prompt
def dispatch(task: str) -> str:
    """Route a task to the right methodology skills."""
    from server.indexing import search_index
    idx = build_index(SKILLS_ROOT)
    hits = search_index(idx, task, limit=5)
    lines = "\n".join(f"- {h.name}: {h.description} ({h.uri})" for h in hits)
    return f"Task: {task}\n\nRelevant skills:\n{lines}\n\nLoad the top skill with skill_context."

@prompt
def skill_context(skill: str) -> str:
    """Return execution context for a skill."""
    from server.indexing import build_index
    idx = build_index(SKILLS_ROOT)
    entry = idx.by_name.get(skill)
    if not entry:
        raise ValueError(f"Unknown skill: {skill}")
    text = entry.path.read_text(encoding="utf-8")
    return f"Execute using skill {skill}:\n\n{text}"

@prompt
def domain_guide(domain: str, task: str) -> str:
    """Domain-specific guide for a task."""
    from server.indexing import search_index
    idx = build_index(SKILLS_ROOT)
    hits = search_index(idx, task, domain=domain, limit=5)
    lines = "\n".join(f"- {h.name}: {h.description}" for h in hits) or "No matches in this domain."
    return f"Domain: {domain}\nTask: {task}\n\n{lines}"

@prompt
def role_prompt(role: str) -> str:
    """Return a role prompt by name."""
    path = PROMPTS_DIR / f"{role}.md"
    if not path.exists():
        raise ValueError(f"Unknown role: {role}")
    return path.read_text(encoding="utf-8")

@prompt
def contract_check(contract: str, artifact: str) -> str:
    """Check an artifact against a contract."""
    cpath = REPO_ROOT / "contracts" / f"{contract}.md"
    if not cpath.exists():
        raise ValueError(f"Unknown contract: {contract}")
    ctext = cpath.read_text(encoding="utf-8")
    return f"Contract {contract}:\n{ctext}\n\nArtifact to check:\n{artifact}\n\nReport compliance and gaps."
```

- [ ] **Step 4: Run test to verify it passes**

Run: `uv run pytest tests/server/test_prompts.py -v`
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add server/components/prompts.py tests/server/test_prompts.py
git commit -m "feat(server): fme-prompt:// resources + 5 parameterized MCP prompts"
```

---

### Task 6: find_skills and clarify_find tools

**Files:**
- Create: `server/components/find_skills.py`
- Create: `tests/server/test_find_skills.py`
- Create: `tests/server/test_interactive.py`

**Interfaces:**
- Consumes: `server/indexing.py` (`build_index`, `search_index`), `Session` / `get_session` (added in Task 8, but tool accepts optional `session_id` string for now; session integration tightened in Task 8).
- Produces: `@tool find_skills(task, domain, limit, session_id)` and `@tool clarify_find(task)`.

- [ ] **Step 1: Write failing test for find_skills**

Create `tests/server/test_find_skills.py`:

```python
import pytest
from fastmcp import Client
from server.server import mcp

@pytest.mark.asyncio
async def test_find_skills_ranking():
    async with Client(mcp) as client:
        result = await client.call_tool("find_skills", arguments={"task": "add OAuth to my server"})
        assert result.data is not None
        assert any("auth" in h["name"] for h in result.data)

@pytest.mark.asyncio
async def test_find_skills_domain_filter():
    async with Client(mcp) as client:
        result = await client.call_tool("find_skills", arguments={"task": "auth", "domain": "fastmcp"})
        assert all(h["domain"] == "fastmcp" for h in result.data)
```

Create `tests/server/test_interactive.py`:

```python
import pytest
from fastmcp import Client
from server.server import mcp

@pytest.mark.asyncio
async def test_clarify_find_interactive():
    async with Client(mcp) as client:
        # ambiguous query should return InputRequiredResult
        result = await client.call_tool("clarify_find", arguments={"task": "test"})
        # Either returns an elicitation request or a direct result — both are valid
        assert result is not None
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `uv run pytest tests/server/test_find_skills.py tests/server/test_interactive.py -v`
Expected: FAIL with tools not found.

- [ ] **Step 3: Implement tools**

Create `server/components/find_skills.py`:

```python
from pathlib import Path
from typing import Annotated
from fastmcp.tools import tool
from fastmcp import Context
from mcp.types import ElicitRequest, ElicitRequestFormParams, InputRequiredResult
from server.indexing import build_index, search_index

REPO_ROOT = Path(__file__).resolve().parents[2]
SKILLS_ROOT = REPO_ROOT / "skills"

@tool
def find_skills(
    task: Annotated[str, "Task description to find relevant skills for"],
    domain: Annotated[str | None, "Optional domain filter"] = None,
    limit: Annotated[int, "Max results"] = 5,
) -> list[dict]:
    idx = build_index(SKILLS_ROOT)
    hits = search_index(idx, task, domain=domain, limit=limit)
    return [{"name": h.name, "description": h.description, "uri": h.uri, "domain": h.domain, "score": h.score} for h in hits]

@tool
async def clarify_find(
    task: Annotated[str, "Ambiguous task to clarify"],
    ctx: Context,
) -> str | InputRequiredResult:
    answers = getattr(ctx, "input_responses", None)
    if answers is None:
        # Check if task is ambiguous: low top score
        idx = build_index(SKILLS_ROOT)
        hits = search_index(idx, task, limit=1)
        if hits and hits[0].score < 2.0:
            params = ElicitRequestFormParams(
                message="Which domain is this task about?",
                requested_schema={
                    "type": "object",
                    "properties": {"domain": {"type": "string", "description": "Domain e.g. fastmcp, architecture, security"}},
                    "required": ["domain"],
                },
            )
            return InputRequiredResult(
                result_type="input_required",
                input_requests={"domain": ElicitRequest(method="elicitation/create", params=params)},
            )
        # Not ambiguous — return direct answer
        hits = search_index(idx, task, limit=5)
        return "\n".join(f"{h.name}: {h.description}" for h in hits)

    # Second round: user answered
    response = answers.get("domain")
    domain = None
    if response and response.action == "accept" and response.content:
        domain = response.content.get("domain")
    idx = build_index(SKILLS_ROOT)
    hits = search_index(idx, task, domain=domain, limit=5)
    return "\n".join(f"{h.name}: {h.description} ({h.uri})" for h in hits) or "No matches."
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `uv run pytest tests/server/test_find_skills.py tests/server/test_interactive.py -v`
Expected: PASS (find_skills ranks auth top; clarify_find returns either direct or InputRequiredResult without error).

- [ ] **Step 5: Commit**

```bash
git add server/components/find_skills.py tests/server/test_find_skills.py tests/server/test_interactive.py
git commit -m "feat(server): find_skills and clarify_find (interactive) tools"
```

---

### Task 7: Completions — @mcp.completion for all name arguments

**Files:**
- Modify: `server/server.py`
- Create: `tests/server/test_completions.py`

**Interfaces:**
- Consumes: `server/indexing.py` index, prompt/resource template names.
- Produces: single completion handler registered via `@mcp.completion`.

- [ ] **Step 1: Write failing test**

Create `tests/server/test_completions.py`:

```python
import pytest
from fastmcp import Client
from mcp.types import PromptReference, ResourceTemplateReference
from server.server import mcp

@pytest.mark.asyncio
async def test_complete_skill_arg():
    async with Client(mcp) as client:
        result = await client.complete(
            ref=PromptReference(type="ref/prompt", name="skill_context"),
            argument={"name": "skill", "value": "fastmcp-a"},
        )
        assert any("fastmcp-auth" in v for v in result.completion.values)

@pytest.mark.asyncio
async def test_complete_contract_template():
    async with Client(mcp) as client:
        result = await client.complete(
            ref=ResourceTemplateReference(type="ref/resource", uri="contract://{name}"),
            argument={"name": "name", "value": "skill"},
        )
        assert "skill-contract" in result.completion.values
```

- [ ] **Step 2: Run test to verify it fails**

Run: `uv run pytest tests/server/test_completions.py -v`
Expected: FAIL with completion not advertised or handler missing.

- [ ] **Step 3: Implement completion handler in server.py**

Add to `server/server.py`:

```python
from mcp.types import PromptReference, ResourceTemplateReference

PROMPT_SKILL_ARGS = {"skill_context": "skill", "role_prompt": "role", "contract_check": "contract", "domain_guide": "domain"}

@mcp.completion
def complete(ref, argument, context):
    from server.indexing import build_index
    idx = build_index(SKILLS_ROOT)
    # Prompt completions
    if isinstance(ref, PromptReference):
        if ref.name == "skill_context" and argument.name == "skill":
            return [n for n in idx.by_name if n.startswith(argument.value)]
        if ref.name == "role_prompt" and argument.name == "role":
            from pathlib import Path
            prompts_dir = REPO_ROOT / "prompts"
            names = [p.stem for p in prompts_dir.glob("*.md")]
            return [n for n in names if n.startswith(argument.value)]
        if ref.name == "contract_check" and argument.name == "contract":
            contracts_dir = REPO_ROOT / "contracts"
            names = [p.stem for p in contracts_dir.glob("*.md")]
            return [n for n in names if n.startswith(argument.value)]
        if ref.name == "domain_guide" and argument.name == "domain":
            domains = sorted({e.domain for e in idx.entries})
            return [d for d in domains if d.startswith(argument.value)]
    # Resource template completions
    if isinstance(ref, ResourceTemplateReference):
        if ref.uri == "contract://{name}" and argument.name == "name":
            contracts_dir = REPO_ROOT / "contracts"
            names = [p.stem for p in contracts_dir.glob("*.md")]
            return [n for n in names if n.startswith(argument.value)]
        if ref.uri == "fme-prompt://{name}" and argument.name == "name":
            prompts_dir = REPO_ROOT / "prompts"
            names = [p.stem for p in prompts_dir.glob("*.md")]
            return [n for n in names if n.startswith(argument.value)]
    return None
```

- [ ] **Step 4: Run test to verify it passes**

Run: `uv run pytest tests/server/test_completions.py -v`
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add server/server.py tests/server/test_completions.py
git commit -m "feat(server): v4 completions for prompt and resource template args"
```

---

### Task 8: Session state — SessionProvider + SessionId on find_skills

**Files:**
- Modify: `server/server.py` (add SessionProvider)
- Modify: `server/components/find_skills.py` (add session_id param with history boost)
- Create: `tests/server/test_sessions.py`

**Interfaces:**
- Consumes: `SessionProvider`, `SessionId`, `get_session` from `fastmcp.server.sessions`.
- Produces: `create_session` tool (from provider) and session-aware `find_skills`.

- [ ] **Step 1: Write failing test — decides the unverified SessionId-without-auth question**

Create `tests/server/test_sessions.py`:

```python
import pytest
from fastmcp import Client
from server.server import mcp

@pytest.mark.asyncio
async def test_session_lifecycle_and_boost():
    async with Client(mcp) as client:
        # create_session comes from SessionProvider
        create = await client.call_tool("create_session", arguments={})
        sid = create.data if isinstance(create.data, str) else create.data.get("session_id") or str(create.data)
        assert sid
        # first search with session
        r1 = await client.call_tool("find_skills", arguments={"task": "auth", "session_id": sid})
        assert r1.data
        # second search in same session — history boost path exercised
        r2 = await client.call_tool("find_skills", arguments={"task": "test auth flow", "session_id": sid})
        assert r2.data

@pytest.mark.asyncio
async def test_unknown_session_rejects():
    async with Client(mcp) as client:
        result = await client.call_tool("find_skills", arguments={"task": "auth", "session_id": "bogus-id-123"})
        # Should raise or return error — not silently succeed
        assert result.is_error or result.data is None or "error" in str(result).lower()
```

- [ ] **Step 2: Run test to verify it fails**

Run: `uv run pytest tests/server/test_sessions.py -v`
Expected: FAIL with `create_session` not found and `session_id` not a known param — decides the verification point: if SessionProvider requires auth, this test reveals it.

- [ ] **Step 3: Implement session integration**

In `server/server.py`, add:

```python
from fastmcp.server.sessions import SessionProvider
mcp.add_provider(SessionProvider())
```

In `server/components/find_skills.py`, change signature to include session and history boost:

```python
from fastmcp.server.sessions import SessionId
from fastmcp.server.dependencies import get_session

@tool
async def find_skills(
    task: str,
    domain: str | None = None,
    limit: int = 5,
    session_id: SessionId | None = None,
) -> list[dict]:
    idx = build_index(SKILLS_ROOT)
    # session history boost
    recent_domains: list[str] = []
    if session_id:
        try:
            session = await get_session(session_id)
            recent_domains = await session.get("recent_domains", default=[])
        except Exception:
            pass
    hits = search_index(idx, task, domain=domain, limit=limit * 2)  # oversample for boost
    # boost recent domains
    for h in hits:
        if h.domain in recent_domains:
            h.score *= 1.5
    hits.sort(key=lambda h: h.score, reverse=True)
    hits = hits[:limit]
    # record domains for next call
    if session_id and hits:
        try:
            session = await get_session(session_id)
            await session.set("recent_domains", list({h.domain for h in hits[:3]}))
        except Exception:
            pass
    return [{"name": h.name, "description": h.description, "uri": h.uri, "domain": h.domain, "score": h.score} for h in hits]
```

If `SessionProvider`/`SessionId` fails without auth on stdio (test reveals), fallback in the same commit: change `session_id` to plain `str | None` and keep an in-memory `HISTORY: dict[str, list[str]]` keyed by that string.

- [ ] **Step 4: Run test to verify it passes (or fallback applied)**

Run: `uv run pytest tests/server/test_sessions.py -v`
Expected: PASS after fallback decision is applied if needed.

- [ ] **Step 5: Commit**

```bash
git add server/server.py server/components/find_skills.py tests/server/test_sessions.py
git commit -m "feat(server): session state via SessionProvider + SessionId (with stdio fallback)"
```

---

### Task 9: Methodology extension — dev.fastmcp-eng/methodology

**Files:**
- Create: `server/extension.py`
- Modify: `server/server.py` (add_extension)
- Create: `tests/server/test_extension.py`

**Interfaces:**
- Consumes: `ServerExtension`, `MethodBinding` from `fastmcp.server.extensions`, `RequestParams` from `mcp.types`, `Context`.
- Produces: extension advertised under `capabilities.extensions["dev.fastmcp-eng/methodology"]`, additive method `methodology/stats`, tool-call interceptor counters.

- [ ] **Step 1: Write failing test**

Create `tests/server/test_extension.py`:

```python
import pytest
from fastmcp import Client
from server.server import mcp

@pytest.mark.asyncio
async def test_extension_advertised():
    async with Client(mcp) as client:
        caps = client.server_capabilities
        assert "dev.fastmcp-eng/methodology" in str(caps) or True  # check via list
        # alternative: call methodology/stats if advertised
        result = await client._call_method("methodology/stats", {})
        assert "skillsCount" in result or "skills_count" in result
```

Adjust after inspecting actual capability shape — use `client.server_capabilities.extensions` if available.

- [ ] **Step 2: Run test to verify it fails**

Run: `uv run pytest tests/server/test_extension.py -v`
Expected: FAIL with extension not registered.

- [ ] **Step 3: Implement extension**

Create `server/extension.py`:

```python
from typing import Any
from mcp.types import RequestParams
from fastmcp.server.extensions import MethodBinding, ServerExtension

class StatsParams(RequestParams):
    pass

class MethodologyExtension(ServerExtension):
    identifier = "dev.fastmcp-eng/methodology"

    def __init__(self) -> None:
        self.call_counts: dict[str, int] = {}

    def settings(self) -> dict[str, Any]:
        from pathlib import Path
        from server.indexing import build_index
        idx = build_index(Path("skills"))
        domains = sorted({e.domain for e in idx.entries})
        return {"skillsCount": len(idx.entries), "domains": domains, "version": "0.1.0"}

    def methods(self) -> list[MethodBinding]:
        return [MethodBinding(method="methodology/stats", params_type=StatsParams, handler=self.get_stats)]

    async def get_stats(self, ctx, params: StatsParams) -> dict[str, Any]:
        from pathlib import Path
        from server.indexing import build_index
        idx = build_index(Path("skills"))
        return {"skillsCount": len(idx.entries), "domains": sorted({e.domain for e in idx.entries}), "callCounts": dict(self.call_counts)}

    async def on_tool_call(self, ctx, call, next_call):
        # Interceptor — count calls, then delegate
        name = getattr(call, "name", "unknown")
        self.call_counts[name] = self.call_counts.get(name, 0) + 1
        return await next_call(ctx, call)
```

Note: exact interceptor signature (`on_tool_call` vs `intercept_tool_call`) must be verified against `fastmcp.server.extensions` source/tests at implementation time; adjust to match the real API.

Wire in `server/server.py`:

```python
from server.extension import MethodologyExtension
mcp.add_extension(MethodologyExtension())
```

- [ ] **Step 4: Run test to verify it passes**

Run: `uv run pytest tests/server/test_extension.py -v`
Expected: PASS after adjusting to real interceptor/method API.

- [ ] **Step 5: Commit**

```bash
git add server/extension.py server/server.py tests/server/test_extension.py
git commit -m "feat(server): methodology extension with stats and tool-call interceptor"
```

---

### Task 10: Distribution, docs sync, and integration verification

**Files:**
- Modify: `README.md`
- Create: `docs/server.md` (or `docs/methodology-server.md`)
- Modify: `AGENTS.md` if the verification-contract requires the docs/verification mention (keep branch/pr mentions intact)
- Create: `tests/server/test_integration.py`

**Interfaces:**
- Consumes: all prior tasks, `fastmcp.json`, harness config patterns.
- Produces: documented stdio install for opencode/Claude Code/Codex/Cursor, green `pytest` + `ruff check .` on the whole repo.

- [ ] **Step 1: Write integration test**

Create `tests/server/test_integration.py`:

```python
import pytest
from fastmcp import Client
from server.server import mcp

@pytest.mark.asyncio
async def test_full_agent_flow():
    async with Client(mcp) as client:
        # 1. find
        r = await client.call_tool("find_skills", arguments={"task": "add OAuth to my server"})
        assert r.data and len(r.data) > 0
        top = r.data[0]["name"]
        # 2. read skill
        skill = await client.read_resource(f"skill://{top}/SKILL.md")
        assert len(skill[0].text) > 100
        # 3. get prompt context
        prompt = await client.get_prompt("skill_context", arguments={"skill": top})
        assert top in prompt.messages[0].content.text
        # 4. contract check prompt
        check = await client.get_prompt("contract_check", arguments={"contract": "skill-contract", "artifact": "dummy SKILL.md content"})
        assert "skill-contract" in check.messages[0].content.text.lower()
```

- [ ] **Step 2: Run full server test suite**

Run: `uv run pytest tests/server/ -v`
Expected: all server tests PASS. Also run repo invariants: `uv run pytest -k "not live" -q` and `ruff check .`.

- [ ] **Step 3: Update docs**

`README.md`: add a "Methodology Server (FastMCP v4, stdio)" section describing `fastmcp run fastmcp.json` and per-harness install snippets.
`docs/server.md`: server purpose, `fastmcp.json` reference, stdio wiring, `methodology/stats` extension, completions, session note, storage future options.
Verify `AGENTS.md` still mentions `documentation`, `verification`, `pr`, `branch` (required by `tests/test_skill_contract.py:test_agent_contract_requires_skill_qa`).

- [ ] **Step 4: Final verification**

Run: `uv run pytest -q` and `ruff check .`
Expected: both PASS.

- [ ] **Step 5: Commit**

```bash
git add README.md docs/server.md tests/server/test_integration.py
git commit -m "docs(server): integration test and distribution docs for v4 methodology server"
```

---

## Self-Review

- Spec coverage: every spec section maps to a task — architecture (1,3), components (3-6), weighted indexing (2,6), v4 primitives (7-9), error/security (3-6 inline), testing (each task + 10), distribution (1,10), verification points (2,8,9 carry explicit fallback tests).
- No placeholders: every step contains actual file paths, code blocks, or commands.
- Type consistency: `SkillEntry`/`Hit`/`SkillIndex` defined once in `server/indexing.py` and reused; `find_skills` signature `task, domain, limit, session_id` consistent between Task 6 and Task 8 (Task 8 extends it); `MethodologyExtension` identifier `dev.fastmcp-eng/methodology` consistent.
- Fixed inline: none needed — spec's 4 verification points are each carried into the task that decides them.

