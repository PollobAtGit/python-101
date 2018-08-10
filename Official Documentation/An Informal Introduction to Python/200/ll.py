class Node:
    def __init__(self, d):
        self.data  = d
        self.next_node = None

class Linked_List:
    def __init__(self):
        self.head = None

    def insert_to_head(self, node):
        if self.head is None:
            self.head = node
        else:
            tmp = self.head
            self.head = node
            node.next_node = tmp

    def traverse(self):
        r = []
        d_h = self.head
        while d_h is not None:
            r.append(d_h.data)
            d_h = d_h.next_node

        return r

ll = Linked_List()

ll.insert_to_head(node=Node(d=10))
ll.insert_to_head(node=Node(d=20))
ll.insert_to_head(node=Node(d=55))
ll.insert_to_head(node=Node(d=65))

print(ll.traverse())
        
