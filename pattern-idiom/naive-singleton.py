class Car:

    class __Car:
        color = 'red'

    __instance = None

    def __init__(self):
        if Car.__instance is None:
            Car.__instance = Car.__Car()
   
    @property
    def instance(self):
        return self.__instance

    def __getattr__(self, name):
        return Car.__instance.__getattr__(name)

print(id(Car().instance))
print(id(Car().instance))
print(id(Car().instance))
print(id(Car().instance))

print(Car().instance.color)

