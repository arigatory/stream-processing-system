import json


class JsonHandler:
    def __init__(self, filename):
        self.filename = filename
        self.data = self.load()

    def load(self):
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save(self):
        with open(self.filename, "w") as file:
            json.dump(self.data, file)
