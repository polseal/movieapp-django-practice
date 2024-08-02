from flask import Flask, jsonify
import pika

app = Flask(__name__)

def callbackFunction(ch,method,properties,body):
    print('Got a message from Queue A: ', body)

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='rabbitmq'))
channel = connection.channel()
channel.exchange_declare(exchange='notifications', exchange_type='direct')
channel.queue_declare(queue='movies')
channel.queue_bind(exchange='notifications', queue='movies', routing_key='movies')
channel.basic_consume(queue='movies', on_message_callback=callbackFunction, auto_ack=True)
channel.start_consuming()

@app.route('/')
def home():
    return jsonify(message="Hello from Flask!")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')