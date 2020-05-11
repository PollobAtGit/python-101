class Node:
    def __init__(self, d):
        self.left = self.right = None
        self.value = data

def populate():
    root = Node(-1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(17)
    root.right.right = Node(33)

    return root

def preorder_iterate(root):
    if root is not None:
        stq = [root]
        r = []
        while stq:
            v = stq.pop()
            r.append(v.value)
           if v.right:
                stq.append(v.right)
            if v.left:
                stq.append(v.left)
 
def inorder_iterate(root):
    if root is not None:
        stck = [[root, False]]
        l = []
        while stck:
            v = stck[len(stck) - 1]
            if not v[1]:
                if v[0].right:
                    stck.append([v[0].right, False])
                if v[0].left:
                    stck.append([v[0].left, False])
                v[1] = True
            else:
                l.append(stck.pop()[0].value)
        return l




