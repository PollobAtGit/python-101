# unpacking elements from iterable of arbitrary length 

records = [
        ('foo', 1, 2, 3),
        ('bar', 4, 5),
        ('others', 44)
]

def do_foo(itr):
    print(itr, "foo")

def do_bar(itr):
    print(itr, "bar")

for operation, *args in records:
    if operation == "foo":
        do_foo(args)
    elif operation == "bar":
        do_bar(args)




