# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    
    def calculate_depth(self, root, prev_level):

        if not root:
            return prev_level - 1

        else:
            left_level = self.calculate_depth(root.left, prev_level+ 1)
            right_level = self.calculate_depth(root.right, prev_level + 1)

            return max(left_level, right_level, prev_level)



    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root:
            return self.calculate_depth(root, 1)
        else:
            return 0
        

a = TreeNode(3)
b = TreeNode(9)
c = TreeNode(20)
d = TreeNode(15)
e = TreeNode(7)

a.left = b
a.right = c

c.left = d
c.right = e

e.left = TreeNode(5)

s = Solution()

print(s.maxDepth(None))
print(s.maxDepth(a))

