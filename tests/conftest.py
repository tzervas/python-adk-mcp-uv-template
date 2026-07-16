"""Shared pytest fixtures."""

from __future__ import annotations

import pytest


@pytest.fixture
def anyio_backend() -> str:
    """Run anyio-marked tests on asyncio only (trio is not a project dependency)."""
    return "asyncio"
