
import os
import codecs
import json
from typing import List

class IReadFiles:
    def read_file(self, filename:str):
        raise NotImplementedError()
    
    def get_all_files(self, folder:str) -> List[str]:
        raise NotImplementedError()


class FileReader(IReadFiles):
    def __init__(self, root):
        self.root = root

    def read_file(self, filename):
        filepath = f'{self.root}/{filename}'
        f = codecs.open(filepath ,"r", encoding = "utf-8", errors="ignore")
        json_data = json.loads(f.read())
        f.close()
        return json_data
    
    def get_all_files(self, folder:str) -> List[str]:
        return os.listdir(f'{self.root}/{folder}')
