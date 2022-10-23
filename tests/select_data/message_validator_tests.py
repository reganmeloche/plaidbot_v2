from datetime import datetime
import unittest
from unittest.mock import MagicMock
from app_lib.classes.message import Message
from app_lib.options.prepro_options import PreproOptions
from app_lib.src.select_data.message_validator import MessageValidator

class MessageValidatorTests(unittest.TestCase):
    def setUp(self):
        self.sut = MessageValidator()
        

    def test_message_validator(self):
        json_msg1 = {
            'type': 'message',
            'client_msg_id': 'id1',
            'user': 'test_user',
            'text': 'test text',
        }
        json_msg2 = {
            'type': 'fail',
            'client_msg_id': 'id1',
            'user': 'test_user',
            'text': 'test text',
        }
        
        res1 = self.sut.validate(json_msg1)
        self.assertTrue(res1)

        res2 = self.sut.validate(json_msg2)
        self.assertFalse(res2)


  
if __name__ == '__main__':
    unittest.main()