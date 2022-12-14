from typing import Dict, List
from src.classes.message import Message
from src.training.select_data.json_file_fetcher import IFetchJsonFiles
from src.training.select_data.raw_message_extractor import IExtractRawMessages

class IFetchMessages:
    def fetch(self, chosen_folders: List[str], user_id_int_dict:Dict[str,int]) -> List[Message]:
        raise NotImplementedError()

class MessageFetcher:
    def __init__(
        self, 
        json_file_fetcher: IFetchJsonFiles,
        raw_message_extractor : IExtractRawMessages
    ):
        self.__json_file_fetcher = json_file_fetcher
        self.__raw_message_extractor = raw_message_extractor
    
    def fetch(self, chosen_folders: List[str], user_id_int_dict:Dict[str,int]) -> List[Message]:
        json_files = self.__json_file_fetcher.fetch(chosen_folders)

        raw_messages = self.__raw_message_extractor.extract(json_files)

        return [
            Message.from_raw(m, user_id_int_dict[m.user_id]) 
            for m 
            in raw_messages 
            if m.user_id in user_id_int_dict
        ]
