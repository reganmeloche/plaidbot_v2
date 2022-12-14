from datetime import datetime
from typing import List 

class PreproOptions:
    user_filename:str = 'users.json'
    
    message_folder:str = '/content/drive/MyDrive/Colab Notebooks/plaidbot/messages'

    selected_folders: List[str] = [
        'general',
        # add more folders...
    ]

    test_size = 0.2

    user_id_int_dict = { 'U0ABCDEFG': 0, 'U0HIJKLMN': 1, 'U0PQRSTUV': 2, }

    # Filtering
    min_date: datetime  = datetime(2018,1,1)

    min_num_words: int = 3

    max_messages: int = 100000