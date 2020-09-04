import timeit

# 0.007204299999999997
print(timeit.timeit("""
from collections import namedtuple
namedtuple('Car', 'color mileage')
""", number=100))

print({'a', 'b'} | {'a', 'b', 'c'})

print(timeit.timeit("""
{'a', 'b'} | {'a', 'b', 'c'}
""", number=1000))

print(timeit.timeit("""
v = [str(x) for x in range(100)]
""", number=1000))

