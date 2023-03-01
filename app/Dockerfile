FROM python:3.11-slim

WORKDIR /app

ARG PIP_NO_CACHE_DIR=1

ENV PYTHONPATH=$PYTHONPATH:/

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

COPY requirements.txt .

RUN apt-get update && \
    apt-get -y install libpq-dev gcc && \
    pip install psycopg2 && \
    pip install --upgrade pip && \
    pip install uvicorn &&\
    pip install -r requirements.txt --no-cache-dir
    # apk --purge del .build-deps

COPY . .
