# Python ADK + MCP + UV Template

<!-- FLEET-BADGES:BEGIN -->
[![CI](https://github.com/tzervas/python-adk-mcp-uv-template/actions/workflows/fleet-ci.yml/badge.svg?branch=main)](https://github.com/tzervas/python-adk-mcp-uv-template/actions/workflows/fleet-ci.yml?query=branch%3Amain)
[![Security](https://github.com/tzervas/python-adk-mcp-uv-template/actions/workflows/fleet-security.yml/badge.svg?branch=main)](https://github.com/tzervas/python-adk-mcp-uv-template/actions/workflows/fleet-security.yml?query=branch%3Amain)
<!-- FLEET-BADGES:END -->

**Project status**: Active **GitHub template** (`isTemplate=true`). Scaffolding works for local install, tests, lint, and docs; live agent/MCP demos need your own API keys and server processes.

**Intent**: A template for building AI agent applications using Google’s Agent Development Kit (ADK), the Model Context Protocol (MCP), and [uv](https://docs.astral.sh/uv/) for fast, reproducible Python dependency management.

**Goals**:

- Provide a standardized setup for AI agent projects.
- Integrate Google ADK for agent creation and MCP for external tool connectivity.
- Use uv for efficient dependency and environment management.
- Ensure testing, linting, and documentation workflows.
- Support containerized development with Docker.

> **Prefer [tz-forge](https://github.com/tzervas/tz-forge) `tz-new`** for general fleet scaffolds (Rust/Python kinds, assistant profiles, fleet modules). Use **this** template when you specifically need the ADK + MCP + uv layout.

## Table of Contents

- [Use this template](#use-this-template)
- [5-minute path](#5-minute-path)
- [Rename the package](#rename-the-package)
- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Configuration](#configuration)
- [Testing](#testing)
- [Development Setup](#development-setup)
- [Docker Setup](#docker-setup)
- [Contribution](#contribution)
- [License](#license)
- [Contact](#contact)
- [Troubleshooting](#troubleshooting)
- [Acknowledgments](#acknowledgments)
- [References](#references)

## Use this template

1. On GitHub, open [python-adk-mcp-uv-template](https://github.com/tzervas/python-adk-mcp-uv-template) and click **Use this template** → **Create a new repository**.
2. Clone your new repo.
3. Follow the [5-minute path](#5-minute-path), then [Rename the package](#rename-the-package).

CLI equivalent (create a repo from the template):

```bash
gh repo create my-adk-agent --template tzervas/python-adk-mcp-uv-template --public --clone
cd my-adk-agent
```

Agent surface for coding assistants: [AGENTS.md](AGENTS.md) · [CLAUDE.md](CLAUDE.md).

## 5-minute path

Prerequisites: [uv](https://docs.astral.sh/uv/getting-started/installation/) and Python **3.12+**.

```bash
# From a clone of this template (or your new repo)
uv sync
make test
# expected: pytest passes (sample_tool / agent unit tests)
```

Smoke import without `make`:

```bash
uv run python -c "from python_adk_mcp_uv_template.agent import sample_tool; print(sample_tool('hi'))"
# expected: {'status': 'success', 'result': 'Processed: hi'}
```

Quality gate used in CI:

```bash
make check   # lock, pre-commit, mypy, deptry
make test
```

## Rename the package

After creating a repo from this template, replace the placeholder package name so imports and metadata match your product.

| Placeholder | Example replacement |
|-------------|---------------------|
| Project / dist name `python-adk-mcp-uv-template` | `my-adk-agent` |
| Import package `python_adk_mcp_uv_template` | `my_adk_agent` |
| Directory `src/python_adk_mcp_uv_template/` | `src/my_adk_agent/` |

Checklist:

1. **Rename the package directory**

   ```bash
   mv src/python_adk_mcp_uv_template src/my_adk_agent
   ```

2. **Update `pyproject.toml`**: set `name = "my-adk-agent"` (and description/urls as needed). Hatch/uv discover packages under `src/`; ensure the new directory name matches the import path.

3. **Rewrite imports** in tests, docs, `Dockerfile`, and any `adk run` paths:

   ```bash
   # example: recursive replace of the import path (review the diff)
   rg -l 'python_adk_mcp_uv_template' | xargs sed -i 's/python_adk_mcp_uv_template/my_adk_agent/g'
   ```

4. **Refresh lock + verify**

   ```bash
   uv sync
   make test
   ```

5. Optional: update README title, Docker image tag, and MkDocs `site_name` in `mkdocs.yml`.

## Description

This template provides a pre-configured Python project structure for developing AI agents with Google ADK and MCP, managed with uv:

- **Google ADK**: Agent definitions, tools, and CLI (`adk`).
- **MCP**: Official Python SDK client helpers for stdio MCP servers.
- **uv**: Lockfile-based package/environment management.
- **Testing and linting**: pytest, Ruff, mypy, pre-commit.
- **CI/CD**: GitHub Actions (self-hosted runners in this repo).
- **Documentation**: MkDocs Material.
- **Docker**: Multi-stage image using uv.

Supported Python versions: **3.12 and 3.13** (`requires-python = ">=3.12,<4.0"`).

## Installation

```bash
git clone https://github.com/tzervas/python-adk-mcp-uv-template.git
cd python-adk-mcp-uv-template
uv sync
```

Or use **[Use this template](#use-this-template)** on GitHub (preferred for new projects).

## Usage

### Basic example (no API key required)

```python
from python_adk_mcp_uv_template.agent import sample_tool

result = sample_tool("test query")
print(result)  # {'status': 'success', 'result': 'Processed: test query'}
```

### Create an ADK agent

```python
from python_adk_mcp_uv_template.agent import create_agent, sample_tool

agent = create_agent()  # loads config.yaml when present
print(agent.name, agent.model)
print(sample_tool("hello"))
```

Live multi-turn execution uses ADK runners (and a model API key), not a method on `Agent` itself. See [docs/adk_guide.md](docs/adk_guide.md).

### Connect to an MCP server

```python
import asyncio
from python_adk_mcp_uv_template.mcp_client import connect_mcp_server

async def main() -> None:
    # Point command/args at your own MCP server process.
    async with connect_mcp_server("uv", ["run", "path/to/mcp_server.py"]) as session:
        tools = await session.list_tools()
        print(tools)

if __name__ == "__main__":
    asyncio.run(main())
```

See [docs/mcp_guide.md](docs/mcp_guide.md).

## Features

- Pre-configured uv project (`pyproject.toml` + `uv.lock`)
- Sample ADK agent (`sample_tool`, `create_agent`, `root_agent`)
- MCP stdio client helper (`connect_mcp_server`)
- pytest + coverage, Ruff, mypy, pre-commit
- GitHub Actions CI
- MkDocs documentation
- Dockerfile for containerized runs

## Configuration

Copy `.env.example` to `.env` when you need live API access:

```env
GOOGLE_API_KEY=your_google_api_key
GOOGLE_CLOUD_PROJECT=your_project_id
GOOGLE_CLOUD_LOCATION=us-central1
ANTHROPIC_API_KEY=your_anthropic_api_key  # optional integrations extra
```

Agent defaults live in `config.yaml`:

```yaml
adk:
  agent_name: sample_agent
  model: gemini-1.5-pro
  max_tokens: 4096
  temperature: 0.7
```

Details: [docs/configuration.md](docs/configuration.md).

## Testing

```bash
uv run pytest
# or
make test
```

Coverage:

```bash
uv run pytest --cov --cov-config=pyproject.toml --cov-report=html
```

## Development Setup

1. Clone and enter the repo.
2. Install uv if needed: <https://docs.astral.sh/uv/getting-started/installation/>
3. `uv sync`
4. Optional: copy `.env.example` → `.env`
5. `uv run pre-commit install` (or `make install`)
6. `uv run pytest`
7. Optional live agent CLI (needs API credentials):

   ```bash
   uv run adk run src/python_adk_mcp_uv_template
   ```

8. Docs:

   ```bash
   uv run mkdocs serve
   ```

Quality gate used in CI:

```bash
make check   # lock, pre-commit, mypy, deptry
make test
```

## Docker Setup

```bash
docker build -t python-adk-mcp-uv-template .
docker run --env-file .env -v "$(pwd)/src:/app/src" python-adk-mcp-uv-template
```

The image default command runs the ADK CLI against the sample package. Provide credentials via `--env-file` for live models.

## Contribution

See [CONTRIBUTING.md](CONTRIBUTING.md). Issues and PRs: [GitHub](https://github.com/tzervas/python-adk-mcp-uv-template).

## License

MIT. See [LICENSE](LICENSE).

## Contact

- **Author**: Tyler Zervas
- **GitHub**: [tzervas](https://github.com/tzervas)
- **X**: [@vec_wt_tech](https://x.com/vec_wt_tech)

## Troubleshooting

- **Dependency issues**: Install uv, then `uv sync`.
- **API key errors**: Set `GOOGLE_API_KEY` (or Vertex env) in `.env` for live agent runs.
- **MCP connection errors**: Ensure the server command exits cleanly and speaks MCP over stdio.
- **Docker**: Mount/pass `.env` with `--env-file`.
- Report bugs on the [issue tracker](https://github.com/tzervas/python-adk-mcp-uv-template/issues).

## Acknowledgments

- [Google ADK](https://github.com/google/adk-python)
- [Model Context Protocol](https://github.com/modelcontextprotocol)
- [uv](https://docs.astral.sh/uv/)
- [Ruff](https://github.com/astral-sh/ruff) and [mypy](https://github.com/python/mypy)

## References

- [Google ADK Documentation](https://google.github.io/adk-docs/)
- [MCP Documentation](https://modelcontextprotocol.io/)
- [uv Documentation](https://docs.astral.sh/uv/)
- [Multi-agent App Codelab](https://codelabs.developers.google.com/multi-agent-app-toolbox-adk)
