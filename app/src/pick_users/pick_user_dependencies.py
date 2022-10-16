from app.src.pick_users.user_fetcher import IFetchUsers, UserFetcher
from app.src.shared.file_reader import FileReader
from app.options.prepro_options import PreproOptions

class PickUserDependencies:
    user_fetcher: IFetchUsers

    def __init__(self, options: PreproOptions):
        file_reader = FileReader(options.message_folder)
        self.user_fetcher = UserFetcher(file_reader)

