# not working :(

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def min_diff_1(self, root):
        
        if not root:
            return None

        left_min = self.min_diff_1(root.left)
        right_min = self.min_diff_1(root.right)

        cu_min = None
        if root.left is not None:
            cu_min = abs(root.val - root.left.val)

            if root.right is not None:
                cu_min = min(cu_min, abs(root.val - root.right.val))

        if left_min is None and root.left is not None:
            left_min = abs(root.val - root.left.val)

        if right_min is None and root.right is not None:
            right_min = abs(root.val - root.right.val)

        return min(left_min, right_min, cu_min)

    def min_diff(self, root):
        if not root:
            # min, current_val
            return (None, None)

        left_min = self.min_diff(root.left)
        right_min = self.min_diff(root.right)

        if not left_min[0] and not left_min[1] and not right_min[0] and not right_min[1]:
            return (root.val, root.val)
        elif not left_min[0] and not left_min[1]:
            return (min(abs(right_min[1] - root.val), right_min[0]), root.val)
        elif not right_min[0] and not right_min[1]:
            return (min(abs(left_min[1] - root.val), left_min[0]), root.val)
        else:
            return (min(abs(left_min[1] - root.val), abs(right_min[1] - root.val), left_min[0], right_min[0]), root.val)

        # print(abs(left_min[1] - root.val), abs(right_min[1] - root.val))
        # print(min(abs(left_min[1] - root.val), abs(right_min[1] - root.val), left_min[0], right_min[0]))

    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root:
            # return self.min_diff(root)[0]
            return self.min_diff_1(root)


s = Solution()

a = TreeNode(4)
b = TreeNode(2)
c = TreeNode(6)
d = TreeNode(1)
# e = TreeNode(3)

a.left = b
a.right = c
b.left = d
# b.right = e

print(s.minDiffInBST(a))

