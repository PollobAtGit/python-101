
class Solution:
    def solve(self, A):
        if A is not None:
            sorted_a = sorted(A)
            for i, x in enumerate(sorted_a):
                if x == len(set(sorted_a[i+1:])):
                    return 1
            return -1

