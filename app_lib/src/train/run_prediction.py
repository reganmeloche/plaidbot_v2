from typing import List
from app_lib.classes.message import Message
from app_lib.src.model.model import Model
from app_lib.src.train.training_dependencies import TrainingDependencies
from app_lib.options.model_options import ModelOptions

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

    

