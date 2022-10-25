from typing import Dict
from src.classes.message import Message
from src.model.input_formatter import IFormatInputs
from src.model.model import IModel
from src.training.prediction.new_message_validator import IValidateNewMessages

class IPredictUser:
    def predict(self, text:str) -> str:
        raise NotImplementedError()

class UserPredictor(IPredictUser):
    def __init__(
        self,
        input_formatter: IFormatInputs,
        model: IModel,
        user_int_name_dict: Dict[int, str],
        message_validator: IValidateNewMessages
    ):
        self.__input_formatter = input_formatter
        self.__model = model
        self.__user_int_name_dict = user_int_name_dict
        self.__message_validator = message_validator
    

    def predict(self, text: str) -> str:
        is_valid, fail_message = self.__message_validator.validate(text)
        if not is_valid:
            return fail_message

        test_message = Message('-1', text, -1, -1)
        
        X, _ = self.__input_formatter.format([test_message])
        
        preds = self.__model.predict(X)
        
        results = [self.__user_int_name_dict[p] for p in preds]
        
        return results[0]
