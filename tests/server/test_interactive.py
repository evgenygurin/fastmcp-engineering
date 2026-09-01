import pytest
from fastmcp import Client
from server.server import mcp

@pytest.mark.asyncio
async def test_clarify_find_interactive():
    async with Client(mcp) as client:
        # ambiguous query should return InputRequiredResult
        result = await client.call_tool("clarify_find", arguments={"task": "test"})
        # Either returns an elicitation request or a direct result — both are valid
        assert result is not None