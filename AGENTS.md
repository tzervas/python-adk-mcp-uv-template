# AGENTS.md — python-adk-mcp-uv-template

Short house rules for AI coding assistants working in this **template** repo
(or a project created from it via **Use this template**).

## What this is

A GitHub template for Python AI-agent projects using:

- **Google ADK** (`google-adk`) for agent definitions
- **MCP** (Model Context Protocol) for tool servers
- **uv** for lockfile-based dependency management

Prefer **[tz-forge](https://github.com/tzervas/tz-forge) `tz-new`** for general
fleet scaffolds (Rust/Python kinds, assistant profiles, fleet modules). Use
**this** template when you specifically need the ADK + MCP + uv layout.

## After cloning / using the template

1. Rename the package (see README **Rename the package**).
2. `uv sync`
3. `make test` (or `uv run pytest`)
4. Optional live agent: set `GOOGLE_API_KEY` / Vertex env in `.env`, then
   `uv run adk run src/<your_package>`

## Local checks

Run before considering work complete:

```bash
uv sync
make check    # lock, pre-commit, mypy, deptry
make test     # pytest + coverage
```

If `make` is unavailable:

```bash
uv lock --locked
uv run pre-commit run -a
uv run mypy
uv run deptry src
uv run python -m pytest --cov --cov-config=pyproject.toml
```

## Project map

```
src/python_adk_mcp_uv_template/   # rename after template use
  agent.py                        # sample_tool, create_agent, root_agent
  mcp_client.py                   # connect_mcp_server helper
tests/                            # pytest
config.yaml                       # ADK agent defaults
docs/                             # MkDocs + FLEET_STANDARDS
.github/workflows/                # fleet-ci, fleet-security, …
```

## PR flow (protect main / dev)

1. Create a feature or chore branch (never commit directly to `main`)
2. Keep diffs small and reviewable
3. Open PR → **`dev`** first when the repo uses a dev trunk; otherwise → `main`
4. Promote `dev` → `main` when ready for release

### Issue linking tiers

| Target branch | Issue keywords |
|---------------|----------------|
| `dev` / feature | **`Refs #n`** / `Related to #n` only — issues stay open |
| `main` | **`Closes #n`** / **`Fixes #n`** for completed work |

Epics close only when the delivery PR to `main` includes `Closes #<epic>`.

## Safety

- No secrets, tokens, or credentials in commits, logs, or issue bodies
- Do **not** request automatic Copilot code review
- Live model / MCP demos need user-supplied API keys and server processes

## Further reading

- [README.md](README.md) — 5-minute path + rename steps
- [docs/FLEET_STANDARDS.md](docs/FLEET_STANDARDS.md)
- [docs/adk_guide.md](docs/adk_guide.md) · [docs/mcp_guide.md](docs/mcp_guide.md)
- [CLAUDE.md](CLAUDE.md) — build/test map for coding assistants
- [tz-forge](https://github.com/tzervas/tz-forge) — preferred general scaffolder
