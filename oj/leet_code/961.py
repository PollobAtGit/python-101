class Solution(object):
    def repeatedNTimes(self, A):
        if A is not None:
            import collections

            c = collections.Counter(A)
            n = len(A) / 2

            for x, c in c.items():
                if c == n:
                    return x
            return None
