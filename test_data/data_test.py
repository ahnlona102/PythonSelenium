import json
class TestDataLoader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self.load_test_data()

    def load_test_data(self):
        with open(self.file_path, 'r') as file:
            data = json.load(file)
        return data

    def get_test_case(self, test_case_name):
        return self.data.get(test_case_name)