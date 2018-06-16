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



