from app.classes.message import InputMessage, Message
from app.src.model.input_message_getter import IGetInputMessages
from app.src.model.tokenizer import ITokenizeTexts

class IFormatInputs:
    def format(self, messages: list[Message]) -> tuple[list[InputMessage], list[int]]:
        raise NotImplementedError()

class InputFormatter(IFormatInputs):
    def __init__(
        self, 
        tokenizer: ITokenizeTexts,
        input_message_getter: IGetInputMessages
    ):
        self.__tokenizer = tokenizer
        self.__input_message_getter = input_message_getter
    
    def format(self, messages: list[Message]) -> tuple[list[InputMessage], list[int]]:
        enc_texts = [self.__tokenizer.tokenize(x.text) for x in messages]
        X = [self.__input_message_getter.get(x) for x in enc_texts]
        y = [m.user_int_id for m in messages]
        return X, y