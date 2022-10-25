from typing import List
from src.classes.message import Message
from src.model.model import Model
from src.training.train.training_dependencies import TrainingDependencies
from options.model_options import ModelOptions

def run_prediction(message_texts: List[str], options: ModelOptions):
    deps = TrainingDependencies(options, True)

    test_messages = [Message('-1', t, -1, -1) for t in message_texts]
    X, _ = deps.input_formatter.format(test_messages)

    model = Model(
        deps.batch_creator,
        deps.inner_model,
        options
    )

    preds = model.predict(X)

    results = [options.user_int_name_dict[p] for p in preds]

    return results

    

