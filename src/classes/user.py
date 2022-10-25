class User:
    def __init__(self, id, name, real_name):
        self.id = id
        self.name = name
        self.real_name = real_name
    
    def to_string(self):
        return f'id: {self.id}, name: {self.name}, real_name: {self.real_name}'

