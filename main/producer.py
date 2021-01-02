

import pika, json

params = pika.URLParameters('amqps://cyxninkm:dSBM16Ilr-6wsH8aX_4aY_PzZ3dKCml3@toad.rmq.cloudamqp.com/cyxninkm')

connection = pika.BlockingConnection(params)
channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)