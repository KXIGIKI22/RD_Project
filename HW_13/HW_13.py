import json
import os
import traceback
from datetime import datetime


FILE_NAME = "phone_book.json"
LOG_FILE_NAME = "phone_book.log"


def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    else:
        return {}


def save_data(phone_book):
    with open(FILE_NAME, "w") as f:
        json.dump(phone_book, f)


def log_exception(exception):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE_NAME, "a") as f:
        f.write(f"{timestamp} - {exception}\n")
        traceback.print_exc(file=f)


class PhoneBookException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


phone_book = load_data()

while True:
    command = input("Введіть команду (stats, add, delete <name>, list, show <name>, exit): ")

    if command == "stats":
        print("Число записів:", len(phone_book))

    elif command == "add":
        name = input("Введіть імя: ")
        number = input("Введіть номер: ")
        try:
            int(number)
        except ValueError:
            error_message = "Номер телефону має бути числом!"
            log_exception(error_message)
            raise PhoneBookException(error_message)

        if name in phone_book:
            print("Запис вже зроблено")
        else:
            phone_book[name] = number
            save_data(phone_book)
            print("Нова запись додана!")

    elif command.startswith("delete"):
        name = command.split(" ")[1]
        try:
            del phone_book[name]
        except KeyError:
            error_message = "Запис не знайдено!"
            log_exception(error_message)
            raise PhoneBookException(error_message)
        else:
            save_data(phone_book)
            print("Видалено!")

    elif command == "list":
        print("Список усіх записів:")
        for name in phone_book:
            print(name)

    elif command.startswith("show"):
        name = command.split(" ")[1]
        if name in phone_book:
            print("Імя:", name)
            print("Номер:", phone_book[name])
        else:
            error_message = "Не знайдено!"
            log_exception(error_message)
            raise PhoneBookException(error_message)

    elif command == "exit":
        save_data(phone_book)
        break

    else:
        error_message = "Інвалідна команда"
        log_exception(error_message)
        raise PhoneBookException(error_message)