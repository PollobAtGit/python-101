
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
