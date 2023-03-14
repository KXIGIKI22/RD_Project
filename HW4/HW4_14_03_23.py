#Завдання 1-3
text = input("Type your text: \n ")

if text.isdigit():
    number = int(text)
    if number % 2 == 0:
        print("The entered number is even. \n")
    else:
        print("The entered number is odd. \n")
elif text.isalpha():
    length = len(text)
    print(f"Lenght of your word: {length} \n")
else:
    print("Your text is not word or number. \n")

#Завдання 4
while True:
    user_input = input("Type your text: ")
    match user_input:
        case '':
            print("Its empyt, try again.\n")
        case input_str if input_str.isdigit():
            print("You write number. \n")
            break
        case input_str if input_str.isalpha:
            print("Your write a text. \n")
            break


