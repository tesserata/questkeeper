FROM python:3.13-slim AS runtime
WORKDIR /app
ENV PYTHONUNBUFFERED=1

COPY pyproject.toml /app/pyproject.toml
COPY uv.lock /app/uv.lock

COPY libs/ /app/libs/

RUN pip install --no-cache-dir uv==0.4.0
RUN uv sync --no-dev

ENV PATH="/app/.venv/bin:$PATH"

COPY services/backend/app ./app
COPY services/backend/alembic.ini ./alembic.ini

EXPOSE 50051