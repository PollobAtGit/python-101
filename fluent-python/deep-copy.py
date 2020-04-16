from copy import deepcopy, copy

class Bus():

    def __init__(self, passengers):
        if not passengers:
            self._passengers = []
        else:
            self._passengers = list(passengers)

    @property
    def passengers(self):
        return self._passengers

    def pick(self, passenger):
        if passenger is not None:
            self._passengers.append(passenger)

    def drop(self, passenger):
        if passenger is not None:
            self._passengers.remove(passenger)

    def __repr__(self):
        return "\n".join([ f"Passenger # {i + 1}: {p}" for i, p in enumerate(self.passengers)])

def copy_with_cyclic_reference():
    a = [1, 3]
    b = [a, 10]
    a.append(b)

    q = list(a)
    r = deepcopy(a)

    # print(a, q)

    # this will create issue in copied list as that's a shallow copy
    a.append('word')

    print(a, q)
    print(a, r)

def bus_operation_coordination():
    b = Bus(['Alice', 'Bob'])
    
    b.pick('charles')
    b.pick('osborn')

    print(b)

    n_b = deepcopy(b)
    nn_b = copy(b)

    b.drop('osborn')

    print(('+' * 10) + ' b ' + ('+' * 10))
    print(b)
    
    print(('+' * 10) + ' n_b ' + ('+' * 10))
    print(n_b)

    print(('+' * 10) + ' nn_b ' + ('+' * 10))
    print(nn_b)

bus_operation_coordination()
copy_with_cyclic_reference()

