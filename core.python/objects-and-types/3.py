count = 0


def show_count():
    print(count)


def set_count(c):
    # count here is in local scope. it doesn't refer to the global scope
    count = c


def set_count_global(c):
    # defines a variable in local scope that refers to the object pointed by global count
    global count
    count = c


show_count()
set_count(78)
show_count()

set_count_global(77)
show_count()
