from typing import List
from sklearn.metrics import classification_report
from src.classes.message import Message
from src.model.model import Model
from src.training.train.training_dependencies import TrainingDependencies
from options.model_options import ModelOptions

def run_evaluation(model: Model, test_messages: List[Message], options: ModelOptions):
    deps = TrainingDependencies(options)

    X, y = deps.input_formatter.format(test_messages)

    preds = model.predict(X)

    print(classification_report(y, preds))

    return
    

