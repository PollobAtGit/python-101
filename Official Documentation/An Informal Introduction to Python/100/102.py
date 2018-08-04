seq = [3, 6, 9, 12]

print(seq)
print(seq[:])

# Sequence concatenation
print(seq + seq)

seq[0] = 100
seq[2] = 200

# In-place substituion(!)
print(seq[:])

# Python has None as a Type?
print(seq.append(18))# None
print(seq)

print(len(seq))
seq.append(18)

# count() searches for an element and returns the occurrence of that
# value in the sequence
print(seq.count(18))# 2

# Following will replace the slice in the original array/sequence
seq[:] = [0, 1, 2, 3]
print(seq)

# Essentially replaces the slice indicated by [2:4]
seq[2:4] = []
print(seq)# [0, 1]

# Essentially appends to the original sequence
seq[2:] = [-1, -3, -6, -9]
print(seq)# [0, 1, -1, -3, -6, -9]

# Clear removes all elements from the sequence
seq.clear()
print(seq)# []

seq = [56, 59, 65, 98]
print(seq)# [56, 59, 65, 98]

# Essentially removing all elements same as seq.clear()
seq[:] = []
print(seq)# []

# Nested Sequence
nested_seq = [
    [1, 2, 3, 4, 5],
    [1, 4, 9, 16, 25],
    [1, 8, 27, 64, 125],
    [-1, -8, -27]
]

print(nested_seq)# [[1, 2, 3, 4, 5], [1, 4, 9, 16, 25], [1, 8, 27, 64, 125]]

print(nested_seq[0][1])# 2
print(nested_seq[1][1])# 4
print(len(nested_seq))# 4
print(len(nested_seq[0]))# 5
print(len(nested_seq[3]))# 3

print('Printing All Elements:')

for sub_array in nested_seq:
    for el in sub_array:
        print(el)


# Generate fib
# 0 1 2 3 5 8 13 ...

print("\nFib\n")

count = 15
a, b = 0, 1

while a < count:
    print(a)
    a, b = a + b, a


val_one = 10
val_two = 20

# Swapping values
val_one, val_two = val_two, val_one

print(val_one)
print(val_two)

    

