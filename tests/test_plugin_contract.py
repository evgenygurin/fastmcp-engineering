from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / ".codex-plugin" / "plugin.json"


def load_manifest() -> dict:
    return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))


def test_plugin_manifest_is_valid_json_and_has_required_identity() -> None:
    manifest = load_manifest()
    assert isinstance(manifest.get("name"), str) and manifest["name"]
    assert isinstance(manifest.get("version"), str) and manifest["version"]
    assert isinstance(manifest.get("description"), str) and manifest["description"]
    assert manifest["skills"] == "./skills/"


def test_plugin_interface_contract() -> None:
    interface = load_manifest().get("interface")
    assert isinstance(interface, dict)
    for key in ("displayName", "shortDescription", "longDescription", "developerName", "category"):
        assert isinstance(interface.get(key), str) and interface[key]

    prompts = interface.get("defaultPrompt")
    assert isinstance(prompts, list)
    assert 1 <= len(prompts) <= 3
    assert all(isinstance(prompt, str) and prompt for prompt in prompts)
    assert all(len(prompt) <= 128 for prompt in prompts)


def test_plugin_resource_paths_are_relative_and_exist() -> None:
    manifest = load_manifest()
    interface = manifest["interface"]
    resource_paths = [manifest["skills"], interface["composerIcon"], interface["logo"]]

    for raw_path in resource_paths:
        assert raw_path.startswith("./"), raw_path
        assert ".." not in Path(raw_path).parts, raw_path
        assert (ROOT / raw_path[2:]).exists(), raw_path


def test_skills_directory_contains_skill_contracts() -> None:
    skills_root = ROOT / "skills"
    skill_files = sorted(skills_root.rglob("SKILL.md"))
    assert len(skill_files) == 59
    assert all((path.parent / "ACCEPTANCE.md").exists() for path in skill_files)
