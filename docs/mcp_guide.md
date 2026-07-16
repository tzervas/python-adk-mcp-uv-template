# MCP client guide

This template includes a small [Model Context Protocol](https://modelcontextprotocol.io/) client helper in `src/python_adk_mcp_uv_template/mcp_client.py`.

MCP is an open protocol (originally published by Anthropic) for connecting models to tools and data sources. The Python SDK is the `mcp` package on PyPI.

## `connect_mcp_server`

Async context manager that:

1. Spawns an MCP server process via stdio (`StdioServerParameters`)
2. Opens a `ClientSession`
3. Calls `initialize()`
4. Yields the session, then cleans up on exit

```python
import asyncio
from python_adk_mcp_uv_template.mcp_client import connect_mcp_server

async def main() -> None:
    # Example: run a local MCP server module with uv
    async with connect_mcp_server("uv", ["run", "path/to/mcp_server.py"]) as session:
        tools = await session.list_tools()
        print(tools)

asyncio.run(main())
```

## Notes

- There is no bundled MCP server in this template; point `command`/`args` at your own server.
- Optional Anthropic SDK support lives under the `integrations` extra (`uv sync --extra integrations`) and is not required for MCP stdio clients.
- SSE/HTTP transports are not wrapped yet; extend `mcp_client.py` using the official SDK transports if you need them.
