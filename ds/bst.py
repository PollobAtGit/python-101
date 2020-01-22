
class Node:
    def __init__(self, data):
        self.data = data
        self.left_next = self.right_next = None

class BinarySearchTree:
    
    def __init__(self):
        self.head = None
    
    # TODO: recursive insertion
    def insert(self, data):
        if data is not None:
            
            n = Node(data)

            if not self.head:
                self.head = n
                return

            parent = self.head
            prev_node = None
            
            while parent:
                prev_node = parent
                if parent.data < data:
                    parent = parent.right_next
                else:
                    parent = parent.left_next
            
            if prev_node.data > data:
                prev_node.left_next = n
            else:
                prev_node.right_next = n
    
    def _inorder_traverse(self, parent):
        if parent is not None:
            return self._inorder_traverse(parent.left_next) + [parent.data] + self._inorder_traverse(parent.right_next)
        return []
    
    def inorder_print(self):
        for x in self._inorder_traverse(self.head):
            print(x)
        # print(" - ".join()
       

def test_code():
    bst = BinarySearchTree()

    for x in [3, 5, 1, 9, -3]:
        bst.insert(x)

    # -3
    # 1
    # 3
    # 5
    # 9

    bst.inorder_print()

test_code()


