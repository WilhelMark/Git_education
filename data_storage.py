import json

class DataStorage:
    def __init__(self, file_name):
        self.file_name = file_name

    def save_data(self, data):
        with open(self.file_name, 'w') as file:
            json.dump(data, file)

    def load_data(self):
        try:
            with open(self.file_name, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []
        return data