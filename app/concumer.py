#!/usr/bin/env python
import pika
import traceback, sys

from rabbit_conn import conn, chan

# import postgresql
# 
# db = postgresql.open('pq://postgres@postgres:5432/template1')
# db.execute("CREATE TABLE IF NOT EXISTS received (id SERIAL PRIMARY KEY, data CHAR(64))")

chan.queue_declare(queue='beat')

print("Waiting for messages. To exit press CTRL+C")

def callback(ch, method, properties, body):
    print(body)
    # ins = db.prepare("INSERT INTO received (data) VALUES ($1)")
    # ins(body)

chan.basic_consume(callback, queue='beat')

try:
    chan.start_consuming()
except KeyboardInterrupt:
    chan.stop_consuming()
except Exception:
    chan.stop_consuming()
    traceback.print_exc(file=sys.stdout)
