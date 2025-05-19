import pika
import json
from report import xml_report, csv_report, excel_report, json_report


class MessageBroker:
    # конструктор определение параметров подключения, инициализация объекта
    def __init__(self):
        self.connection = None
        self.channel = None
        self.host = "localhost"

    # подключение к брокеру сообщени rabbit mq
    def connect(self):
        if self.connection is None:
            try:
                self.connection = pika.BlockingConnection(
                    pika.ConnectionParameters(host=self.host)
                )
                self.channel = self.connection.channel()
                print(f"Соединение установлено, адрес соединения {self.host}")
            except Exception as error:
                print(f"Ошибка соединения при подключении к брокеру: {error}")

    # создание очереди для отправки сообщений
    def declare_queue(self, queue_name):
        if self.connection is None:
            print(f"Соединение с брокером не установлено")
        self.channel.queue_declare(queue=queue_name, durable=True)

    # отправка сообщений
    def send_message(self, routing_key, body):
        if self.connection is None:
            print(f"Соединение с брокером не установлено")
        try:
            self.channel.basic_publish(
                exchange="",
                routing_key=routing_key,
                body=body,
            )
            print(f" [X]  Отправка сообщения")
        except Exception as error:
            print(f"Отправка сообщения не удалась: {error}")

    # получение сообщений из очереди через обменник
    def receive_message(self, queue_name):
        if self.connection is None:
            print(f"Соединение с брокером не установлено")
        # повторно объявим очередь, если она не создалась ранее
        # если очередь все же создана, повторное создание не произойдет
        self.channel.queue_declare(queue=queue_name, durable=True)

        def callback(ch, method, properties, body):
            try:
                print(f"[X] Получение сообщения {body}")
                # декодируем body из байт в обычную строку
                message = body.decode("utf-8")
                # преобразуем строку в словарь
                message = json.loads(message)
                # в этой строке у нас данные, о типе отчета, необходимые заголовки, и полезная нагрузка
                report_type: str = message["type"]
                headers: list[str] = message["headers"]
                data: list[list] = message["data"]

                filename = f"C:/Users/i.bondarenko/Desktop/222/report.{report_type}"

                if report_type == "excel":
                    filename = f"C:/Users/i.bondarenko/Desktop/222/report.xlsx"
                    excel_report.generate(headers=headers, data=data, filename=filename)
                elif report_type == "csv":
                    filename = f"C:/Users/i.bondarenko/Desktop/222/report.csv"
                    csv_report.generate(headers=headers, data=data, filename=filename)
                elif report_type == "xml":
                    filename = f"C:/Users/i.bondarenko/Desktop/222/report.xml"
                    xml_report.generate(headers=headers, data=data, filename=filename)
                elif report_type == "json":
                    filename = f"C:/Users/i.bondarenko/Desktop/222/report.json"
                    json_report.generate(headers=headers, data=data, filename=filename)
                else:
                    print(f"Неизвестный тип отчета: {report_type}")
            except Exception as error:
                print(f"Ошибка обработки сообщения {error}")

        self.channel.basic_consume(
            queue=queue_name,
            on_message_callback=callback,
            auto_ack=True,
        )

        print(f"Ожидаем сообщения в очереди. Для выхода нажмите CTRL+C")
        try:
            self.channel.start_consuming()
        except KeyboardInterrupt:
            print("Чтение сообщений прервано")

    def close_connection(self):
        if self.connection:
            print(f"Соединение с брокером сообщений закрывается")
            self.connection.close()


broker = MessageBroker()
