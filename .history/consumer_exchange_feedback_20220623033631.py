from itsdangerous import Serializer
import pika


def callback(channel, method, properties, body):
    print(f"Recebido: {body} **** {method.routing_key}")
    serializer = Serializer(secret_key="lio")
    payload = serializer.load_payload(body)
    
    print(f"Recebido => {payload}")
    payload['saved'] = True

    channel.basic_publish(
        exchange='',
        routing_key=properties.reply_to,
        properties=pika.BasicProperties(correlation_id=properties.correlation_id),
        body=serializer.dump_payload(payload)
    )

    channel.basic_ack(delivery_tag=method.d)


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
