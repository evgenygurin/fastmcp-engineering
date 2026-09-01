from pathlib import Path
from fastmcp.resources import resource
from fastmcp.prompts import prompt
from server.indexing import build_index, search_index

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
    idx = build_index(SKILLS_ROOT)
    hits = search_index(idx, task, limit=5)
    lines = "\n".join(f"- {h.name}: {h.description} ({h.uri})" for h in hits)
    return f"Task: {task}\n\nRelevant skills:\n{lines}\n\nLoad the top skill with skill_context."

@prompt
def skill_context(skill: str) -> str:
    """Return execution context for a skill."""
    idx = build_index(SKILLS_ROOT)
    entry = idx.by_name.get(skill)
    if not entry:
        raise ValueError(f"Unknown skill: {skill}")
    text = entry.path.read_text(encoding="utf-8")
    return f"Execute using skill {skill}:\n\n{text}"

@prompt
def domain_guide(domain: str, task: str) -> str:
    """Domain-specific guide for a task."""
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