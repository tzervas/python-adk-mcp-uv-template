from mcp import FastMCP
from anthropic import Anthropic
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def connect_mcp_server(server_path: str = None):
    try:
        if not server_path:
            raise ValueError("MCP server path not specified")
        client = Anthropic()
        mcp = FastMCP(client=client)
        await mcp.connect_stdio(server_path)
        logger.info(f"Connected to MCP server at {server_path}")
        return mcp
    except Exception as e:
        logger.error(f"Failed to connect to MCP server: {e}")
        raise
