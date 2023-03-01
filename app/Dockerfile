FROM python:3.11-slim

WORKDIR /app

ARG PIP_NO_CACHE_DIR=1

ENV PYTHONPATH=$PYTHONPATH:/

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip && \
    pip install uvicorn &&\
    pip install -r requirements.txt

COPY . .
