FROM python:3.11-slim

ENV POETRY_VERSION=1.8.2 \
    PYTHONUNBUFFERED=1 \
    POETRY_NO_INTERACTION=1

WORKDIR /app

RUN apt-get update && apt-get install -y curl && \
    pip install --upgrade pip && \
    pip install "poetry==$POETRY_VERSION"

COPY pyproject.toml poetry.lock* /app/

RUN poetry install --only main --no-root

COPY . /app

EXPOSE 8000

CMD ["poetry", "run", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
