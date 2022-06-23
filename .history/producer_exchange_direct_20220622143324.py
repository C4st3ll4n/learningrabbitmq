import math
from random import random
import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', '49154'))
channel = connection.channel()

messages = {
    "Store-Mobile": {
        "message":"Falha ao baixar app",
        "type": "Error"
    },
    "Store-Mobile": {
        "message":"Falha ao autenticar no multicanalidade",
        "type": "Warning"
    },
    "Store-Mobile": {
        "message":"Comunicação com o servidor ultrapassou 20 segundos",
        "type": "Info"
    },
}

for i in range(0,100):
    random()
    if div==0:


for msg in messages:
    channel.basic_publish(
        exchange='logs',routing_key='',body=msg
    )

    print(f"Enviado: {msg}")
    time.sleep(1)
connection.close()