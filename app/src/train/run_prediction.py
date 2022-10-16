from typing import List
from app.classes.message import Message
from app.src.model.model import Model
from app.src.train.training_dependencies import TrainingDependencies
from app.options.model_options import ModelOptions

def run_prediction(model, message_texts: List[str], options: ModelOptions):
    deps = TrainingDependencies(options, True)

    test_messages = [Message('-1', t, -1, -1) for t in message_texts]
    X, _ = deps.input_formatter.format(test_messages)

    if model is None:
        model = Model(
            deps.batch_creator,
            deps.inner_model,
            options
        )

    preds = model.predict(X)

    results = [options.user_int_name_dict[p] for p in preds]

    return results

    

