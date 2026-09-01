import pytest
from fastmcp import Client
from server.server import mcp

@pytest.fixture
async def mcp_client():
    async with Client(mcp) as client:
        yield client
