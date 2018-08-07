class MyQueue:

    def __init__(self):
        self.internal_stack = []

    def push(self, x):
        self.internal_stack.append(x)

    def pop(self):
        popped_element = self.internal_stack[:1]
        self.internal_stack[:] = self.internal_stack[1:]

        return popped_element[0] if popped_element else None

    def peek(self):
        first_element_arr = self.internal_stack[:1]
        return first_element_arr[0] if first_element_arr else None

    def empty(self):
        return len(self.internal_stack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

queue = MyQueue()

queue.push(1)
queue.push(2)
print(queue.peek())
print(queue.pop())
print(queue.empty())
print(queue.internal_stack)
print(queue.pop())
print(queue.internal_stack)
print(queue.pop())
print(queue.internal_stack)
print(queue.peek())
