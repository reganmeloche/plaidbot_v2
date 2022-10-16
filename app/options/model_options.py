class ModelOptions:
    max_len:int = 150
    bert_model_name:str = 'distilbert-base-uncased'
    val_size = 0.2
    num_epochs = 2
    batch_size = 8
    device = 'cpu' #cuda:0
    learning_rate = 2e-5
    
    user_int_name_dict = { 0: 'alice', 1: 'bob', 2: 'charlie', }
    user_int_name_dict = {0: 'ruhanga', 1: 'Ardan Burton', 2: 'Matthieu Belanger', 3: 'Bert', 4: 'ChubThumper'}
    num_labels = 5 # Get rid of this... make it dynamic..
