import random
import numbers

# pycharm requires below
# from .tombola import Tombola

# to run as main following is required
from tombola import Tombola


class LotteryBlower(Tombola):
    def __init__(self, iterable):
        self._balls = list(iterable)  # idiomatic usage if receiving a iterable!

    def load(self, iterable):
        self._balls.extend(iterable)

    def pick(self):
        try:
            position = random.randrange(len(self._balls))
        except ValueError:
            raise LookupError('pick from empty lottery blower')
        return self._balls.pop(position)

    def loaded(self):
        return bool(self._balls)

    def inspect(self):
        return tuple(sorted(self._balls))


# because of @Tombola.register python runtime doesn't check the class for abstract method implementation
@Tombola.register
class TombolaUsingRegister:
    pass


if __name__ == "__main__":
    # True
    print(isinstance(LotteryBlower([]), Tombola))

    print(isinstance(LotteryBlower([]), numbers.Integral))

    print(isinstance(TombolaUsingRegister(), Tombola))
