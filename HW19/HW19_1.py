class Bot:
    def __init__(self, name):
        self.name = name

    def say_name(self):
        print(self.name)

    def send_message(self, message):
        print(message)


class TelegramBot(Bot):
    def __init__(self, name):
        super().__init__(name)
        self.url = None
        self.chat_id = None

    def send_message(self, message):
        if self.url is None:
            url_str = "None"
        else:
            url_str = str(self.url)

        if self.chat_id is None:
            chat_id_str = "None"
        else:
            chat_id_str = str(self.chat_id)

        print(f"{self.name} bot says {message} to chat {chat_id_str} using {url_str}")

    def set_url(self, url):
        self.url = url

    def set_chat_id(self, chat_id):
        self.chat_id = chat_id



some_bot = Bot('Marvin')
some_bot.say_name()
some_bot.send_message("Hello")

telegram_bot = TelegramBot("TG")
telegram_bot.say_name()
telegram_bot.send_message('Hello')

telegram_bot.set_chat_id(1)
telegram_bot.send_message('Hello')
