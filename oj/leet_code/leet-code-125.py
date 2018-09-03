class Solution:
    def is_alphanumeric(self, c):
        c = c.lower()
        return (ord(c) >= 97 and ord(c) <= 122) or (ord(c) >= 48 and ord(c) <= 57)

    def isPalindrome(self, s):
        if s is not None:
            s = list(s)

            head = 0
            tail = len(s) - 1

            while head < tail:

                while head < len(s) and not self.is_alphanumeric(s[head]):
                    head = head + 1

                while tail >= 0 and not self.is_alphanumeric(s[tail]):
                    tail = tail - 1

                if head < len(s) and tail >= 0 and s[head].lower() != s[tail].lower():
                    return False

                head = head + 1
                tail = tail - 1

            return True

s = Solution()

'''
print(s.isPalindrome("A man, a plan, a canal: Panama"))
print(s.isPalindrome("race a car"))
'''

print(s.isPalindrome(".,"))
print(s.isPalindrome("0P"))

