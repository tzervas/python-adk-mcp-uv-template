"""Minimal MCP stdio client helpers for this template.

Uses the official Model Context Protocol Python SDK (``mcp`` package) to spawn
a server process and open an initialized :class:`mcp.ClientSession`.
"""

from __future__ import annotations

import logging
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

logger = logging.getLogger(__name__)


@asynccontextmanager
async def connect_mcp_server(
    command: str,
    args: list[str] | None = None,
    *,
    cwd: str | None = None,
    env: dict[str, str] | None = None,
) -> AsyncIterator[ClientSession]:
    """Connect to an MCP server over stdio and yield an initialized session.

    Args:
        command: Executable used to start the MCP server (e.g. ``"uv"`` or ``"npx"``).
        args: Arguments for the command (e.g. ``["run", "server.py"]``).
        cwd: Optional working directory for the server process.
        env: Optional environment variables for the server process.

    Yields:
        An initialized :class:`mcp.ClientSession`.

    Raises:
        ValueError: If ``command`` is empty.
    """
    if not command:
        msg = "MCP server command not specified"
        raise ValueError(msg)

    server = StdioServerParameters(
        command=command,
        args=args or [],
        cwd=cwd,
        env=env,
    )
    try:
        async with (
            stdio_client(server) as (read_stream, write_stream),
            ClientSession(read_stream, write_stream) as session,
        ):
            await session.initialize()
            logger.info(
                "Connected to MCP server via %s %s",
                command,
                " ".join(args or []),
            )
            yield session
    except Exception:
        logger.exception("Failed to connect to MCP server")
        raise
