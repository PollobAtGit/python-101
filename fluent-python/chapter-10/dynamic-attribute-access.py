import numbers

class Vector:
    _component_shortcuts = 'xyz'

    def __init__(self, components):
        self._components = components

    def __getitem__(self, item):
        if isinstance(item, numbers.Integral):
            return self._components[item]
        raise NotImplementedError

    def __getattr__(self, item):
        if item in self._component_shortcuts:
            i = self._component_shortcuts.find(item)
            return self._components[i]
        raise AttributeError

    def __setattr__(self, key, value):
        if key in self._component_shortcuts:
            i = self._component_shortcuts.find(key)
            if i <= 0 < len(self._component_shortcuts):
                self._components[i] = value
        super().__setattr__(key, value) # important

    def __str__(self):
        return " | ".join([str(x) for x in self._components])


if __name__ == "__main__":
    v = Vector([9, 10, 77])
    print(v)
    print(v[0])
    print(v[1])
    print(v.x)
    print(v.y)

    try:
        print(v.a)
    except AttributeError:
        print('key not found')

    v.x = 99
    print(v)
