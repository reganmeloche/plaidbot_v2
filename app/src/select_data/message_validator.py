class IValidateMessages:
    def validate(self, msg):
        raise NotImplementedError()

class MessageValidator(IValidateMessages):
    def validate(self, msg):
        return msg['type'] == 'message' and \
            msg.get('subtype') is None and \
            msg['text'] and \
            msg.get('client_msg_id') and \
            msg.get('user')
                    