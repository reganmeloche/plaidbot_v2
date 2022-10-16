from app.classes.message import Message
from app.lib.model.model import Model
from app.lib.predict.prediction_dependencies import PredictionDependencies
from app.options.model_options import ModelOptions

def run_prediction(model: Model, message_texts: list[str], options: ModelOptions):
    deps = PredictionDependencies(options)

    test_messages = [Message('-1', t, -1, -1) for t in message_texts]
    X, _ = deps.input_formatter.format(test_messages)

    preds = model.predict(X)

    results = [options.user_int_name_dict[p] for p in preds]

    return results

    

