import unittest
from unittest.mock import MagicMock
from app_lib.src.pick_users.user_fetcher import UserFetcher
from app_lib.src.select_data.json_extractor import JsonExtractor
from app_lib.src.shared.file_reader import IReadFiles

class JsonExtractorTests(unittest.TestCase):
    def setUp(self):
        file_reader = IReadFiles()
        fake_folders = [
            'folder1',
            'folder2',
            '.some_file'
        ]
        file_reader.get_all_files = MagicMock(return_value=fake_folders)

        fake_file1 = { 'test': 'a'}
        fake_file2 = { 'test': 'b'}
        file_reader.read_file = MagicMock(side_effect=[fake_file1, fake_file2])

        self.sut = JsonExtractor(file_reader)
        

    def test_json_extractor(self):
        results = self.sut.extract_json('test_folder')

        self.assertEqual(len(results), 2)
        self.assertEqual(results[0]['test'], 'a')

  
if __name__ == '__main__':
    unittest.main()