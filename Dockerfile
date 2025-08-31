FROM python:3.13-slim-trixie

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

WORKDIR /core

RUN apt update -y && \
    apt install -y python3-dev \
    gcc \
    musl-dev

    COPY pyproject.toml poetry.lock* /core/

    RUN pip install --upgrade pip
    RUN pip install poetry

    RUN poetry config virtualenvs.create false
    RUN poetry install --no-root --no-interaction --no-ansi

    COPY . /core/

    COPY entrypoint.sh /entrypoint.sh
    RUN chmod +x /entrypoint.sh
