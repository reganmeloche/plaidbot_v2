from datetime import datetime
import copy
import random
from typing import List

from app_lib.classes.message import Message
from app_lib.options.prepro_options import PreproOptions

class IFilterMessages:
    def filter(self, messages: List[Message], opts: PreproOptions):
        raise NotImplementedError()

class MessageFilterer(IFilterMessages):
    def filter(self, messages: List[Message], opts: PreproOptions):
        f_messages = copy.deepcopy(messages)

        # Filter by date
        timestamp = datetime.timestamp(opts.min_date)
        f_messages = [m for m in f_messages if float(m.ts) > timestamp]

        # Filter by num words
        f_messages = [m for m in f_messages if len(str(m.text).split(' ')) >= opts.min_num_words]

        # Take a max
        if opts.max_messages > 0 :
            f_messages.sort(key=lambda x: x.ts, reverse=True)
            f_messages = f_messages[0 : opts.max_messages]
        
        random.shuffle(f_messages)

        return f_messages