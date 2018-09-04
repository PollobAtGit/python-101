class Node:
	def __init__(self, x):
		self.value = x
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

def bfs(root):
	if root is not None:

		q = Queue()

		q.enqueue(root)

		while not q.is_empty():

			e = q.dequeue()

			print('exploring: ', e.value)

			if e.children:
				q.enqueue(e.children)


class NodeLevel:
	def __init__(self, node, level):
		self.node = node
		self.level = level

def mod_bfs(root):
	if root is not None:

		q = Queue()

		q.enqueue(NodeLevel(root, 1))

		ret = []

		while not q.is_empty():

			e = q.dequeue()

			if e.level - 1 < len(ret):
				ret[e.level- 1].append(e.node.value)
			else:
				ret.append([e.node.value])

			if e.node.children:
				q.enqueue([NodeLevel(x, e.level + 1) for x in e.node.children])

		return ret


'''
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
h = Node('h')


a.children = [b, c]
b.children = [d, e]
c.children = [f, g]
e.children = [h]

'''

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
c.children = [g]
g.children = [h]
d.children = [i]

# bfs(a)
print(mod_bfs(a))
