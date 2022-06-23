import math
from random import Random, random
import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', '49154'))
channel = connection.channel()

messages = [
    {
        "application": "Store-mobile",
        "message":"Falha ao baixar app",
        "type": "Error"
    },
    {
        "application": "Store-mobile",
        "message":"Falha ao autenticar no multicanalidade",
        "type": "Warning"
    },
    {
        "application": "Store-mobile",
        "message":"Comunicação com o servidor ultrapassou 20 segundos",
        "type": "Info"
    },
]

for i in range(0,100):
    destino = Random.randint(0,2)
    log_type = Random.randint(0,2)
    
    log = ""
    app = ""
    if log_type == 0:
        log = "Info"
    elif log_type == 0:
        log = "Warning"
    elif log_type == 0:
        log = "Error"

    if destino == 0:
        
        messages.append({
            "application": "ADP-Client",
        "message":"Comunicação com o servidor ultrapassou 20 segundos",
        "type": "Info"
        })
    elif destino == 1:
        messages.append({
            "application": "ADP-Client",
        "message":"Comunicação com o servidor ultrapassou 20 segundos",
        "type": "Info"
        })
    elif destino == 2:
        messages.append({
            "application": "ADP-Client",
        "message":"Comunicação com o servidor ultrapassou 20 segundos",
        "type": "Info"
        })


for msg in messages:
    channel.basic_publish(
        exchange='logs',routing_key='',body=msg
    )

    print(f"Enviado: {msg}")
    time.sleep(1)
connection.close()