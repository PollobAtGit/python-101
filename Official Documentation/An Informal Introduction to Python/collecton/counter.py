import collections


def convert_to_collection(iterator):
    if iterator:
        return collections.Counter(iterator)


def find_uniqueness(seq):
    if seq:
        for _, count in collections.Counter(seq).items():
            if count > 1:
                return False
        return True
    return None


def find_uniqueness_using_dic(seq):
    if seq:
        dic = {}
        for x in seq:
            if x in dic:
                return False
            else:
                dic[x] = 1
        return True
    return None


print(find_uniqueness([1, 2, 3, 3, 2, 1]))
print(find_uniqueness([1, 2, 3]))
print(find_uniqueness([1]))
print(find_uniqueness([1, 1]))

print()

print(find_uniqueness_using_dic([1, 2, 3, 3, 2, 1]))
print(find_uniqueness_using_dic([1, 2, 3]))
print(find_uniqueness_using_dic([1]))
print(find_uniqueness_using_dic([1, 1]))


def test_code():
    print(convert_to_collection([1, 2, 3, 3, 2, 1]))

    c = convert_to_collection(['q', 'r', 's', 's', 'r', 'q'])

    for x in c.items():
        print(x)


test_code()
