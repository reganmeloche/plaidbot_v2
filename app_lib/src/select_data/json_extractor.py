from app_lib.src.shared.file_reader import IReadFiles

class IExtractJson:
    def extract_json(self, folder_name):
        raise NotImplementedError()


class JsonExtractor(IExtractJson):
    def __init__(
        self, 
        file_reader: IReadFiles
    ):
        self.__file_reader = file_reader
    
    def extract_json(self, folder_name):
        files = self.__file_reader.get_all_files(folder_name)
        a_list = []

        for a_file in files:
            filepath = f'{folder_name}/{a_file}'
            if not a_file.startswith("."):
                next_file = self.__file_reader.read_file(filepath)
                a_list.append(next_file)
        
        return a_list
