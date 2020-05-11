
import copy

class GoodBus():

    def __init__(self, passengers):
        self._passengers = copy.deepcopy(passengers) if passengers else []

    def pick(self, p):
        if p:
            self._passenger.append(p)

    def drop(self, p):
        if p:
            self._passengers.remove(p)

    def __repr__(self):
        return " ".join(map(str, self._passengers))

class HauntedBus():

    # default list will be shared between multiple instances of HauntedBus
    def __init__(self, passengers = []):
        self._passengers = passengers

    def pick(self, passenger):
        self._passengers.append(passenger)

    def drop(self, passenger):
        self._passengers.remove(passenger)

    def __repr__(self):
        return " ".join(map(str, self._passengers))

def issue_with_default_function_argument():
    b = HauntedBus(['charles'])
    b.pick('osborn')

    print(b)

    c = HauntedBus()
    c.pick('charles')
    
    q = HauntedBus()
    q.pick('james')
    
    print(c, q)
    
    print(dir(HauntedBus.__init__))

    # following shows __defaults__ has empty list already populated
    print(HauntedBus.__init__.__defaults__)

    # both objects share the same underlying list
    print(HauntedBus.__init__.__defaults__[0] is c._passengers, HauntedBus.__init__.__defaults__[0] is q._passengers) 

def check_modifying_list():
    passengers = ['charles', 'beki']
    b = HauntedBus(passengers)

    print(b)

    # this will modify 'passengers' list also
    b.drop('charles')
    b.pick('jemmy')

    print(b, passengers)

def func(a):
    a = 78
    print(a)

def f(a, b):
    a += b

def test():
    x, y = 10, 40

    # will not have any impact on original value
    f(x, y)
    
    p, q = [9, 88], [67, 76]
    
    # will modify the list as lists are mutable
    f(p, q)

    r, s = ('a', 'b'), ('t', 'y')
    
    # will not have any impact on tuple as tuples are immutable
    f(r, s) 

    print(x, y)
    print(p, q)
    print(r, s)

def test_good_bus():
    passengers = ['charles', 'johny']
    
    b = GoodBus(passengers)
    hb = HauntedBus(passengers)

    print(b)

    # this will have impact on underlying data type of Bus
    passengers.append('osborn')
    print(b, hb)

def initialize_wth_tuple():
    print(GoodBus((1, 3)))
    print(HauntedBus((1, 2)))

test()
func(6)
issue_with_default_function_argument()
check_modifying_list()
test_good_bus()
initialize_wth_tuple()

