class Solution(object):
    def sumZero(self, n):
        if n is not None:
            if n == 1:
                return [0]
            q = n // 2
            return [-1 * x for x in range(1, q + 1)] + ([0] if n % 2 != 0 else []) + [x for x in range(1, q + 1)]
