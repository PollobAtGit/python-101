class Gizmo:
    def __init__(self):
        print('Gizmo id: %d' % id(self)) # id(..) function is a builtin function which returns and unique integer representing the object (sort of like hash value in C#) id(...) might in some situation return non-unique values

def id_of_none():
    print({} is None)
    print(None is None)
    print(id(None)) # 264404036

# notes: 
#   'is' compares object identity (via id())
#   '==' compares the values of the object
#   default implementation of __eq__ is same as == but most of the time __eq__ is overridden in custom types
#   'is' faster than '==' because 'is' can't be oerridden which means python runtime don't need to look for a special implementation of 'is'
#       also most of the type equality for == will require traversing through big object graph

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

def tuples_relative_mutability():
    q_one = (1, 2, [56, -4])
    q_two = (1, 2, [56, -4])

    print(q_one == q_two)
    print(id(q_one), id(q_two))
    q_ne_last_el_id = id(q_one[-1])

    print(q_one[-1])

    # q_one[-1] = None # this will throw panic because tuples are immutable but following is fine

    # relative immutability
    q_one[-1].append('one')

    print(q_one)

    print(q_one == q_two)
    print(id(q_one), id(q_two))

    # object id(...) didn't change
    print(q_ne_last_el_id == id(q_one[-1]))

# note:
#   best way to copy any object is to use the default constructor

def copies_are_shallow_by_default():
    
    print('*' * 10 + ' COPIES ARE SHALLOW BY DEFAULT ' + '*' * 10)

    l = [1, 2]

    # copies the original object
    l_copy = list(l)

    print(l == l_copy)
    print(l is l_copy)

    l.append('__')
    print(l == l_copy)

    print(l_copy)
    print(l)

    q = [1, [-2, -3], ('one', 'two')]
    q_copy = list(q)
    q[0] = -22

    # all nested objects are shallow copied! list and tuple here
    print('q[i] is q_copy[i] : %s, %s, %s' % (q[0] is q_copy[0], q[1] is q_copy[1], q[2] is q_copy[2]))

    # mutability of q has no impact on q_copy
    print(q[0], q_copy[0])

    # mutability of list at index 1 has impact on q and q_copy
    q[1] = q[1] + [-99]
    print(q, q_copy)

    # for tuple the scenario is not same as list. mutation in q[2] has no impact on q_copy[2]. why?
    q[2] = ('tuple replaced', -99)
    print(q, q_copy)

    print(q[1] == q_copy[1])
    print(q[2] == q_copy[2])

    # True, False, False
    print('q[i] is q_copy[i] : %s, %s, %s' % (q[0] is q_copy[0], q[1] is q_copy[1], q[2] is q_copy[2]))
    print(q is q_copy)

variables_are_label()
lewis_and_charles_are_same()
id_of_none()
tuples_relative_mutability()
copies_are_shallow_by_default()

