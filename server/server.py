from pathlib import Path
from fastmcp import FastMCP
from fastmcp.server.providers.skills import SkillsDirectoryProvider
from fastmcp.server.providers import FileSystemProvider

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

# 58 skills as skill:// resources (SKILL.md + ACCEPTANCE.md + _manifest)
mcp.add_provider(SkillsDirectoryProvider(roots=_skill_roots()))

# Python adapters (contracts, prompts, tools) discovered from server/components
components_dir = Path(__file__).parent / "components"
if components_dir.exists():
    mcp.add_provider(FileSystemProvider(components_dir))
