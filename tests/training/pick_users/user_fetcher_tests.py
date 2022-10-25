import unittest
from unittest.mock import MagicMock
from src.training.pick_users.user_fetcher import UserFetcher
from src.shared.file_reader import IReadFiles

class UserFetcherTests(unittest.TestCase):
    def setUp(self):
        file_reader = IReadFiles()
        fake_json_users = [
            {
                'real_name': 'alice',
                'id': 'id1'
            },
            {
                'real_name': 'bob',
                'id': 'id2'
            },
            {
                'id': 'id3'
            }
        ]
        file_reader.read_file = MagicMock(return_value=fake_json_users)
        self.sut = UserFetcher(file_reader)
        

    def test_user_fetcher(self):
        results = self.sut.fetch('users.json')

        self.assertEqual(len(results), 2)
        self.assertEqual(results[0].id, 'id1')

  
if __name__ == '__main__':
    unittest.main()