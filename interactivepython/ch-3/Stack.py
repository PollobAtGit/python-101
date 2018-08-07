class Stack:

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

    def emit_as_list(self):
    	return self.internal_queue[:]

    # need to implement interator individually to ensure stack behavior
    # def __iter__(self):
    #     return iter(self.internal_queue)
