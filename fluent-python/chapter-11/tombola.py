import abc


class Tombola(abc.ABC):

    @abc.abstractmethod
    def load(self, iterable):
        '''Adds items from an iterable'''

    @abc.abstractmethod
    def pick(self):
        '''
        Remove item at random returning it
        This method should raise LookupError when the instance is empty
        '''

    def loaded(self):
        return bool(self.inspect())

    def inspect(self):
        items = []
        while True:
            try:
                items.append(self.pick())
            except ValueError:
                break

        self.load(items)
        return tuple(sorted(items))


class FakeTombola(Tombola):
    def pick(self):
        pass

    # def load(self, iterable):
    #     pass


# python 3
# class TombolaAbc(metaclass=abc.ABC):
#     pass

# following is not working in python 3.7.1
# class Python2TombolaAbc():
#     __metaclasss__ = abc.ABC


if __name__ == "__main__":
    try:
        # will throw error because FakeTombola doesn't implement 'load' abstract method
        print(FakeTombola())
    except TypeError:
        print('type error occurred')
