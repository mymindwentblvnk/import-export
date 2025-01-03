FROM python:3.13-slim

WORKDIR /app
COPY poetry.lock pyproject.toml /app/

RUN pip install poetry --upgrade pip \
    && poetry config virtualenvs.in-project true

COPY --chown=1000:1000 import_export /app/import_export/

RUN poetry install --only main

USER 1000:1000