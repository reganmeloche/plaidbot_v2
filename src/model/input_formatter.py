from typing import List, Tuple
from src.classes.message import InputMessage, Message
from src.model.input_message_getter import IGetInputMessages, InputMessageGetter
from src.model.tokenizer import ITokenizeTexts, Tokenizer

from src.options.model_options import ModelOptions
from transformers import DistilBertTokenizer

class IFormatInputs:
    def format(self, messages: List[Message]) -> Tuple[List[InputMessage], List[int]]:
        raise NotImplementedError()

class InputFormatter(IFormatInputs):
    def __init__(
        self, 
        tokenizer: ITokenizeTexts,
        input_message_getter: IGetInputMessages
    ):
        self.__tokenizer = tokenizer
        self.__input_message_getter = input_message_getter
    
    def format(self, messages: List[Message]) -> Tuple[List[InputMessage], List[int]]:
        enc_texts = [self.__tokenizer.tokenize(x.text) for x in messages]
        X = [self.__input_message_getter.get(x) for x in enc_texts]
        y = [m.user_int_id for m in messages]
        return X, y
    
    @staticmethod
    def build(options: ModelOptions) -> IFormatInputs:
        inner_tokenizer: DistilBertTokenizer = DistilBertTokenizer.from_pretrained(options.bert_model_name)
        tokenizer = Tokenizer(inner_tokenizer, options.max_len)
        input_message_getter = InputMessageGetter(options.max_len)
        return InputFormatter(tokenizer, input_message_getter)
