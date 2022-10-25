import unittest
from unittest.mock import MagicMock
from app_lib.src.train.user_predictor import IPredictUser
from app_lib.src.web.prediction_handler import PredictionRequestHandler

class PredictionHandlerTests(unittest.TestCase):
    def setUp(self):
        self.predictor = IPredictUser()
        self.predictor.predict = MagicMock(return_value='test_user')
        self.sut = PredictionRequestHandler(self.predictor)

    def test_prediction_handler(self):
        result = self.sut.handle('This is a test')
        self.assertTrue('test_user' in result)
        self.assertEqual(self.predictor.predict.call_count, 1)
  
if __name__ == '__main__':
    unittest.main()