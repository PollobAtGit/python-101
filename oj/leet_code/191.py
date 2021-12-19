from collections import deque


class Solution(object):
    def hammingWeight(self, n):
        if n is not None:

            binary = deque()

            while n:
                binary.appendleft(n % 2)
                n //= 2

            return len([x for x in binary if x == 1])


s = Solution()

assert s.hammingWeight(0) == 0
assert s.hammingWeight(4294967295) == 32

assert s.hammingWeight(11) == 3
assert s.hammingWeight(128) == 1
assert s.hammingWeight(4294967293) == 31
