import re
from utils.json_handler import JsonHandler


class MessageCensor:
    def __init__(self):
        self.banned_words = JsonHandler("banned_words.json")

    def censor_message(self, message):
        for word in self.banned_words.data:
            message = re.sub(word, "*" * len(word), message, flags=re.IGNORECASE)
        return message

    def update_banned_words(self, new_words):
        self.banned_words.data.extend(new_words)
        self.banned_words.save()
