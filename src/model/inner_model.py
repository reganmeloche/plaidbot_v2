import torch
from torch.utils.data import DataLoader
from torch.optim import AdamW
from transformers import PreTrainedModel
import time
from src.shared.printer import IPrintMessages


class IInnerModel:
    def train(self, train_loader: DataLoader, val_loader: DataLoader, num_epochs):
        raise NotImplementedError()
    
    def predict(self, test_loader: DataLoader):
        raise NotImplementedError()
    
    def get_base_model(self) -> PreTrainedModel:
        raise NotImplementedError()


class InnerModel(IInnerModel):
    def __init__(
        self, 
        base_model: PreTrainedModel, 
        device: str, 
        optimizer: AdamW,
        printer: IPrintMessages
    ):
        self.__base_model = base_model
        self.__device = device
        self.__optimizer = optimizer
        self.__printer = printer
        
    def get_base_model(self):
        return self.__base_model

    def train(self, train_loader: DataLoader, val_loader: DataLoader, num_epochs):
        for i in range(num_epochs):
            self._run_training_epoch(i, train_loader, val_loader)


    def predict(self, test_loader: DataLoader):
        y_pred = []
        y_true = []
        y_logits = []

        self.__base_model.eval()

        for i, batch in enumerate(test_loader):
            _, next_preds, next_labels, next_logits = self._run_batch(i, batch, use_grad=False)
            y_pred.extend(next_preds.to('cpu').numpy())
            y_true.extend(next_labels.to('cpu').numpy())
            y_logits.extend(next_logits.to('cpu').numpy())

        return y_pred, y_true, y_logits


    def _run_training_epoch(self, epoch, train_loader, val_loader):
        self.__printer.mprint(f'\n\n --- Epoch {epoch+1}')
        start = time.time()

        # Set to train mode: Tells model to compute gradients 
        self.__base_model.train()
        train_loss, train_acc = self._run_training_step(train_loader, use_grad=True)

        # Set to eval mode
        self.__base_model.eval()
        val_loss, val_acc = self._run_training_step(val_loader, use_grad=False)

        end = time.time()

        # Display results
        hours, rem = divmod(end-start, 3600)
        minutes, seconds = divmod(rem, 60)
        self.__printer.mprint(f'Epoch {epoch+1}: train_loss: {train_loss:.4f} train_acc: {train_acc:.4f} | val_loss: {val_loss:.4f} val_acc: {val_acc:.4f}')
        self.__printer.mprint("{:0>2}:{:0>2}:{:05.2f}".format(int(hours),int(minutes),seconds))



    # Can be for either training or validation mode
    def _run_training_step(self, data_loader, use_grad):
        total_loss = 0
        total_acc  = 0

        for i, batch in enumerate(data_loader):
            next_loss, next_preds, next_labels, _ = self._run_batch(i, batch, use_grad=use_grad)
            total_loss += next_loss
            total_acc += self._get_acc(next_preds, next_labels)
        
        loss = total_loss / len(data_loader)
        acc = total_acc / len(data_loader)
        return loss, acc



    # Used for training, validation, and prediction
    def _run_batch(self, i, batch, use_grad):
        # Add batch to device
        batch = tuple(t.to(self.__device) for t in batch)

        # Unpack inputs from the dataloader
        b_inputs, b_masks, b_labels = batch

        # Clear gradients
        self.__optimizer.zero_grad()

        with torch.set_grad_enabled(use_grad):
            loss, logits = self.__base_model(b_inputs, 
                                        #token_type_ids=None, # Not needed for DistilBERT
                                        attention_mask=b_masks, 
                                        labels=b_labels).values()
        
        preds = self._logits_to_preds(logits)

        if use_grad:
            loss.backward()
            self.__optimizer.step()
        
        if i%500==0:
            self.__printer.mprint(f'...batch {i}')

        return loss.item(), preds, b_labels, logits


    def _logits_to_preds(self, logits):
        _sm = torch.log_softmax(logits, dim=1)
        _argmax = _sm.argmax(dim=1)
        return _argmax

    def _get_acc(self, y_pred, y_true):
        _comp = (y_pred == y_true)
        _sum = _comp.sum().float()
        _size = float(y_true.size(0))
        return _sum / _size