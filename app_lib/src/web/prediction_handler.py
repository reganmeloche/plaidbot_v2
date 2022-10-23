import random
from app_lib.src.train.user_predictor import IPredictUser

class IHandlePredictionRequests:
    def handle(self, text: str):
        raise NotImplementedError()

class PredictionRequestHandler(IHandlePredictionRequests):
    def __init__(self, predictor: IPredictUser):
        self.__predictor = predictor
    
    def handle(self, text: str):
        pred_text = self._pick_pred_text()
        answer = self.__predictor.predict(text)
        result_text = pred_text.replace('X', answer)
        result = {
            'response_type': 'in_channel',
            'text': result_text
        }
        return result
    
    def _pick_pred_text(self) -> str:
        pred_list = [
            'Hmmm... seems like something X would say',
            'That\'s gotta be X',
            'Almost certainly X',
            'I suppose that would have to be X',
            'Tough one, but I\'m gonna go with X']
        pick = random.choice(pred_list)
        return pick