FROM python:3.13-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    g++ \
    curl \
    unixodbc \
    unixodbc-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir poetry
RUN poetry config virtualenvs.create false

WORKDIR /

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-interaction --no-ansi --no-root

COPY ./app /app/

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
