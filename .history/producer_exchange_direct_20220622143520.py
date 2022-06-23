import math
from random import Random, random
import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', '49154'))
channel = connection.channel()

messages = [
    {
        "message":"Falha ao baixar app",
        "type": "Error"
    },
    {
        "message":"Falha ao autenticar no multicanalidade",
        "type": "Warning"
    },
    "Store-Mobile": {
        "message":"Comunicação com o servidor ultrapassou 20 segundos",
        "type": "Info"
    },
]

for i in range(0,100):
    destino = Random.randint(0,2)
    if destino == 0:
        messages['']
    elif destino == 1:

    elif destino == 2:



for msg in messages:
    channel.basic_publish(
        exchange='logs',routing_key='',body=msg
    )

    print(f"Enviado: {msg}")
    time.sleep(1)
connection.close()