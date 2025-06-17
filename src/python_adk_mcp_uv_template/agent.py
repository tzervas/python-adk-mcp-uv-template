import yaml
from google.adk.agents import Agent
from google.adk.tools.mcp_tool import MCPToolset
from mcp.client.stdio import StdioServerParameters

def load_config():
    with open("config.yaml", "r") as f:
        return yaml.safe_load(f)

config = load_config()
server_params = StdioServerParameters(
    command="python",
    args=["path/to/external/mcp_server.py"],
)
mcp_toolset = MCPToolset(server_params)
"""
Example of an agent that uses external MCP tools. You can use this agent to
run external MCP tools by specifying the server path.
"""
"""
name="MyAgent",
description="An agent that uses external MCP tools",
model="gemini-1.5-pro-0404",
tools=[mcp_toolset],
"""
agent = Agent(
    name=config["adk"]["agent_name"],
    tools=[mcp_toolset],
    config={
        "model": config["adk"]["model"],
        "max_tokens": config["adk"]["max_tokens"],
        "temperature": config["adk"]["temperature"],
    },
)
