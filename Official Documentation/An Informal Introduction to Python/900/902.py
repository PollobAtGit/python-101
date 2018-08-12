class Mapping:

    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        self.items_list = [x for x in iterable]

    # avoids breaking base class if derived class overrides the method 'update'
    __update = update

m = Mapping([1, 2, 3])

print(m.items_list)
m.update([5, 6])

print(m.items_list)

class MappingSubClass(Mapping):
    def update(self, iterable_one, iterable_two):
        self.items_list = [x for x in zip(iterable_one, iterable_two)]

ms = MappingSubClass([])

class Employee:
    pass

e = Employee()
e.n_id_card = "0123"

print(e.n_id_card)

it = iter([5, 6, 10])

print(next(it))
print(next(it))
print(next(it))


class ReversedString:

    def __init__(self, iterable):
        self._iterable_sequence = iterable

    def __iter__(self):
        return iter(self._iterable_sequence)


rstr = ReversedString([5, 6, 9])

print()

for x in rstr:
    print(x)

