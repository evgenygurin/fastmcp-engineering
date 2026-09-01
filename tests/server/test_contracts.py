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