# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def traverse(self, root, prev_depth):
        
        if not root:
            return prev_depth
        else:

            left_depth = self.traverse(root.left, prev_depth + 1)
            right_depth = self.traverse(root.right, prev_depth + 1)

            return max(left_depth,  right_depth)

    def maxDepth(self, A):

        if A:
            return self.traverse(A, 0)
        



a = TreeNode(10)
b = TreeNode(20)
c = TreeNode(30)
d = TreeNode(40)


a.left = b
"""
a.right = c

c.right = d
"""
s = Solution()

print(s.maxDepth(a))
