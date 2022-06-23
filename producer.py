import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', '49154'))
channel = connection.channel()

messages = ["1a","2a","a3","a4","aaaaaaaa","1a","2a","a3","a4","aaaaaaaa","1a","2a","a3","a4","aaaaaaaa","1a","2a","a3","a4","aaaaaaaa","1a","2a","a3","a4","aaaaaaaa","1a","2a","a3","a4","aaaaaaaa"]

for i in range(0,100):
    messages.append(f"a{i}")

for msg in messages:
    channel.basic_publish(
        exchange='',routing_key='hello',body=msg
    )

    print(f"Enviado: {msg}")
    time.sleep(1)
connection.close()