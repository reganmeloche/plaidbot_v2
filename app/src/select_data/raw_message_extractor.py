from app.classes.message import RawMessage
from app.lib.select_data.message_validator import IValidateMessages

class IExtractRawMessages:
    def extract(self, json_files) -> list[RawMessage]:
        raise NotImplementedError()

class RawMessageExtractor:
    def __init__(self, validator: IValidateMessages):
        self.__validator = validator

    def extract(self, json_files) -> list[RawMessage]:
        results = []
        for json_file in json_files:
            for msg in json_file:
                if self.__validator.validate(msg):
                    next_message = RawMessage(msg)
                    results.append(next_message)
        return results
    