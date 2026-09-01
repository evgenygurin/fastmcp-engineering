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
