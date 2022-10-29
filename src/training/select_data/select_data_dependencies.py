from src.options.prepro_options import PreproOptions
from src.shared.printer import ConsolePrinter, IPrintMessages
from src.training.select_data.json_extractor import JsonExtractor
from src.training.select_data.json_file_fetcher import JsonFileFetcher
from src.training.select_data.message_fetcher import IFetchMessages, MessageFetcher
from src.training.select_data.message_filterer import IFilterMessages, MessageFilterer
from src.training.select_data.message_validator import MessageValidator
from src.training.select_data.raw_message_extractor import RawMessageExtractor
from src.training.select_data.select_data_printer import IPrintDataSelection, SelectDataPrinter
from src.shared.file_reader import FileReader


class SelectDataDependencies:
    message_fetcher: IFetchMessages
    message_filterer: IFilterMessages
    data_printer: IPrintDataSelection

    def __init__(self, options : PreproOptions):
        file_reader = FileReader(options.message_folder)
        json_extractor = JsonExtractor(file_reader)
        json_file_fetcher = JsonFileFetcher(json_extractor, file_reader)
        message_validator = MessageValidator()
        raw_message_extractor = RawMessageExtractor(message_validator)
        printer = ConsolePrinter()
        
        self.message_fetcher = MessageFetcher(json_file_fetcher, raw_message_extractor)
        self.message_filterer = MessageFilterer()
    
        self.data_printer = SelectDataPrinter(printer)
    