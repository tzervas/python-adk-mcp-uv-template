# Use a slim Python base image
FROM python:3.12-slim

# Install uv from a pre-built image for efficiency
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# Set working directory
WORKDIR /app

# Copy lockfile and pyproject.toml for dependency caching
COPY uv.lock /app/uv.lock
COPY pyproject.toml /app/pyproject.toml

# Install dependencies without project to leverage caching
RUN uv sync --frozen --no-install-project

# Copy the rest of the project
COPY . /app

# Sync the project to ensure all dependencies are installed
RUN uv sync --frozen

# Expose port if needed (optional, adjust as per project needs)
# EXPOSE 8080

# Command to run the ADK agent
CMD ["uv", "run", "adk", "run", "src"]
