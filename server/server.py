from pathlib import Path
from fastmcp import FastMCP
from fastmcp.server.providers.skills import SkillsDirectoryProvider
from fastmcp.server.providers import FileSystemProvider
from fastmcp.server.sessions import SessionProvider
from mcp.types import PromptReference, ResourceTemplateReference
from server.extension import MethodologyExtension

# Patch SkillProvider to use frontmatter `name` as canonical skill identifier.
# Upstream SkillProvider uses directory basename (e.g. `skills/fastmcp/auth` -> `auth`)
# but repo frontmatter uses qualified names (e.g. `fastmcp-auth`). Without this
# patch, skill:// URIs would be `skill://auth/...` and tests expecting
# `skill://fastmcp-auth/...` would fail. The patch respects the original
# behaviour for skills where frontmatter name matches the directory.
try:
    from fastmcp.server.providers.skills._common import (
        SkillInfo,
        parse_frontmatter,
        scan_skill_files,
    )
    from fastmcp.server.providers.skills.skill_provider import SkillProvider

    _orig_load_skill = SkillProvider._load_skill

    def _patched_load_skill(self) -> None:
        main_file = self._skill_path / self._main_file_name
        if not self._skill_path.exists():
            raise FileNotFoundError(f"Skill directory not found: {self._skill_path}")
        if not main_file.exists():
            raise FileNotFoundError(
                f"Main skill file not found: {main_file}. "
                f"Expected {self._main_file_name} in {self._skill_path}"
            )
        content = main_file.read_text(encoding="utf-8")
        frontmatter, body = parse_frontmatter(content)
        description = frontmatter.get("description", "")
        if not description:
            for line in body.strip().split("\n"):
                line = line.strip()
                if line and not line.startswith("#"):
                    description = line[:200]
                    break
                elif line.startswith("#"):
                    description = line.lstrip("#").strip()[:200]
                    break
        files = scan_skill_files(self._skill_path)
        skill_name = frontmatter.get("name") or self._skill_path.name
        self._skill_info = SkillInfo(
            name=skill_name,
            description=description or f"Skill: {skill_name}",
            path=self._skill_path,
            main_file=self._main_file_name,
            files=files,
            frontmatter=frontmatter,
        )

    SkillProvider._load_skill = _patched_load_skill
except Exception:
    pass

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

# Methodology extension — stats and tool-call interceptor
mcp.add_extension(MethodologyExtension())

# SessionProvider enables create_session/end_session tools and SessionId resolution
mcp.add_provider(SessionProvider())

# 58 skills as skill:// resources (SKILL.md + ACCEPTANCE.md + _manifest)
mcp.add_provider(SkillsDirectoryProvider(roots=_skill_roots()))

# Python adapters (contracts, prompts, tools) discovered from server/components
components_dir = Path(__file__).parent / "components"
if components_dir.exists():
    mcp.add_provider(FileSystemProvider(components_dir))

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
