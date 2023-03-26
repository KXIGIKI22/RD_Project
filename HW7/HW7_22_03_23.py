phone_book = {}

def stats():
    print("Number of records:", len(phone_book))

def add(name, number):
    if name not in phone_book:
        phone_book[name] = number
        print("Record added successfully!")
    else:
        print("Record already exists")

def delete(name):
    if name in phone_book:
        del phone_book[name]
        print("Record deleted successfully!")
    else:
        print("Record not found!")

def list_records():
    print("List of all records:")
    for name in phone_book:
        print(name)

def show(name):
    if name in phone_book:
        print("Name:", name)
        print("Number:", phone_book[name])
    else:
        print("Record not found!")