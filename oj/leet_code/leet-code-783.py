# not working :(

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def inorder(self, root):
        if not root:
            return []

        l_tr = self.inorder(root.left)
        r_tr = self.inorder(root.right)

        return l_tr + [root.val] + r_tr

    def min_diff_recur_inorder(self, root):
        if root:
            inorder = self.inorder(root)

            import sys
            min_diff = sys.maxsize

            for i, _ in enumerate(inorder):
                if i + 1 < len(inorder):
                    min_diff = min(min_diff, abs(inorder[i] - inorder[i + 1]))

            return min_diff


    def min_diff_recur(self, root):
        if not root or (not root.left and not root.right):
            return None

        l_m = self.min_diff_recur(root.left)
        r_m = self.min_diff_recur(root.right)

        current_min = None
        if root.left and root.right:
            current_min = min(abs(root.val - root.right.val), abs(root.val - root.left.val))
        elif root.right:
            current_min = abs(root.val - root.right.val)
        else:
            current_min = abs(root.val - root.left.val)

        if l_m and r_m:
            current_min = min(current_min, l_m, r_m)
        elif l_m:
            current_min = min(current_min, l_m)
        # else:
        elif r_m:
            current_min = min(current_min, r_m)

        return current_min

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
e = TreeNode(3)

a.left = b
a.right = c
b.left = d
b.right = e
# c.left = f
# c.right = g

print(s.min_diff_recur_inorder(a))

a = TreeNode(90)
b = TreeNode(69)
c = TreeNode(49)
d = TreeNode(52)
e = TreeNode(89)

a.left = b
b.left = c
b.right = e
c.right = d
# c.right = g


print(s.min_diff_recur_inorder(a))

