class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):

        if A:
            
            sorted_a = sorted(A)

            a = None
            b = None

            for i, x in enumerate(sorted_a):
                if (i + 1) < len(sorted_a) and x == sorted_a[i + 1]:
                    a = x
                elif (i + 1) < len(sorted_a) and abs(x - sorted_a[i + 1]) > 1:
                    b = x + 1

            if not b:
                b = A[-1] + 1 if A[0] == 1 else 1

            return [a, b]


s = Solution()
print(s.repeatedNumber([3, 1, 2, 5, 3]))
print(s.repeatedNumber([1, 1, 2]))
print(s.repeatedNumber([1, 1, 3]))
print(s.repeatedNumber([2, 2]))
