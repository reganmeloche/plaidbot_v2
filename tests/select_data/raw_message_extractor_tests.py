import unittest
from unittest.mock import MagicMock
from app.src.select_data.message_validator import IValidateMessages
from app.src.select_data.raw_message_extractor import RawMessageExtractor

class RawMessageExtractorTests(unittest.TestCase):
    def setUp(self):
        self.validator = IValidateMessages()
        self.validator.validate = MagicMock(return_value=True)

        self.sut = RawMessageExtractor(self.validator)
        

    def test_raw_message_extractor(self):
        json_files = [
            [
                {
                    'client_msg_id': 'id1',
                    'user': 'test_user',
                    'text': 'this is a test',
                    'ts': 123456789
                },
                {
                    'client_msg_id': 'id1',
                    'user': 'test_user',
                    'text': 'this is a test',
                    'ts': 123456789
                }
            ],
            [
                {
                    'client_msg_id': 'id1',
                    'user': 'test_user',
                    'text': 'this is a test',
                    'ts': 123456789
                }
            ]
        ]
        result = self.sut.extract(json_files)
        self.assertEqual(len(result),3)


  
if __name__ == '__main__':
    unittest.main()