
class Vector2D:

    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def __repr__(self):
        return str(type(self))

    def __eq__(self, other):
        # use tuple
        return self._x == other.x and self._y == other.y

def test_vector():
    v  = Vector2D(55, 45)
    
    print(v.x, v.y)
    print(type(v))
    print(repr(v))
    print(dir(type(v)))

    print(v == Vector2D(55, 45))
    print(v == Vector2D(55, 4))

test_vector()

