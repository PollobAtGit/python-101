class Node:
    def __init__(self, d):
        self.data = d
        self.next = None


class SinglyLinkedList:
    def __init__(self, first_node):
        self.head = first_node

    def print(self):
        if self.head:
            self._iterate(lambda x: print(x.data))

    def _iterate(self, fn):
        if self.head:
            c_node = self.head
            while c_node != None:
                fn(c_node)
                c_node = c_node.next

    def _search_recursively(self, c_node, v):
        if c_node and v:
            if c_node.data == v:
                return True
            return self._search_recursively(c_node.next, v)
        return False

    def search(self, v):
        if self.head and v:
            return self._search_recursively(self.head, v)

    def append(self, v):
        if self.head and v:
            c_node = self.head
            while c_node.next != None:
                c_node = c_node.next
            c_node.next = Node(v)

    def prepend(self, v):
        if self.head and v:
            node = Node(v)
            node.next = self.head
            self.head = node

    def length(self):
        if self.head:
            length = 0

            c_node = self.head
            while c_node != None:
                length = length + 1
                c_node = c_node.next

            return length

    def index_of(self, v):
        if self.head and v:
            index = 0

            c_node = self.head
            while c_node != None and c_node.data != v:
                index = index + 1
                c_node = c_node.next

            if c_node != None:
                return index
            return -1

    def element_at_index(self, i):
        if self.head and i is not None and i < self.length():
            index = 0
            c_node = self.head
            while c_node != None:
                if index == i:
                    return c_node.data
                index = index + 1
                c_node = c_node.next


def test_code():
    p = Node(10)
    q = Node(30)
    r = Node(20)

    p.next = q
    q.next = r

    linked_list = SinglyLinkedList(p)

    print(linked_list.length())
    print()

    linked_list.print()

    print(linked_list.search(20))
    print(linked_list.search(40))
    print(linked_list.search(30))
    print(linked_list.search(10))

    print()

    linked_list.append(89)
    linked_list.append(-9)
    linked_list.prepend(-9.23)
    linked_list.prepend(-90.23)

    linked_list.print()
    print(linked_list.length())

    print()
    print()
    print()

    def print_index_of_all():
        if linked_list.head:
            c_node = linked_list.head
            while c_node != None:
                print(c_node.data, linked_list.index_of(c_node.data))
                c_node = c_node.next

    print_index_of_all()

    print()

    def element_at_each_index():
        for x in range(linked_list.length()):
            print(x, linked_list.element_at_index(x))

    element_at_each_index()

test_code()
