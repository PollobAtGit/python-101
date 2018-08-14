# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution(object):
    
    def calculate_max_level(self, root, prev_level):
        
        if not root:
            return prev_level - 1
        else:

            max_level = -1

            for x in root.children:
                max_level = max(max_level, self.calculate_max_level(x, prev_level + 1))

            return max(max_level, prev_level)



    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root:
            return self.calculate_max_level(root, 1)
        else:
            return 0


def traverse(root):
    
    """
    if not root:
        return None
    """

    if root:
        ret = []
        
        for x in root.children:
            ret.append(traverse(x))

        return ret + [root.val]



root = Node(10, [
        Node(20, [
                Node(30, []),
                Node(31, [])
            ]),
        Node(21, [
                Node(32, []),
                Node(33, [
                        Node(400, [])
                    ])
            ]),
        Node(22, [
                Node(34, [])
            ])
    ])

a_root = Node(1, [
        Node(3, [
                Node(5, []),
                Node(6, [])
            ]),
        Node(2, []),
        Node(4, [])
    ])


print(traverse(root))

s = Solution()

print(s.maxDepth(root))
print(s.maxDepth(a_root))
print(s.maxDepth(Node(1, [])))
print(s.maxDepth(None))
