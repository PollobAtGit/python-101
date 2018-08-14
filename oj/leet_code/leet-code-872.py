# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def traverse_leaf(self, tree_root):

        if not tree_root:
            return None

        else:
            left_ret = self.traverse_leaf(tree_root.left)
            right_ret = self.traverse_leaf(tree_root.right)

            if not left_ret and not right_ret:
                return [tree_root.val]
            elif not left_ret:
                return right_ret
            elif not right_ret:
                return left_ret
            else:
                return left_ret + right_ret
                



    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """

        if root1 and root2:
            
            left_leaves = self.traverse_leaf(root1)
            right_leaves = self.traverse_leaf(root2)

            # print(left_leaves, right_leaves)

            return left_leaves == right_leaves
        


# left subtree

a = TreeNode(3)
b = TreeNode(5)
c = TreeNode(1)
d = TreeNode(6)
e = TreeNode(2)
f = TreeNode(7)
g = TreeNode(4)
h = TreeNode(9)
i = TreeNode(8)

a.left = b
a.right = c

b.left = d
b.right = e

e.left = f
e.right = g

c.left = h
c.right = i

# right subtree

_a = TreeNode(0)
_b = TreeNode(6)
_c = TreeNode(0)
_d = TreeNode(7)
_e = TreeNode(0)
_f = TreeNode(4)
_g = TreeNode(0)
_h = TreeNode(9)
_i = TreeNode(8)

_a.left = _b
_a.right = _c

_c.left = _d
_c.right = _e

_e.left = _f
_e.right = _g

_g.left = _h
_g.right = _i


s = Solution()
print(s.leafSimilar(a, _a))
# print(s.traverse_leaf(_a))
