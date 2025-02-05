#!/usr/bin/python3
"""
This is the ``task_03_countediterator`` module
"""


class CountedIterator:
    """
    This is the ``CounteredIterator`` class
    """

    def __init__(self, some_iterable):
        self.iterator = iter(some_iterable)
        self.counter = 0
        self.some_iterable = some_iterable

    def __next__(self):
        try:
            item = next(self.iterator)
        except StopIteration:
            raise StopIteration
        self.counter += 1
        return item

    def get_count(self):
        return self.counter
