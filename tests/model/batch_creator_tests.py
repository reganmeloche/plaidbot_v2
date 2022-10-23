import unittest
from unittest.mock import MagicMock
from app_lib.src.model.batch_creator import BatchCreator
from tests.helpers.test_messages import TestMessages

class BatchCreatorTests(unittest.TestCase):
    def setUp(self):
        self.batch_size = 8
        self.sut = BatchCreator(self.batch_size)
        

    def test_batch_creator(self):
        input_len = 20
        messages = []
        labels = []
        for _ in range(5):
            for j in range(3):
                next_msg = TestMessages.input_msg(input_len)
                messages.append(next_msg)
                labels.append(j)

        results = self.sut.create(messages, labels)

        exp_size = int(input_len / self.batch_size)
        self.assertEqual(len(results), exp_size)

        for x in results:
            self.assertEqual(len(x), 3)


        

  
if __name__ == '__main__':
    unittest.main()