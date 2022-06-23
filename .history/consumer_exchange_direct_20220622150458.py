import pika
def callback(channel, method, properties, body):
    print(f"Recebido: {body} **** ")

connection = pika.BlockingConnection(
    pika.ConnectionParameters(
    'localhost', '49154')
    )

channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='direct')

result = channel.queue_declare('', exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='logs', queue=queue_name)

print("Waiting for messages...")

channel.basic_consume(
    queue=queue_name,
     auto_ack=True,
      on_message_callback=callback)

channel.start_consuming()