print(dir(list))
print('__iter__' in dir(list))
print(iter(list()))  # <list_iterator object at 0x015D06D0>
print('__next__' in dir(list))

items = [1]

print(next(iter(items)))

# not throwing StopIteration error?
print(next(iter(items)))


# following will TypeError because list(...) is not an iterator though it's iterable
# print(next(list()))

def yield_to_10():
    for x in range(10):
        yield x


nums = []
for xy in yield_to_10():
    nums.append(xy)

print(nums)

# yield_to_10 implements both __iter__ and __next__ meaning a generator is both a iterator and iterable
print('__iter__' in dir(yield_to_10()))
print('__next__' in dir(yield_to_10()))


class Range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    # __iter__ must return an object that implements __next__
    def __iter__(self):
        return self

    # __next__ raises StopIteration error when there's no next value
    def __next__(self):
        if self.start > self.end:
            raise StopIteration
        else:
            current = self.start
            self.start += 1
            return current


rng = Range(10, 20)

qrt = []
for x in rng:
    qrt.append(x)

print(qrt)
