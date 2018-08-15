
class Animal(object):
    def legs_count(self):
        pass

# no exception
class Dog(Animal):
    pass

animal = Animal()

# no error in general
animal.legs_count()

dog = Dog()

dog.legs_count()

from abc import ABC, abstractmethod

class ElectronicsDevice(ABC):
    
    def __init__(self):
        super().__init__()

    @abstractmethod
    def required_voltage(self):
        pass

class Computer(ElectronicsDevice):
    
    def required_voltage(self):
        return 10


# can't instantiate abstract class exception
# ed = ElectronicsDevice()

computer = Computer()
print(computer.required_voltage())


# Duck Typing


class Duck:
    def can_fly(slef):
        return True

class WoodenDuck:
    def can_fly(self):
        return False

def display_duck_flying_status(duck_instance):
    
    if duck_instance:

        # there's no guarantee that following invocation will not fail

        try:
            flying_status = duck_instance.can_fly()

            if flying_status:
                print("duck can fly")
            else:
                print("duck can't fly")
        except AttributeError as e:
            print(e)

display_duck_flying_status(WoodenDuck())
display_duck_flying_status(Duck())

def is_duck(duck_instance):
    if duck_instance:
        
        # strongly linked with Duck type. Is it related to duck typing? may be not
        return isinstance(duck_instance, Duck)

print(is_duck(WoodenDuck()))
print(is_duck(Duck()))


def display_duck_flying_status_non_pythonic_way(duck_instance):
    
    if duck_instance:

        # checking for an attribute
        if hasattr(duck_instance, 'can_fly'):

            # checking if an attribute is callable meaning a method
            if callable(duck_instance.can_fly):
                flying_status = duck_instance.can_fly()
                if flying_status:
                    print("the duck can fly")
                else:
                    print("duck can't fly")


display_duck_flying_status_non_pythonic_way(Duck())# True

class A:
    pass

# will throw exception
# 'or' can handle exception in which case ''A' object has no attribute 'can_fly''
display_duck_flying_status(A())


person_dto = {'name':'x','age':10,'location':'tyu'}

# non-pythonic approach
def person_str(person):
    if person:
        if 'name' in person and 'age' in person and 'location' in person:
            return "i am {name}, aged {age}, lives in {location}".format(**person)

def person_str_pythonic(person):
    if person:
        try:
            return "i am {name}, aged {age} and currently lives at {location}".format(**person)
        # except AttributeError as e:
        
        # KeyError is relevant for dictionary & AttributeError is relavent for instance
        except KeyError as e:
            print(e)


print(person_str(person_dto))# i am x, aged 10, lives in tyu
print(person_str_pythonic(person_dto))# i am x, aged 10 and currently lives at tyu

# delete key from dictionary
del person_dto['age']
print(person_str_pythonic(person_dto))




