from typing import List
from app.classes.message import Message
from app.src.model.model import Model
from app.src.train.training_dependencies import TrainingDependencies
from app.options.model_options import ModelOptions

def run_training(messages: List[Message], options: ModelOptions) -> Model:
    deps = TrainingDependencies(options)
    
    model = Model(
        deps.batch_creator,
        deps.inner_model,
        options
    )

    X, y = deps.input_formatter.format(messages)

    model.fit(X, y)

    return model