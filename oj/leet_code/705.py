class MyHashSet(object):

    def __init__(self):
        self.internal_storage = []

    def add(self, key):
        if key is not None and self.findIndex(key) is None:
            self.internal_storage.append(key)

    def findIndex(self, key):
        if key is not None and self.internal_storage:
            for i, v in enumerate(self.internal_storage):
                if key == v:
                    return i

    def remove(self, key):
        i = self.findIndex(key)

        if i is None or key is None:
            return

        self.internal_storage = self.internal_storage[:i] + self.internal_storage[i + 1:]

    def contains(self, key):
        if self.findIndex(key) is not None:
            return True
        return False

obj = MyHashSet()

obj.add(5)
print(obj.contains(5))

obj.remove(5)
print(obj.contains(5))

obj.remove(5)
print(obj.contains(5))
print(obj.contains(8))

obj.add("word")
print(obj.contains("word"))

obj.add(None)

print(obj.internal_storage)

print(obj.contains(None))

