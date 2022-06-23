import sys
import pika
def callback(channel, method, properties, body):
    print(f"Recebido: {body} **** {method.routing_key}")

connection = pika.BlockingConnection(
    pika.ConnectionParameters(
    'localhost', '49154')
    )

channel = connection.channel()

channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

result = channel.queue_declare('', exclusive=True)
queue_name = result.method.queue

binding_keys = sys.argv[1:]

if not binding_keys:
    sys.stderr.write(f"Usage: {sys.argv[0]}\n")
    sys.exit(1)

for severity in severities:
    channel.queue_bind(exchange='topic_logs', queue=queue_name, routing_key=severity)

print("Waiting for messages...")

channel.basic_consume(
    queue=queue_name,
     auto_ack=True,
      on_message_callback=callback)

channel.start_consuming()