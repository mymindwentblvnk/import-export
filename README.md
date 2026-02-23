# import-export

A blueprint for building data ingestion pipelines with Python.

This repository provides a foundational framework and patterns for implementing robust data import and export workflows, designed to streamline the development of ETL (Extract, Transform, Load) processes.

## Requirements

- Python 3.13+
- Poetry for dependency management
- Docker (optional, for containerized deployment)

## Local Setup

### Option 1: Poetry (Recommended for Development)

1. Install Poetry if you haven't already:
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

2. Install project dependencies:
   ```bash
   poetry install
   ```

3. Activate the virtual environment:
   ```bash
   poetry shell
   ```

### Option 2: Docker

Build the Docker image:

```bash
docker build -t import-export .
```

Run the container:

```bash
docker run import-export
```

The Docker image:
- Uses Python 3.13 slim base image
- Installs only production dependencies (`--only main`)
- Runs as non-root user (1000:1000) for security

## Development

This project uses the following tools for code quality and consistency:

- **Ruff**: Fast Python linter
- **Black**: Code formatter (line length: 120)
- **Pytest**: Testing framework
- **Coverage**: Test coverage reporting
- **PyHamcrest**: Matcher library for assertions

### Running Tests

Run the test suite:

```bash
poetry run pytest
```

Run tests with coverage:

```bash
poetry run coverage run -m pytest
poetry run coverage report -m
```

### Code Quality

Lint the codebase:

```bash
poetry run ruff check .
```

Format code:

```bash
poetry run black .
```

Check formatting without modifying files:

```bash
poetry run black --check .
```

## CI/CD Pipeline

This project uses GitHub Actions for continuous integration and deployment:

### Build Workflow

Triggered on changes to `pyproject.toml` or `tests/**`:

- **Setup**: Installs Python 3.13 and Poetry dependencies
- **Linting**: Runs Ruff to check code quality
- **Style Check**: Validates code formatting with Black
- **Testing**: Executes test suite with coverage reporting

### Release Workflow

Triggered on changes to core project files:

- Prepares release version
- Runs build workflow
- Creates GitHub releases (on main branch for non-dev versions)
- Docker image build (currently commented out)
