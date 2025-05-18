import json
from report import ExcelReport, CSVReport, JSONReport, XMLReport
import pika


class MessageBroker:
    def __init__(self):
        self.connection = None
        self.channel = None
        self.host = "localhost"

    def connect(self):
        if self.connection is None:
            try:
                self.connection = pika.BlockingConnection(
                    pika.ConnectionParameters(host=self.host)
                )
                self.channel = self.connection.channel()
                print(f"Соединение установлено с брокером по адресу {self.host}")
            except Exception as error:
                print(f"Произошла ошибка при подключении: {error}")

    def declare_queue(self, queue_name):
        if self.channel is None:
            return "Ошибка, соединение не установлено"
        try:
            self.channel.queue_declare(queue=queue_name, durable=True)
        except Exception as error:
            print(f"Ошибка при объявлении очереди: {error}")

    def send_message(self, routing_key, body):
        if self.channel is None:
            return "Ошибка, соединение не установлено"
        try:
            self.channel.basic_publish(
                exchange="",
                routing_key=routing_key,
                body=body,
            )
            print("[X] Сообщение отправлено")
        except Exception as error:
            print(f"Ошибка при попытке отправки сообщения: {error}")

    def receive_message(self, queue_name):
        if self.channel is None:
            print("Ошибка, соединение не установлено")
            return

        self.channel.queue_declare(queue=queue_name, durable=True)

        def callback(ch, method, properties, body):
            print(f"[X] Получаем сообщение: {body}")

            try:
                # Декодируем и парсим JSON
                message = json.loads(body.decode("utf-8"))
                report_type = message["type"]
                headers = message["headers"]
                data = message["data"]

                # Формируем путь для сохранения файла
                filename = f"C:/Users/i.bondarenko/Desktop/report.{report_type}"

                # В зависимости от типа отчета вызываем соответствующий класс
                if report_type == "excel":
                    filename = "C:/Users/i.bondarenko/Desktop/report.xlsx"
                    ExcelReport().generate(headers, data, filename)
                elif report_type == "csv":
                    filename = "C:/Users/i.bondarenko/Desktop/report.csv"
                    CSVReport().generate(headers, data, filename)
                elif report_type == "json":
                    filename = "C:/Users/i.bondarenko/Desktop/report.json"
                    JSONReport().generate(headers, data, filename)
                elif report_type == "xml":
                    filename = "C:/Users/i.bondarenko/Desktop/report.xml"
                    XMLReport().generate(headers, data, filename)
                else:
                    print(f"Неизвестный тип отчета: {report_type}")

            except Exception as e:
                print(f"Ошибка обработки сообщения: {e}")

        # Основная настройка потребителя
        self.channel.basic_consume(
            queue=queue_name,
            auto_ack=True,
            on_message_callback=callback,
        )

        print("Ожидание сообщений. Для выхода нажмите Ctrl+C")
        try:
            self.channel.start_consuming()
        except KeyboardInterrupt:
            print("Чтение сообщений завершено")

    def close_connection(self):
        if self.connection:
            print("Соединение с брокером закрывается!")
            self.connection.close()


broker = MessageBroker()
