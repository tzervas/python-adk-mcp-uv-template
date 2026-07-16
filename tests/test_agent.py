"""Unit tests for the sample agent and MCP helpers."""

from __future__ import annotations

import pytest

from python_adk_mcp_uv_template.agent import create_agent, load_config, sample_tool
from python_adk_mcp_uv_template.mcp_client import connect_mcp_server


def test_sample_tool() -> None:
    result = sample_tool("test query")
    assert result["status"] == "success"
    assert result["result"] == "Processed: test query"


def test_load_config() -> None:
    config = load_config()
    assert "adk" in config
    assert config["adk"]["agent_name"] == "sample_agent"


def test_create_agent() -> None:
    agent = create_agent()
    assert agent.name == "sample_agent"
    assert agent.model == "gemini-1.5-pro"


def test_create_agent_with_explicit_config() -> None:
    agent = create_agent({
        "adk": {
            "agent_name": "custom_agent",
            "model": "gemini-2.0-flash",
            "max_tokens": 1024,
            "temperature": 0.1,
        }
    })
    assert agent.name == "custom_agent"
    assert agent.model == "gemini-2.0-flash"


@pytest.mark.anyio
async def test_mcp_connection_requires_command() -> None:
    with pytest.raises(ValueError, match="command"):
        async with connect_mcp_server(""):
            pass
