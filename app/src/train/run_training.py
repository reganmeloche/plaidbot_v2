from app.classes.message import Message
from app.lib.model.model import Model
from app.lib.train.training_dependencies import TrainingDependencies
from app.options.model_options import ModelOptions

def run_training(messages: list[Message], options: ModelOptions) -> Model:
    deps = TrainingDependencies(options)
    
    model = Model(
        deps.batch_creator,
        deps.inner_model,
        options
    )

    X, y = deps.input_formatter.format(messages)

    model.fit(X, y)

    return model