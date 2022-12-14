import unittest
from unittest.mock import MagicMock
from src.options.model_options import ModelOptions
from src.model.input_formatter import InputFormatter
from src.model.input_message_getter import InputMessageGetter
from src.model.tokenizer import ITokenizeTexts
from tests.helpers.test_messages import TestMessages

class InputFormatterTests(unittest.TestCase):
    def setUp(self):
        self.tokenizer = ITokenizeTexts()
        self.tokenizer.tokenize = MagicMock(return_value=[12, 0, 20, 100])

        self.input_message_getter = InputMessageGetter(4)
        fake_input_messages = [TestMessages.input_msg(10) for _ in range(10)]
        self.input_message_getter.get = MagicMock(return_value=fake_input_messages)

        self.sut = InputFormatter(self.tokenizer, self.input_message_getter)
        

    def test_user_fetcher(self):
        messages = [TestMessages.create() for _ in range(10)]
        results = self.sut.format(messages)

        self.assertEqual(len(results[0]), 10)
        self.assertEqual(len(results[1]), 10)
        self.assertEqual(results[1], [0]*10)

    @unittest.skip # Can skip when options are not loaded
    def test_input_formatter_build(self):
        opts = ModelOptions()
        result = InputFormatter.build(opts)
        self.assertEqual(type(result), InputFormatter)

  
if __name__ == '__main__':
    unittest.main()