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