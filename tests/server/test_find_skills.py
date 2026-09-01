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