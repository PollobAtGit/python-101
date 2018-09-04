# Definition for a Node.
class Node(object):
    def __init__(self, val):
        self.val = val
        self.children = None

class Queue:
    def __init__(self):
        self.internal_ds = []

    def enqueue(self, x):
        if x is not None:
            if isinstance(x, list):
                self.internal_ds = self.internal_ds + x
            elif isinstance(x, NodeLevel):
                self.internal_ds = self.internal_ds + [x]

    def dequeue(self):
        if self.internal_ds:
            popped = self.internal_ds[0]
            self.internal_ds = self.internal_ds[1:]
            return popped

    def is_empty(self):
        return False if self.internal_ds else True

class NodeLevel:
    def __init__(self, node, level):
        if isinstance(node, Node):
            self.node = node
            self.level = level

class Solution(object):
    def levelOrder(self, root):
        if root is not None:

            q = Queue()

            q.enqueue(NodeLevel(root, 1))

            ret = []

            while not q.is_empty():

                e = q.dequeue()

                if e.level - 1 < len(ret):
                    ret[e.level - 1].append(e.node.val)
                else:
                    ret.append([e.node.val])

                if e.node.children:
                    q.enqueue([NodeLevel(x, e.level + 1) for x in e.node.children])

            return ret
        return []

a = Node(1)
b = Node(3)
c = Node(2)
d = Node(4)
e = Node(5)
f = Node(6)
g = Node(10)
h = Node(11)
i = Node(20)

a.children = [b, c, d]
b.children = [e, f]
# c.children = [g]
# g.children = [h]
# d.children = [i]

s= Solution()
print(s.levelOrder(a))
print(s.levelOrder(None))

# bfs(a)
# print(mod_bfs(a))
