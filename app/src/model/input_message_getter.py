from typing import List
from app.classes.message import InputMessage

class IGetInputMessages:
    def get(self, enc_text: List[int]) -> InputMessage:
        raise NotImplementedError()

class InputMessageGetter(IGetInputMessages):
    def __init__(self, max_len):
        self.__max_len = max_len
    
    def get(self, enc_text: List[int]) -> InputMessage:
        max_text = enc_text[0 : self.__max_len]

        next_input = [0]*self.__max_len
        next_input[0:len(max_text)] = max_text

        next_mask = [0]*self.__max_len
        next_mask[0:len(max_text)] = [1]*len(max_text)

        return InputMessage(next_input, next_mask)