FROM python:3.10 AS base
WORKDIR /code/api


FROM base AS python-deps
RUN pip install pipenv
RUN apt-get update && apt-get install -y --no-install-recommends gcc

COPY ./api/Pipfile .
COPY ./api/Pipfile.lock .

COPY ./api/* .
CMD "pipenv install"
