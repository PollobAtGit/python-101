
def min_of_x_y(self, x, y):
    return min(x, y)

def min_of_x_y_without_self(x, y):
    return min(x, y)

class C(object):
    self_min = min_of_x_y

    # This will not work in respect to an object instance because the function doesn't
    # expect the first parameter to be an instance of an object
    min_without_self = min_of_x_y_without_self

    method_refering_to_another_method_of_the_same_class = self_min


c = C()
print(c.self_min(10, 20))
# print(c.min_without_self(10, 20))

print(c.method_refering_to_another_method_of_the_same_class(89, 9))


# by definition inheriting from Object
class Bag:
    def __init__(self):
        self.internal_sequence = []

    def add(self, x):
        self.internal_sequence.append(x)

    def add_twice(self, x):
        self.add(x)
        self.add(x)

    # arguments will be converted to a tuple
    def add_all_args(self, *args):
        self.internal_sequence = self.internal_sequence + [x for x in args]

b = Bag()
b.add(10)
b.add_twice(99)

print(b.internal_sequence)

# all arguments will be converted to a tuple
b.add_all_args(56, 93.23, 7)
print(b.internal_sequence)



"""
        Inheritance
        TODO:
            How to invoke base?
            How is instance resolution works for isinstance(...)?
            How to method overloading
"""

class Animal:

    def __init__(self):
        self._class_name = "animal"
        self._weight = 0

    def get_weight(self):
        return self._weight

    def get_class_name(self):
        return self._class_name

    def set_weight(self, weight):
        self._weight = weight

class Dog(Animal):
    pass


# WeightyAnimal doesn't have _weight property
class WeightyAnimal:
    def get_weight(self):
        return self._weight * 10

# When combined with Animal class we have _weight property
# To resolve multiple inheritance issue python starts searching for instance member from
# the class itself then takes the first class mentioned in inheritence order if not found
# there then goes to the next inheritance class mentioned in order

class Cat(WeightyAnimal, Animal):
    def get_class_name(self):
        raise TypeError()


d = Dog()
d.set_weight(59)
print(d.get_weight())# 0
print(d.get_class_name())

c = Cat()

def try_possible_invalid_operation(func):
    try:
        return func()
    except Exception as e:
        print("invalid operation")

try_possible_invalid_operation(c.get_class_name)

c.set_weight(89)
print(try_possible_invalid_operation(c.get_weight))# 890

print(isinstance(c, Cat))# True
print(isinstance(d, Cat))# False
print(isinstance(d, Animal))# True
print(isinstance(1, object))# True
print(isinstance(True, object))
print(isinstance(True, bool))# True

print()

print(issubclass(Cat, WeightyAnimal))# True
print(issubclass(Cat, Animal))# True
print(issubclass(Dog, WeightyAnimal))# False


