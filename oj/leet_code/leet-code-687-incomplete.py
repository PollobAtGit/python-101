# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def go(self, root):
        if root is not None:
            left = self.go(root.left)
            right = self.go(root.right)

            if left[0] and right[0] and left[0] == root.val == right[0]:
                cur_high = max(left[1], right[1]) + 1
                return (root.val, cur_high, max(cur_high, left[2], right[2]))

            if left[0]:
                if left[0] == root.val:
                    cur_high = left[1] + 1
                    return (root.val, cur_high, max(cur_high, left[2]))
            
            if right[0]:
                if right[0] == root.val:
                    cur_high = right[1] + 1
                    return (root.val, cur_high, max(cur_high, right[2]))

            return (root.val, 0, max(left[2], right[2]))
        return (None, 0, 0)

    def longestUnivaluePath(self, root):
        if root is not None:
            goresult = self.go(root)
            return goresult[2]

a = TreeNode(5)
b = TreeNode(4)
c = TreeNode(5)
d = TreeNode(1)
e = TreeNode(1)
f = TreeNode(5)
g = TreeNode(5)

a.left = b
a.right = c

b.left = d
b.right = e

c.right = f

f.left = g

'''

a = TreeNode(1)
b = TreeNode(4)
c = TreeNode(5)
d = TreeNode(4)
e = TreeNode(4)
f = TreeNode(5)


a.left = b
a.right = c

b.left = d
b.right = e

c.left = f

'''

s = Solution()
print(s.longestUnivaluePath(a))


