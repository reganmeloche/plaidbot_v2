
from app.options.prepro_options import PreproOptions
from app.src.select_data.json_extractor import JsonExtractor
from app.src.select_data.json_file_fetcher import JsonFileFetcher
from app.src.select_data.message_fetcher import MessageFetcher
from app.src.select_data.message_filterer import MessageFilterer
from app.src.select_data.message_validator import MessageValidator
from app.src.select_data.raw_message_extractor import RawMessageExtractor
from app.src.select_data.select_data_printer import SelectDataPrinter
from app.src.shared.file_reader import FileReader


class SelectDataDependencies:
    def __init__(self, options : PreproOptions):
        file_reader = FileReader(options.message_folder)
        json_extractor = JsonExtractor(file_reader)
        json_file_fetcher = JsonFileFetcher(json_extractor, file_reader)
        message_validator = MessageValidator()
        raw_message_extractor = RawMessageExtractor(message_validator)
        
        self.message_fetcher = MessageFetcher(json_file_fetcher, raw_message_extractor)
        self.message_filterer = MessageFilterer()
        #self.printer = SelectDataPrinter()
    