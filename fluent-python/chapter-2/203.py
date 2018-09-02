from collections import namedtuple

City = namedtuple('city', 'lat longi');
print(City(lat="a", longi='b'))

# _make can work with any iterables in this case list
print(City._make([56, 150]))

# _make working with __tuple__ to create tuple [City]
print(City._make((60, 'er')))

# _make works with any iterable. [set] is an iterable sequence
print(City._make({899, 'xyz'}))

# converting list to tuple
print(tuple([5, 25, 30]))

def div_mod(x, y):
	return x % y, int(x / y)

# list unpacking
print(div_mod(*[5, 25]))

# list unpacking
# tuples are immutable version of list. as tuples can be unpacked so as list can be unpacked. may be under the hood the list is converted to tuple
print(*[1, 2, 3])

t = [1, 2]
t_tuple = tuple(t)
t[0] = 10

print(t)
print(t_tuple)
print(t_tuple[0])

# t_tuple is tuple. tuples are immutable. in other words, they are immutable version of list
# t_tuple[0] = 10

# to convert from tuple to list use __list__ constructor
print(list(t_tuple))

# above is not the same as [t_tuple]
# following creates a list of tuples
print([t_tuple])


t_one = (-1, 23.2)
t_two = (-1, 0)

# tuple supports concatenation rather than __add__
# as tuples are immutable there's no reason to have __add__ for tuple
# list has __add__ (append) also set has __add__
print(t_one + t_two)# (-1, 23.2, -1, 0)

# t_one is replaced wholly by t_one + t_two
t_one += t_two
print(t_one)

print(0 in t_one)# True
print(-1 in t_one)# True

print(t_one.count(-1))# 2
print(t_one.count(23))
print(t_one[2])
print(t_one.index(0))# 3

print([1] * 5)# [1, 1, 1, 1, 1]
print((1,) * 5)# (1, 1, 1, 1, 1)
print(tuple([1] * 5))# (1, 1, 1, 1, 1)

print(list(reversed([1, 2])))# 2, 1
print(tuple(reversed((1, 2))))# 2, 1

# generate 10 elements sequentially (starting from 0)
lst = list(range(10))

# get everything until 3 and excluding index 3 itself (0, 1, 2)
print(lst[:3])

# to compute length of a soliced array perform (stop - start)
print(lst[4:6], 6 - 4, len(lst[4:6]))

# here start is 0
print(lst[:3], 3 - 0, len(lst[:3]))

# here stop is len(lst)
print(lst[4:], len(lst) - 4, len(lst[4:]))

print(lst[:], len(lst) - 0, len(lst[:]))
print(lst[3:7], 7 - 3, len(lst[3:7]))

# split list from an index
split_index = 5

# no overlapping elements => split operation
print(lst[:split_index], lst[split_index:])

print(lst[:split_index], lst[split_index - 1:])
print(lst[:split_index + 1], lst[split_index -  1:])
print(list(reversed(lst[:split_index])), list(reversed(lst[split_index:])))

print(lst[:])
print(lst[::1])

# every other element. first element index [0] then [0 + 2] then [0 + 2 + 2] etc.
print(lst[::2])
print(lst[::3])
print(lst[::5])

# note every 50th element will be chosen from the list but that also means element at index 0 will be chosen even if there's not enough 
# elements to show the next element
print(lst[::50])

# negative means counting will start from end of the list
print(lst[::-2])

# short hand for reversing list
# negation means evaluation starts from the end and every element will be evaluated
print(lst[::-1])
print(list(reversed(lst)))

# slice is a type
print(type(slice))



