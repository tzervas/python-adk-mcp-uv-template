# Build stage
FROM python:3.12-slim AS builder
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv
WORKDIR /app
COPY uv.lock pyproject.toml .
RUN uv sync --frozen --no-install-project
COPY . .
RUN uv sync --frozen

# Runtime stage
FROM python:3.12-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv
WORKDIR /app
COPY --from=builder /app /app
# Install runtime dependencies
RUN uv sync --frozen
# Health check
HEALTHCHECK --interval=30s --timeout=3s \
  CMD uv run python -c "import sys; sys.exit(0)" || exit 1
CMD ["uv", "run", "adk", "run", "src"]
