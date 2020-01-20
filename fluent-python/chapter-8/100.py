class Gizmo:
    def __init__(self):
        print('Gizmo id: %d' % id(self)) # id(..) function is a builtin function which returns and unique integer representing the object (sort of like hash value in C#) id(...) might in some situation return non-unique values


def lewis_and_charles_are_same():
    charles = {'name': 'Charles L. Dodgson', 'born': 1832}
    richard = {'name': 'Charles L. Dodgson', 'born': 1832}

    lewis = charles

    # what is being referenced? id(...)?

    print(('*' * 10) + '[is] operator' + ('*' * 10))
    print(lewis is charles)
    print(charles is lewis)
    print(richard is lewis)
    print(richard is not lewis)

    print(('*' * 10) + '[==] operator' + ('*' * 10))

    print(lewis == charles)
    print(charles == lewis)
    
    # == is not same as is (is internally uses __eq__ method which relies on dictionary value so value comparison)
    print(richard == lewis)

    print(lewis['name'])
    print(charles['name'])

    print("Charles id: %d, lewis id %d & richard id %d" % (id(charles), id(lewis), id(richard)))

    print("{} == {} => %r" % richard == lewis)

    # 'is' operator relies on id(...)
    print("{} is {} => %s" % ({} is {}))

    # '==' operatr by default relies on implementation of __eq__
    print("{} == {} => %s" % ({} == {}))

def variables_are_label():
    x = Gizmo()
    y = Gizmo()

    print(dir()) # returns the names in current scope. so returning right now [x, y]
    print(dir(x)) # returns names of provided argument
    print(dir(y))

variables_are_label()
lewis_and_charles_are_same()

