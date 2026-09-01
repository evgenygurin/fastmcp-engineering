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
