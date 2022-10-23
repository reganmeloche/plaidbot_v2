from typing import List
import torch
from torch.utils.data import TensorDataset, DataLoader

from app_lib.classes.message import InputMessage

class ICreateBertBatches:
    def create(self, input_messages: List[InputMessage], labels: List[int]) -> DataLoader:
        raise NotImplementedError()

class BatchCreator(ICreateBertBatches):
    def __init__(self, batch_size=8):
        self.__batch_size = batch_size
    
    def create(self, input_messages: List[InputMessage], labels: List[int]) -> DataLoader:
        t_inputs = torch.tensor([x.input_ids for x in input_messages])
        t_masks = torch.tensor([x.mask_ids for x in input_messages])
        t_labels = torch.tensor(labels)

        t_dataset = TensorDataset(t_inputs, t_masks, t_labels)
        batches = DataLoader(t_dataset, shuffle=True, batch_size=self.__batch_size)
        
        return batches
    
