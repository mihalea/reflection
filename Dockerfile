FROM python:3
ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app

RUN mkdir config
ADD config/requirements.txt config/
RUN pip install -r config/requirements.txt

RUN mkdir web
RUN mkdir data

WORKDIR /app/web
