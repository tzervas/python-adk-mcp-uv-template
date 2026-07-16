"""Sample Google ADK agent definition for this template."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml
from google.adk.agents import Agent
from google.genai import types


def sample_tool(query: str) -> dict[str, str]:
    """Process a simple query string.

    Args:
        query: User query text.

    Returns:
        A status/result payload suitable for use as an ADK tool.
    """
    return {"status": "success", "result": f"Processed: {query}"}


def load_config(config_path: str | Path | None = None) -> dict[str, Any]:
    """Load YAML configuration from the project root by default.

    Args:
        config_path: Optional path to a YAML file. Defaults to ``config.yaml``.

    Returns:
        Parsed configuration mapping.

    Raises:
        FileNotFoundError: If the config file does not exist.
        ValueError: If the file does not contain a YAML mapping.
    """
    path = Path(config_path) if config_path is not None else Path("config.yaml")
    with path.open(encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict):
        msg = f"Expected a mapping in config file {path}, got {type(data).__name__}"
        raise TypeError(msg)
    return data


def create_agent(config: dict[str, Any] | None = None) -> Agent:
    """Create an ADK ``Agent`` from config or project defaults.

    Args:
        config: Optional configuration mapping. When omitted, loads ``config.yaml``
            if present; otherwise uses built-in defaults.

    Returns:
        A configured :class:`google.adk.agents.Agent` instance.
    """
    if config is None:
        try:
            config = load_config()
        except FileNotFoundError:
            config = {}

    adk = config.get("adk", {}) if config else {}
    name = str(adk.get("agent_name", "sample_agent"))
    model = str(adk.get("model", "gemini-1.5-pro"))
    max_tokens = int(adk.get("max_tokens", 4096))
    temperature = float(adk.get("temperature", 0.7))

    return Agent(
        name=name,
        model=model,
        instruction="You are a helpful assistant from the python-adk-mcp-uv-template.",
        tools=[sample_tool],
        generate_content_config=types.GenerateContentConfig(
            max_output_tokens=max_tokens,
            temperature=temperature,
        ),
    )


# ADK CLI discovery (`adk run`) expects a module-level `root_agent` in agent packages.
root_agent = create_agent()
