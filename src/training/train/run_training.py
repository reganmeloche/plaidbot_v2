from typing import List
from src.classes.message import Message
from src.model.model import Model
from src.training.train.training_dependencies import TrainingDependencies
from options.model_options import ModelOptions

def run_training(messages: List[Message], options: ModelOptions) -> Model:
    deps = TrainingDependencies(options, False)
    
    model = Model(
        deps.batch_creator,
        deps.inner_model,
        options
    )

    X, y = deps.input_formatter.format(messages)

    model.fit(X, y)

    return model