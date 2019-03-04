#!/usr/bin/env python3

import pika
import time
import sys
import random

from rabbit_conn import conn, chan

chan.queue_declare(queue='beat')

#while True:
for i in range(10):
    msg = str(random.randint(1, 1337))
    chan.basic_publish(
        exchange='',
        routing_key='beat',
        body=msg
    )
    print('Sent', msg)
    time.sleep(random.randint(1, 3))

conn.close()
