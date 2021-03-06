import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare('task_queue')

def callback(ch, method, properties, body):
	print(" [x] Received %r" % body)
	time.sleep(body.count(b'.'))
	print(" [x] Done")


channel.basic_consume(callback, queue='task_queue', no_ack=True)
print(" [*] Waiting for messages. To exit press ctrl+c.")

channel.start_consuming()