from .tombola import Tombola
import random


class BingoCage(Tombola):
    def __init__(self, items):
        self._randomizer = random.SystemRandom
        self._items = []
        self.load(items)

    def load(self, iterable):
        self._items.extend(iterable)
        self._randomizer.shuffle(self._items)

    def pick(self):
        try:
            self._items.pop()
        except IndexError:
            raise LookupError('pick from empty bingo cage')

    def __call__(self):
        self.pick()
