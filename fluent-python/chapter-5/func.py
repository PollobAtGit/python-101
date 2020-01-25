
'''
a feature in a programming language is a first class citizen if
    
    $$ it can be passed as function parameter
    $$ it can be received as function argument
    $$ it can assigned to a storage/variable
    $$ it can be created dynamically

higher order functions are those functions which can 
    
    $$ receive function as parameter
    $$ return function

'''

def sort_by_occurrances_a(x):
    return len(list(filter(lambda c : c == 'a', x))) 

def reverse_word(x):
    return x[::-1]

def sort_fruits():
    f = ['banana', 'pine-apple', 'apple']
    
    print(sorted(f, key=len))
    print(sorted(f, key=sort_by_occurrances_a))
    print(sorted(f, key=reverse_word), sorted(f, key=lambda w : w))

def factorial(n):
    ''' returns factorial of n '''
    return 1 if n < 2 else n * factorial(n - 1)

def test_func():
    print(factorial.__doc__)

    # 'factorial' is an instance of type 'function'
    print(type(factorial))

def factorial_range():
    print(list(map(factorial, range(10))))

def work_with_callable():
    print(callable(len), callable(work_with_callable))
    print(callable(Bus), callable(Bus()))

    # Hundai instance is callable bcause Hundai implements __call__
    print(callable(Hundai), callable(Hundai()))

    h = Hundai()
    h()

def bingo_case_callable():
    bc = BingoCase(['3', '60', '99'])

    print(bc())
    print(bc())
    print(bc())

    # will raise lookup error
    # print(bc())

def arbitrary_args_passing(q, r, s):
    print(q, r, s)

class Bus():
    pass

class Hundai():
    def __call__(self):
        print('invoking as callable')

import random

class BingoCase():

    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty bingo case')

    def __call__(self):
        return self.pick()

def show_def_defaults_and_code(unsued_var=None):
    print(show_def_defaults_and_code.__defaults__)
    print(show_def_defaults_and_code.__code__)

test_func()
factorial_range()
sort_fruits()
work_with_callable()
bingo_case_callable()
arbitrary_args_passing(**{'q': 1, 'r': 2, 's': 3})
show_def_defaults_and_code()

