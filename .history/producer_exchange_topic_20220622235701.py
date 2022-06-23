import random
from itsdangerous import JSONWebSignatureSerializer, Serializer
import pika
import time

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost', '49154'))
    
channel = connection.channel()
channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

messages = [
    {
        "application": "Store-mobile",
        "message": "Falha ao baixar app",
        "type": "Error"
    },
    {
        "application": "Store-mobile",
        "message": "Falha ao autenticar no multicanalidade",
        "type": "Warning"
    },
    {
        "application": "Store-mobile",
        "message": "Comunicação com o servidor ultrapassou 20 segundos",
        "type": "Info"
    },
]

for i in range(0, 100):
    destino = random.randint(0,2)
    log_type = random.randint(0,2)

    log = ""
    msg = ""
    app = ""

    if log_type == 0:
        log = "Info"
        msg = "User logou !"
    elif log_type == 1:
        log = "Warning"
        msg = "Comunicação com o servidor ultrapassou 20 segundos"
    elif log_type == 2:
        log = "Error"
        msg = "App crashou"

    if destino == 0:
        app = "ADP-Client"
    elif destino == 1:
        app = "Showcase"
    elif destino == 2:
        app = "Store-mobile"

    messages.append(
        {
            "application": app,
            "message": msg,
            "type": log
        }
    )

for msg in messages:
    serializer = Serializer(secret_key="lio")
    payload = serializer.dump_payload(msg)
    routing_key = f"{msg['type']}.{msg['app']}"
    channel.basic_publish(
        exchange='topic_logs',
         routing_key=msg['type'],
         body=payload
    )
    print(f"Enviado: {msg} ")
    
    time.sleep(1)
connection.close()
