def sort_list(lst):
    lst.sort() # in place sort
    return lst

def i_make_shallow_copy(lst):
    return lst.copy();

def reverse_list(lst):
    lst.reverse() # in place reverse
    return lst

main_list = [1, 2]

print(sort_list([96, 56]))

copied_list = i_make_shallow_copy(main_list)
print(copied_list)

main_list.clear()
print(main_list)
print(copied_list)

print(reverse_list([1, 2])) # [2, 1]

ascending_list = [56, 89]
ascending_list.sort(reverse=True)

print(ascending_list)# [89, 56]

ascending_list.sort(reverse=False)

print(ascending_list)# [56, 89]

t = []
t.append([1, 't'])
t.append(78)

print(t)# [[1, 't'], 78]

y = t[:]
print(y)

t.clear()

# []
# [[1, 't'], 78]
print(t)
print(y)

# combination of append() & pop() is LIFO/stack

stack = []

stack.append(10)
stack.append(112)

print(stack)
print(stack.pop())# 112
print(stack)

from collections import deque

queue = deque([1, 2, 3])

print(queue)
print(queue.popleft())# 1
print(queue)

queue.append(89)

print(queue.popleft())# 2
print(queue)
print(queue.pop())
print(queue)

# starting from zero
for x in range(10):
    print(x)

print(list())

squares = list(map(lambda x: x ** 2, range(10)))

print(squares)

# shorthand
other_squares = [x ** 2 for x in range(10)]

print(other_squares)

# list comprehension
print([(i, j) for i in [1, 2, 3] for j in [3, 4, 5] if i != j])
print([(i, j) for i in [1, 2, 3] for j in [3, 4, 5]])
