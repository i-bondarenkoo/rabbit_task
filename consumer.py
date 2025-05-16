import pika


class MessageBroker:
    def __init__(self, connection, channel, host="localhost"):
        self.connection = connection
        self.channel = channel

    # соединение с брокером
    def connect(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=self.host)
        )
        self.channel = self.connection.channel()

    # создание очереди
    def declare_queue(self, queue_name):
        self.channel.queue_declare(queue=queue_name, durable=True)
