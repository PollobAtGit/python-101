import collections

# defining a class as tuple/dto type
# rank and suit are defined in __init__ so during construction they are required
# apparently, __str__ has been defined automatically
Card = collections.namedtuple('Card', ['rank', 'suit'])

print(Card)
print(Card(rank=1, suit=2))

class FrenchDeck:

    ranks = [str(x) for x in range(2, 11)] + list('JQKA')
    spades = "spades diamonds clubs hearts".split()

    def __init__(self):
        super(FrenchDeck, self).__init__()
        self._cards = [Card(rank = x, suit = y) for x in self.ranks for y in self.spades]

    def __len__(self):
        return len(self._cards)

    def __iter__(self):
        return iter(self._cards)

    # __getitem__ is enough for slicing but boundary condition check in that case can't be imposed
    def __getitem__(self, position):
        return self._cards[position]

    # todo: enable slicing

fd = FrenchDeck()

print([x for x in fd][:5])
print(fd[30])
# print(fd[80])
print(fd[-52])
print(len(fd))
print(fd[:3])

from random import choice

# random.choice works for __getitem__
print(choice(fd))

# in works here because FrenchDeck is iterable
print(Card('0', '0') in fd)
print(choice(fd) in fd)# True

# sorted/random.choice all works because we had implemented __len__ and __getitem__
print(sorted(fd, reverse = True))

