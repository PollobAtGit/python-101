class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        if s is None: return ""

        return " ".join([x[::-1] for x in s.split()])
        
s = Solution()
print(s.reverseWords("Let's take LeetCode contest"))
print(s.reverseWords(""))
print(s.reverseWords(None))
