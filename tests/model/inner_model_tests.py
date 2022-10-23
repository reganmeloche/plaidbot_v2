import unittest
from unittest.mock import MagicMock
from transformers import DistilBertForSequenceClassification
from app_lib.src.model.inner_model import InnerModel
from app_lib.src.model.optimizer_builder import OptimizerBuilder
from tests.helpers.test_messages import TestMessages

class InnerModelTests(unittest.TestCase):
    def setUp(self):
        self.base_model = DistilBertForSequenceClassification.from_pretrained('distilbert-base-uncased', num_labels=2)
        device = 'cpu'
        optimizer = OptimizerBuilder.build(self.base_model, 2e-5)
        self.sut = InnerModel(self.base_model, device, optimizer)
        

    def test_inner_model_train(self):
        train_loader, val_loader, test_loader = TestMessages.full_train_data()
        self.sut.train(train_loader, val_loader, 2)

        result, _, _ = self.sut.predict(test_loader)
        self.assertEqual(result[0], 1)

    def test_inner_model_base(self):
        result = self.sut.get_base_model()
        self.assertEqual(type(result), DistilBertForSequenceClassification)
  
if __name__ == '__main__':
    unittest.main()