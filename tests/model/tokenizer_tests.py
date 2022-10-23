import unittest
from unittest.mock import MagicMock
from app_lib.src.model.tokenizer import Tokenizer
from transformers import DistilBertTokenizer

class TokenizerTests(unittest.TestCase):
    def setUp(self):
        self.inner_tokenizer = DistilBertTokenizer.from_pretrained('hf-internal-testing/tiny-bert')
        self.sut = Tokenizer(self.inner_tokenizer, 13)
        
    #@unittest.skip # Can often skip due to needing to load tokenizer
    def test_tokenizer(self):
        text = 'This is a test.'
        result = self.sut.tokenize(text)
        self.assertEqual(result[0], 101)
        self.assertEqual(result[-1], 102)
        self.assertEqual(len(result), 7)

        text = 'This is a test. That is all that this test is.'
        result = self.sut.tokenize(text)
        self.assertEqual(result[0], 101)
        self.assertEqual(result[-1], 102)
        self.assertEqual(len(result), 13)

  
if __name__ == '__main__':
    unittest.main()