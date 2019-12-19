class Error():
    def __init__(self):
        self.list = []

    def add_error(self, error_text):
        self.list.append(error_text)

    def get_list_of_errors(self):
        return self.list
    
    def delete_errors(self):
        self.list.clear()

