from transformers import BertTokenizer

class ITokenizeTexts:
    def tokenize(self, text: str):
        raise NotImplementedError()
    
class Tokenizer(ITokenizeTexts):
    def __init__(
        self, 
        inner_tokenizer: BertTokenizer, 
        max_len: int
    ):
        self.__inner_tokenizer = inner_tokenizer
        self.__max_len = max_len

    def tokenize(self, text: str):
        return self.__inner_tokenizer.encode(text, add_special_tokens=True, max_length = self.__max_len, truncation=True)