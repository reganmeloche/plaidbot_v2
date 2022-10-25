import unittest
from unittest.mock import MagicMock
from options.model_options import ModelOptions
from src.model.input_formatter import IFormatInputs
from src.model.model import IModel
from src.training.prediction.new_message_validator import IValidateNewMessages
from src.training.prediction.user_predictor import UserPredictor
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

        self.message_validator = IValidateNewMessages()
        fake_validation = [(True,''), (False, 'failed'), (False, 'failed')]
        self.message_validator.validate = MagicMock(side_effect=fake_validation)

        self.sut = UserPredictor(self.input_formatter, self.model, self.user_int_name_dict, self.message_validator)

    def test_user_predictor(self):
        result = self.sut.predict('This is a test')
        self.assertEqual(result, 'test2')
    
        result = self.sut.predict('too short')
        self.assertEqual(result, 'failed')
    
        result = self.sut.predict('also too short')
        self.assertEqual(result, 'failed')
    
    @unittest.skip # Can skip when options are not loaded
    def test_user_predictor_build(self):
        opts = ModelOptions()
        result = UserPredictor.build(opts)
        self.assertEqual(type(result), UserPredictor)

  
if __name__ == '__main__':
    unittest.main()