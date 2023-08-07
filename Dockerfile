FROM python:3.8-alpine

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

COPY . .
COPY ./project/.bak.env ./project/.env

RUN pip install --upgrade pip
RUN pip install pipenv
RUN pip install --no-cache-dir -r requirements.txt
RUN chmod +x /usr/src/app/wait-for