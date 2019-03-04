FROM python:3.7.2-alpine3.9

WORKDIR /app
ADD producer.py /app
ADD concumer.py /app
ADD rabbit_conn.py /app
ADD requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt
