FROM python:3.11

WORKDIR /app

COPY ./app /app

RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get install -y postgresql-client