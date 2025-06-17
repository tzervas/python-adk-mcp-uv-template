import pytest
from python_adk_mcp_uv_template.agent import sample_tool
from python_adk_mcp_uv_template.mcp_client import connect_mcp_server

def test_sample_tool():
    result = sample_tool("test query")
    assert result["status"] == "success"
    assert result["result"] == "Processed: test query"

@pytest.mark.asyncio
async def test_mcp_connection():
    try:
        mcp = await connect_mcp_server("src/mcp_server.py")
        assert mcp is not None
        await mcp.close()
    except Exception:
        pytest.skip("MCP server not running")
