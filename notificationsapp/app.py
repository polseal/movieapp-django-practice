import json
import os
from flask import Flask, jsonify # type: ignore
from dotenv import load_dotenv
from flask_mail import Mail, Message
import pika
import threading

load_dotenv()
app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = os.environ.get('USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('PASSWORD')
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)

def callbackFunction(ch,method,properties,body):
    try:
        message = json.loads(body)
        print("JSON decoded")
        title = message.get('title')
        action = message.get('action')
        print(f"Movie was {action}: {title}")
        with app.app_context():
            msg = Message('Movie Notification', sender=os.getenv("USERNAME"), recipients=[os.getenv("RECIPIENT")])
            msg.body = f"Movie was {action}: {title}"
            try:
                mail.send(msg)
                print("Email sent successfully")
            except Exception as e:
                print(f"Error sending email: {str(e)}")
    except json.JSONDecodeError:
            print("Error decoding JSON message")
    except Exception as e:
            print(f"An error occurred: {str(e)}")


def consume():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='rabbitmq')) #localhost if debugging locally
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
    consumer_thread = threading.Thread(target=consume)
    consumer_thread.start()
    app.run(debug=True, host='0.0.0.0', port='5000')