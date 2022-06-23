import sys
import pika
def callback(channel, method, properties, body):
    print(f"Recebido: {body} **** {method.routing_key}")

connection = pika.BlockingConnection(
    pika.ConnectionParameters(
    'localhost', '49154')
    )

channel = connection.channel()


result = channel.queue_declare('', exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='topic_logs', queue=queue_name, routing_key=bk)

print("Waiting for messages...")

channel.basic_consume(
    queue=queue_name,
     auto_ack=True,
      on_message_callback=callback)

channel.start_consuming()