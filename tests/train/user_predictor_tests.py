import unittest
from unittest.mock import MagicMock
from app_lib.src.model.input_formatter import IFormatInputs
from app_lib.src.model.model import IModel
from app_lib.src.train.user_predictor import UserPredictor
from tests.helpers.test_messages import TestMessages

class UserPredictorTests(unittest.TestCase):
    def setUp(self):
        self.input_formatter = IFormatInputs()
        fake_x = [TestMessages.input_msg(10)]
        fake_y = [0]
        self.input_formatter.format = MagicMock(return_value=(fake_x, fake_y))

        self.model = IModel()
        self.model.predict = MagicMock(return_value = [2])

        self.user_int_name_dict = { 0: 'test0', 2: 'test2'}

        self.sut = UserPredictor(self.input_formatter, self.model, self.user_int_name_dict)

    def test_user_predictor(self):
        result = self.sut.predict('This is a test')
        self.assertEqual(result, 'test2')
        self.assertEqual(self.input_formatter.format.call_count, 1)
        self.assertEqual(self.model.predict.call_count, 1)

  
if __name__ == '__main__':
    unittest.main()