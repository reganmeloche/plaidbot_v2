from typing import List
from sklearn.metrics import classification_report
from app_lib.classes.message import Message
from app_lib.src.model.model import Model
from app_lib.src.train.training_dependencies import TrainingDependencies
from app_lib.options.model_options import ModelOptions

def run_evaluation(model: Model, test_messages: List[Message], options: ModelOptions):
    deps = TrainingDependencies(options, True)

    X, y = deps.input_formatter.format(test_messages)

    preds = model.predict(X)

    print(classification_report(y, preds))

    return
    

