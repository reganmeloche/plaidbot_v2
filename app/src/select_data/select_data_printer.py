import random
from typing import List
import numpy as np

from app.classes.message import Message

class SelectDataPrinter:
    def __init__(self, do_print=True):
        self.__do_print = do_print
    
    def print_begin(self):
        self._print('Beginning data selection...')
    
    def print_initial_messages(self, messages: List[Message]):
        self._print('Fetched messages')
        self._print(f'Num messages: {len(messages)}')
        #random_message = random.choice(messages)
        #self._print(f'Sample message: {random_message.text}')

    def print_final_messages(self, messages: List[Message]):
        self._print('Filtered messages')
        self._print(f'Num messages: {len(messages)}')
        #self._print(f'Sample message: {random.choice(messages)}')


    def print_finished(self, df):
        self._print('Sample of Data')
        if self.__do_print:
            print(df.head())
            print('\n')

        chars = df['text'].apply(len)
        words = df['text'].apply(lambda x: len(x.split(' ')))
        dist = np.unique(df['user'], return_counts=True)
        self._print(f'Average # chars: {chars.mean()}; ({chars.min()}, {chars.max()})')
        self._print(f'Average # words: {words.mean()}; ({words.min()}, {words.max()})')
        self._print(f'Distribution: {dist}')
        self._print('Data selection complete')


    def _print(self, text):
        if self.__do_print:
            print(f'-- {text}\n')

    