first_tuple = 12, 56, 'hello!'

print(first_tuple)# (12, 56, 'hello!')
print(type(first_tuple))# <class 'tuple'>

print(first_tuple[0])# 12
print(first_tuple[2])# hello!

# index must be valid
# print(first_tuple[4])

print((1, 2))# (1, 2)
print((1, 2)[1])# 2
print((1, 2)[0])# 1

l = []
print(l)# []

# list is mutable
l = [1]
print(l)# [1]

# list items are mutable
l[0] = 't'# ['t']
print(l)

# tuple elements are immutable
# TypeError: 'tuple' object does not support item assignment
# first_tuple[0] = 't'

complex_tuple = ('A', [1, 2]), ('B', [3, 4, None], None), ('Z', [7])

# ('A', [1, 2]) ('B', [3, 4, None]) ('Z', [7])
print()
print(first_tuple)
print(len(first_tuple))# 3

print(len(complex_tuple))# 3
print(len(complex_tuple[0]))
print(len(complex_tuple[1]))#3

a, b, c = complex_tuple
print(a)
print(b)
print(c)

def unpacked_items(argument_one, argument_two, argument_three):
    return [y for x in argument_one if x != None for y in x] \
        + [y for x in argument_two if x != None for y in x] \
        + [y for x in argument_three if x != None for y in x]


# unpacking with astericks
flattened_items = unpacked_items(*complex_tuple)

print('Unpacking')

# ['A', 1, 2, 'B', 3, 4, None, 'Z', 7]
print(flattened_items) # ['A', 1, 2]

one_tuple = 1, 5

# unlike js there must be equal number of elements in the tuple
# TypeError: unpacked_items() missing 1 required positional argument: 'argument_three'
# unpacked_items(*one_tuple)
