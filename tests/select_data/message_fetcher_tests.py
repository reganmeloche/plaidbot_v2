import unittest
from unittest.mock import MagicMock
from app.classes.message import RawMessage
from app.src.select_data.message_fetcher import MessageFetcher
from app.src.select_data.json_file_fetcher import IFetchJsonFiles
from app.src.select_data.raw_message_extractor import IExtractRawMessages

class MessageFetcherTests(unittest.TestCase):
    def setUp(self):
        self.json_file_fetcher = IFetchJsonFiles()
        self.json_file_fetcher.fetch = MagicMock(return_value=None)
        self.raw_message_extractor = IExtractRawMessages()
        raw_messages = [
            RawMessage({
                'client_msg_id': 'id1',
                'text': 'this is a test',
                'ts': 12345,
                'user': 'test_user1'
            }),
            RawMessage({
                'client_msg_id': 'id2',
                'text': 'this is another test',
                'ts': 98765,
                'user': 'test_user2'
            })
        ]
        self.raw_message_extractor.extract = MagicMock(return_value=raw_messages)

        self.sut = MessageFetcher(
            self.json_file_fetcher,
            self.raw_message_extractor
        )
        

    def test_message_fetcher(self):
        chosen_folders = ['folder1', 'folder2']
        user_id_int_dict = { 'test_user1': 1 }
        results = self.sut.fetch(chosen_folders, user_id_int_dict)

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].id, 'id1')
        self.assertEqual(results[0].user_int_id, 1)

  
if __name__ == '__main__':
    unittest.main()