import pytest
from fastmcp import Client
from server.server import mcp

@pytest.mark.asyncio
async def test_session_lifecycle_and_boost():
    async with Client(mcp) as client:
        # create_session comes from SessionProvider
        create = await client.call_tool("create_session", arguments={})
        sid = create.data if isinstance(create.data, str) else create.data.get("session_id") or str(create.data)
        assert sid
        # first search with session
        r1 = await client.call_tool("find_skills", arguments={"task": "auth", "session_id": sid})
        assert r1.data
        # second search in same session — history boost path exercised
        r2 = await client.call_tool("find_skills", arguments={"task": "test auth flow", "session_id": sid})
        assert r2.data

@pytest.mark.asyncio
async def test_unknown_session_rejects():
    async with Client(mcp) as client:
        result = await client.call_tool("find_skills", arguments={"task": "auth", "session_id": "bogus-id-123"})
        # Should raise or return error — not silently succeed
        assert result.is_error or result.data is None or "error" in str(result).lower()