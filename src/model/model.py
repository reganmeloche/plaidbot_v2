from typing import List
from sklearn.model_selection import train_test_split
from transformers import PreTrainedModel
from src.options.model_options import ModelOptions
from src.classes.message import InputMessage
from src.model.batch_creator import ICreateBertBatches, BatchCreator
from src.model.inner_model import IInnerModel, InnerModel
from src.model.optimizer_builder import OptimizerBuilder

class IModel:
    def fit(self, X: List[InputMessage], y: List[int]):
        raise NotImplementedError()

    def predict(self, X: List[InputMessage]) -> List[int]:
        raise NotImplementedError()

    def get_inner_model(self) -> IInnerModel:
        raise NotImplementedError()


class Model(IModel):
    def __init__(
        self, 
        batch_creator: ICreateBertBatches,
        inner_model: IInnerModel,
        options: ModelOptions
    ):
        self.__batch_creator = batch_creator
        self.__inner_model = inner_model
        self.__opts = options

    def fit(self, X: List[InputMessage], y: List[int]):
        X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=self.__opts.val_size, stratify=y)
        
        train_loader = self.__batch_creator.create(X_train, y_train)
        val_loader = self.__batch_creator.create(X_val, y_val)

        self.__inner_model.train(train_loader, val_loader, self.__opts.num_epochs)

        return 

    def predict(self, X: List[InputMessage]) -> List[int]:
        fake_labels = [0]*len(X)
        pred_loader = self.__batch_creator.create(X, fake_labels)
        
        predictions, _, _ = self.__inner_model.predict(pred_loader)        

        return predictions

    def get_inner_model(self):
        return self.__inner_model
    
    @staticmethod
    def build(base_model: PreTrainedModel, options: ModelOptions) -> IModel:
        optimizer = OptimizerBuilder.build(base_model, options.learning_rate)
        batch_creator = BatchCreator(options.batch_size)
        inner_model = InnerModel(base_model, options.device, optimizer)
        return Model(batch_creator, inner_model, options)