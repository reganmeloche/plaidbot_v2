import unittest
from unittest.mock import MagicMock
from options.model_options import ModelOptions
from src.model.batch_creator import ICreateBertBatches
from src.model.inner_model import IInnerModel
from src.model.model import Model
from tests.helpers.test_messages import TestMessages

class ModelTests(unittest.TestCase):
    def setUp(self):
        self.batch_creator = ICreateBertBatches()
        fake_batch = TestMessages.data_loader()
        self.batch_creator.create = MagicMock(return_value=fake_batch)

        self.inner_model = IInnerModel()
        self.inner_model.train = MagicMock(return_value=None)
        self.inner_model.predict = MagicMock(return_value=[[1,2,3],[0],[0]])

        opts = ModelOptions()
        opts.val_size = 0.2

        self.sut = Model(self.batch_creator, self.inner_model, opts)
        

    def test_model_fit(self):
        x = [TestMessages.input_msg(10) for _ in range(10)]
        y = [0] * 10
        self.sut.fit(x,y)

        self.assertEqual(self.batch_creator.create.call_count, 2)
        self.assertEqual(self.inner_model.train.call_count, 1)

    def test_model_predict(self):
        x = [TestMessages.input_msg(10) for _ in range(10)]
        result = self.sut.predict(x)

        self.assertEqual(result, [1,2,3])
        self.assertEqual(self.batch_creator.create.call_count, 1)
        self.assertEqual(self.inner_model.predict.call_count, 1)
    
    def test_model_get_inner(self):
        res = self.sut.get_inner_model()
        self.assertEqual(type(res), IInnerModel)
  
if __name__ == '__main__':
    unittest.main()