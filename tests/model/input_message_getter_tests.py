import unittest
from unittest.mock import MagicMock
from app_lib.src.model.input_message_getter import InputMessageGetter

class InputMessageGetterTests(unittest.TestCase):
    def setUp(self):
        self.sut = InputMessageGetter(4)
        
    def test_input_message_getter(self):
        enc_text1 = [1, 2, 3, 4, 5, 6, 7]
        result1 = self.sut.get(enc_text1)
        self.assertEqual(result1.input_ids, [1,2,3,4])
        self.assertEqual(result1.mask_ids, [1,1,1,1])

        enc_text2 = [1, 2]
        result2 = self.sut.get(enc_text2)
        self.assertEqual(result2.input_ids, [1,2,0,0])
        self.assertEqual(result2.mask_ids, [1,1,0,0])

  
if __name__ == '__main__':
    unittest.main()