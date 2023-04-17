class MyCustomException(Exception):
    def __init__(self):
        super().__init__("Custom exception is occurred")

phone_book = {}

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
            print("Номер телефону має бути числом!")
            continue

        if name in phone_book:
            print("Запис вже зроблено")
        else:
            phone_book[name] = number
            print("Нова запись додана!")

    elif command.startswith("delete"):
        name = command.split(" ")[1]
        try:
            del phone_book[name]
        except KeyError:
            print("Запис не знайдено!")
        else:
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
            print("Не знайдено!")

    elif command == "exit":
        break

    else:
        raise MyCustomException()