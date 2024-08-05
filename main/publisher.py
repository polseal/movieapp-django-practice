import json
import pika

def publish_message(exchange, routing_key, message_body):
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq')) #localhost if debugging locally
    channel = connection.channel()
    
    channel.exchange_declare(exchange=exchange, exchange_type='direct')

    channel.basic_publish(
        exchange=exchange,
        routing_key=routing_key,
        body=json.dumps(message_body),
        properties=pika.BasicProperties(
            delivery_mode=2  
        )
    )