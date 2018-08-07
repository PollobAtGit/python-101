class MyStack:

    def __init__(self):
        self.internal_queue = []

    def push(self, x):
        self.internal_queue.append(x)

    def pop(self):
        if self.internal_queue:
            return self.internal_queue.pop()

    def top(self):
        if self.internal_queue:
            return self.internal_queue[-1]

    def empty(self):
        return len(self.internal_queue) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

stack = MyStack()

stack.push(1)
stack.push(2)
print(stack.top())
print(stack.pop())
print(stack.empty())

print(stack.internal_queue)
print(stack.pop())
print(stack.pop())
print(stack.empty())
