from transformers import DistilBertTokenizer, DistilBertForSequenceClassification, PreTrainedModel
from app.src.model.batch_creator import BatchCreator
from app.src.model.inner_model import InnerModel

from app.src.model.input_formatter import InputFormatter
from app.src.model.input_message_getter import InputMessageGetter
from app.src.model.optimizer_builder import OptimizerBuilder
from app.src.model.tokenizer import Tokenizer
from app.options.model_options import ModelOptions


class TrainingDependencies:
    def __init__(self, options: ModelOptions):
        inner_tokenizer: DistilBertTokenizer = DistilBertTokenizer.from_pretrained(options.bert_model_name)
        
        tokenizer = Tokenizer(inner_tokenizer, options.max_len)

        input_message_getter = InputMessageGetter(options.max_len)

        self.input_formatter = InputFormatter(tokenizer, input_message_getter)

        self.batch_creator = BatchCreator(options.batch_size)

        base_model = DistilBertForSequenceClassification.from_pretrained(options.bert_model_name, num_labels=options.num_labels)
        base_model.to(options.device)
        optimizer = OptimizerBuilder.build(base_model, options.learning_rate)
        self.inner_model = InnerModel(base_model, options.device, optimizer)

