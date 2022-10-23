from typing import List
from app_lib.classes.message import Message
from app_lib.src.model.model import Model
from app_lib.src.train.training_dependencies import TrainingDependencies
from app_lib.options.model_options import ModelOptions

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