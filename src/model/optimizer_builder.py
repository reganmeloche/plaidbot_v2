from torch.optim import AdamW
from transformers import PreTrainedModel

class OptimizerBuilder:

    @staticmethod
    def build(model: PreTrainedModel, learning_rate) -> AdamW:
        param_optimizer = list(model.named_parameters())
        no_decay = ['bias', 'gamma', 'beta']
        optimizer_grouped_parameters = [
            {'params': [p for n, p in param_optimizer if not any(nd in n for nd in no_decay)],
            'weight_decay_rate': 0.01},
            {'params': [p for n, p in param_optimizer if any(nd in n for nd in no_decay)],
            'weight_decay_rate': 0.0}
        ]

        # This variable contains all of the hyperparameter information our training loop needs
        optimizer = AdamW(optimizer_grouped_parameters, lr=learning_rate)

        return optimizer

