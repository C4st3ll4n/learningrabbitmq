from itsdangerous import Serializer
import pika


def callback(channel, method, properties, body):
    print(f"Recebido: {body} **** {method.routing_key}")
    serializer = Serializer(secret_key="lio")
    payload = serializer.load_payload(body)

    payload['saved'] = True

    channel.basic_publish(
        exchange='',
        routing_key=properties.reply_to,
        properties=pika.BasicProperties(correlation_id=properties.correlation_id),
        body=serializer.dump_payload(payload)
    )

    print(f"Enviado => {}")
    channel.basic_ack(delivery_tag=method.delivery_tag)


connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        'localhost', '49154')
)

channel = connection.channel()


result = channel.queue_declare(queue='rpc')

print("Waiting for messages...")

channel.basic_consume(
    queue='rpc',
    on_message_callback=callback)

channel.start_consuming()
