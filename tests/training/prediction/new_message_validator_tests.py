import unittest
from unittest.mock import MagicMock
from src.training.prediction.new_message_validator import NewMessageValidator

class NewMessageValidatorTests(unittest.TestCase):
    def setUp(self):
        self.sut = NewMessageValidator()

    def test_validation(self):
        val, msg = self.sut.validate('This is a test')
        self.assertTrue(val)

        val2, msg = self.sut.validate('too short')
        self.assertFalse(val2)

        val3, msg = self.sut.validate('toooooo shooooort')
        self.assertFalse(val3)


  
if __name__ == '__main__':
    unittest.main()