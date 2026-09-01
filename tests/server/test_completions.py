import pytest
from fastmcp import Client
from mcp.types import PromptReference, ResourceTemplateReference
from server.server import mcp


@pytest.mark.asyncio
async def test_complete_skill_arg():
    async with Client(mcp) as client:
        result = await client.complete(
            ref=PromptReference(type="ref/prompt", name="skill_context"),
            argument={"name": "skill", "value": "fastmcp-a"},
        )
        assert any("fastmcp-auth" in v for v in result.values)


@pytest.mark.asyncio
async def test_complete_contract_template():
    async with Client(mcp) as client:
        result = await client.complete(
            ref=ResourceTemplateReference(type="ref/resource", uri="contract://{name}"),
            argument={"name": "name", "value": "skill"},
        )
        assert "skill-contract" in result.values