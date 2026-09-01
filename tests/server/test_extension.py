import pytest
from fastmcp import Client
from server.server import mcp
from mcp.types import Request, RequestParams
from pydantic import TypeAdapter


class StatsRequest(Request):
    method: str = "methodology/stats"
    params: RequestParams = RequestParams()
    name_param: str | None = None


@pytest.mark.asyncio
async def test_extension_advertised():
    async with Client(mcp) as client:
        caps = client.server_capabilities
        # Check if extension is advertised in capabilities.extensions
        extensions = getattr(caps, "extensions", {})
        assert "dev.fastmcp-eng/methodology" in extensions
        
        # Call the methodology/stats method
        request = StatsRequest()
        result = await client.session.send_request(request, TypeAdapter(dict))
        assert "skillsCount" in result
        assert "domains" in result
        assert "callCounts" in result
        assert result["skillsCount"] == 58


@pytest.mark.asyncio
async def test_extension_tool_call_interceptor():
    async with Client(mcp) as client:
        # Get initial stats
        request = StatsRequest()
        initial = await client.session.send_request(request, TypeAdapter(dict))
        initial_counts = dict(initial.get("callCounts", {}))
        
        # Call a tool (find_skills)
        await client.call_tool("find_skills", arguments={"task": "auth"})
        
        # Check that call count increased
        after = await client.session.send_request(request, TypeAdapter(dict))
        after_counts = dict(after.get("callCounts", {}))
        
        # The tool call should be counted
        assert after_counts.get("find_skills", 0) > initial_counts.get("find_skills", 0)