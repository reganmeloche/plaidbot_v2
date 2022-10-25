from options.model_options import ModelOptions
from src.prediction.user_predictor import UserPredictor
from src.web.prediction_handler import PredictionRequestHandler

class WebDependencies:
    def __init__(self, options: ModelOptions):
        predictor = UserPredictor.build(options)
        self.prediction_handler = PredictionRequestHandler(predictor)

