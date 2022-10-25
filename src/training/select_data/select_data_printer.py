from typing import List
import numpy as np
from src.classes.message import Message

class SelectDataPrinter:
    def print_message_summary(self, messages: List[Message]):
        md = self._get_message_data(messages)
        
        print('\nMessage Summary:')
        print(f'Num Messages: {len(messages)}')

        for x in md['labels']:
            print(f'{x["label"]}: {x["total"]} ({x["percent"]}%)')
        
        ch = md['ch']
        wd = md['wd']
        print(f'# chars: {ch["av"]} ({ch["min"]} - {ch["max"]})')
        print(f'# words: {wd["av"]} ({wd["min"]} - {wd["max"]})')
        
    def _get_message_data(self, messages: List[Message]):
        result = {}

        n = len(messages)
        labels = set([x.user_int_id for x in messages])
        for x in labels:
            t = len([m for m in messages if m.user_int_id == x])
            p = round(100 * t / n, 2)
            result[x] = {
                'total': t,
                'percent': p
            }
        
        char_ct = [len(x.text) for x in messages]
        result['ch'] = {
            'av': round(np.average(char_ct), 2),
            'min': np.min(char_ct),
            'max': np.max(char_ct)
        }

        word_ct = [len(x.text.split()) for x in messages]
        result['wd'] = {
            'av': round(np.average(word_ct), 2),
            'min': np.min(word_ct),
            'max': np.max(word_ct)
        }

        return result
