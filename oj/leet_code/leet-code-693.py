class Solution:
    def hasAlternatingBits(self, n):
        if n is not None:
            while n > 0:
                k = n & 3
                if k not in (1, 2):
                    return False
                n = n >> 1
            return True
        
s = Solution()

'''
print(s.hasAlternatingBits(5))
print(s.hasAlternatingBits(7))
print(s.hasAlternatingBits(11))
print(s.hasAlternatingBits(10))
'''

print(s.hasAlternatingBits(20))
print(s.hasAlternatingBits(21))
print(s.hasAlternatingBits(22))
