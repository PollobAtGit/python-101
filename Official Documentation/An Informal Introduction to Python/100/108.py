for x in range(10):
    print(x)

# weird ! python is not block scoped. x exists here 
print(x)# 9

print([x * x for x in range(10)])# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

squares = list(map(lambda x : x ** x, range(10)))

print(squares)# [1, 1, 4, 27, 256, 3125, 46656, 823543, 16777216, 387420489]

# Generate all pairs

abc = ['a', 'b', 'c']
numbers = [1, 2, 3]

# Is slicing required?
other_squares = [(i, j) for i in abc[:] for j in numbers[:] if i != j]

print(other_squares)# [('a', 1), ('a', 2), ('a', 3), ('b', 1), ('b', 2), ('b', 3), ('c', 1), ('c', 2), ('c', 3)]

# tuple
print(('p', 2))# ('p', 2)
print((1, 2, 3))# (1, 2, 3)
print((1, 2, 3, 4, 5, 'r', None))# (1, 2, 3, 4, 5, 'r', None)

######### listing #########

print( [x for x in range(10) if x % 2 == 0])# [0, 2, 4, 6, 8]

def filter_out_evens(lst):
    return [x for x in lst[:] if x % 2 != 0]

print(filter_out_evens(list(range(10))))# [1, 3, 5, 7, 9]

# transformation (Select(...) in C#)

# ['STR: 0', 'STR: 1', 'STR: 2', 'STR: 3', 'STR: 4', 'STR: 5', 'STR: 6', 'STR: 7', 'STR: 8', 'STR: 9']
print([('STR: ' + str(x)) for x in range(10)])

fresh_fruit = ['  banana', '  loganberry ', 'passion fruit  ']
print([fruit.strip() for fruit in fresh_fruit])#['banana', 'loganberry', 'passion fruit']

# pairing with tuple

# [(0, 1), (1, 1), (2, 4), (3, 27), (4, 256), (5, 3125), (6, 46656)]
print([(x, x ** x) for x in range(7)])

# 2D array
vec = [[1, 2], [3, 4], [5, 6]]

# [1, 2, 3, 4, 5, 6]
print([inner for outer in vec for inner in outer])

# list comprehension creates a list ... (usage of map) [period]
# In this case it's creating an inner list
print([[x] for x in range(5)])

# What's the usage of zip?
print(list(zip(*vec))) #[(1, 3, 5), (2, 4, 6)]

sample_list = [1, 2, 25]
sample_list.remove(2)

print(sample_list)# [1, 25]
# sample_list.remove(18)

del sample_list[0]

print(sample_list)# [25]

sample_list[1:] = [56, 89, 78]

print(sample_list)# [25, 56, 89, 78]

del sample_list[:]

print(sample_list)# []

other_list = [89, 85, 100, 101, 89.23]

del other_list[2:4]
print(other_list)# [89, 85, 89.23]
