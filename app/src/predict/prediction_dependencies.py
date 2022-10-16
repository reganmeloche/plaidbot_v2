from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
from app.lib.model.batch_creator import BatchCreator
from app.lib.model.inner_model import InnerModel

from app.lib.model.input_formatter import InputFormatter
from app.lib.model.input_message_getter import InputMessageGetter
from app.lib.model.optimizer_builder import OptimizerBuilder
from app.lib.model.tokenizer import Tokenizer
from app.options.model_options import ModelOptions


class PredictionDependencies:
    def __init__(self, options: ModelOptions):
        # will likely come from a saved file..?
        inner_tokenizer: DistilBertTokenizer = DistilBertTokenizer.from_pretrained(options.bert_model_name)
        
        tokenizer = Tokenizer(inner_tokenizer, options.max_len)

        input_message_getter = InputMessageGetter(options.max_len)

        self.input_formatter = InputFormatter(tokenizer, input_message_getter)


