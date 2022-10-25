from typing import List
import numpy as np
from src.classes.message import Message
from src.shared.printer import IPrintMessages

class IPrintDataSelection:
    def print_message_summary(self, messages: List[Message]):
        raise NotImplementedError()
    


class SelectDataPrinter(IPrintDataSelection):
    def __init__(self, printer: IPrintMessages):
        self.__printer = printer

    def print_message_summary(self, messages: List[Message]):
        md = self._get_message_data(messages)
        
        self.__printer.mprint('\nMessage Summary:')
        self.__printer.mprint(f'Num Messages: {len(messages)}')

        for x in md['labels']:
            self.__printer.mprint(f'{x["label"]}: {x["total"]} ({x["percent"]}%)')
        
        ch = md['ch']
        wd = md['wd']
        self.__printer.mprint(f'# chars: {ch["av"]} ({ch["min"]} - {ch["max"]})')
        self.__printer.mprint(f'# words: {wd["av"]} ({wd["min"]} - {wd["max"]})')
        
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
