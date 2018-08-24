
class Vector:

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    # containers always invoke __repr__ never __str__ It's better to implement __repr__
    def __repr__(self):
        return "Vector (%r, %r)" % (self.x, self.y)

    # __str__ takes precedence over __repr__ when using in print(...) API
    def __str__(self):
        return "Vector => (%r, %r)" % (self.x, self.y)
        # concat only works when all parts of the string are string. So conversion to str(...) is required
        # return "Vector => (" + str(self.x) + ", " + str(self.y) + ")"

    def __add__(self, other_vector):
        return Vector(self.x + other_vector.x, self.y + other_vector.y)

    # python doesn't have method overloading apparently
    def __mul__(self, other_vector):
        return Vector(self.x * other_vector.x, self.y * other_vector.y)

    def __abs__(self):
        from math import hypot

        # what does hypot really do?
        return hypot(self.x, self.y)

    # __len__ indeed is invoked to determine truthiness
    # def __len__(self):
        # return 1

    def __bool__(self):
        return bool(abs(self))

        # faster because no round trip to abs ... hypot etc.
        # return bool(self.x or self.y)

        # following will cause if--else condition to return false always
        # return False

v_one = Vector(2, 4)
v_two = Vector(2, 1)

print(v_one +  v_two)
print(abs(v_one))
print(v_one * v_two)

# container's invoke __repr__ rather than __str__
print([Vector(1, 2), Vector(5, 9), Vector(-9, 10)])# [Vector (1, 2), Vector (5, 9), Vector (-9, 10)]

# once agian containers invoke __repr__ not __str__
# note that the key of the second element is set to be an instance of a Vector
# the __repr__ representation is evaluated then the evaluated string is used as key
print({ '1': Vector(2, 5), Vector(3, 7): Vector(3, 7) })

print(v_one)
# print(v_one * 10)

# python interpreter will invoke __bool__ first to see if it's truthy or not then if not found
# it will invoke __len__
# none of them is implemented then it will consider the type to be truthy (by default)
print(v_one if v_one else v_two)

# Vector implements __bool__ so if--else can use that implementation of __bool__
print("empty vector" if not Vector(0, 0) else "non-empty vector")

