class Solution(object):
    def fairCandySwap(self, A, B):
        a_sum = sum(A)
        b_sum = sum(B)
        set_b = set(B)
        for x in A:
            y = (b_sum - a_sum + 2 * x) / 2
            if y in set_b:
                return [x, y]
