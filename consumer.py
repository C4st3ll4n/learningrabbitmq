import pika
def callback(channel, method, properties, body):
    print(f"Recebido: {body}")
    channel.basic_ack(delivery_tag = method.delivery_tag)
    print("FINALIZADO !")

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', '49154'))
channel = connection.channel()
channel.queue_declare('hello')
channel.basic_consume(queue='hello', auto_ack=False, on_message_callback=callback)
print("Waiting for messages...")
channel.start_consuming()