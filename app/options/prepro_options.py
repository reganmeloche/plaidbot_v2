from datetime import datetime 

class PreproOptions:
    user_filename:str = 'users.json'
    
    message_folder:str = 'data/target_convos'

    selected_folders: list[str] = [
        'general',
        # add more folders...
    ]

    user_id_int_dict = { 'U0ABCDEFG': 0, 'U0HIJKLMN': 1, 'U0PQRSTUV': 2, }

    # Filtering
    min_date: datetime  = datetime(2018,1,1)

    min_num_words: int = 3

    max_messages: int = 100000