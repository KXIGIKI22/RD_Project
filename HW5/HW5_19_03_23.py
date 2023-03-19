#Завдання 1
text = input("Type your text: ")

for char in text:
    if char.isdigit():
        if int(char) % 2 == 0:
            print(f'its number {char} - even')
        else:
            print(f'its number {char} - Odd')
    elif char.isalpha():
        if char.isupper():
            print(f'its word {char} - Large')
        else:
            print(f'its word {char} - SmalL')
    else:
        print('its symbol', char)

#Завдання 2
import time

while True:
    print("I love Python")
    time.sleep(4.2)