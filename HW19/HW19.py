
class Bot:
    def __init__(self, name):
        self.name = name

    def say_name(self):
        print(self.name)

    def send_message(self, message):
        print(message)

bot = Bot("My homework bot")
bot.say_name()
bot.send_message("Hello word!")

