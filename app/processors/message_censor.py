import re
from app.utils.json_handler import JsonHandler


class MessageCensor:
    def __init__(self):
        self.banned_words = JsonHandler("banned_words.json")
        if not isinstance(self.banned_words.data, list):
            self.banned_words.data = []

    def censor_message(self, message):
        censored_message = message
        for word in self.banned_words.data:
            pattern = re.compile(re.escape(word), re.IGNORECASE)
            censored_message = pattern.sub("*" * len(word), censored_message)
        return censored_message

    def update_banned_words(self, new_words):
        self.banned_words.data += new_words
        self.banned_words.save()
