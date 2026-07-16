# Configuration Guide

How to configure this Python ADK + MCP + UV template.

## Environment variables

Copy `.env.example` to `.env` and set values as needed:

| Variable | Purpose |
| --- | --- |
| `GOOGLE_API_KEY` | Google AI / Gemini API key for ADK agents |
| `GOOGLE_CLOUD_PROJECT` | Optional Vertex AI / GCP project |
| `GOOGLE_CLOUD_LOCATION` | Optional GCP region (default in example: `us-central1`) |
| `ANTHROPIC_API_KEY` | Optional; used only with the `integrations` extra |

API keys are **not** required to import the package or run unit tests. They are required for live model calls.

## `config.yaml`

The sample agent loads project-root `config.yaml` when present:

```yaml
adk:
  agent_name: sample_agent
  model: gemini-1.5-pro
  max_tokens: 4096
  temperature: 0.7
mcp:
  # Documented for future use; connect_mcp_server currently takes command/args.
  server_path: src/mcp_server.py
  transport: stdio
  server_url: http://localhost:8050/sse
```

## Code entry points

- **ADK**: `create_agent()` / `root_agent` in `agent.py`
- **MCP**: `connect_mcp_server(command, args=...)` in `mcp_client.py`
