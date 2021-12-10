from collections import deque

class RecentCounter(object):

    def __init__(self):
        self.internal_storage = []
        self.currentLowest = 0
        self.deque = deque()
        
    def pingWithQueue(self, value):
        if value is not None:
            self.deque.append(value)

            while self.deque[0] < value - 3000:
                self.deque.popleft()

            return len(self.deque)

    def ping(self, t):
       if t is not None:

           self.internal_storage.append(t)
           threshold = t - 3000
           
           if threshold > 0 and self.internal_storage[self.currentLowest] < threshold and len(self.internal_storage) > 1:
               i = 0
               for j, v in enumerate(self.internal_storage[self.currentLowest:]):
                    i = j
                    if v >= threshold:
                        break
               self.currentLowest = self.currentLowest + i

           return len(self.internal_storage) - self.currentLowest

# Your RecentCounter object will be instantiated and called as such:
obj = RecentCounter()
assert obj.ping(1) == 1
assert obj.ping(100) == 2
assert obj.ping(3001) == 3
assert obj.ping(3002) == 3

assert obj.pingWithQueue(1) == 1
assert obj.pingWithQueue(100) == 2
assert obj.pingWithQueue(3001) == 3
assert obj.pingWithQueue(3002) == 3

_obj = RecentCounter()
assert _obj.ping(642) == 1
assert _obj.ping(1849) == 2
assert _obj.ping(4921) == 1
assert _obj.ping(5936) == 2
assert _obj.ping(5957) == 3

assert _obj.pingWithQueue(642) == 1
assert _obj.pingWithQueue(1849) == 2
assert _obj.pingWithQueue(4921) == 1
assert _obj.pingWithQueue(5936) == 2
assert _obj.pingWithQueue(5957) == 3
