# python-adk-mcp-uv-template — Claude / coding-assistant context

## Overview

GitHub **template** for Python AI agents: Google ADK + MCP + uv.
Scaffolding works offline (install, tests, lint, docs). Live agent/MCP demos
need API keys and external server processes.

## Project map

```
src/python_adk_mcp_uv_template/
  __init__.py      # re-exports create_agent, root_agent, sample_tool
  agent.py         # ADK agent factory + sample_tool
  mcp_client.py    # async stdio MCP session helper
tests/
  test_agent.py
config.yaml        # adk.agent_name / model / tokens / temperature
Makefile           # install, check, test, docs
docs/              # MkDocs Material
.github/workflows/ # fleet-ci, fleet-security, close/reopen issues
```

## Development commands

```bash
# Install
uv sync
# or
make install

# Quality gate (CI-equivalent)
make check

# Tests
make test
# or
uv run pytest -q

# Docs
uv run mkdocs serve

# Live agent CLI (needs credentials in .env)
uv run adk run src/python_adk_mcp_uv_template
```

## Rename after "Use this template"

1. Pick a package name (`my_agent`) and project name (`my-agent`).
2. Rename `src/python_adk_mcp_uv_template` → `src/my_agent`.
3. Update `name` / imports in `pyproject.toml`, `README.md`, tests, docs, Dockerfile.
4. `uv sync && make test`.

See README **Use this template** for the full checklist.

## Coding standards

- Prefer small, reviewable diffs
- No secrets in commits or logs
- Run `make check` + `make test` before claiming work complete
- Do **not** enable automatic Copilot code review on PRs
- Python **3.12–3.13**; manage deps with **uv** only (commit `uv.lock`)

## PR hygiene

- Feature branch → `dev` (use `Refs #n` only) when applicable
- `dev` → `main` delivery (use `Closes #n` / `Fixes #n`)
- See `AGENTS.md` for fuller agent rules and issue-close policy

## Further reading

- README.md
- docs/FLEET_STANDARDS.md
- docs/adk_guide.md
- docs/mcp_guide.md
- AGENTS.md
