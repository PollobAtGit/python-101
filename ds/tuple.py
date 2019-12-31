tuple = (4, 'one item', -8)


def print_all(t):
    for item in t:
        print(item, end=' ')
    print()

# sort() doesn't work on tuple


def sort_tuple(t):
    t.sort()


print_all(tuple)
print(len(tuple))
print(tuple[0])
print(tuple[len(tuple)-1])

print_all((1, 2, 3, tuple))
print(tuple[0])

# sort_tuple(tuple)
print_all(tuple)

# tuples are not deletable
# del tuple[0]
print_all(tuple)
