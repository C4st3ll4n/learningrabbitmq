import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', '49154'))
channel = connection.channel()

messages = {
    ""
}

for i in range(0,100):
    messages.append(f"a{i}")
    messages.append(f"b{i}")
    messages.append(f"c{i}")
messages.append("FIM")

for msg in messages:
    channel.basic_publish(
        exchange='logs',routing_key='',body=msg
    )

    print(f"Enviado: {msg}")
    time.sleep(1)
connection.close()