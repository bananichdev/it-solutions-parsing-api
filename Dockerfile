FROM python:3.12-alpine
LABEL authors="Dmitriy Panin"

RUN pip install poetry
WORKDIR /parse-api

COPY . .
RUN poetry install

CMD poetry run alembic upgrade head && poetry run python main.py
