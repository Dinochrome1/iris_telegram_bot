FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY pyproject.toml /app
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --only main
COPY /app /app