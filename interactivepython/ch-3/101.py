from Stack import Stack

stack = Stack()

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

    str_stack = Stack()
    for x in mystr:
        str_stack.push(x)

    ret = []
    while not str_stack.empty():
        ret.append(str_stack.pop())

    return "".join(ret)


print(revstring("someT"))
