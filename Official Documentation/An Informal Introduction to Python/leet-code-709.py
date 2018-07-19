class Solution:
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        if str is not None:
            return str.lower()

s = Solution()
print(s.toLowerCase(None))
print(s.toLowerCase('l'))
print(s.toLowerCase('L'))
