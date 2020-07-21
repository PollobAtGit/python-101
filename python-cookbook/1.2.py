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


## SUM WITH UNPACKING ELEMENTS

def sum(item_list):
    head, *tail = item_list
    return head + sum(tail) if tail else head 


print(sum([1, 2, 3]))

## SPLIT FROM PATTERNED TUPLE

def find_month_year(csvLine):
    _, (_, _), year, (*month_date, amount) = csvLine
    return year, month_date[0]

print(find_month_year((None, (None, None), 34, ([5, 6, 7, 's']))))


