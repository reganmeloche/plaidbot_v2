class RawMessage:
    def __init__(self, json_msg):
        self.id = json_msg['client_msg_id']
        self.text = json_msg['text']
        self.ts = json_msg['ts']
        self.user_id = json_msg['user']
    
class Message:
    def __init__(self, id, text, ts, user_int_id):
        self.id = id
        self.text = text
        self.ts = ts
        self.user_int_id = user_int_id
    
    @staticmethod
    def from_raw(raw_message: RawMessage, user_int_id: int):
        return Message(
            raw_message.id,
            raw_message.text,
            raw_message.ts,
            user_int_id
        )


class InputMessage:
    def __init__(self, input_ids: list[int], mask_ids: list[int]):
        self.input_ids = input_ids
        self.mask_ids = mask_ids