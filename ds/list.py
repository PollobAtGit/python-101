
list = [1, 2, 89]


def print_list(ls):
    for item in ls:
        print(item, end=' ')
    print()


# ls is not a deep copy of the passed list so append changes the passed list
def append_to_list(ls, item):
    ls.append(item)


# sort() modifies the original list that is passed
def sort_list(ls):
    ls.sort()


print_list(list)

append_to_list(list, 26.03)

append_to_list(list, -9)
sort_list(list)
print_list(list)

del list[0]
print_list(list)

del list[len(list) - 1]
print_list(list)
