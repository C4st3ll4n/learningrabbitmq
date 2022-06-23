import sys
import pika
def callback(channel, method, properties, body):
    print(f"Recebido: {body} **** {method.routing_key}")

connection = pika.BlockingConnection(
    pika.ConnectionParameters(
    'localhost', '49154')
    )

channel = connection.channel()

channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

result = channel.queue_declare('', exclusive=True)
queue_name = result.method.queue

severities = sys.argv[1:]

if not severities:
    sys.stderr.write(f"Usage: {sys.argv[0]}\n [Info] [Warning] [Error]")

channel.queue_bind(exchange='logs', queue=queue_name)

print("Waiting for messages...")

channel.basic_consume(
    queue=queue_name,
     auto_ack=True,
      on_message_callback=callback)

channel.start_consuming()