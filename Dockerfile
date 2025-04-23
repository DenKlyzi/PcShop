FROM python:3.11-slim-bookworm

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    python3-dev \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

ENV PYTHONUNBUFFERED=1 \
    POETRY_VERSION=1.8.2 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN pip install "poetry==${POETRY_VERSION}" && \
    poetry install --no-interaction --no-ansi --no-root

COPY . .

RUN pip install -e .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]