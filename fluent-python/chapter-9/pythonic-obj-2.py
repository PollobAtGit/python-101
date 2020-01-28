'''
    To covert something to tuple(...) that convertable object must a iterable. So if a custom object is to be converted to a tuple then it can be done
    only when the object itself is iterable
'''

class Demo:
    
    typecode = 'd'

    def __init__(self, tc):
        # following will shadow the class member
        self.typecode = tc

class Vector:

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __abs__(self):
        import math
        return math.hypot(self.x, self.y)

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __eq__(self, other):
        return tuple(self) == tuple(other)
    
    def __str__(self):
        return str(tuple(self))

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)

    # classmethod by default gets an argument passed which is the class instance itself
    @classmethod
    def vector_class(*args):
        return args

def test_vector():
    v = Vector(55, 78.90)
    
    print(v)
    print(f"{abs(v):.2f}")
    
    for x in v:
        print(x, end=' ')

    print()

    # class method is invoked upon the class not instance of the class
    default_passed_args = Vector.vector_class('custom parameter')

    print(default_passed_args)
    print(set(dir(default_passed_args)) - set(dir(v.vector_class())))

    print(hash(v))

def test_demo():
    print(Demo.typecode)
    print(Demo('ww').typecode)

test_vector()
test_demo()
