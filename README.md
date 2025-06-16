# Python ADK + MCP + UV Template

🚀 **Project Status**: In active development. All components subject to change. Contributions and feedback welcome.

🎯 **Intent**: A template for building AI agent applications using Google’s Agent Development Kit (ADK), Anthropic’s Model Context Protocol (MCP), and UV for fast, reproducible Python dependency management.

🛠️ **Goals**:
- Provide a standardized setup for AI agent projects.
- Integrate Google ADK for agent creation and Anthropic MCP for external data connectivity.
- Use UV for efficient dependency and environment management.
- Ensure robust testing, linting, and documentation workflows.
- Support containerized development with Docker.

## Table of Contents

- [Python ADK + MCP + UV Template](#python-adk--mcp--uv-template)
  - [Table of Contents](#table-of-contents)
  - [Description](#description)
  - [Installation](#installation)
  - [Usage](#usage)
    - [Basic Example](#basic-example)
    - [Advanced Usage](#advanced-usage)
  - [Features](#features)
  - [Configuration](#configuration)
  - [Testing](#testing)
  - [Development Setup](#development-setup)
  - [Docker Setup](#docker-setup)
  - [Proposed Implementation](#proposed-implementation)
    - [Proof of Concept (POC)](#proof-of-concept-poc)
    - [Minimum Viable Product (MVP)](#minimum-viable-product-mvp)
  - [Contribution](#contribution)
  - [License](#license)
  - [Contact](#contact)
  - [Troubleshooting](#troubleshooting)
  - [Acknowledgments](#acknowledgments)
  - [References](#references)

## Description

This template provides a pre-configured Python project structure for developing AI agents using Google’s ADK and Anthropic’s MCP, managed with UV for dependency resolution. It includes:

- **Google ADK**: Tools for building AI agents, compatible with Gemini and other models.
- **Anthropic MCP**: Protocol for connecting AI models to external data sources (e.g., databases, APIs).
- **UV**: Fast, Rust-based package manager for reproducible environments.
- **Testing and Linting**: Configured with pytest, Ruff, mypy, and pre-commit hooks.
- **CI/CD**: GitHub Actions for automated testing and linting.
- **Documentation**: MkDocs setup for project documentation.
- **Docker**: Containerized development environment.

The template is designed for rapid project initialization, ensuring consistency and best practices for AI application development.

## Installation

To install the template, clone the repository and use UV to manage dependencies.

```bash
git clone https://github.com/tzervas/python-adk-mcp-uv-template.git
cd python-adk-mcp-uv-template
uv sync
```

Alternatively, use as a GitHub template by clicking "Use this template" on the repository page.

## Usage

### Basic Example

Run a sample ADK agent:

```python
from python_adk_mcp_uv_template.agent import sample_tool

# Basic usage
result = sample_tool("test query")
print(result)  # Output: {'status': 'success', 'result': 'Processed: test query'}
```

### Advanced Usage

Connect to an MCP server and run an ADK agent:

```python
import asyncio
from python_adk_mcp_uv_template.mcp_client import connect_mcp_server
from google.adk.agents import Agent

async def main():
    mcp = await connect_mcp_server("path/to/mcp/server")
    agent = Agent(name="sample_agent", tools=[sample_tool])
    # Add agent logic here
    await mcp.close()

if __name__ == "__main__":
    asyncio.run(main())
```

See the [Proposed Implementation](#proposed-implementation) section for more details.

## Features

- Pre-configured UV for dependency management.
- Google ADK integration for AI agent development.
- Anthropic MCP client for external data connectivity.
- Comprehensive testing with pytest and coverage reports.
- Linting and type checking with Ruff and mypy.
- Pre-commit hooks for code quality.
- GitHub Actions CI/CD pipeline.
- MkDocs-based documentation.
- Docker support for containerized development.

## Configuration

Configure the project using a `.env` file. Copy `.env.example` to `.env` and set the required keys:

```env
GOOGLE_API_KEY=your_google_api_key
ANTHROPIC_API_KEY=your_anthropic_api_key
GOOGLE_CLOUD_PROJECT=your_project_id
```

For advanced configuration, create a `config.yaml`:

```yaml
adk:
  agent_name: sample_agent
mcp:
  server_path: path/to/mcp/server
```

See [Configuration Guide](docs/configuration.md) for details.

## Testing

Run tests with pytest:

```bash
uv run pytest
```

Generate coverage reports:

```bash
uv run pytest --cov=src --cov-report=html
```

Ensure development dependencies are installed via `uv sync`.

## Development Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/tzervas/python-adk-mcp-uv-template.git
   ```
2. Navigate to the project directory:
   ```bash
   cd python-adk-mcp-uv-template
   ```
3. Install UV if not already installed:
   ```bash
   pip install uv
   ```
4. Sync dependencies:
   ```bash
   uv sync
   ```
5. Set up environment variables by copying `.env.example` to `.env` and filling in API keys.
6. Install pre-commit hooks:
   ```bash
   uv run pre-commit install
   ```
7. Run tests to verify setup:
   ```bash
   uv run pytest
   ```
8. Start the agent:
   ```bash
   uv run adk run src
   ```
9. Serve documentation locally:
   ```bash
   uv run mkdocs serve
   ```

## Docker Setup

Build and run the project in a Docker container:

```bash
docker build -t python-adk-mcp-uv-template .
docker run --env-file .env -v $(pwd)/src:/app/src python-adk-mcp-uv-template
```

The Dockerfile ensures all dependencies are installed and the project is synced with UV.

## Proposed Implementation

### Proof of Concept (POC)

Demonstrates a basic ADK agent with MCP connectivity:

```python
from google.adk.agents import Agent
from python_adk_mcp_uv_template.mcp_client import connect_mcp_server
import asyncio

async def poc():
    mcp = await connect_mcp_server("mock/server")
    agent = Agent(name="poc_agent", tools=[sample_tool])
    result = agent.run("test query")
    print(result)
    await mcp.close()

asyncio.run(poc())
```

### Minimum Viable Product (MVP)

A robust agent with configurable MCP connections and deployment-ready setup:

```python
import asyncio
from google.adk.agents import Agent
from python_adk_mcp_uv_template.mcp_client import connect_mcp_server
from python_adk_mcp_uv_template.agent import sample_tool

async def mvp():
    mcp = await connect_mcp_server("path/to/production/server")
    agent = Agent(
        name="mvp_agent",
        tools=[sample_tool],
        config={"model": "gemini-1.5-pro"}
    )
    result = await agent.run_async("production query")
    print(result)
    await mcp.close()

if __name__ == "__main__":
    asyncio.run(mvp())
```

## Contribution

Contributions are welcome! Please review the [Developer Guide](docs/devel-docs/developer_guide.md) and [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines. Submit issues or pull requests via [GitHub](https://github.com/tzervas/python-adk-mcp-uv-template).

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Contact

- **Author**: Tyler Zervas
- **GitHub**: [tzervas](https://github.com/tzervas)
- **X**: [@vec_wt_tech](https://x.com/vec_wt_tech)

## Troubleshooting

- **Dependency Issues**: Ensure UV is installed and run `uv sync`.
- **API Key Errors**: Verify `.env` contains valid Google and Anthropic API keys.
- **Docker Issues**: Check `.env` is mounted correctly with `--env-file`.
- Report issues on the [issue tracker](https://github.com/tzervas/python-adk-mcp-uv-template/issues).

## Acknowledgments

- [Google ADK](https://github.com/google/adk-python) for agent development tools.
- [Anthropic MCP](https://github.com/modelcontextprotocol) for external data connectivity.
- [UV](https://docs.astral.sh/uv/) for fast dependency management.
- [Ruff](https://github.com/astral-sh/ruff) and [mypy](https://github.com/python/mypy) for code quality.

## References

- [Google ADK Documentation](https://google.github.io/adk-docs/)
- [Anthropic MCP Documentation](https://modelcontextprotocol.io/)
- [UV Documentation](https://docs.astral.sh/uv/)
- [Multi-agent App Codelab](https://codelabs.developers.google.com/multi-agent-app-toolbox-adk)
