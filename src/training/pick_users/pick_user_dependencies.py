from src.training.pick_users.user_fetcher import IFetchUsers, UserFetcher
from src.shared.file_reader import FileReader
from src.shared.printer import ConsolePrinter, IPrintMessages
from src.options.prepro_options import PreproOptions

class PickUserDependencies:
    user_fetcher: IFetchUsers
    printer: IPrintMessages

    def __init__(self, options: PreproOptions):
        file_reader = FileReader(options.message_folder)
        self.user_fetcher = UserFetcher(file_reader)
        self.printer = ConsolePrinter()

