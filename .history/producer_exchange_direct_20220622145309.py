from random import Random
import pika
import time

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost', '49154'))
channel = connection.channel()

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
    destino = Random.randint(a:0b:2)
    log_type = Random.randint(2)

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
    channel.basic_publish(
        exchange='direct_logs',
         routing_key=msg['type'],
         body=msg
    )

    print(f"Enviado: {msg}")
    time.sleep(1)
connection.close()
