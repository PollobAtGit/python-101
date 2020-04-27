import numbers


class Queue(object):

    def __init__(self, collection=None):
        if collection is None:
            self._internal_collection = []
        else:
            self._internal_collection = list(collection)

    def __getitem__(self, index):
        if isinstance(index, slice):
            # taking type of 'self' & initializing an instance of  that type
            return type(self)(self._internal_collection[index])
        elif isinstance(index, numbers.Integral):
            return self._internal_collection[index]
        else:
            raise TypeError(f'{type(self).__name__} indices must be integer or slice')

    def __str__(self):
        return " | ".join([str(x) for x in self._internal_collection])


def print_collection(collection):
    # 'for' loop needs __getitem__ protocol to be implemented not __len__
    for x in collection:
        print(x)


if __name__ == '__main__':
    q = Queue(range(9))

    # print_collection(q)

    # slicing only requires __getitem__ to be implemented
    print(q[:])
    print(q[4:9:2])

    try:
        print(q['s'])
    except:
        print('something went wrong')
