from app.classes.user import User
from app.src.shared.file_reader import IReadFiles

class IFetchUsers:
    def fetch(self, user_file:str = 'users.json') -> list[User]:
        raise NotImplementedError()

class UserFetcher(IFetchUsers):
    def __init__(
        self, 
        file_reader: IReadFiles
    ):
        self.__file_reader = file_reader
    
    def fetch(self, user_file:str = 'users.json') -> list[User]:
        results = []
        users_json = self.__file_reader.read_file(user_file)
        for raw_user in users_json:
            if 'real_name' in raw_user:
                next_user = User(
                    raw_user['id'],
                    raw_user['real_name'],
                    raw_user['real_name']
                )
                results.append(next_user)

        return results