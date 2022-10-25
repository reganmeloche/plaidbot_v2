from typing import Tuple

class IValidateNewMessages:
    def validate(self, message: str) -> Tuple[bool, str]: 
        raise NotImplementedError()

class NewMessageValidator(IValidateNewMessages):
    def __init__(self):
        self.__min_message_len = 10
        self.__min_num_words = 3

    def validate(self, message: str) -> Tuple[bool, str]:
        # Check num chars
        if len(message) < self.__min_message_len:
            return False, 'Message is too short'

        # Check num words
        if len(message.split()) < self.__min_num_words:
            return False, 'Message is too short'

        return True, '' 
