"""
not done
"""

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """

        if num is not None:
            
            if num < 2:
                return True

            for x in range(2, (num / 2) + 1):
                if x * x == num:
                    return True

            return False

s = Solution()

"""
print(s.isPerfectSquare(16))
print(s.isPerfectSquare(14))
print(s.isPerfectSquare(0))
print(s.isPerfectSquare(1))
print(s.isPerfectSquare(2))
print(s.isPerfectSquare(4))
"""

print(s.isPerfectSquare(2147483647))
