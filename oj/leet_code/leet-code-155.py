import sys

class MinStack:

    def __init__(self):
        self.internal_sequence = []
        self.current_min = sys.maxsize
        

    def push(self, x):

        if x is not None:
            if x < self.current_min:
                self.current_min = x
            self.internal_sequence.append(x)
        

    def pop(self):
        
        if self.internal_sequence:
            popped = self.internal_sequence[-1]
            self.internal_sequence = self.internal_sequence[:-1] # end index is exclusive

            if self.internal_sequence:
                self.current_min = min(self.internal_sequence)
            else:
                self.current_min = sys.maxsize

            return popped
        

    def top(self):
        
        if self.internal_sequence:
            return self.internal_sequence[-1]
        

    def getMin(self):

        if self.internal_sequence:
            return self.current_min
        

'''
# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(10)
print(obj.pop())
print(obj.top())
print(obj.getMin())

minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())   # --> Returns -3.
print(minStack.pop())

print(minStack.internal_sequence)


print(minStack.top())      # --> Returns 0.
print(minStack.getMin())   # --> Returns -2.
'''



["MinStack","push","push","push","top","pop","getMin","pop","getMin","pop","push","top","getMin","push","top","getMin","pop","getMin"]
[[],[2147483646],[2147483646],[2147483647],[],[],[],[],[],[],[2147483647],[],[],[-2147483648],[],[],[],[]]

_minStack = MinStack()
_minStack.push(2147483646)
_minStack.push(2147483646)
_minStack.push(2147483647)
print(_minStack.top())
print(_minStack.pop())
print(_minStack.getMin())
print(_minStack.pop())
print(_minStack.getMin())
print(_minStack.pop())
_minStack.push(2147483647)
print(_minStack.top())
print(_minStack.getMin())
_minStack.push(-2147483648)
print(_minStack.top())
print(_minStack.getMin())
print(_minStack.pop())
print(_minStack.getMin())