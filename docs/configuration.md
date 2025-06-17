# Configuration Guide

This guide details how to configure the Python ADK + MCP + UV Template.

## Environment Variables
Copy `.env.example` to `.env` and set the following:
- `GOOGLE_API_KEY`: Your Google Cloud API key for ADK integration.
- `ANTHROPIC_API_KEY`: Your Anthropic API key for MCP functionality.
- `GOOGLE_CLOUD_PROJECT`: Your Google Cloud project ID.

## Config YAML
Create a `config.yaml` file in the project root with the following structure:
```yaml
adk:
  agent_name: sample_agent
  model: gemini-1.5-pro
  max_tokens: 4096
  temperature: 0.7
mcp:
  server_path: src/mcp_server.py
  transport: stdio  # Options: stdio, sse, http
  server_url: http://localhost:8050/sse  # Required for sse or http transports
```

## Advanced Options
- **ADK**: Customize the model, token limits, or add tools via `Agent` parameters in `agent.py`.
- **MCP**: Adjust transport types or specify custom server URLs in `mcp_client.py`.