from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / ".codex-plugin" / "plugin.json"


def test_codex_plugin_manifest_exists_and_is_valid() -> None:
    assert MANIFEST.is_file()
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))

    assert manifest["name"] == "fastmcp-engineering"
    assert manifest["version"] == "0.1.0"
    assert manifest["description"]
    assert manifest["author"]["name"] == "evgenygurin"
    assert manifest["skills"] == "./skills/"

    interface = manifest["interface"]
    for field in ("displayName", "shortDescription", "longDescription", "developerName", "category"):
        assert interface[field].strip()

    skills_path = ROOT / manifest["skills"][2:]
    assert skills_path.is_dir()
    assert list(skills_path.rglob("SKILL.md"))


def test_manifest_does_not_reference_missing_optional_surfaces() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))

    if "mcpServers" in manifest:
        assert (ROOT / manifest["mcpServers"][2:]).is_file()
    if "apps" in manifest:
        assert (ROOT / manifest["apps"][2:]).is_file()
