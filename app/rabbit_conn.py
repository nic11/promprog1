import pika
import time
import sys

def try_connect(conn_params):
    try:
        return pika.BlockingConnection(conn_params)
    except pika.exceptions.ConnectionClosed:
        print('rabbitmq down, retrying')
        time.sleep(5)
        return try_connect(conn_params)

host, port = sys.argv[1:]

conn_params = pika.ConnectionParameters(host, port)
conn = try_connect(conn_params)
chan = conn.channel()
