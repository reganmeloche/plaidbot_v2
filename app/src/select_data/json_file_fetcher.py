from app.lib.select_data.json_extractor import IExtractJson
from app.lib.shared.file_reader import IReadFiles

class IFetchJsonFiles:
    def fetch(self, chosen_folders: list[str]):
        raise NotImplementedError()

class JsonFileFetcher(IFetchJsonFiles):
    def __init__(
        self,
        json_extractor: IExtractJson,
        file_reader: IReadFiles
    ):
        self.__file_reader = file_reader
        self.__json_extractor = json_extractor

    def fetch(self, chosen_folders: list[str]):
        json_files = []
        all_folders = self.__file_reader.get_all_files('')

        # Get json files
        for cf in chosen_folders:
            if cf in all_folders:
                next_files = self.__json_extractor.extract_json(cf)
                json_files.extend(next_files)

        return json_files