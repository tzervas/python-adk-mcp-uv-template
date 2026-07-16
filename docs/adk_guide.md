# Google ADK guide

This template wires a sample [Google Agent Development Kit (ADK)](https://google.github.io/adk-docs/) agent in `src/python_adk_mcp_uv_template/agent.py`.

## Sample pieces

| Symbol | Role |
| --- | --- |
| `sample_tool` | A plain Python function registered as an ADK tool |
| `create_agent()` | Builds an `Agent` from `config.yaml` (or defaults) |
| `root_agent` | Module-level agent for ADK CLI discovery |

## Config keys (`config.yaml`)

```yaml
adk:
  agent_name: sample_agent
  model: gemini-1.5-pro
  max_tokens: 4096
  temperature: 0.7
```

These map to ADK `Agent` fields (`name`, `model`) and `GenerateContentConfig` (`max_output_tokens`, `temperature`).

## Running

With dependencies installed and a valid `GOOGLE_API_KEY` (or Vertex credentials):

```bash
uv run adk run src/python_adk_mcp_uv_template
```

Or construct an agent in code:

```python
from python_adk_mcp_uv_template.agent import create_agent, sample_tool

agent = create_agent()
print(sample_tool("hello"))
```

Live multi-turn runs typically go through ADK's `Runner` / `InMemoryRunner` APIs rather than calling methods on `Agent` directly. See the [official ADK docs](https://google.github.io/adk-docs/).
