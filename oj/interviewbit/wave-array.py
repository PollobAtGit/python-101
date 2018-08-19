class Solution:
    # @param A : list of integers
    # @return a list of integers
    def wave(self, A):

        if A is not None:
            sorted_a = sorted(A)

            waved = []

            i = 0
            while i < len(sorted_a):

                if i + 1 < len(sorted_a):
                    waved.append(sorted_a[i + 1])

                if i < len(sorted_a):
                    waved.append(sorted_a[i])

                if i + 3 < len(sorted_a):
                    waved.append(sorted_a[i + 3])

                if i + 2 < len(sorted_a):
                    waved.append(sorted_a[i + 2])

                i = i + 4

            return waved
        return []


s = Solution()
print(s.wave([1, 2, 3, 4]))
# print(s.wave([5, 4, 2, 3, 1]))
print(s.wave([ 5, 1, 3, 2, 4 ]))