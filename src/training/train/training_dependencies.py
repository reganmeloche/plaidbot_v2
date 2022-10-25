from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
from src.model.batch_creator import BatchCreator
from src.model.inner_model import InnerModel
from src.model.input_formatter import InputFormatter
from src.model.input_message_getter import InputMessageGetter
from src.model.optimizer_builder import OptimizerBuilder
from src.model.tokenizer import Tokenizer
from options.model_options import ModelOptions


class TrainingDependencies:
    def __init__(self, options: ModelOptions, pred_toggle:bool = False):
        inner_tokenizer: DistilBertTokenizer = DistilBertTokenizer.from_pretrained(options.bert_model_name)
        
        tokenizer = Tokenizer(inner_tokenizer, options.max_len)

        input_message_getter = InputMessageGetter(options.max_len)

        self.input_formatter = InputFormatter(tokenizer, input_message_getter)

        self.batch_creator = BatchCreator(options.batch_size)

        if pred_toggle:
            base_model = DistilBertForSequenceClassification.from_pretrained(options.saved_model_name, use_auth_token=options.auth_token)
        else:
            num_labels = len(options.user_int_name_dict)
            base_model = DistilBertForSequenceClassification.from_pretrained(options.bert_model_name, num_labels=num_labels)
        
        base_model.to(options.device)
        optimizer = OptimizerBuilder.build(base_model, options.learning_rate)
        self.inner_model = InnerModel(base_model, options.device, optimizer)

