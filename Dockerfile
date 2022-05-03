FROM python:3.8

ARG CURRENT_ENV=${CURRENT_ENV}
ENV PYTHONBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /code
COPY requirements.txt /code/

RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install -r requirements.txt --no-cache-dir
