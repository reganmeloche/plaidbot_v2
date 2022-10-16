class ModelOptions:
    max_len:int = 150
    bert_model_name:str = 'distilbert-base-uncased'
    val_size = 0.2
    num_epochs = 2
    batch_size = 8
    device = 'cuda:0' #cpu
    learning_rate = 2e-5
    
    saved_model_name = 'username/model-name'
    auth_token = 'auth-token-goes-here'
    user_int_name_dict = { 0: 'alice', 1: 'bob', 2: 'charlie', }
    num_labels = 5 # Get rid of this... make it dynamic..
