from app_lib.classes.message import InputMessage, Message
import torch
from torch.utils.data import TensorDataset, DataLoader
from sklearn.model_selection import train_test_split
from transformers import DistilBertTokenizer

from app_lib.src.model.batch_creator import BatchCreator
from app_lib.src.model.input_formatter import InputFormatter
from app_lib.src.model.input_message_getter import InputMessageGetter
from app_lib.src.model.tokenizer import Tokenizer

class TestMessages:
    @staticmethod
    def create() -> Message:
        return Message('id1', 'this is a test', 123456789, 0)
    
    @staticmethod
    def input_msg(input_len) -> InputMessage:
        input_ids = [0]*input_len
        mask_ids = [0]*input_len
        return InputMessage(input_ids, mask_ids)

    @staticmethod
    def data_loader() -> DataLoader:
        a = torch.tensor([[0],[1]])
        b = torch.tensor([[0],[1]])
        c = torch.tensor([[0],[1]])
        t_dataset = TensorDataset(a,b,c)
        return DataLoader(t_dataset, shuffle=True, batch_size=1)
    
    @staticmethod
    def full_train_data() -> DataLoader:
        # Data
        texts = [
            'I hated this movie.',
            'This TV show is funny!',
            'I had a great time last night',
            'The party was so fun and exciting.',
            'That was an extremely sad funeral.',
            'I love listening to this music!',
            'It was a beautiful and sunny day at the beach.',
            'It stormed all day so we had to stay inside',
            'I hate you and I never want to see you again',
            'The puppy is super playful and energetic',
            'I really enjoy eating ice cream with friends!'
        ]
        labels = [0,1,1,1,0,1,1,0,0,1,0]
        messages = [Message('id0', t, -1, u) for t,u in zip(texts,labels)]

        # Options
        max_len = 20
        batch_size = 2
        inner_tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')
        val_size = 0.2
        
        # Format data
        tokenizer = Tokenizer(inner_tokenizer, max_len)
        input_message_getter = InputMessageGetter(max_len)
        input_formatter = InputFormatter(tokenizer, input_message_getter)
        X, y = input_formatter.format(messages)
        X_t = X[0:10]
        y_t = y[0:10]

        # Batch it
        X_train, X_val, y_train, y_val = train_test_split(X_t, y_t, test_size=val_size, stratify=y_t)
        batch_creator = BatchCreator(batch_size)
        
        train_loader = batch_creator.create(X_train, y_train)
        val_loader = batch_creator.create(X_val, y_val)

        X_test = X[10:]
        y_test = y[10:]
        test_loader = batch_creator.create(X_test, y_test)

        return train_loader, val_loader, test_loader
