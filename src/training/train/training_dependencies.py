from transformers import DistilBertForSequenceClassification
from src.model.batch_creator import BatchCreator, ICreateBertBatches
from src.model.inner_model import IInnerModel, InnerModel
from src.model.input_formatter import IFormatInputs, InputFormatter
from src.model.optimizer_builder import OptimizerBuilder
from src.options.model_options import ModelOptions
from src.shared.printer import ConsolePrinter

class TrainingDependencies:
    input_formatter: IFormatInputs
    batch_creator: ICreateBertBatches
    inner_model: IInnerModel
    
    def __init__(self, options: ModelOptions):
        num_labels = len(options.user_int_name_dict)
        base_model = DistilBertForSequenceClassification.from_pretrained(options.bert_model_name, num_labels=num_labels)
        base_model.to(options.device)
        optimizer = OptimizerBuilder.build(base_model, options.learning_rate)
        printer = ConsolePrinter()

        self.input_formatter = InputFormatter.build(options)
        self.batch_creator = BatchCreator(options.batch_size)
        self.inner_model = InnerModel(base_model, options.device, optimizer, printer)

