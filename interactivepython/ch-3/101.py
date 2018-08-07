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

    # need to implement interator individually to ensure stack behavior
    # def __iter__(self):
    #     return iter(self.internal_queue)


stack = MyStack()

stack.push(10)
stack.push(30)
stack.push(25)
stack.push(-2)

print("ITERATE_THROUGH_ARR")


def iterate_through_arr(stck):
    while not stck.empty():
        print(stck.pop())


iterate_through_arr(stack)


def revstring(mystr):

    str_stack = MyStack()
    for x in mystr:
        str_stack.push(x)

    ret = []
    while not str_stack.empty():
        ret.append(str_stack.pop())

    return "".join(ret)


print(revstring("someT"))
