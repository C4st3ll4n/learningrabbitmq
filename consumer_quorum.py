import sys
import pika
def callback(channel, method, properties, body):
    print(f"Recebido: {body} **** {method.routing_key}")
    channel.basic_nack(delivery_tag=method.delivery_tag, requeue=True)

connection = pika.BlockingConnection(
    pika.ConnectionParameters(
    'localhost', '49154')
    )
channel = connection.channel()

channel.exchange_declare(exchange="dlx_logs", exchange_type='topic')
result = channel.queue_declare('dlq_logs', exclusive=False)
channel.queue_bind(exchange='dlx_logs', queue='dlq_logs', routing_key="#")


channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

result = channel.queue_declare('log_quorum', exclusive=False,durable=True,
arguments={
    "x-dead-letter-exchange": "dlx_logs",
    "x-dead-letter-routing-key": "#",
    "x-queue-type":"quorum",
    "x-delivery-limit":5,
})
queue_name = result.method.queue

binding_keys = sys.argv[1:]

if not binding_keys:
    sys.stderr.write(f"Usage: {sys.argv[0]}\n")
    sys.exit(1)

for bk in binding_keys:
    channel.queue_bind(exchange='topic_logs', queue=queue_name, routing_key=bk)

print("Waiting for messages...")

channel.basic_consume(
    queue=queue_name,
     auto_ack=False,
      on_message_callback=callback)

channel.start_consuming()