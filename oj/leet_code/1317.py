class Solution(object):
    def getNoZeroIntegers(self, n):
        if n is not None:
            for x in range(1, (n / 2) + 1):
                if "0" not in str(x) and "0" not in str(n - x):
                    return [x, n - x]
        return None
