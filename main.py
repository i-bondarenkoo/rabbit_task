from broker import broker
import json

message = {
    "type": "json",
    "headers": ["Заголовок 1", "Заголовок 2", "Заголовок 3"],
    "data": [
        [1, "a", True],
        [2, "b", False],
        [3, "c", True],
    ],
}


def main():
    # соединение
    broker.connect()
    broker.declare_queue(queue_name="testing_report")

    print("Пробуем отправить сообщения")
    formats = ["json", "xml", "csv", "excel"]

    for i in formats:
        # Обновляем тип отчета
        message["type"] = i
        broker.send_message("report_queue", json.dumps(message))

    print("Пробуем получить сообщения")
    broker.receive_message(queue_name="report_queue")


if __name__ == "__main__":
    main()
