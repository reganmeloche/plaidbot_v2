from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
from src.model.batch_creator import BatchCreator
from src.model.inner_model import InnerModel

from src.model.input_formatter import InputFormatter
from src.model.input_message_getter import InputMessageGetter
from src.model.model import Model
from src.model.optimizer_builder import OptimizerBuilder
from src.model.tokenizer import Tokenizer
from options.model_options import ModelOptions
from src.training.prediction.new_message_validator import NewMessageValidator
from src.training.prediction.user_predictor import UserPredictor
from src.web.prediction_handler import PredictionRequestHandler

class WebDependencies:
    def __init__(self, options: ModelOptions):
        inner_tokenizer: DistilBertTokenizer = DistilBertTokenizer.from_pretrained(options.bert_model_name)
        tokenizer = Tokenizer(inner_tokenizer, options.max_len)
        input_message_getter = InputMessageGetter(options.max_len)
        input_formatter = InputFormatter(tokenizer, input_message_getter)

        batch_creator = BatchCreator(options.batch_size)
        base_model = DistilBertForSequenceClassification.from_pretrained(options.saved_model_name, use_auth_token=options.auth_token)
        base_model.to(options.device)
        optimizer = OptimizerBuilder.build(base_model, options.learning_rate)
        inner_model = InnerModel(base_model, options.device, optimizer)
        model = Model(batch_creator, inner_model, options)

        message_validator = NewMessageValidator()
        predictor = UserPredictor(input_formatter, model, options.user_int_name_dict, message_validator)
        self.prediction_handler = PredictionRequestHandler(predictor)

