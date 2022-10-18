from datetime import datetime
import unittest
from unittest.mock import MagicMock
from app.classes.message import Message
from app.options.prepro_options import PreproOptions
from app.src.select_data.message_filterer import MessageFilterer

class MessageFiltererTests(unittest.TestCase):
    def setUp(self):
        self.sut = MessageFilterer()
        

    def test_message_filterer(self):
        messages = [
            Message('id1', 'this is a test', 1609477201, 1), # good
            Message('id2', 'too short', 1609477201, 1), # too short
            Message('id3', 'this is another test', 1609477100, 2), # too early
            Message('id4', 'this is a test', 1609477201, 1), # good
            Message('id5', 'this is a test', 1609477200, 1), # too many
        ]
        opts = PreproOptions()
        opts.max_messages = 2
        opts.min_date = datetime(2021, 1, 1, 0, 0, 0)
        opts.min_num_words = 3

        results = self.sut.filter(messages, opts)

        self.assertEqual(len(results), 2)
        ids = [x.id for x in results]
        self.assertTrue('id1' in ids)
        self.assertTrue('id4' in ids)

  
if __name__ == '__main__':
    unittest.main()