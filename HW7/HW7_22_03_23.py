phone_book = {}
def stats():
    return len(phone_book)

def add(name, phone, email):
    phone_book[name] = {'phone': phone, 'email': email}

def delete(name):
    if name in phone_book:
        del phone_book[name]
        print('Contact is add')
    else:
        print('Contact dont find')

def list_all():
    if len(phone_book) == 0:
        print('Contactlist is empty')
    else:
        for name in phone_book:
            print(name)

def show(name):
    if name in phone_book:
        print('Nmae:', name)
        print('Phone:', phone_book[name]['phone'])
        print('Email:', phone_book[name]['email'])
    else:
        print('Contact doesnt find')

while True:
    print('Write your command: stats, add, delete, list, show, або exit')
    command = input().lower()

    if command == 'stats':
        print('List in contactbook:', stats())

    elif command == 'add':
        print('Write name of contact:')
        name = input()
        print('Write your number:')
        phone = input()
        print('Write email:')
        email = input()
        add(name, phone, email)
        print('Contact succefully add')

    elif command.startswith('delete'):
        name = command.split(' ')[1]
        delete(name)

    elif command == 'list':
        list_all()

    elif command.startswith('show'):
        name = command.split(' ')[1]
        show(name)

    elif command == 'exit':
        break

    else:
        print('Error')













