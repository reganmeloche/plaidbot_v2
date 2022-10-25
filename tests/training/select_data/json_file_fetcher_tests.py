import unittest
from unittest.mock import MagicMock
from src.training.select_data.json_extractor import IExtractJson
from src.training.select_data.json_file_fetcher import JsonFileFetcher
from src.shared.file_reader import IReadFiles

class JsonFileFetcherTests(unittest.TestCase):
    def setUp(self):
        file_reader = IReadFiles()
        fake_folders = [
            'folder1',
            'folder2',
            'bad_folder'
        ]
        file_reader.get_all_files = MagicMock(return_value=fake_folders)

        self.json_extractor = IExtractJson()
        fake_results = ['a', 'b']
        self.json_extractor.extract_json = MagicMock(side_effect=fake_results)

        self.sut = JsonFileFetcher(self.json_extractor, file_reader)
        

    def test_json_extractor(self):
        chosen_folders = ['folder1', 'folder2', 'not_there']
        results = self.sut.fetch(chosen_folders)

        self.assertEqual(len(results), 2)
        self.assertEqual(self.json_extractor.extract_json.call_count, 2)
        self.assertEqual(results[0], 'a')

  
if __name__ == '__main__':
    unittest.main()