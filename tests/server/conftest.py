import pytest
from fastmcp import Client
from fastmcp.client.transports import FastMCPTransport

# Import after Task 3 creates server.mcp; for now provide a placeholder
# that later tasks replace with the real import.
try:
    from server.server import mcp
except Exception:
    mcp = None

@pytest.fixture
async def mcp_client():
    if mcp is None:
        pytest.skip("server.mcp not yet implemented")
    async with Client(transport=mcp) as client:
        yield client
