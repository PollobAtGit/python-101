def iterate_over_iterator(iterator):
    try:
        print(next(iterator))
    except StopIteration as e: 
        print("iteration done")
    finally:
        pass

def reverse(str):
    if str:
        for x in str:
            yield x

iterator = reverse("string")

print(type(iterator))

iterate_over_iterator(iterator)
iterate_over_iterator(iterator)
iterate_over_iterator(iterator)
iterate_over_iterator(iterator)
iterate_over_iterator(iterator)
iterate_over_iterator(iterator)
iterate_over_iterator(iterator)
iterate_over_iterator(iterator)
iterate_over_iterator(iterator)
iterate_over_iterator(iterator)
iterate_over_iterator(iterator)

xs = [56, 89, 79]
ys = [25, 23, 29]

print(sum(x * y for x, y in zip(xs, ys)))

