from typing import List
from app.classes.message import InputMessage

class IGetInputMessages:
    def get(self, enc_text: List[int]) -> InputMessage:
        raise NotImplementedError()

class InputMessageGetter(IGetInputMessages):
    def __init__(self, max_len):
        self.__max_len = max_len
    
    def get(self, enc_text: List[int]) -> InputMessage:
        n = self.__max_len
        max_text = enc_text[0:n]
        m = len(max_text)

        next_input = [0] * n
        next_input[0:m] = max_text

        next_mask = [0] * n
        next_mask[0:m] = [1] * m

        return InputMessage(next_input, next_mask)